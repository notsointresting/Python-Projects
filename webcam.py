import cv2

imgcap = cv2.VideoCapture(0)
result = True

while result:
    ret, frame = imgCapture.read()
    cv2.imwrite('test.jpg',frame)

    result = False
    print('Image Captured')

imgcapture.release()