import random
N = int(input("Zadej počet čísel (1 až 100): "))

A = []
for i in range(N):
    A.append(random.randint(1, 15))

print("Původní pole náhodných čísel:")
print(A)

for i in range(0, N-1):
    for j in range(i+1, N):
        if A[i] < A[j]:  
            P = A[i]
            A[i] = A[j]
            A[j] = P
print("\nSeřazené pole (sestupně):")
print(A)