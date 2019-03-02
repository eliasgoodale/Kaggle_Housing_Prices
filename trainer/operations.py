import numpy as np
from functools import reduce
processing_dict = {
    "first": [
        {
            "op_name": "prod",
            "targets": [10, 2],
        },
        {
            "op_name": "sum",
            "targets": [12]
        }
    ]
}



def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def process_inputs(self, df_name, processing_dict): 
    for key, value in processing_dict.items():
        pipeline = value
        for idx, op in enumerate(pipeline):
            func = getattr(pd.Series, op["op_name"])
            inputs = op["targets"] if idx == 0 else [result, *op["targets"]]
            result = func(inputs)

