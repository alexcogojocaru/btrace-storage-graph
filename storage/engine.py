from abc import ABC
from network import Network
from queue import Queue


class Engine(ABC):
    def __init__(self, network: Network, sync_queue: Queue) -> None:
        self._network = network
        self._queue = sync_queue
