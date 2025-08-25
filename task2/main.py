#Task 2 - Power of Four

def isPowerOfFour(n: int) -> bool:
    if n <= 0:
        return False
    while n % 4 == 0:
        n //= 4
    return n == 1

n = int(input("Bir sayı girin: "))

if isPowerOfFour(n):
    print("{} sayısı 4'ün kuvvetidir.".format(n))
else:
    print("{} sayısı 4'ün kuvveti değildir.".format(n))

   