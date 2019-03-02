import numpy as np

processing_dict = {
    "first": [
        {
            "op": "prod",
            "targets": [10, 2],
        },
        {
            "op": "sum",
            "targets": ["result", 12]
        }
    ]
}

for key, value in processing_dict.items():
    pipeline = np.array(value)
    result = 0
    for operation in pipeline:
        if "result" in operation["targets"]:
            idx = operation["targets"].index("result")
            operation["targets"][idx] = result

        func = getattr(np, operation["op"])
        result = func(operation["targets"]).astype(np.int)
    print(result)

