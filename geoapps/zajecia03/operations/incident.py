class Incident:
    def __init__(self, id, description):
        self.id = id
        self.description = description

    def __repr__(self):
        return f"Incident(id={self.id!r}, description={self.description!r})"

    def __str__(self):
        return f"Incident {self.id}: {self.description}"