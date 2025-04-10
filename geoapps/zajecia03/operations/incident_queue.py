from .incident import Incident

class IncidentQueue:
    def __init__(self):
        self.__queue = []

    def __getitem__(self, position):
        return self.__queue[position]

    def __setitem__(self, position, value):
        self.__queue[position] = value

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.__queue):
            result = self.__queue[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __contains__(self, incident):
        return incident in self.__queue

    def __repr__(self):
        return f"IncidentQueue({self.__queue!r})"

    def __str__(self):
        if len(self):
            return "\n".join([f"{' ' * (4 * idx)}{incident}" for idx, incident in enumerate(self.__queue)])
        else:
            return "Empty queue"

    def __add__(self, other):
        if isinstance(other, Incident):
            new__queue = IncidentQueue()
            new__queue.__queue = self.__queue[:] 
            new__queue += other
            return new__queue
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Incident):
            new__queue = IncidentQueue()
            new__queue += other
            new__queue.__queue += self.__queue
            return new__queue
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Incident):
            self.__queue.append(other)
        return self

    def __call__(self, id):
        for incident in self.__queue:
            if incident.id == id:
                return incident
            pass
        raise ValueError("No incident found with the given ID")

    def __lt__(self, other):
        return len(self.__queue) < len(other.__queue)

    def __gt__(self, other):
        return len(self.__queue) > len(other.__queue)

    def __bool__(self):
        return bool(self.__queue)

    def __len__(self):
        return len(self.__queue)

if __name__ == "__main__":
    queue = IncidentQueue()
    incident1 = Incident(1, "Power outage in sector 4")
    incident2 = Incident(2, "Fire alarm in building 21")
    incident4 = Incident(4, "Fire alarm in building 129")

    print(f"---------- wyświetlanie za pomocą __str__ ----------")
    print(queue)

    print(f"---------- dodanie za pomocą __iadd__ ----------")
    queue += incident1
    queue += incident2
    print(queue)
    print(f"---------- dodanie za pomocą __add__ ----------")
    queue = queue + incident4
    print(queue)

    print(f"---------- dostęp za pomocą __getitem__ ----------")
    print(queue[0])
    print(f"---------- sprawdzenie za pomocą __contains__ ----------")
    print(incident1 in queue)

    print(f"---------- iteracja za pomocą __iter__ i __next__ ----------")
    for incident in queue:
        print(incident)

    print(f"---------- dodawanie prawostronne za pomocą __radd__ ----------")
    new_incident = Incident(3, "Test incident")
    queue = new_incident + queue

    print(f"---------- test za pomocą __bool__ ----------")
    if queue:
        print("Queue is not empty.")

    print(f"---------- długość kolejki za pomocą __len__ ----------")
    print(len(queue))

    print(f"---------- wyszukiwanie za pomocą __call__ ----------")
    print(queue(1))