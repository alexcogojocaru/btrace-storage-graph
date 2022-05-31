import json
import networkx as nx
import pickle


if __name__ == '__main__':
    DG = nx.DiGraph(trace_id='6ea1e01ac59d90b236224dbd65d9dbff')

    DG.add_node('0a5dae65161276a1', name='Main', parent_id='0000000000000000')
    DG.add_node('ee2d8605865b982b', name='SecondMain', parent_id='0a5dae65161276a1')
    DG.add_node('483aa59976dce3e1', name='ThirdMain', parent_id='0a5dae65161276a1')
    DG.add_node('94a8eefd77d9be19', name='FourthMain', parent_id='483aa59976dce3e1')

    DG.add_edge('0a5dae65161276a1', 'ee2d8605865b982b')
    DG.add_edge('0a5dae65161276a1', '483aa59976dce3e1')
    DG.add_edge('483aa59976dce3e1', '94a8eefd77d9be19')

    serialized_data = { 'nodes': list(DG.nodes.data()), 'edges': list(DG.edges) }
    with open('__index001', 'wb') as fo:
        pickle.dump(serialized_data, fo)
