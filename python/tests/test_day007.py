import io

from .. import day007


def test_parse_line_to_edges():
    """Test parsing an individual rule into a set of graph edges"""
    rule = "dark orange bags contain 3 bright white bags, 4 muted yellow bags."

    edges = day007.parse_rule_to_edges(rule)

    assert len(edges) == 2
    assert ("dark orange", "bright white", 3) in edges
    assert ("dark orange", "muted yellow", 4) in edges


def test_parse_line_to_edges_single_edge():
    rule = "bright white bags contain 1 shiny gold bag."

    edges = day007.parse_rule_to_edges(rule)

    assert len(edges) == 1
    assert ("bright white", "shiny gold", 1) in edges


def test_parse_line_to_edges_none_contained():
    rule = "faded blue bags contain no other bags"
    edges = day007.parse_rule_to_edges(rule)

    assert edges == []


def test_build_rule_graph_empty_rules():
    data = ""
    graph = day007.build_rule_graph(io.StringIO(data))

    assert not graph.node_index


def test_build_rule_graph():
    data = """
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    """
    graph = day007.build_rule_graph(io.StringIO(data))

    assert len(graph.node_index) == 6
    assert "light red" in graph.node_index
    assert "muted yellow" in graph.node_index
    assert graph.node_index["dark orange"].edges_to["bright white"][1] == 3
    assert graph.node_index["dark orange"].edges_to["muted yellow"][1] == 4


def test_part_one_example():
    data = """
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags."""

    graph = day007.build_rule_graph(io.StringIO(data))
    solution = day007.part_one(graph)

    assert solution == 4


def test_part_two_example_1():
    """Test first example from the problem statement"""
    data = """
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags."""

    graph = day007.build_rule_graph(io.StringIO(data))
    solution = day007.part_two(graph)

    assert solution == 32


def test_part_two_example_2():
    """Test second example from the problem statement"""
    data = """
    shiny gold bags contain 2 dark red bags.
    dark red bags contain 2 dark orange bags.
    dark orange bags contain 2 dark yellow bags.
    dark yellow bags contain 2 dark green bags.
    dark green bags contain 2 dark blue bags.
    dark blue bags contain 2 dark violet bags.
    dark violet bags contain no other bags."""

    graph = day007.build_rule_graph(io.StringIO(data))
    solution = day007.part_two(graph)

    assert solution == 126
