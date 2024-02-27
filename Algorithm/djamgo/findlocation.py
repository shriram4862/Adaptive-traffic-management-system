import cv2

def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

cv2.namedWindow('ROI')
cv2.setMouseCallback('ROI', POINTS)

cap = cv2.VideoCapture('C:/Users/Admin/Downloads/djamgo-20240221T124800Z-001/djamgo/cars.mp4')
count = 0

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, int(frame.shape[0] * (640 / frame.shape[1]))))

    if not ret:
        break

    count += 1
    if count % 3 != 0:
        continue     

    cv2.imshow("ROI", frame)
    if cv2.waitKey(1) == ord('q'):  # changed waitKey(0) to waitKey(1) to avoid blocking
        break

cap.release()
cv2.destroyAllWindows()
