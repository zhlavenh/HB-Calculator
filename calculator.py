"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# repeat forever:

while True:

    #     read input
    equation = input("Enter your equation:")

    #     tokenize input

    tokens = equation.split(" ")
    if "q" in tokens[0][0]:
        print("you are exiting!")
        break
        
    else:

        #             (decide which math function to call based on first token)
        #             if the first token is 'pow':
        #                   call the power function with the other two tokens

        #             (...etc.)

        num1 = int(tokens[1])

        if len(tokens) > 2:

            num2 = int(tokens[2])

        if tokens[0] == "+":
            ans = add(num1,num2)
    
        elif tokens[0] == "-":
            ans = subtract(num1, num2)
    
        elif tokens[0] == "*":
            ans = multiply(num1, num2)
        
        elif tokens[0] == "/":
            ans = divide(num1,num2)
    
        elif tokens[0] == "square":
            ans = square(num1)
            
        elif tokens[0] == "cube":
            ans = cube(num1)

        elif tokens[0] == "pow":
            ans = pow(num1,num2)
        
        elif tokens[0] == "mod":
            ans = mod(num1,num2)
        
        else:
            print("Please input proper format!")

            
    print(ans)

