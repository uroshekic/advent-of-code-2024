def calculate(memory: str) -> int:
    i = 0
    result = 0
    while i < len(memory):
        if memory[i:i+4] == 'mul(':
            i = i + 4
            
            # scan numbers until ','
            factor1 = find_factor(memory, i, ",")
            if factor1 is None:
                i += 1
                continue
            i += len(factor1) + 1
            
            # scan numbers until ')'
            factor2 = find_factor(memory, i, ")")
            if factor2 is None:
                i += 1
                continue
            i += len(factor2) + 1
            
            result += int(factor1) * int(factor2)
        else:
            i += 1
    
    return result


def calculate2(memory: str) -> int:
    i = 0
    result = 0
    mul_instructions_enabled = True
    while i < len(memory):
        if i + 4 < len(memory) and memory[i:i+4] == "do()":
            i += 4
            mul_instructions_enabled = True
        elif i + 7 < len(memory) and memory[i:i+7] == "don't()":
            i += 7
            mul_instructions_enabled = False
        
        if i + 4 < len(memory) and memory[i:i+4] == "mul(":
            i = i + 4
            
            # scan numbers until ','
            factor1 = find_factor(memory, i, ",")
            if factor1 is None:
                i += 1
                continue
            i += len(factor1) + 1
            
            # scan numbers until ')'
            factor2 = find_factor(memory, i, ")")
            if factor2 is None:
                i += 1
                continue
            i += len(factor2) + 1
            
            if mul_instructions_enabled:
                result += int(factor1) * int(factor2)
        else:
            i += 1
    
    return result


def find_factor(memory: str, i: int, end_char: str) -> str:
    j = i
    while j < len(memory):
        if is_digit(memory[j]):
            j += 1
        elif memory[j] == end_char:
            break
        else:
            return None
    return memory[i:j]


def is_digit(c: str) -> bool:
    return c in "0123456789"


if __name__ == '__main__':
    inp = open("./03_input.txt").read().strip()
    print(calculate(inp))
    print(calculate2(inp))
