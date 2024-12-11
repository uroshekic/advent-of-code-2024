def word_search(puzzle: str, word: str) -> int:
    w = len(puzzle[0])
    h = len(puzzle)
    nr_occurrences = 0
    for j in range(h):
        for i in range(w):
            nr_occurrences += find_word(puzzle, i, j, word)
    return nr_occurrences


def word_search2(puzzle: str, word: str) -> int:
    w = len(puzzle[0])
    h = len(puzzle)
    nr_occurrences = 0
    for j in range(h):
        for i in range(w):
            nr_occurrences += find_2mas(puzzle, i, j, word)
        # print()
    return nr_occurrences


def find_word(puzzle: str, i: int, j: int, word: str) -> int:
    # if puzzle[j][i] != 'X': return 0
    w = len(puzzle[0])
    h = len(puzzle)
    l = len(word)
    occurences = 0
    # words = [word, word[::-1]]
    # horizontal, vertical, diagonal, written backwards, or even overlapping other words
    if i + l <= w and puzzle[j][i:i+l] == word:
        occurences += 1
    if i - l >= -1 and (puzzle[j][i-l+1:i+1])[::-1] == word:
       occurences += 1
    if j + l <= h and get_vertical_word(puzzle, i, j, l) == word:
        occurences += 1
    if j - l >= -1 and get_vertical_word_inverse(puzzle, i, j, l) == word:
       occurences += 1
    # diagonal
    if i + l <= w and j + l <= h and get_diagonal_word(puzzle, i, j, l, 1, 1) == word:
        occurences += 1
    if i + l <= w and j - l >= -1 and get_diagonal_word(puzzle, i, j, l, 1, -1)  == word:
        occurences += 1
    if i - l >= -1 and j + l <= h and get_diagonal_word(puzzle, i, j, l, -1, 1)  == word:
       occurences += 1
    if i - l >= -1 and j - l >= -1 and get_diagonal_word(puzzle, i, j, l, -1, -1)  == word:
       occurences += 1
    return occurences


def find_2mas(puzzle: str, i: int, j: int, word) -> int:
    # if puzzle[j][i] != 'X': return 0
    w = len(puzzle[0])
    h = len(puzzle)
    l = len(word)
    occurences = 0
    words = [word, word[::-1]]
    # diagonal
    if i + l <= w and j + l <= h and get_diagonal_word(puzzle, i, j, l, 1, 1) in words:
        j += 2
        if i + l <= w and j - l >= -1 and get_diagonal_word(puzzle, i, j, l, 1, -1) in words:
            occurences += 1
    return occurences


def get_vertical_word(puzzle: str, i: int, j: int, l: int) -> str:
    return "".join(puzzle[j+x][i] for x in range(l))


def get_vertical_word_inverse(puzzle: str, i: int, j: int, l: int) -> str:
    return "".join(puzzle[j-x][i] for x in range(l))


def get_diagonal_word(puzzle: str, i: int, j: int, l: int, i_m: int, j_m: int) -> str:
    return "".join(puzzle[j + x * j_m][i + x * i_m] for x in range(l))


if __name__ == '__main__':
    WORD = "XMAS"
    puzzle = list(map(lambda x: x.strip(), open("./04_input.txt").readlines()))
    print('xmas', word_search(puzzle, WORD))
    print('2-mas', word_search2(puzzle, "MAS"))
    # print(); for line in puzzle: print(line); print()
    # print(get_vertical_word(puzzle, 0, 0, 4))
    # j = 0
    # i = 3
    # l = 4
    # print((puzzle[j][i-l+1:i+1])[::-1])
    # print(get_diagonal_word(puzzle, 4, 4, len(WORD), -1, -1))
