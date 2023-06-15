def secant(test_function, prev_x, main_x, tol):
    while abs(test_function(main_x)) >= tol:
        main_f = test_function(main_x)
        prev_f = test_function(prev_x)
        next_x = main_x-(main_f*(main_x-prev_x))/(main_f-prev_f)
        prev_x = main_x
        main_x = next_x

    return main_x


def test_function(x):
    return x**3+x-1


first_guess = 1
second_guess = 2
tolerance = 0.001


answer = secant(test_function, first_guess, second_guess, tolerance)
print(answer)
