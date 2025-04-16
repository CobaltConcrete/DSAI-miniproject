def isStrictlyPalindromic(n: int) -> bool:
    # 9 = 1 + 0*2 + 0*4 + 1*8

    for base in range(2, n-1):
        print(base)
        m = n
        binary = []
        while m != 0:
            remainder = m % base
            m //= base
            binary.insert(0, remainder)

        length = len(binary)
        left, right = 0, length-1

        while left < right:
            if binary[left] != binary[right]:
                return False

            left+=1
            right-=1

        print(binary)
        print('m', m)

    return True

isStrictlyPalindromic(9)
    