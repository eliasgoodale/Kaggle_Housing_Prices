import numpy as np
from functools import reduce
processing_dict = {
    "first": [
        {
            "op_name": "multiply",
            "targets": [10, 2],
        },
        {
            "op_name": "add",
            "targets": [12]
        }
    ]
}



def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

for key, value in processing_dict.items():
    pipeline = value
    for idx, op in enumerate(pipeline):
        func = getattr(np, op["op_name"])
        if idx == 0:
            result = reduce(func, op["targets"])
        else:
            result = reduce(func, [result, *op["targets"]])

print (result)
    
    #pipeline = value
    #result = reduce(evaluate, pipeline)
    #print(result)

