'''This function should test if the factor is a factor of base.

Return true if it is a factor or false if it is not.'''


def check_for_factor(base, factor):
    if base % factor == 0:
        return True
    return False


print(check_for_factor(10, 2))

#Done!!!