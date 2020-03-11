import os, subprocess

from ASTModels import Node

"""
    c_imp = {
        "nodeName":"c_code"
    }
"""
c_imp = {
    'INCREMENT':'mem[p]+={value};',
    'DECREMENT':'mem[p]-={value};',
    'INCREMENT_POINTER':'p+={value};',
    'DECREMENT_POINTER':'p-={value};',
    'OUTPUT':'putchar(mem[p]);',
    'INPUT':'mem[p] = getchar();',
    'LOOP':'while(mem[p]){{{body}}}',
    'CLEAR':'mem[p] = 0;',
}

base_c = "#include <stdio.h>\nint main(){{int mem[30000];int p; {body}return 0;}}"

def compile(
    ast: [Node],
    bin_output_location: str,
    c_output_location:str = None) -> None:
    
    del_c_code = False

    c_code = base_c.format(
        body=''.join(
            map(_node_to_c,ast)
        )
    )
    if not c_output_location:
        c_output_location = "tmp.c"
        del_c_code = True

    with open(c_output_location,"w") as f:
        f.write(c_code)

    try:
        subprocess.run([
            "gcc", 
            c_output_location,
            "-o",
            bin_output_location
        ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    except subprocess.CalledProcessError as suberror:
        print(suberror.stdout.decode("utf-8"))
    else:
        if del_c_code:
            os.remove(c_output_location)
    


def _node_to_c(node: Node) -> str:
    if node.node_type == "INCREMENT":
        return c_imp["INCREMENT"].format(value=node.val)

    elif node.node_type == "DECREMENT":
        return c_imp["DECREMENT"].format(value=node.val)


    elif node.node_type == "INCREMENT_POINTER":
        return c_imp["INCREMENT_POINTER"].format(value=node.val)

    elif node.node_type =="DECREMENT_POINTER":
        return c_imp["DECREMENT_POINTER"].format(value=node.val)


    elif node.node_type == "OUTPUT":
        return c_imp["OUTPUT"]
    
    elif node.node_type == "INPUT":
        return c_imp["INPUT"]

    
    elif node.node_type =="LOOP":
        return c_imp["LOOP"].format(
            body=''.join(
                map(_node_to_c,node.nodes)
            )
        )
