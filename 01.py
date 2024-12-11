TEST_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

inp = open("./01_input.txt").read()

l = []
r = []
for line in inp.strip().split("\n"):
    a, b = line.split()
    l.append(int(a))
    r.append(int(b))

l.sort()
r.sort()

diffs = [abs(l[i] - r[i]) for i in range(len(l))]
total_distance = sum(diffs)

occurences = [l[i] * r.count(l[i]) for i in range(len(l))]
similarity_score = sum(occurences)

print(total_distance)
print(similarity_score)
