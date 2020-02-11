from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    # print("x0: " + x0 + " x1: " + x1 + " y0: " + y0 + " y1: " + y1)
    if (x1 < x0): # x1 should always be >= x0
        x1, x0 = x0, x1
        y1, y0 = y0, y1 # have to reverse y's too

    A = int(y1) - int(y0) #change in Y
    B = int(x0) - int(x1) #negative change in X

    if (B == 0): # check vertical line first to prevent 0 division
        for y in range (y0, y1 + 1):
            plot(screen, color, x0, y)
    else:
        slope = float(A / -B)
        print(slope)
        if (slope == 0): # horizontal line
            for x in range (x0, x1 + 1):
                plot(screen, color, x, y0)

        # octant 1 and 5
        # print(slope)
        x = int(x0)
        y = int(y0)
        A2 = 2 * A
        B2 = 2 * B
        if (slope <= 1 and slope > 0 ):
            print("octant 1 or 5")
            d = A2 + B
            while (x <= x1):
                plot (screen, color, x, y)
                if (d > 0):
                    y = y + 1
                    d = d + B2
                x = x + 1
                d = d + A2
        # octant 2 and 6
        elif (slope > 1):
            print("octant 2 or 6")
            d = A + B2
            while (y <= y1):
                plot (screen, color, x, y)
                if d < 0:
                    x = x + 1
                    d = d + A2
                y = y + 1
                d = d + B2
        # octant 4 and 8
        elif (slope >= -1 and slope < 0):
            print("octant 4 or 8")
            d = A2 + B
            while (x <= x1):
                plot (screen, color, x, y)
                if d < 0:
                    y = y - 1
                    d = d - B2
                x = x + 1
                d = d + A2

        # octant 3 and 7
        elif (slope < -1):
            print("octant 3 or 7")
            d = A + B2
            while (y <= y1):
                plot (screen, color, x, y)
                if (d > 0):
                    x = x + 1
                    d = d + A2
                y = y - 1
                d = d - B2
