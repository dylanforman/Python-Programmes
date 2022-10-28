
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  num1 = float(input("What is the first number? "))
  
  for operator in operations:
    print(operator)
  
  chosen_operator = input("Pick an operation from the line above: ")
  num2 = float(input("What is the second number? "))
  
  calculation_function = operations[chosen_operator]
  answer = calculation_function(num1, num2)
  
  print(f"{num1} {chosen_operator} {num2} = {answer}")
  
  keep_calculating = True
  while keep_calculating:
    previous_answer = answer
    should_continue = input(f"Type 'y' to continue calculating with {previous_answer} or type 'n' to start over.").lower()
    if should_continue == 'y':
      chosen_operator = input("Pick another operator: ")
      next_number = float(input("Pick another number: "))
      calculation_function = operations[chosen_operator]
      answer = calculation_function(answer, next_number)
      print(f"{previous_answer} {chosen_operator} {next_number} = {answer}")
    elif should_continue == 'n':
      keep_calculating = False
      calculator()

calculator()