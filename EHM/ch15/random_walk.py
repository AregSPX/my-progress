from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_walk(self):
         # Decide which direction to go, and how far to go.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            self.x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            self.y_step = y_direction * y_distance

    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            self.get_walk()
            
            # Reject moves that go nowhere.
            if self.x_step == 0 and self.y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + self.x_step
            y = self.y_values[-1] + self.y_step

            self.x_values.append(x)
            self.y_values.append(y)
    
    