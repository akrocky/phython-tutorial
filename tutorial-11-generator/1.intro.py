
# normal function1-return2- variable are garbage


# Gen Fun
# 1yield
# -acess to variable after function execution
def firsr_Generator():
    x = 1
    print("1st iteration")
    yield x
    x = 2
    print("2nd iteration")

    x = 3
    print("3rd generator")
    yield x


my_gen = firsr_Generator()
print(my_gen)
print(next(my_gen))
