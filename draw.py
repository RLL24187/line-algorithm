from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if (x1 < x0): # x1 should always be >= x0
        x1, x0 = x0, x1
        y1, y0 = y0, y1 # have to reverse y's too

    A = int(y0) - int(y1) #change in Y
    B = int(x1) - int(x0) #negative change in X
    tempx = int(x0)
    tempy = int(y0)

    if (B == 0): # check vertical line first to prevent 0 division
        for y in range (y0, y1 + 1):
            plot(screen, color, tempx, y)
    else:
        slope = float(A / -B)
        print(slope)
        if (slope == 0): # horizontal line
            for x in range (x0, x1 + 1):
                plot(screen, color, x, tempy)

        # octant 1 and 5
        # print(slope)
        A2 = 2 * A
        B2 = 2 * B
        if (slope <= 1 and slope > 0 ):
            print("octant 1 or 5")
            d = A2 + B
            while (tempx <= x1):
                # print("A: " + str(A) + "| B: " + str(B))
                # print("d: " + str(d) + " x: " +str(x) + " y: " + str(y))
                plot (screen, color, tempx, tempy)
                if (d > 0):
                    tempy = tempy + 1
                    d = d + B2
                tempx = tempx + 1
                d = d + A2
