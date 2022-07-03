import hashlib
import json
from engine import Engine
from loguru import logger
from network import Network
from queue import Queue
from threading import Thread, Event

import os
import pickle


class SnapshotEngine(Engine, Thread):
    def __init__(self, network: Network, sync_queue: Queue, event: Event, snapshot_path: str) -> None:
        super().__init__(network, sync_queue)
        Thread.__init__(self)

        self._snapshot_path = snapshot_path
        self._event = event

        if not os.path.exists(snapshot_path):
            os.mkdir(snapshot_path)

        self._nodes_folder_path = os.path.join(snapshot_path, 'nodes')
        if not os.path.exists(self._nodes_folder_path):
            os.mkdir(self._nodes_folder_path)
        
        for filename in os.listdir(self._nodes_folder_path):
            _, service_name = filename.split('_node_')

            with open(os.path.join(self._nodes_folder_path, filename), 'rb') as fo:
                data = pickle.load(fo)
                self._network.load_service_data(service_name, data)

    def run(self):
        last_dict_hash = None
        current_dict_hash = None

        while not self._event.wait(1):
            if self._queue.qsize():
                service_name = self._queue.get()
                logger.debug(f'Received event: {service_name} node')
                data = self._network.get_service_data(service_name)

                current_dict_hash = json.dumps(data, sort_keys=True).encode()
                current_dict_hash = hashlib.md5(current_dict_hash).hexdigest()
                if current_dict_hash != last_dict_hash:
                    logger.debug('Different hash - indexing to file system')
                    node_filename = f'_node_{service_name}'
                    node_file_path = os.path.join(self._nodes_folder_path, node_filename)
                    with open(node_file_path, 'wb') as fo:
                        pickle.dump(data, fo)

                last_dict_hash = current_dict_hash
                self._queue.task_done()
        
        logger.debug('SnapshotEngine stopping')
