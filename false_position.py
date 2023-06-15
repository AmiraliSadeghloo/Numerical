def false_position(func, a, b, tol):
    if func(a)*func(b) >= 0:
        return False

    while True:
        c = (a*func(b)-b*func(a))/(func(b)-func(a))

        if abs(func(c)) < tol:
            return c

        if func(a)*func(c) < 0:
            b = c
        else:
            a = c

    return False

def test_function(x):
    return x**2-4

tol = 0.001
root = false_position(test_function, 0, 3, tol)
print(root)
