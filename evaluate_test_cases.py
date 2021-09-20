from termcolor import colored

def color(later,color):
    return colored(later, color, attrs=['reverse', 'blink'])

def evaluate_test_cases(index,Actual,Expected):
    print(f"""
  Test case\t{index} 
  Your output:\t\t {Actual if Expected == Actual else  color(Actual,'red')}
  Expected  output:\t {Expected }
  """)
