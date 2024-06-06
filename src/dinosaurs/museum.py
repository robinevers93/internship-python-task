class Museum:
    def __init__(self, dinosaurs: list[str]):
        self.dinosaurs: list[str] = ["Tyrannosaurus Rex", "Velociraptor", "Stegosaurus", "Spinosaurus"]

    def add_dinosaur(self, dinosaur: str) -> list[str]:
        self.dinosaurs.append(dinosaur)
        return self.dinosaurs

    def get_dinosaurs(self) -> list[str]:
        return self.dinosaurs

    def check_for_dinosaur(self, dinosaur: str) -> bool:
        if self.dinosaurs.pop() != dinosaur:
            self.check_for_dinosaur(dinosaur)
        else:
            return True

    def number_of_dinosaurs(self) -> int:
        return self.dinosaurs.__sizeof__()
