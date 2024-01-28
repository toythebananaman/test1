from vActual import current_version
module_name = "vLEEZL.v" + current_version
exec(f"from {module_name} import parser")
exec(f"from {module_name} import lexer")


def compile(p):
    m = lexer(p)
    result = parser(m)
    return(result)
print(compile(3))