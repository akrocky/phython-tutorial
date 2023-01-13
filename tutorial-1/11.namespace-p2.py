# --------------------
# -----------Namespace part 2 ------------------

# -----------------------example

def outer():
    outer_number = 100
    global global_number
    global_number = 100

    def inner():
        inner_number = 200
        print("Inner number =", inner_number)
        print("Outer Number", outer_number)
    inner()


global_number = 300
outer()
print(global_number)
