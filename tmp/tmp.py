import cv2 as cv

def test1():
    img = cv.imread('P2805__1__824___824.png')
    ll = open('P2805__1__824___824.txt').readlines()
    for l in ll:
        l2 = l.split(' ')
        print(l2)
        point_color = (0, 255, 0)
        thickness = 1
        lineType = 4
        cv.line(img, (int(float(l2[0])), int(float(l2[1]))), (int(float(l2[2])), int(float(l2[3]))), point_color, thickness, lineType)
        cv.line(img, (int(float(l2[4])), int(float(l2[5]))), (int(float(l2[2])), int(float(l2[3]))), point_color, thickness, lineType)
        cv.line(img, (int(float(l2[4])), int(float(l2[5]))), (int(float(l2[6])), int(float(l2[7]))), point_color, thickness, lineType)
        cv.line(img, (int(float(l2[0])), int(float(l2[1]))), (int(float(l2[6])), int(float(l2[7]))), point_color, thickness, lineType)

    cv.imwrite('test.png', img)

def test2():
    img = cv.imread('P2805__1__824___824.png')
    ll = open('P2805__1__824___824.txt').readlines()
    for l in ll:
        l2 = l.split(' ')
        print(l2)
        point_color = (0, 255, 0)
        thickness = 1
        lineType = 4

        x1 = max([int(float(l2[0])), int(float(l2[2])), int(float(l2[4])), int(float(l2[6]))])
        x2 = min([int(float(l2[0])), int(float(l2[2])), int(float(l2[4])), int(float(l2[6]))])
        y1 = max([int(float(l2[1])), int(float(l2[3])), int(float(l2[5])), int(float(l2[7]))])
        y2 = min([int(float(l2[1])), int(float(l2[3])), int(float(l2[5])), int(float(l2[7]))])

        cv.line(img, (x1, y1), (x2, y1), point_color, thickness, lineType)
        cv.line(img, (x2, y2), (x2, y1), point_color, thickness, lineType)
        cv.line(img, (x2, y2), (x1, y2), point_color, thickness, lineType)
        cv.line(img, (x1, y1), (x1, y2), point_color, thickness, lineType)

    cv.imwrite('test1.png', img)

test2()