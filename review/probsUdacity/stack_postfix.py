"""Reverse Polish Notation

**Reverse Polish notation**, also referred to as **Polish postfix notation** is a way of laying out operators and operands. 

When making mathematical expressions, we typically put arithmetic operators (like `+`, `-`, `*`, and `/`) *between* operands. For example: `5 + 7 - 3 * 8`

However, in Reverse Polish Notation, the operators come *after* the operands. For example: `3 1 + 4 *`

The above expression would be evaluated as `(3 + 1) * 4 = 16`

The goal of this exercise is to create a function that does the following:
* Given a *postfix* expression as input, evaluate and return the correct final answer. 

**Note**: In Python 3, the division operator `/` is used to perform float division. So for this problem, you should use `int()` after every division to convert the answer to an integer.
"""


def evaluate_post_fix(input_list):
    stack = Stack()
    j = 0
    i = 0
    n = len(input_list)
    while i < n:
        if input_list[i] == "+":
            x = stack.pop()
            y = stack.pop()
            z = int(x) + int(y)
            stack.push(z)
        elif input_list[i] == "/":
            x = stack.pop()
            y = stack.pop()
            z = int(x) / int(y)
            stack.push(z)
        elif input_list[i] == "*":
            x = stack.pop()
            y = stack.pop()
            z = int(x) * int(y)
            stack.push(z)
        else:
            stack.push(input_list[i])
        i += 1
    return stack.pop()