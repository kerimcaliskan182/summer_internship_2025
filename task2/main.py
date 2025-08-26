#Task 2 - Power of Four

""""
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

"""

# without loops or recursion 

def isPowerOfFour(n: int) -> bool:
    # pozitif mi 
    if n <= 0:
        return False

    # 2'nin kuvveti mi?  (tek bir bit 1 ise evet)
    if (n & (n - 1)) != 0:     
        return False

    # 3) mod 3 = 1 mi?
    if n % 3 != 1:
        return False

    return True

n = int(input("Bir sayı girin: "))

if isPowerOfFour(n):
    print("{} sayısı 4'ün kuvvetidir.".format(n))
else:
    print("{} sayısı 4'ün kuvveti değildir.".format(n))
   