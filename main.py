from display import *
from draw import *
import math

s = new_screen()
c = [ 0, 255, 0 ]

# #octants 1 and 5
# draw_line(0, 0, XRES-1, YRES-1, s, c)
# draw_line(0, 0, XRES-1, int(YRES / 2), s, c)
# draw_line(XRES-1, YRES-1, 0, int(YRES / 2), s, c)
#
# #octants 8 and 4
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES-1, 0, s, c);
# draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
# draw_line(XRES-1, 0, 0, YRES/2, s, c);
#
# #octants 2 and 6
# c[RED] = 255;
# c[GREEN] = 0;
# c[BLUE] = 0;
# draw_line(0, 0, XRES/2, YRES-1, s, c);
# draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);
#
# #octants 7 and 3
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES/2, 0, s, c);
# draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);
#
# #horizontal and vertical
# c[BLUE] = 0;
# c[GREEN] = 255;
# draw_line(0, int(YRES/2), XRES-1, int(YRES/2), s, c);
# draw_line(int(XRES/2), 0, int(XRES/2), YRES-1, s, c);


x0 = int(XRES/2)
y0 = int(YRES/2)

for x in range (0, XRES + 1):
    x1 = int(XRES / x)
    y1 = int(math.sin(x)) + int(math.cos(x))
    draw_line(x0, y0, x1, y1, s, c)
    if (x < (XRES + 1) / 3):
        c[RED] = (c[RED] + 1) % 256
    elif (x < (XRES + 1) * 2 / 3):
        c[BLUE] = (c[BLUE] - 1) % 256
    else:
        c[GREEN] = (c[GREEN] + 1) % 256
    x += 3
    if (x % 5 == 0):
        draw_line(x1, y0, x1, y1, s, [255, 255, 255])
    if (x % 7 == 0):
        draw_line(x1, y1, x0, y1, s, [255, 30, 240])

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
