INSIDE = 0 # 0000 
LEFT = 1 # 0001 
RIGHT = 2 # 0010 
BOTTOM = 4 # 0100 
TOP = 8  # 1000 


xmax = 3.0
ymax = 3.0
xmin = -3.0
ymin = -3.0

#Line points
x1, y1 = 0.0, 0.0
x2, y2 = 4.0, 4.0
accept = True

def encode(x, y): 
    code = INSIDE 
    if x < xmin:     #อยู่นอกด้านซ้าย
        code |= LEFT 
    elif x > xmax:   #อยู่นอกด้านขวา
        code |= RIGHT 
    if y < ymin:     #
        code |= BOTTOM 
    elif y > ymax: #
        code |= TOP 

    return code 

def ClipLine():
    global accept
    global x1, y1, x2, y2

    while True: 
        code1 = encode(x1, y1) 
        code2 = encode(x2, y2) 
        if (code1 | code2) == 0: 
            accept = True
            break
        elif (code1 & code2) != 0:
            accept = False
            break
        else: 
            if not(code1):
                x1,y1,x2,y2 = x2,y2,x1,y1
                code1,code2, = code2,code1

            if code1 & TOP: 
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1) 
                y = ymax 
            elif code1 & BOTTOM: 
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1) 
                y = ymin 
            elif code1 & RIGHT: 
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1) 
                x = xmax 
            elif code1 & LEFT: 
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1) 
                x = xmin 

            if code1 == code1: 
                x1 = x 
                y1 = y 
                code1 = encode(x1, y1) 
            else: 
                x2 = x 
                y2 = y 
                code2 = encode(x2, y2) 

ClipLine() 
if accept:
    print ("Line points are (%.2f, %.2f)  and (%.2f, %.2f)" % (x1, y1, x2, y2))
else: 
    print("Line rejected") 