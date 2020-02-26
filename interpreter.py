from ASTModels import Node

memory_size = 30000

def execute(ast: [Node]) -> ([int],int):
    memory = [0]*memory_size
    mp = 0
    for node in ast:
        memory, mp = _evaluate(node,memory,mp)

    print()

    return memory, mp
    
def _evaluate(node: Node, memory: [int], mp: int) -> ([int],int):
    if node.node_type == "INCREMENT":
        memory[mp] += node.val
        if memory[mp] >= 256:
            memory[mp] -= 256

    elif node.node_type == "DECREMENT":
        memory[mp] -= node.val
        if memory[mp] < 0:
            memory[mp] += 255

    elif node.node_type == "INCREMENT_POINTER":
        mp += node.val
        if mp > memory_size:
            mp -= memory_size-1

    elif node.node_type =="DECREMENT_POINTER":
        mp -= node.val
        if mp < 0:
            mp += memory_size-1

    elif node.node_type == "OUTPUT":
        print(chr(memory[mp]),end='')
    
    elif node.node_type == "INPUT":
        i = ''
        while i == '':
            i = input()
        memory[mp] = ord(i[0])
    
    elif node.node_type =="LOOP":
        while memory[mp] != 0:
            for block_node in node.nodes:
                memory, mp = _evaluate(block_node,memory,mp)

    return memory, mp
