
def outer():
    x = "old"
    def changer():
        nonlocal x
        x = "new"
        print("Inner variable {}".format(x))
    print("Before change")
    print("Outer variable {}".format(x))
    changer()
    print("After change")
    print("Outer variable {}".format(x))

outer()
