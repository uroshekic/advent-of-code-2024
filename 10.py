def solve(tmap):
    scores = {}
    trailheads = find_trailheads(tmap)
    for trailhead in trailheads:
        trailhead_x, trailhead_y = trailhead
        score = is_9_reachable(tmap, trailhead_x, trailhead_y, [])
        if score > 0:
            # print(trailhead, score)
            scores[trailhead] = score
    return sum(scores.values())


def solve2(tmap):
    scores = {}
    trailheads = find_trailheads(tmap)
    for trailhead in trailheads:
        trailhead_x, trailhead_y = trailhead
        score = is_9_reachable2(tmap, trailhead_x, trailhead_y)
        if score > 0:
            # print(trailhead, score)
            scores[trailhead] = score
    return sum(scores.values())


def find_trailheads(tmap):
    trailheads = []
    for y in range(len(tmap)):
        for x in range(len(tmap[y])):
            if tmap[y][x] == 0:
                trailheads.append((x, y))
    return trailheads


def is_9_reachable(tmap, x, y, already_visited):
    current = tmap[y][x]

    if current == 9 and (x, y) not in already_visited:
        already_visited.append((x, y))
        return 1

    score = 0
    # Up
    if y - 1 >= 0 and current + 1 == tmap[y-1][x]:
        score += is_9_reachable(tmap, x, y-1, already_visited)
    # Down
    if y + 1 < len(tmap) and current + 1 == tmap[y+1][x]:
        score += is_9_reachable(tmap, x, y+1, already_visited)
    # Left
    if x - 1 >= 0 and current + 1 == tmap[y][x-1]:
        score += is_9_reachable(tmap, x-1, y, already_visited)
    # Right
    if x + 1 < len(tmap) and current + 1 == tmap[y][x+1]:
        score += is_9_reachable(tmap, x+1, y, already_visited)
    
    # print(x, y, "->", score)
    return score


def is_9_reachable2(tmap, x, y):
    current = tmap[y][x]

    if current == 9:
        return 1

    score = 0
    # Up
    if y - 1 >= 0 and current + 1 == tmap[y-1][x]:
        score += is_9_reachable2(tmap, x, y-1)
    # Down
    if y + 1 < len(tmap) and current + 1 == tmap[y+1][x]:
        score += is_9_reachable2(tmap, x, y+1)
    # Left
    if x - 1 >= 0 and current + 1 == tmap[y][x-1]:
        score += is_9_reachable2(tmap, x-1, y)
    # Right
    if x + 1 < len(tmap) and current + 1 == tmap[y][x+1]:
        score += is_9_reachable2(tmap, x+1, y)
    
    # print(x, y, "->", score)
    return score


def print_map(tmap):
    for l in tmap:
        print("".join(str(i) for i in l))


if __name__ == '__main__':
    topographical_map = open("./10_test.txt").readlines()
    topographical_map = open("./10_input.txt").readlines()
    topographical_map = list(map(lambda x: list(map(lambda y: int(y), x.strip())), topographical_map))
    print_map(topographical_map)
    print(solve(topographical_map))
    print(solve2(topographical_map))
