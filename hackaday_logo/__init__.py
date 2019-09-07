import displaybuffer
import utime
import leds

ROW_OFFSET = 9 #Used to center image vertically

values = [[((x * 360.0) / 11), 1.0, 1] for x in range(11)]


disp = displaybuffer.open()


def drawWrencher():
    for i in range((160*61)/8):
        row = int(i/20)+ROW_OFFSET
        column = int((i%20)*8)
        for j in range(8):
            if hackaday[i] & (1<<(7-j)):
                disp.pixel(column+j,row,col=[255,255,255])

counter = 0
while True:
    res = disp.rainbowbuff(counter)
    res = disp.wrencher()
    res = disp.showbuff()

    counter += 1
    if counter > 95:
        counter = 0

    if counter%7 == 0:
        x = values.pop()
        values.insert(0,x)
        leds.set_all_hsv(values)
    
