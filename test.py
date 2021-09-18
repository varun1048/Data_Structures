
from termcolor import colored
def color(later,color):
    return colored(later, color, attrs=['reverse', 'blink'])

def output(index,Expected,Actual):
    print(f"""
  Test case\t{index} 
  Actual \t{Expected } 
  Expected   \t{Actual if Expected == Actual else  color(Actual,'red')} """)



tests= []
# tests.append({
#     "inputs":{
#         "cards":list(range(0,21)),
#         "query":2
#     },
#     "output":1
# })


tests.append({
    "inputs":{
        "cards":range(11),
        "query":9
    },
    "output":1
})

# tests.append({
#     "inputs":{
#         "cards":[3,5,3,9,7,6],
#         "query":7
#     },
#     "output":4
# })

# tests.append({
#     "inputs":{
#         "cards":[9,1,2],
#         "query":9
#     },
#     "output":0
# })

# tests.append({
#     "inputs":{
#         "cards":[],
#         "query":23
#     },
#     "output":-1
# })