"""
    rules:
        [
            (regex,tokenname)
        ]
"""
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