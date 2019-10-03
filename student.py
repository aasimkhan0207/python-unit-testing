class Student:
    """A sample Student class"""

    raise_score = 1.05

    def __init__(self, first, last, score):
        self.first = first
        self.last = last
        self.score = score

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.score = int(self.score * self.raise_score)
