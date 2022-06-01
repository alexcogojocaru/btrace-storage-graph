import json
from typing import Dict, List
import networkx as nx
import pickle


class Network:
    def __init__(self) -> None:        
        self._services: Dict[str, Dict[str, nx.DiGraph]] = {}

    def add_node(self, servicename, traceid, spanid, name, parentid):
        if servicename not in self._services:
            graph = nx.DiGraph(traceid=traceid)
            graph.add_node(spanid, name=name, parentid=parentid)
            self._services[servicename] = { traceid: graph }
        else:
            if traceid not in self._services:
                self._services[servicename][traceid] = nx.DiGraph(traceid=traceid)

            graph = self._services[servicename][traceid]
            graph.add_node(spanid, name=name, parentid=parentid)
            
            if parentid != '0000000000000000':
                graph.add_edge(parentid, spanid)
            # print(f'{traceid} {spanid} {parentid}')
            self._services[servicename][traceid] = graph

    def get_successors(self, servicename, traceid, spanid):
        return self._services[servicename][traceid].successors(spanid)

    def get_data(self):
        for service, service_data in self._services.items():
            print(service)
            for traceid, graph in service_data.items():
                print(f'\t{traceid}')
                print(json.dumps(list(graph.nodes.data()), indent=4))

if __name__ == '__main__':
    network = Network()

    args = { 
        'servicename': 'BTracer',
        'traceid': '6ea1e01ac59d90b236224dbd65d9dbff',
        'spanid': '0a5dae65161276a1',
        'name': 'Main',
        'parentid': '0000000000000000'
    }

    network.add_node(**args)
    network.add_node('BTracer', '6ea1e01ac59d90b236224dbd65d9dbff', 'ee2d8605865b982b', 'SecondMain', '0a5dae65161276a1')
    network.add_node('BTracer', '6ea1e01ac59d90b236224dbd65d9dbff', '483aa59976dce3e1', 'ThirdMain', '0a5dae65161276a1')
    network.add_node('BTracer', '6ea1e01ac59d90b236224dbd65d9dbff', '94a8eefd77d9be19', 'FourthMain', '483aa59976dce3e1')

    # network.add_node('BTracer', '2145435fsdfjk234bj23kjnk235jk325', '94a8eefd77d9be19', 'RedisCall', '0000000000000000')
    # network.add_node('BTracer', '2145435fsdfjk234bj23kjnk235jk325', '483aa59976dce3e1', 'RedisCall', '94a8eefd77d9be19')

    # network.add_node('BunaSiua', '2145435fsdfjk234bj23kjnk235jk325', '94a8eefd77d9be19', 'RedisCall', '0000000000000000')
    # network.add_node('BunaSiua', '2145435fsdfjk234bj23kjnk235jk325', '483aa59976dce3e1', 'RedisCall', '94a8eefd77d9be19')

    network.get_data()

    # print(list(network.get_successors('BTracer', '2145435fsdfjk234bj23kjnk235jk325', '94a8eefd77d9be19')))

    # serialized_data = { 'nodes': list(DG.nodes.data()), 'edges': list(DG.edges) }
    # with open('__index001', 'wb') as fo:
    #     pickle.dump(serialized_data, fo)
