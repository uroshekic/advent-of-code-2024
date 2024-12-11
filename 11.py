def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            new_stones.append(int(stone[:len(stone)//2]))
            new_stones.append(int(stone[len(stone)//2:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones


def blink_count(stone, remaining_blinks):
    if remaining_blinks == 0:
        return 1

    if (stone, remaining_blinks) in solved_blinks:
        return solved_blinks[(stone, remaining_blinks)]

    # 0
    if stone == 0:
        # return blink_count(1, remaining_blinks-1)
        solved_blinks[(stone, remaining_blinks)] = blink_count(1, remaining_blinks-1)
        return solved_blinks[(stone, remaining_blinks)]
    
    # Even
    sstone = str(stone)
    if len(sstone) % 2 == 0:
        # return blink_count(int(sstone[:len(sstone)//2]), remaining_blinks-1) + blink_count(int(sstone[len(sstone)//2:]), remaining_blinks-1)
        solved_blinks[(stone, remaining_blinks)] = blink_count(int(sstone[:len(sstone)//2]), remaining_blinks-1) + blink_count(int(sstone[len(sstone)//2:]), remaining_blinks-1)
        return solved_blinks[(stone, remaining_blinks)]
    
    # Odd
    # return blink_count(stone * 2024, remaining_blinks-1)
    solved_blinks[(stone, remaining_blinks)] = blink_count(stone * 2024, remaining_blinks-1)
    return solved_blinks[(stone, remaining_blinks)]


def solve2(stones, blinks):
    return sum(blink_count(stone, blinks) for stone in stones)


if __name__ == '__main__':
    line = open("./11_test.txt").read().strip().split(" ")
    # line = [125, 17]
    line = open("./11_input.txt").read().strip().split(" ")
    stones = list(map(lambda x: int(x), line))
    # print(stones)
    
    # for i in range(25):
    #     stones = blink_count(stones)
    # print(len(stones))
    solved_blinks = {}
    print(solve2(stones, 75))
