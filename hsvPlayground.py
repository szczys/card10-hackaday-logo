#Give me 72 values of hue covering full range (0-360)
values = [[((x*360.0)/72), 1.0, 1] for x in range(72)]

fastLEDrainbow = [
    [ 0xFF, 0x00, 0x00],
    [ 0xD5, 0x2A, 0x00],
    [ 0xAB, 0x55, 0x00],
    [ 0xAB, 0x7F, 0x00],
    [ 0xAB, 0xAB, 0x00],
    [ 0x56, 0xD5, 0x00],
    [ 0x00, 0xFF, 0x00],
    [ 0x00, 0xD5, 0x2A],
    [ 0x00, 0xAB, 0x55],
    [ 0x00, 0x56, 0xAA],
    [ 0x00, 0x00, 0xFF],
    [ 0x2A, 0x00, 0xD5],
    [ 0x55, 0x00, 0xAB],
    [ 0x7F, 0x00, 0x81],
    [ 0xAB, 0x00, 0x55],
    [ 0xD5, 0x00, 0x2B]
    ]

def spreadFastRainbow(steps=5):
    expandedRainbow = list()
    for i in range(len(fastLEDrainbow)):
        thisColor = fastLEDrainbow[i]
        if i == (len(fastLEDrainbow)-1):
            nextColor = fastLEDrainbow[0]
        else:
            nextColor = fastLEDrainbow[i+1]
        rstep = (nextColor[0]-thisColor[0])/steps
        gstep = (nextColor[1]-thisColor[1])/steps
        bstep = (nextColor[2]-thisColor[2])/steps
        expandedRainbow.append(thisColor)
        for i in range(steps):
            expandedRainbow.append([int(thisColor[0]+(i*rstep)), int(thisColor[1]+(i*gstep)), int(thisColor[2]+(i*bstep))])
    return expandedRainbow
        
def rgb2rgb565(color):
    tempr = int(0b11111*(color[0]/255.0))
    tempg = int(0b111111*(color[1]/255.0))
    tempb = int(0b11111*(color[2]/255.0))

    return [tempr<<3 | tempg>>3, (tempg<<5 & 0xFF) | tempb]

def calcK(h,n):
    return ((h/60)+n)%6

def colorPercent(k,s,v):
    return v-v*s*max(min(k,4-k,1),0)

def hsv2rgb(h,s=1.0,v=1.0,rgb565=False):
    rk = calcK(h,5)
    gk = calcK(h,3)
    bk = calcK(h,1)

    rP = colorPercent(rk,s,v)
    gP = colorPercent(gk,s,v)
    bP = colorPercent(bk,s,v)

    if rgb565:
        tempr = int(0b11111*rP)
        tempg = int(0b11111*gP)
        tempb = int(0b11111*bP)

        return [tempr<<3 | tempg>>3, (tempg<<5 & 0xFF) | tempb]
    
    return [int(rP*255),int(gP*255),int(bP*255)]

x = spreadFastRainbow()
smoothRainbow = list()
for i in x:
    smoothRainbow.append(rgb2rgb565(i))

print(smoothRainbow)
