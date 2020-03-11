"""
    rules:
        [
            (regex,tokenname)
        ]
"""
optimised_rules = [
    ('\[-]', 'CLEAR'),
]

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