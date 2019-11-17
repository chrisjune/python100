def one(n):
    def two(value):
        return value ** n
    return two

a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))


def power(fun):
    fun()
    def inner(value):
        return value ** 2
    return inner

@power
def make_power():
    print(1)

print(make_power(10))
