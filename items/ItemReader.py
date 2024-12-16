import os
from items.Item import Item

class ItemReader:
    @staticmethod
    def read_items(file_path):
        items = []
        try:
            with open(file_path, 'r') as file:
                id = 1
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split()
                        if len(parts) >= 2:
                            try:
                                weight = float(parts[0])
                                value = float(parts[1])
                                items.append(Item(id, weight, value))
                                id += 1
                            except ValueError:
                                # Handle the case where conversion to float fails
                                continue
        except IOError:
            print(f"Error reading the file: {file_path}")

        return items
