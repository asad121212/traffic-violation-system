from vehicle import Vehicle


class RiderAssociation:

    def __init__(self):
        # Maximum horizontal distance from bike center
        self.max_x_distance = 120

        # How far above the motorcycle a rider can be
        self.top_offset = 140

        # Small margin below the motorcycle
        self.bottom_offset = 40

    def associate(self, persons, motorcycles):

        vehicles = []

        for bike in motorcycles:

            vehicle = Vehicle(bike)

            bx1, by1, bx2, by2 = bike

            bike_center_x = (bx1 + bx2) // 2

            # Expanded region around the bike
            left = bike_center_x - self.max_x_distance
            right = bike_center_x + self.max_x_distance

            top = by1 - self.top_offset
            bottom = by2 + self.bottom_offset

            assigned = []

            for person in persons:

                px1, py1, px2, py2 = person

                person_center_x = (px1 + px2) // 2
                person_center_y = (py1 + py2) // 2

                if (
                    left <= person_center_x <= right
                    and top <= person_center_y <= bottom
                ):
                    assigned.append(person)

            # Remove duplicates if any
            unique_riders = []

            for rider in assigned:
                if rider not in unique_riders:
                    unique_riders.append(rider)

            vehicle.riders = unique_riders

            vehicles.append(vehicle)

        return vehicles