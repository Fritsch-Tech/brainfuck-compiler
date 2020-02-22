import re

from models import Token


class LexerError(Exception):
    """ Lexer error exception.
        pos:
            Position in the input line where the error occurred.
    """
    def __init__(self, pos):
         Exception.__init__(self,"Lexer error at position {}".format(pos)) 

rules = [
    ('\++', 'INCREMENT'),
    ('\-+', 'DECREMENT'),
    ('\>+', 'INCREMENT_POINTER'),
    ('\<+', 'DECREMENT_POINTER'),
    ('\.',  'OUTPUT'),
    ('\,',  'INPUT'),
    ('\[',  'LOOP_OPEN'),
    ('\]',  'LOOP_CLOSE'),
]

"""
    > 	increment the data pointer (to point to the next cell to the right).
    < 	decrement the data pointer (to point to the next cell to the left).
    + 	increment (increase by one) the byte at the data pointer.
    - 	decrement (decrease by one) the byte at the data pointer.
    . 	output the byte at the data pointer.
    , 	accept one byte of input, storing its value in the byte at the data pointer.
    [ 	if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.
    ] 	if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command. 
"""

rules = [(re.compile(regex,re.MULTILINE),type) for regex, type in rules]

def lexer(input:str) -> [Token]:
    code = ''.join(list(filter(_valide_symbol,input)))
    tokens = []
    pos = 0

    while pos < len(code):

        matches = [re.match(code,pos) for re,_ in rules]

        try:
            match = [(match, rules[idx][1]) for idx,match in enumerate(matches) if match][0]
        except IndexError:
            print('Invalide Symbol \"{}\"'.format(code[pos]))
            raise LexerError(pos)
        
        tokens.append(Token(match[1],len(match[0].group(0))))
        pos = match[0].end()

    return tokens

def _valide_symbol(char:str) -> bool:
    valide_symbols = [
        "<",
        ">",
        "+",
        "-",
        ".",
        ",",
        "[",
        "]"
        ]
    if char in valide_symbols:
        return True
    else:
        return False
