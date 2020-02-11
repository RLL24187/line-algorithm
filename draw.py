from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if (x1 < x0): # x1 should always be >= x0
        x1, x0 = x0, x1
        y1, y0 = y0, y1 # have to reverse y's too

    Y = int(y0) - int(y1) #change in Y a.k.a. A
    X = int(x0) - int(x0) #change in X a.k.a. -B
    x = x0
    y = y0

    if (X == 0): # check vertical line first to prevent 0 division
        for y in range (y0, y1 + 1):
            plot(screen, color, x, y)
    else:
        slope = float(Y / X)
        if (slope == 0): # horizontal line
            for x in range (x0, x1 + 1):
                plot(screen, color, x, y)

        # octant 1 and 5
        # print(slope)
        A2 = 2 * Y
        B2 = -2 * X
        if (slope <= 1 and slope > 0 ):
            print("octant 1 or 5")
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
