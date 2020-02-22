from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    node_type = "BASE"


@dataclass
class LoopNode(Node):
    node_type = "LOOP"
    nodes: List[Node]


@dataclass
class DecrementNode(Node):
    node_type = "DECREMENT"
    val: int

@dataclass
class IncrementNode(Node):
    node_type = "INCREMENT"
    val: int

@dataclass
class DecrementPointerNode(Node):
    node_type = "DECREMENT_POINTER"
    val: int

@dataclass
class IncrementPointerNode(Node):
    node_type = "INCREMENT_POINTER"
    val: int

@dataclass
class InputNode(Node):
    node_type = "INPUT"


@dataclass
class OutputNode(Node):
    node_type = "OUTPUT"
