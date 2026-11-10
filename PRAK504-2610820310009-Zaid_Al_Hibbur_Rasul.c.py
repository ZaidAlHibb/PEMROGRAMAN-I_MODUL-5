def reverse(n):
    return int(str(n)[::-1])

A, B = map(int, input().split())

A_prime = reverse(A)
B_prime = reverse(B)

C = A_prime + B_prime
print(reverse(C))