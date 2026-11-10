def max_bilangan(a, b, c, d):
    nilai_max = a
    if b > nilai_max:
        nilai_max = b
    if c > nilai_max:
        nilai_max = c
    if d > nilai_max:
        nilai_max = d
    return nilai_max

a, b, c, d = map(int, input().split())

hasil = max_bilangan(a, b, c, d)
print(hasil)