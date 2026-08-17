import cv2
from ultralytics import YOLO

model = YOLO("models/helmet.pt")

cap = cv2.VideoCapture("videos/traffic.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame, verbose=False)

    annotated = results[0].plot()

    cv2.imshow("Helmet Detection", annotated)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()