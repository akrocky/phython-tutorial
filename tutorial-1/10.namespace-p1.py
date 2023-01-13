# --------------------------
# ----------------name space part 1-------------

# +++++++++++----Eample
# number =1001
# print(id(number))
# print(id(1001))
# --------example
a = 2
print("a:", id(a)
      )
a = a + 1
print("a1:", id(a))
print("three:", id(3))

b = 2
print("b:", id(b))
print("Two", id(2))
# --------example

something = 12
something = "jack"
something = ["a", 2, True]

# --------example


def hello():
    print("hello World")


something = hello
something()
