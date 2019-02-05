# 1. Napisz program, który zwraca ciąg Fibonacciego od 1 do granicy wyznaczonej przez dowolną liczbę x. 
# Np. dla x = 8, program powinien wyprintować 1, 1, 2, 3, 5, 8
# (wzór na n-ty wyraz ciągu: an = an-1 + an-2)


x = 100
a = 1
b = 1

while a + b <= x:
    if b == 1:
        print(a)
        print(b)
    temp = b
    b += a
    a = temp
    print(b)

print("#############")
# 2. Napisz program, który skończony ciąg geometryczny dla następujących parametrów: a - wyraz początkowy; q - iloraz ciągu; g - granica ciągu

#zmienne parametry:
a = 1
q = 3
g = 150

# algorytm:
an = a
while an <= g:
    print(an)
    an *= q

print("############")
# 3. Napisz program, który dla określonych parametrów ciągu geometrycznego a - wyraz początkowy, q - iloraz ciągu, n - poszukiwany wyraz, zwróci n-ty wyraz ciągu

a = 1
q = 4
n = 5

an = a*q**(n-1)
print(an)