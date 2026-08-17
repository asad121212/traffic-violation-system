from ultralytics import YOLO


class VehicleDetector:

    def __init__(self):

        self.vehicle_model = YOLO("models/vehicle.pt")
        self.helmet_model = YOLO("models/helmet.pt")

    def detect_vehicles(self, frame):

        return self.vehicle_model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            verbose=False,
        )

    def detect_helmets(self, frame):

     return self.helmet_model(
        frame,
        imgsz=1280,
        conf=0.20,
        verbose=False,
    )