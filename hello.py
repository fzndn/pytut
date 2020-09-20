import math

def rumus_abc(a, b, c):
    x_1 = (-b + math.sqrt(b**2 - 4 * a * c))/(2 * a)

    x_2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c))/(2 * a)

    print("Akar-akarnya adalah " + str(x_1) + " dan " + str(x_2) + ".")

rumus_abc(1, 2, 1)    # x_1 = -1.0     x_2 = -1.0
rumus_abc(2, -5, -3)  # x_1 = -0.5     x_2 =  3.0