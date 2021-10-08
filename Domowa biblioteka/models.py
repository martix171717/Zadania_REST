import json

class Towatches:
    def __init__(self):
        try:
            with open("towatches.json", "r") as f:
                self.towatches = json.load(f)
        except FileNotFoundError:
            self.towatches = []

    def all(self):
        return self.towatches

    def get(self, id):
        towatch = [towatch for towatch in self.all() if towatch['id'] == id]
        if towatch:
            return towatch[0]
        return []

    def create(self, data):
        self.towatches.append(data)
        self.save_all()

    def save_all(self):
        with open("towatches.json", "w") as f:
            json.dump(self.towatches, f)

    def update(self, id, data):
        towatch = self.get(id)
        if towatch:
            index = self.towatches.index(towatch)
            self.towatches[index] = data
            self.save_all()
            return True
        return False

    def delete(self, id):
        towatch = self.get(id)
        if towatch:
            self.towatches.remove(towatch)
            self.save_all()
            return True
        return False

towatches=Towatches()
