import re

def print_puzzle(puzzle):
    print("\n".join("".join(line) for line in puzzle))

def solve(puzzle):
    # Find all unique single lowercase letter, uppercase letter, or digit
    antennas = set()
    antennas_locations = {}
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            current = puzzle[y][x]
            if re.match('^[a-zA-Z\d]$', current):
                antennas.add(current)
                if current not in antennas_locations:
                    antennas_locations[current] = []
                antennas_locations[current].append((x, y))
    
    antinodes = {}
    for antenna in antennas:
        if len(antennas_locations[antenna]) < 1:
            continue
        i = 0
        antinodes[antenna] = []
        antenna_locations = antennas_locations[antenna]
        # print("\n")
        # print(antenna, len(antenna_locations))
        while i < len(antenna_locations):
            j = 0
            while j < i:
                if i == j:
                    j += 1
                    continue
                
                x_i, y_i = antenna_locations[i]
                x_j, y_j = antenna_locations[j]
                x_diff = x_i - x_j
                y_diff = y_i - y_j
                # print(x_i, y_i, x_j, y_j)

                ax1 = x_i + x_diff
                ay1 = y_i + y_diff
                ax2 = x_j - x_diff
                ay2 = y_j - y_diff
                # print(ax1, ay1, ax2, ay2)

                if 0 <= ax1 < len(puzzle[0]) and 0 <= ay1 < len(puzzle):
                    antinodes[antenna].append((ax1, ay1))
                if 0 <= ax2 < len(puzzle[0]) and 0 <= ay2 < len(puzzle):
                    antinodes[antenna].append((ax2, ay2))
                
                j += 1
            i += 1

    # print(antinodes)
    globally_unique_antinodes = set(antinode for antinode_key in antinodes for antinode in antinodes[antinode_key])
    # print(globally_unique_antinodes)
    return len(globally_unique_antinodes)


def solve2(puzzle):
    # Find all unique single lowercase letter, uppercase letter, or digit
    antennas = set()
    antennas_locations = {}
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            current = puzzle[y][x]
            if re.match('^[a-zA-Z\d]$', current):
                antennas.add(current)
                if current not in antennas_locations:
                    antennas_locations[current] = []
                antennas_locations[current].append((x, y))
    
    antinodes = {}
    for antenna in antennas:
        if len(antennas_locations[antenna]) < 1:
            continue
        i = 0
        antinodes[antenna] = []
        antenna_locations = antennas_locations[antenna]
        # print("\n")
        # print(antenna, len(antenna_locations))
        while i < len(antenna_locations):
            j = 0
            while j < i:
                if i == j:
                    j += 1
                    continue
                
                x_i, y_i = antenna_locations[i]
                x_j, y_j = antenna_locations[j]
                x_diff = x_i - x_j
                y_diff = y_i - y_j
                # print(x_i, y_i, x_j, y_j)

                for k in range(max(len(puzzle), len(puzzle[0]))):
                    ax1 = x_i + k * x_diff
                    ay1 = y_i + k * y_diff
                    ax2 = x_j - k * x_diff
                    ay2 = y_j - k * y_diff
                    # print(ax1, ay1, ax2, ay2)

                    if 0 <= ax1 < len(puzzle[0]) and 0 <= ay1 < len(puzzle):
                        antinodes[antenna].append((ax1, ay1))
                    if 0 <= ax2 < len(puzzle[0]) and 0 <= ay2 < len(puzzle):
                        antinodes[antenna].append((ax2, ay2))
                
                j += 1
            i += 1

    # print(antinodes)
    globally_unique_antinodes = set(antinode for antinode_key in antinodes for antinode in antinodes[antinode_key])
    # print(globally_unique_antinodes)
    return len(globally_unique_antinodes)


if __name__ == '__main__':
    puzzle = open("./08_input.txt").read().strip().split("\n")
    puzzle = list(map(lambda x: list(x), puzzle))
    print_puzzle(puzzle)
    # print(len(puzzle[0]), len(puzzle))  # 12 x 12
    print(solve(puzzle))
    print(solve2(puzzle))
