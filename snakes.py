:qclass Snake:
    """A dangerous and/or harmless serpent."""
    pass


class Cobra(Snake):
    """Definitely dangerous, yup."""
    
    def bite(self, other):
        """Deliver a dose of venom."""
        print("Snake~~~~~~~~~~~~~", other)

    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other):
        """Give a hug."""
        print("H~~~~~~u~~~~~g")

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""

    def __init__(self):
        """Create a new BoatConstrictor"""
        super().__init__()
        self.size = "enormous"
