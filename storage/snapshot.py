from engine import Engine
from loguru import logger
from network import Network
from queue import Queue
from threading import Thread

import os
import pickle


class SnapshotEngine(Engine, Thread):
    POLLING_TIME = 10

    def __init__(self, network: Network, sync_queue: Queue, snapshot_path: str) -> None:
        super().__init__(network, sync_queue)
        Thread.__init__(self)

        self._snapshot_path = snapshot_path
        self.daemon = True

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
        while True:
            service_name = self._queue.get()
            logger.debug(f'Received event: {service_name} node')
            data = self._network.get_service_data(service_name)

            node_filename = f'_node_{service_name}'
            with open(os.path.join(self._nodes_folder_path, node_filename), 'wb') as fo:
                pickle.dump(data, fo)

            self._queue.task_done()
