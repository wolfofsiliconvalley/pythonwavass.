
check_prime = [26, 39, 51, 53, 57, 79, 85]
for number in check_prime:
    for i in range(2, int(number**(1/2)) + 1):
        if (number%i == 0):
            factor = i
            print("{} is NOT a prime number, because {} is a factor of {}".format(number, factor, number))
            break

    else: # we can use for...else clause to reduce the use of flags
        print("{} IS a prime number".format(number))



