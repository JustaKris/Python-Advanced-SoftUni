n, m = [int(num) for num in input().split()]

n_set = set()
for _ in range(n):
    number = int(input())
    n_set.add(number)

m_set = set()
for _ in range(m):
    number = int(input())
    m_set.add(number)

print(*n_set.intersection(m_set), sep="\n")
