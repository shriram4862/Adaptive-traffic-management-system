import cv2

def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

cv2.namedWindow('ROI')
cv2.setMouseCallback('ROI', POINTS)

# Change the file path to your image file
image_path = 'C:\Users\Admin\Downloads\djamgo-20240221T124800Z-001\djamgo\cars.jpg'
frame = cv2.imread(image_path)

while True:
    frame_resized = cv2.resize(frame, (640, int(frame.shape[0] * (640 / frame.shape[1]))))

    cv2.imshow("ROI", frame_resized)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
