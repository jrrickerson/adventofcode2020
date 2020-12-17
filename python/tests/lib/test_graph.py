import pytest

from python.lib.graph import Node, Graph


def test_node_sets_key():
    expected_key = "test_node"
    node = Node(expected_key)

    assert node.key == expected_key


def test_node_starts_empty():
    expected_key = "test_node"
    node = Node(expected_key)

    assert not node.edges_to
    assert not node.edges_from


def test_link_to_adds_edge():
    source = Node("source")
    dest = Node("destination")

    source.link_to(dest)

    assert dest.key in source.edges_to
    assert source.edges_to[dest.key][0] == dest
    assert source.edges_to[dest.key][1] is None


def test_link_to_adds_edge_with_weight():
    source = Node("source")
    dest = Node("destination")
    weight = 12

    source.link_to(dest, weight)

    assert dest.key in source.edges_to
    assert source.edges_to[dest.key][0] == dest
    assert source.edges_to[dest.key][1] == weight


def test_link_to_adds_backlink():
    source = Node("source")
    dest = Node("destination")

    source.link_to(dest)

    assert source.key in dest.edges_from
    assert dest.edges_from[source.key] == source


def test_link_to_raises_on_duplicate_edge():
    source = Node("source")
    dest = Node("destination")

    source.link_to(dest)
    with pytest.raises(ValueError):
        source.link_to(dest)


def test_graph_init_empty():
    graph = Graph()

    assert not graph.node_index


def test_graph_init_from_edges():
    edges = [("A", "B", None), ("A", "C", None), ("D", "E", None), ("E", "A", None)]
    graph = Graph(edges)

    assert all([key in graph.node_index for key in ("A", "B", "C", "D", "E")])
    assert "B" in graph.node_index["A"].edges_to
    assert "C" in graph.node_index["A"].edges_to
    assert "E" in graph.node_index["D"].edges_to
    assert "A" in graph.node_index["E"].edges_to
    assert not graph.node_index["B"].edges_to
    assert not graph.node_index["C"].edges_to
    assert not graph.node_index["D"].edges_from


def test_graph_descendents():
    edges = [("A", "B", None), ("A", "C", None), ("D", "E", None), ("E", "A", None)]
    graph = Graph(edges)

    descendents = graph.descendents("E")

    assert descendents == ["A", "B", "C"]


def test_graph_descendents_with_weights():
    edges = [("A", "B", 1), ("A", "C", 2), ("D", "E", 3), ("E", "A", 4)]
    graph = Graph(edges)

    descendents = graph.descendents("E", with_weights=True)

    assert descendents == [("A", 4), ("B", 1), ("C", 2)]


def test_graph_descendents_invalid_key():
    edges = [("A", "B", None), ("A", "C", None), ("D", "E", None), ("E", "A", None)]
    graph = Graph(edges)

    descendents = graph.descendents("Z")

    assert descendents == []


def test_graph_descendents_leaf_node():
    edges = [("A", "B", None), ("A", "C", None), ("D", "E", None), ("E", "A", None)]
    graph = Graph(edges)

    descendents = graph.descendents("C")

    assert descendents == []


def test_graph_ancestors():
    edges = [("A", "B", None), ("A", "C", None), ("D", "E", None), ("E", "A", None)]
    graph = Graph(edges)

    ancestors = graph.ancestors("A")

    assert ancestors == ["E", "D"]


def test_graph_ancestors_invalid_key():
    edges = [("A", "B", None), ("A", "C", None), ("D", "E", None), ("E", "A", None)]
    graph = Graph(edges)

    ancestors = graph.ancestors("Z")

    assert ancestors == []


def test_graph_ancestors_empty():
    edges = [("A", "B", None), ("A", "C", None), ("D", "E", None), ("E", "A", None)]
    graph = Graph(edges)

    ancestors = graph.ancestors("D")

    assert ancestors == []


def test_sum_product_edges():
    edges = [("A", "B", 1), ("A", "C", 2), ("D", "E", 3), ("E", "A", 4)]
    graph = Graph(edges)

    # E -> A (4) + E -> A (4) * (A -> B (1) + A -> C (2))
    # 4 + 4 * (1 + 2) = 16
    sum_product = graph.sum_product_edges("E")

    assert sum_product == 16


def test_sum_product_edges_no_weights():
    edges = [("A", "B", None), ("A", "C", None), ("D", "E", None), ("E", "A", None)]
    graph = Graph(edges)

    sum_product = graph.sum_product_edges("E")

    assert sum_product == 0


def test_sum_product_edges_no_edges():
    edges = [("A", "B", None), ("A", "C", None), ("D", "E", None), ("E", "A", None)]
    graph = Graph(edges)

    sum_product = graph.sum_product_edges("B")

    assert sum_product == 0
