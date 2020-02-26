from lexer import lexer
from parser import parse
from interpreter import execute
from compiler import compile

def compiler(input_path:str):
    print_tokens = False
    print_nodes  = False

    with open(input_path,"r") as f:
        tokens = lexer(f.read())
    
    if print_tokens:
        for token in tokens:
            print(token)
    
    nodes = parse(tokens)
    
    if print_nodes:
        for node in nodes:
            print(node)
    

    compile(
        nodes,
        "/home/sakuk/Documents/brainfuck-compiler/tests",
        #"/home/sakuk/Documents/brainfuck-compiler/tests.c"
    )

def interpreter(input_path:str):
    print_tokens = False
    print_nodes  = False

    with open(input_path,"r") as f:
        tokens = lexer(f.read())
    
    if print_tokens:
        for token in tokens:
            print(token)
    
    nodes = parse(tokens)
    
    if print_nodes:
        for node in nodes:
            print(node)
    

    memory, mp = execute(nodes)
    #print(memory)
    #print()
    #print(mp)

if __name__ == "__main__":
    compiler("/home/sakuk/Documents/brainfuck-compiler/tests.bf")