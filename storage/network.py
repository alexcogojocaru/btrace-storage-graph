import networkx as nx

from enum import Enum
from storage_pb2 import StorageSpan
from typing import Dict


class NodeTag(Enum):
    TRACE = 0x1
    SPAN  = 0x2

class Network:
    NULL_SPAN = '0000000000000000'
    
    def __init__(self) -> None:        
        self._services: Dict[str, nx.DiGraph] = {}

    def add_service(self, service_name: str) -> bool:
        '''
            Adds a new service in the network

            @param service_name :str: - the name of the service
            @returns :bool: - True if the service was added, False if the service already exists
        '''
        
        if service_name not in self._services:
            self._services[service_name] = nx.DiGraph(service=service_name)
            return True
        return False

    def add_trace(self, service_name: str, traceid: str):
        self.add_service(service_name)
        self._services[service_name].add_node(traceid, tag=NodeTag.TRACE.value)

    def add_span(self, service_name: str, traceid: str, span: StorageSpan):
        self.add_trace(service_name, traceid)

        source = traceid if span.parentSpanID == self.NULL_SPAN else span.parentSpanID
        self._services[service_name].add_node(span.spanID, tag=NodeTag.SPAN.value, data=self._proto_to_dict(span))
        self._services[service_name].add_edge(source, span.spanID)
        return True

    def _proto_to_dict(self, span: StorageSpan):
        return {
            'spanName':     span.spanName,
            'traceID':      span.traceID,
            'spanID':       span.spanID,
            'parentSpanID': span.parentSpanID,
        }

    def load_service_data(self, service_name: str, data: dict):
        self._services[service_name] = nx.node_link_graph(data)

    def get_data(self):
        return { 
            service_name: nx.node_link_data(self._services[service_name]) 
            for service_name in self._services 
        }
    
    def get_service_data(self, service_name: str):
        if service_name in self._services:
            return nx.node_link_data(self._services[service_name])
        return None
