class Vehicle:

    def __init__(self, bike_box):

        # Motorcycle bounding box
        self.box = bike_box

        # List of rider bounding boxes
        self.riders = []

        # Helmet status
        self.with_helmet = False
        self.without_helmet = False

        # Number plate (Module 5)
        self.number_plate = None

        # Screenshot path (Module 6)
        self.image_path = None

    @property
    def rider_count(self):
        return len(self.riders)

    @property
    def triple_riding(self):
        return self.rider_count >= 3

    @property
    def no_helmet(self):
        return self.without_helmet

    @property
    def violation(self):
        return self.triple_riding or self.no_helmet