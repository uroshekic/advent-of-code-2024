GUARD_UP = "^"
GUARD_DOWN = "v"
GUARD_LEFT = "<"
GUARD_RIGHT = ">"
OBSTRUCTION = "#"

# If there is something directly in front of you, turn right 90 degrees. 
# Otherwise, take a step forward.

def get_starting_point(puzzle):
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            if puzzle[y][x] in [GUARD_UP, GUARD_DOWN, GUARD_LEFT, GUARD_RIGHT]:
                return x, y


def print_puzzle(puzzle):
    print("\n".join("".join(line) for line in puzzle))


def get_distinct_positions(puzzle):
    visited_positions = []
    cycles = []
    x, y = get_starting_point(puzzle)
    while x < len(puzzle[0]) and y < len(puzzle) and x >= 0 and y >= 0:
        # print_puzzle(puzzle); print(puzzle[y][x]); print()
        # print(x, y)
        direction = puzzle[y][x]
        if (x, y) not in visited_positions:
            visited_positions.append((x, y))
        # else:
        #     # Cycle detected - if we add an obstacle, we might not get an infinite loop
        #     if direction == GUARD_UP and y > 0:
        #         if detect_loop(puzzle, x, y, (x, y-1)):
        #             cycles.append((x, y-1))
        #     elif direction == GUARD_DOWN and y < len(puzzle) - 1:
        #         if detect_loop(puzzle, x, y, (x, y+1)):
        #             cycles.append((x, y+1))
        #     elif direction == GUARD_LEFT and x > 0:
        #         if detect_loop(puzzle, x, y, (x-1, y)):
        #             cycles.append((x-1, y))
        #     elif direction == GUARD_RIGHT and x < len(puzzle[0]) - 1:
        #         if detect_loop(puzzle, x, y, (x+1, y)):
        #             cycles.append((x+1, y))
        if direction == GUARD_UP:
            if y  - 1 < 0:
                break
            if puzzle[y-1][x] == OBSTRUCTION:
                puzzle[y][x] = GUARD_RIGHT
            else:
                puzzle[y][x] = "."
                y -= 1
                puzzle[y][x] = direction
        elif direction == GUARD_DOWN:
            if y + 1 >= len(puzzle):
                break
            if puzzle[y+1][x] == OBSTRUCTION:
                puzzle[y][x] = GUARD_LEFT
            else:
                puzzle[y][x] = "."
                y += 1
                puzzle[y][x] = direction
        elif direction == GUARD_LEFT:
            if x - 1 < 0:
                break
            if puzzle[y][x-1] == OBSTRUCTION:
                puzzle[y][x] = GUARD_UP
            else:
                puzzle[y][x] = "."
                x -= 1
                puzzle[y][x] = direction
        elif direction == GUARD_RIGHT:
            if x + 1 >= len(puzzle[0]):
                break
            if puzzle[y][x+1] == OBSTRUCTION:
                puzzle[y][x] = GUARD_DOWN
            else:
                puzzle[y][x] = "."
                x += 1
                puzzle[y][x] = direction
    return visited_positions, cycles


def detect_loop(puzzle, x, y, obstacle, loop):
    if puzzle[y][x] == OBSTRUCTION:
        # print("obstruction on starting point")
        return False

    o_x, o_y = obstacle

    # if (o_x, o_y) in [(3, 6), (7, 6), (7, 7), (1, 8), (3, 8), (7, 9)]:
    #     print("This should be a loop, obstacle", (o_x, o_y))

    if puzzle[o_y][o_x] == OBSTRUCTION:
        # print("obstruction already")
        return False
    
    # We can't put an obstruction on our starting point! (last fix :)
    if x == o_x and y == o_y:
        return False
    
    initial_x = x
    initial_y = y
    turns = 0
    puzzle2 = puzzle  # copy_puzzle(puzzle)
    puzzle2[o_y][o_x] = OBSTRUCTION
    while x >= 0 and x < len(puzzle2[0]) and y >= 0 and y < len(puzzle2):
        turns += 1
        direction = puzzle2[y][x]
        # print("Status", x, y, direction)

        # if x == initial_x and y == initial_y and turns > 1:
        if (x, y, direction) in loop:  # and (x != initial_x and y != initial_y):
            # print("Loop confirmed", turns, puzzle2[y][x])
            # i = loop.index((x, y, direction))
            # loop = loop[i:]
            return True

        loop.append((x, y, direction))

        if direction == GUARD_UP:
            if y  - 1 < 0:
                break
            if puzzle2[y-1][x] == OBSTRUCTION:
                puzzle2[y][x] = GUARD_RIGHT
            else:
                puzzle2[y][x] = "."
                y -= 1
                puzzle2[y][x] = direction
        elif direction == GUARD_DOWN:
            if y + 1 >= len(puzzle2):
                break
            if puzzle2[y+1][x] == OBSTRUCTION:
                puzzle2[y][x] = GUARD_LEFT
            else:
                puzzle2[y][x] = "."
                y += 1
                puzzle2[y][x] = direction
        elif direction == GUARD_LEFT:
            if x - 1 < 0:
                break
            if puzzle2[y][x-1] == OBSTRUCTION:
                puzzle2[y][x] = GUARD_UP
            else:
                puzzle2[y][x] = "."
                x -= 1
                puzzle2[y][x] = direction
        elif direction == GUARD_RIGHT:
            if x + 1 >= len(puzzle[0]):
                break
            if puzzle2[y][x+1] == OBSTRUCTION:
                puzzle2[y][x] = GUARD_DOWN
            else:
                puzzle2[y][x] = "."
                x += 1
                puzzle2[y][x] = direction

    # print("Loop rejected", x, y, puzzle2[y][x])
    return False


def copy_puzzle(puzzle):
    return [l[:] for l in puzzle]


def get_distinct_loops_with_obstruction(puzzle):
    obstructions = []
    unique_loops = []
    sx, sy = get_starting_point(puzzle)
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            print("Testing for loop", sx, sy, (x, y))
            loop = []
            if detect_loop(copy_puzzle(puzzle), sx, sy, (x, y), loop):
                # print(loop)
                if loop not in unique_loops:
                    obstructions.append((x, y))
                    unique_loops.append(loop)
            # print("\n")
    return unique_loops, obstructions


if __name__ == '__main__':
    puzzle = open("./06_input.txt").read().strip().split("\n")
    puzzle = list(map(lambda x: list(x), puzzle))
    # print_puzzle(puzzle)
    distinct_positions, cycles = get_distinct_positions(copy_puzzle(puzzle))
    print(len(distinct_positions))
   
    # print((list(set(cycles))))  # (3, 6), (7, 6), (7, 7), (1, 8), (3, 8), (7, 9)
    # print(len(list(set(cycles)))) 
    unique_loops, obstructions = get_distinct_loops_with_obstruction(copy_puzzle(puzzle))
    # print(obstructions)
    # print(unique_loops)
    print(len(unique_loops))
