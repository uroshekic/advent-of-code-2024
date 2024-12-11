def get_disk_representation(puzzle):
    i = 0
    line = []
    block_index = 0
    while i < len(puzzle):
        if i % 2 == 0:
            # File block
            line += [str(block_index)] * puzzle[i]
            block_index += 1
        else:
            # Free space
            line += ["."] * puzzle[i]
        i += 1
    return line


def swap_block(disk_representation, file_block, free_block):
    block = disk_representation[file_block]
    disk_representation[free_block] = block
    disk_representation[file_block] = "."
    return disk_representation


def calculate_checksum(disk_representation):
    checksum = 0
    for i in range(len(disk_representation)):
        if disk_representation[i] == '.':
            continue
        checksum += i * int(disk_representation[i])
    return checksum


def solve(puzzle):
    disk_representation = get_disk_representation(puzzle)
    # print_disk(disk_representation)
    free_space = disk_representation.count(".")
    i = 0
    j = len(disk_representation) - 1
    swaps = 0
    while i < len(disk_representation) and j >= 0:
        if disk_representation[i] != '.':
            i += 1
            continue
        if i >= j:
            break
        if disk_representation[j] != '.':
            disk_representation = swap_block(disk_representation, j, i)
            swaps += 1
            # print_disk(disk_representation); print()
        j -= 1
        # print_disk(disk_representation)
    
    # print_disk(disk_representation)
    return calculate_checksum(disk_representation)


def print_disk(disk_representation):
    print("".join(disk_representation))


def solve2(puzzle):
    disk_representation = get_disk_representation(puzzle)
    # print_disk(disk_representation)
    free_space = disk_representation.count(".")
    j = len(disk_representation) - 1
    swaps = 0
    already_moved = []
    while j >= 0:
        # Check if there are any free spaces on the left of current block
        if sum(1 for c in disk_representation[:j] if c == '.') == 0:
            break

        # Find file block
        if disk_representation[j] == '.':
            j -= 1
            continue
        file_block_end = j
        while j > 0 and disk_representation[j] == disk_representation[j-1]:
            j -= 1
        file_block_start = j
        file_block_size = file_block_end - file_block_start + 1
        # print(disk_representation[j], ":", file_block_start, file_block_end, file_block_size)

        # Find free block of given size
        i = 0
        free_block_size = 0
        while i < len(disk_representation):
            while i < len(disk_representation) and disk_representation[i] != '.':
                i += 1
                continue
            
            free_block_start = i
            while i + 1 < len(disk_representation) and disk_representation[i+1] == '.':
                i += 1
            free_block_end = i
            free_block_size = free_block_end - free_block_start + 1
            # print(". :", free_block_start, free_block_end, free_block_size)

            if free_block_size >= file_block_size:
                break
            i += 1

        # Skip to next file block if indices cross
        if i >= j:
            j -= 1
            continue
        
        # Attempt to move each file only once
        if disk_representation[file_block_start] in already_moved:
            j -= 1
            continue

        if free_block_size >= file_block_size:
            # print("Moving", disk_representation[file_block_start])
            already_moved.append(disk_representation[file_block_start])
            # Swap file               
            for z in range(file_block_size):
                disk_representation = swap_block(disk_representation, file_block_start+z, free_block_start+z)
            # print_disk(disk_representation)
            j -= 1

        # print_disk(disk_representation)
    
    # print_disk(disk_representation)
    return calculate_checksum(disk_representation)


if __name__ == '__main__':
    puzzle = list(open("./09_test.txt").read().strip())
    puzzle = list(open("./09_input.txt").read().strip())
    puzzle = list(map(lambda x: int(x), puzzle))
    # print(puzzle)
    print(solve(puzzle))
    print(solve2(puzzle))
