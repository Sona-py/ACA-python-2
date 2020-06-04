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


















