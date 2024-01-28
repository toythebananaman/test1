from vActual import current_version
module_name = "vLEEZL.v" + current_version
exec(f"from {module_name} import parser")
exec(f"from {module_name} import lexer")

import something
#compile a string "" that you import from file or app, in this case a file

def compile(code):
    tokens = lexer(code)
    result = parser(tokens)
    
compile(something)