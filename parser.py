from models import Token
from ASTModels import *

def parse(tokens: [Token]) -> [Node]:
    nodes = []

    while tokens:
        tokens, tmp = _parse(tokens)
        nodes.append(tmp)

    return nodes

def _parse_block(tokens: [Token]) -> ([Token],[Node]):
    nodes = []

    while tokens:
        tokens, tmp = _parse(tokens)
        
        if tmp == None:
            return (tokens,nodes)
        else:
            nodes.append(tmp)


    return (tokens,nodes)
    
def _parse(tokens: [Token]) -> ([Token],Node):
    if not tokens:
        print("EOF")
        return None

    elif tokens[0].type == "INCREMENT":
        return (tokens[1:],IncrementNode(tokens[0].val))
    
    elif tokens[0].type == "DECREMENT":
        return (tokens[1:],DecrementNode(tokens[0].val))

    elif tokens[0].type == "INCREMENT_POINTER":
        return (tokens[1:],IncrementPointerNode(tokens[0].val))
    
    elif tokens[0].type == "DECREMENT_POINTER":
        return (tokens[1:],DecrementPointerNode(tokens[0].val))
    
    elif tokens[0].type == "OUTPUT":
        return (tokens[1:],OutputNode())
    
    elif tokens[0].type == "INPUT":
        return (tokens[1:],InputNode())
    
    elif tokens[0].type == "LOOP_CLOSE":
        return (tokens[1:],None)

    elif tokens[0].type == "LOOP_OPEN":
        tokens, block_nodes = _parse_block(tokens[1:])
        return (tokens,LoopNode(block_nodes))
        
    
    raise ParserError(tokens[0]) 


class ParserError(Exception):
    """ Lexer error exception.
        pos:
            Position in the input line where the error occurred.
    """
    def __init__(self, token):
         Exception.__init__(self,"Unrecognized Token {}".format(token)) 
