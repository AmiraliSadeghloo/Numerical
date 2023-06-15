def fixed_point(func, guess, tol):
    x = guess
    while True:
        next_x = func(x)
        if abs(next_x-x) < tol:
            return next_x
        x = next_x

def test_function(x):
    return 0.5*x+1

guess = 2
tol = 0.001

root = fixed_point(test_function, guess, tol)
print(root)
