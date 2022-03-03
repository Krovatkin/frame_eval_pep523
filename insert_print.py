from types import CodeType
import dis
def wadd(a, b):
    print("rara")
    return a + b



def fix_function(func, payload):
    fn_code = func.__code__
    print(type(fn_code.co_argcount).__name__)
    func.__code__ = CodeType(fn_code.co_argcount,
                             fn_code.co_posonlyargcount,
                             fn_code.co_kwonlyargcount,
                             fn_code.co_nlocals,
                             fn_code.co_stacksize,
                             fn_code.co_flags,
                             #fn_code.co_code,
                             payload,
                             fn_code.co_consts,
                             fn_code.co_names,
                             fn_code.co_varnames,
                             fn_code.co_filename,
                             fn_code.co_name,
                             fn_code.co_firstlineno,
                             fn_code.co_lnotab,
                             fn_code.co_freevars,
                             fn_code.co_cellvars,
                             )

a = """
def fact(a, b):
    print("hello")
    return a * b
"""
c = compile(a, '<string>', 'exec')
mul_code = c.co_consts[0]
print(mul_code.co_consts)

print(dis.dis(mul_code.co_code[:6]))

payload = mul_code
dis.dis(payload)
# dis.dis(wadd.__code__.co_code)
wadd(3, 1)  # The result is: 64
# Now it's (x - y) instead of (x+y)
fix_function(wadd, payload.co_code)
print(wadd(3, 3))  # The result is: 8