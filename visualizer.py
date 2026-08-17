import cv2


class Visualizer:

    def __init__(self):
        pass

    def draw(self, frame, vehicles):

        for vehicle in vehicles:

            x1, y1, x2, y2 = vehicle.box

            # -------------------------
            # Decide color
            # -------------------------

            color = (0, 255, 0)

            if vehicle.violation:
                color = (0, 0, 255)

            # -------------------------
            # Draw motorcycle box
            # -------------------------

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                color,
                2,
            )

            # -------------------------
            # Build labels
            # -------------------------

            labels = []

            labels.append(f"Riders : {vehicle.rider_count}")

            if vehicle.triple_riding:
                labels.append("TRIPLE RIDING")

            if vehicle.no_helmet:
                labels.append("NO HELMET")

            # -------------------------
            # Draw background panel
            # -------------------------

            panel_height = 25 * len(labels)

            cv2.rectangle(
                frame,
                (x1, y1 - panel_height - 8),
                (x1 + 170, y1),
                color,
                -1,
            )

            # -------------------------
            # Draw labels
            # -------------------------

            y = y1 - panel_height + 12

            for label in labels:

                cv2.putText(
                    frame,
                    label,
                    (x1 + 5, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.55,
                    (255, 255, 255),
                    2,
                )

                y += 24

        return frame