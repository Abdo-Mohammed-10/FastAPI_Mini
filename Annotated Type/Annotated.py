# import annotated 
from typing import Annotated , get_args , get_origin , get_type_hints
from  functools  import wraps

def check_bounds(func):
    @wraps(func)
    def wrapper(x):
        type_hints = get_type_hints(func)
        hint = type_hints['x']
        
        if get_origin(hint) is Annotated:
            hint_type, *hint_args = get_args(hint)
            lower, upper = hint_args[0]
            
            if not (lower <= x <= upper):
                raise ValueError(f"x must be between {lower} and {upper}")
        
        return func(x)
    return wrapper


def double(x: Annotated[int, (0,10)]) -> int:
    type_hints = get_type_hints(double , include_extras=True)
    hint = type_hints['x']
    
    if get_origin(hint) is Annotated:
        hint_type, *hint_args = get_args(hint)
        lower, upper = hint_args[0]
        
        if not (lower <= x <= upper):
            raise ValueError(f"x must be between {lower} and {upper}")
    return x * 2


result = double(2855656)

print(result)


# x: Annotated[int, "This is an integer"] = 5
# y: Annotated[str, "This is a string"] = "Hello, World!"
# z: Annotated[float, "This is a float"] = 3.14
# print(x)
# print(y)
# print(z)
