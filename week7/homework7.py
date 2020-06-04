import json
def print_dict(x):
    print(json.dumps(x, sort_keys=True, indent=4))

print_dict({"s":1,"o":2,"n":3,"a":4})


















