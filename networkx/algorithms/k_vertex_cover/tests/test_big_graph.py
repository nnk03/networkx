import networkx as nx
from networkx.algorithms.k_vertex_cover.k_vertex_cover import (
    is_vertex_cover,
    k_vertex_cover,
)
from networkx.generators import random_graphs
from networkx.generators.classic import complete_graph


class TestBigGraph:
    def test_complete_graph(self):
        G = complete_graph(100)
        k = 97
        is_k_vc_exists, vertex_cover = k_vertex_cover(G, k)
        if is_k_vc_exists:
            assert len(vertex_cover) <= k, f"size of vertex cover must be atmost k={k}"
            assert is_vertex_cover(G, vertex_cover)

        G = complete_graph(150)
        k = 20
        is_k_vc_exists, vertex_cover = k_vertex_cover(G, k)
        if is_k_vc_exists:
            assert len(vertex_cover) <= k, f"size of vertex cover must be atmost k={k}"
            assert is_vertex_cover(G, vertex_cover)

        G = complete_graph(150)
        k = 49
        is_k_vc_exists, vertex_cover = k_vertex_cover(G, k)
        if is_k_vc_exists:
            assert len(vertex_cover) <= k, f"size of vertex cover must be atmost k={k}"
            assert is_vertex_cover(G, vertex_cover)

        G = complete_graph(150)
        k = 75
        is_k_vc_exists, vertex_cover = k_vertex_cover(G, k)
        if is_k_vc_exists:
            assert len(vertex_cover) <= k, f"size of vertex cover must be atmost k={k}"
            assert is_vertex_cover(G, vertex_cover)

        G = complete_graph(150)
        k = 150
        is_k_vc_exists, vertex_cover = k_vertex_cover(G, k)
        if is_k_vc_exists:
            assert len(vertex_cover) <= k, f"size of vertex cover must be atmost k={k}"
            assert is_vertex_cover(G, vertex_cover)

    def test_random_big_graph(self):
        G = random_graphs.erdos_renyi_graph(1500, 0.9)
        k = 750
        is_k_vc_exists, vertex_cover = k_vertex_cover(G, k)
        if is_k_vc_exists:
            assert len(vertex_cover) <= k, f"size of vertex cover must be atmost k={k}"
            assert is_vertex_cover(G, vertex_cover)

    def test_bipartite_graph(self):
        G = nx.complete_bipartite_graph(50, 50)
        k = 100
        is_k_vc_exists, vertex_cover = k_vertex_cover(G, k)
        if is_k_vc_exists:
            assert len(vertex_cover) <= k, f"size of vertex cover must be atmost k={k}"
            assert is_vertex_cover(G, vertex_cover)
