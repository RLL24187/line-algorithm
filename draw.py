from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    A = int(y0) - int(y1) #change in Y
    B = int(x0) - int(x0) #change in X
    # slope = float(A / B)
    # # octant 1 and 5
    # print(slope)
    # if (slope <= 1 and slope > 0 ):
    print("octant 1 or 5")
    oct1(1, 1, x0, y0, x1, y1, screen, color)

def oct1(A, B, x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    d = (2 * A) + B
    while (x <= x1):
        # print("A: " + str(A) + "| B: " + str(B))
        # print("d: " + str(d) + " x: " +str(x) + " y: " + str(y))
        plot (screen, color, x, y)
        if (d > 0):
            y = y + 1
            d = d + (2 * B)
        x = x + 1
        d = d + (2 * A)
