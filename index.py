# Assignment 1: Design Your Own Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def display_specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB"

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    def gaming_performance(self):
        return f"{self.brand} {self.model} has a powerful {self.gpu} GPU for gaming!"

phone = Smartphone("Samsung", "Galaxy S21", 128)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 256, "Adreno 660")
print(phone.display_specs())
print(gaming_phone.display_specs())
print(gaming_phone.gaming_performance())
