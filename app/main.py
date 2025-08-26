import cv2
from detector import ObjectDetector

detector = ObjectDetector()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = detector.detect(frame)

    cv2.imshow('Object Detection', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

