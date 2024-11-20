import networkx as nx
from networkx.algorithms.k_vertex_cover.test_helper_functions import (
    check_vertex_cover,
)


class TestPetersenGraphVertexCover:
    def test_vertex_cover(self):
        G = nx.petersen_graph()

        for k in range(len(G) + 1):
            check_vertex_cover(G, k)


if __name__ == "__main__":
    test_class = TestPetersenGraphVertexCover()
    test_class.test_vertex_cover()