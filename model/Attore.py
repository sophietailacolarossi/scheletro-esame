import time
from dataclasses import dataclass


@dataclass

class Attore:
    id: str
    name: str
    height: int
    date_of_birth: time.datetime
    known_for_movies: str

    def __hash__(self):
        return hash(self.id)
    def __eq__(self, other):
        return self.id == other.id
    def __str__(self):
        return f"{self.name} - {self.date_of_birth}"
