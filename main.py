import cv2

from detector import VehicleDetector
from association import RiderAssociation
from helmet import HelmetAssociation
from visualizer import Visualizer

# -----------------------------------
# Initialize Modules
# -----------------------------------

detector = VehicleDetector()
association = RiderAssociation()
helmet = HelmetAssociation()
visualizer = Visualizer()

# -----------------------------------
# Open Video
# -----------------------------------

# Use 0 for webcam
# Use "videos/traffic.mp4" for a video file

VIDEO_SOURCE = 0

cap = cv2.VideoCapture(VIDEO_SOURCE)

if not cap.isOpened():
    print("Could not open video.")
    exit()

# -----------------------------------
# Main Loop
# -----------------------------------

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Create a clean copy for drawing
    output = frame.copy()

    # ------------------------------
    # Detection
    # ------------------------------

    vehicle_results = detector.detect_vehicles(frame)
    helmet_results = detector.detect_helmets(frame)

    persons = []
    motorcycles = []

    # ------------------------------
    # Extract detections
    # ------------------------------

    if vehicle_results[0].boxes is not None:

        for box in vehicle_results[0].boxes:

            cls = int(box.cls[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            if cls == 0:
                persons.append((x1, y1, x2, y2))

            elif cls == 3:
                motorcycles.append((x1, y1, x2, y2))

    # ------------------------------
    # Associate riders
    # ------------------------------

    vehicles = association.associate(
        persons,
        motorcycles
    )

    # ------------------------------
    # Associate helmets
    # ------------------------------

    helmet.associate(
        vehicles,
        helmet_results
    )

    # ------------------------------
    # Draw everything ourselves
    # ------------------------------

    output = visualizer.draw(
        output,
        vehicles
    )

    cv2.imshow(
        "Traffic Violation Detection",
        output
    )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()