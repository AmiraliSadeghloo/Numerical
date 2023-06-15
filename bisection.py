def bisection(function, a, b, tol):
    if function(a)*function(b) >= 0:
        return False

    while (b-a)/2 > tol
        c = (a+b)/2
        if function(c) == 0:
            return c
        elif function(a)*function(c) < 0:
            b = c
        else:
            a = c

    return (a+b)/2


def test_function(x):
    return x**3-10


first_boundy = 5
second_bound = 3
tol = 0.001

answer = bisection(test_function, first_boundy, second_bound, tol)

print(answer)
