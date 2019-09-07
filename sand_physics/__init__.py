import displaybuffer
import utime
import bhi160

disp = displaybuffer.open()
column = 0
lasttiltx = 0
lasttilty = 0
bhi = bhi160.BHI160Accelerometer()

for i in range(40):
    disp.setbuff(i,i,0xFF,0xFF);

while True:
    step = 0

    sensorData = bhi.read()
    #print(sensorData)
    if sensorData:
        tiltx = sensorData[0].x
        tilty = sensorData[0].y
    else:
        tiltx = lasttiltx
        tilty = lasttilty

    res = 0
    if tilty > 0.2:
        res = disp.driftsouth();
    elif tilty < -0.2:
        res = disp.driftnorth();
    if tiltx > 0.2:
        res = disp.driftwest();
    elif tiltx < -0.2:
        res = disp.drifteast();

    lasttiltx = tiltx
    lasttilty = tilty

    if res != 0:
        res = disp.showbuff();
