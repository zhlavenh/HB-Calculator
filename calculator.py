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
    if "q" in tokens[0]:
        print("you are exiting!")
        break
        
    else:

        #             (decide which math function to call based on first token)
        #             if the first token is 'pow':
        #                   call the power function with the other two tokens

        #             (...etc.)

        if tokens[0] == "+":
            ans = add(tokens[1],tokens[2])
    
        elif tokens[0] == "-":
            ans = subtract(token[1] - token[2])
    
        elif tokens[0] == "*":
            ans = multiply(tokens[1], tokens[2])
        
        elif tokens[0] == "/":
            ans = divide(tokens[1],tokens[]2)
    
        elif tokens[0] == "square":
            ans = square(tokens[1])
            
        elif tokens[0] == "cube":
            ans = cube(tokens[1])

        elif tokens[0] == "pow":
            ans = pow(tokens[1],tokens[2])
        
        elif token[0] == "mod":
            ans = mod(tokens[1],tokens[2])
        
        else:
            print("Please input proper format!")

            
    print(ans)

