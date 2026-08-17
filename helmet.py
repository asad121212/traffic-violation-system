class HelmetAssociation:

    def __init__(self):
        # Maximum distance between a helmet/head detection
        # and the motorcycle center.
        self.max_distance = 180

    def associate(self, vehicles, helmet_results):

        if (
            helmet_results is None
            or len(helmet_results) == 0
            or helmet_results[0].boxes is None
        ):
            return

        for box in helmet_results[0].boxes:

            cls = int(box.cls[0])

            hx1, hy1, hx2, hy2 = map(int, box.xyxy[0])

            helmet_center_x = (hx1 + hx2) // 2
            helmet_center_y = (hy1 + hy2) // 2

            nearest_vehicle = None
            nearest_distance = float("inf")

            for vehicle in vehicles:

                bx1, by1, bx2, by2 = vehicle.box

                bike_center_x = (bx1 + bx2) // 2

                # We compare with the top of the motorcycle
                bike_head_y = by1

                distance = (
                    abs(helmet_center_x - bike_center_x)
                    + abs(helmet_center_y - bike_head_y)
                )

                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_vehicle = vehicle

            if nearest_vehicle is None:
                continue

            if nearest_distance > self.max_distance:
                continue

            # Model classes
            # 0 -> With helmet
            # 1 -> Without helmet

            if cls == 0:
                nearest_vehicle.with_helmet = True

            elif cls == 1:
                nearest_vehicle.without_helmet = True