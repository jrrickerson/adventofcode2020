"""Advent of Code 2020
   Day 7 Solution - Handy Haversacks
"""
from .lib import graph

NULL_KEY = "no other"


def parse_rule_to_edges(rule):
    """Given a rule statement in English, parse to a list of tuples
    "yellow bags contain 1 light red bag, 3 purple bags." returns
    [("yellow", "light red", 1), ("yellow", "purple", 3)]"""
    # Clean up the rule text
    rule = (
        rule.strip()
        .strip(".")
        .replace("contain", ">")
        .replace("bags", "")
        .replace("bag", "")
    )

    # Split into "from" and "to" components
    container, contained = rule.split(">")
    source = container.strip()
    # Look for multiple "to" components
    destinations = contained.split(",")
    edges = []
    for destination in destinations:
        if NULL_KEY in destination:
            break
        value, key = destination.strip().split(" ", 1)
        edges.append((source, key, int(value)))
    return edges


def build_rule_graph(rules):
    edges = []
    for rule in rules:
        if rule.strip():
            edges += parse_rule_to_edges(rule)
    rule_graph = graph.Graph(edges)
    return rule_graph


def part_one(rule_graph):
    ancestors = rule_graph.ancestors("shiny gold")
    return len(set(ancestors))


def part_two(rule_graph):
    total_bags = rule_graph.sum_product_edges("shiny gold")
    return total_bags


def solve(filename):
    with open(filename) as f:
        rule_graph = build_rule_graph(f)
    solution = part_one(rule_graph)
    print("Day 007 (Part 1): ", solution)
    solution = part_two(rule_graph)
    print("Day 007 (Part 2): ", solution)


if __name__ == "__main__":
    solve("data/day007.in")
