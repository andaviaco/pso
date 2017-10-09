
class Particle(object):
    best_pos = None

    """docstring for Particle"""
    def __init__(self, initial_position, initial_velocity):
        super(Particle).__init__()

        self.position = initial_position
        self.velocity = initial_velocity
        self.best_pos = initial_position

    def __repr__(self):
        return f'<Particle pos: {self.position} velocity: {self.velocity} >'
