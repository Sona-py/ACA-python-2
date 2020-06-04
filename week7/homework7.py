#problem 1
import json
def print_dict(x):
    print(json.dumps(x, sort_keys=True, indent=4))

print_dict({"s":1,"o":2,"n":3,"a":4})

#problem 2
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

pyData=json.loads(sampleJson)

def recursive_items(pyData):
    for key, value in pyData.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

for key, value in recursive_items(pyData):
    if key=="salary":
        print(key)
        
#problem 3
import json
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

jsonStr = json.dumps(vehicle.__dict__, indent=4)
print(jsonStr)

#problem 4

import json
from collections import namedtuple
from json import JSONEncoder

def customStudentDecoder(jsformat):
    return namedtuple('X', jsformat.keys())(*jsformat.values())

jsformat = '{"name":"Toyota Rav4", "engine": "2.5L", "price": 32000}'
Vehicle = json.loads(jsformat, object_hook=customStudentDecoder)

print(Vehicle.name)















