A = int(input('Enter first number: '))
B = int(input('Enter second number: '))
C = int(input('Enter third number: '))
if A >= B >= C:
    A *= 2
    B *= 2
    C *= 2
else:
    A, B = B, A
print(A, B, C)