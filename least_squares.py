def least_squares(x, y):
    n = len(x)

    plus_x = 0
    plus_y = 0
    plus_x_2 = 0
    plus_xy = 0

    for i in range(n):
        plus_x = plus_x+x[i]
        plus_y = plus_y+y[i]
        plus_x_2 = plus_x_2+x[i]**2
        plus_xy = plus_xy+(x[i]*y[i])

    a = (n*plus_xy-plus_x*plus_y)/(n*plus_x_2-plus_x**2)
    b = (plus_y-a*plus_x)/n

    return a, b

x = [1, 2, 3]
y = [4, 5, 6]

c, d = least_squares(x, y)
print(c, d)
