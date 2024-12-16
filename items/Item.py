class Item:
    def __init__(self, item_id, weight, value):
        self.id = item_id
        self.weight = weight
        self.value = value

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value

    def __str__(self):
        return f"Item{{id={self.id}, weight={self.weight}, value={self.value}}}"
