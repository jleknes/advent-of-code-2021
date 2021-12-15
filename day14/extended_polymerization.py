import fileinput, time
from collections import Counter

rules = {}
memo = {}


def read_input():
    template = ""
    for line in fileinput.input():
        if "->" in line:
            lookup, insert = map(str.strip, line.split(" -> "))
            rules[lookup] = insert
        else:
            template += line.strip()
    return template


def count(seq, steps):
    if steps == 0:
        return Counter(seq)
    # slå opp i tabellen hvis innslag eksisterer
    if seq + str(steps) in memo:
        return memo[seq + str(steps)]
    else:
        insert = rules[seq]
        res = count(seq[0:1] + insert, steps - 1) + count(insert + seq[1:2], steps - 1) - Counter(insert)
        memo[seq + str(steps)] = res
        return res


def main():
    start_time = time.time()
    template = read_input()
    steps = 40
    res = Counter()
    for i in range(len(template) - 1):
        res += count(template[i : i + 2], steps)
    res -= Counter(template[1 : len(template) - 1])
    counter = Counter(res).most_common()
    print(counter[0][1] - counter[len(counter) - 1][1])

    print("--- %s seconds ---" % (time.time() - start_time))


main()