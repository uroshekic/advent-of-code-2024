import itertools


def solve(equations):
    correct_equations = []
    for result, operands in equations:
        # print(result, operands)
        for operations in itertools.product(OPERATIONS, repeat=len(operands)-1):
            # print(operations)
            r = operands[0]
            i = 0
            while i < len(operations):
                if operations[i] == "+":
                    r += operands[i+1]
                elif operations[i] == "*":
                    r *= operands[i+1]
                elif operations[i] == "||":
                    r = int(str(r) + str(operands[i+1]))
                i += 1
            if r == result:
                correct_equations.append((result, operands))
                break
                
    return sum(result for result, _ in correct_equations)


if __name__ == '__main__':
    lines = open("./07_input.txt").read().strip().split("\n")
    equations = []
    for line in lines:
        result, operands = line.split(": ")
        result = int(result)
        operands_list = list(map(lambda x: int(x), operands.split(" ")))
        equations.append((result, operands_list))
    
    OPERATIONS = ["+", "*"]
    print(solve(equations))

    OPERATIONS = ["+", "*", "||"]
    print(solve(equations))
