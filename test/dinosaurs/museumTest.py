import unittest

from src.dinosaurs.museum import Museum

tyrannosaurus: str = "Tyrannosaurus Rex"
triceratops: str = "Triceratops"
velociraptor: str = "Velociraptor"

dinos_in_museum: list[str] = [tyrannosaurus, triceratops]
museum: Museum = Museum(dinos_in_museum)


class MuseumTest(unittest.TestCase):

    def test_initial_state(self):
        expected_dinosaurs: list[str] = [tyrannosaurus, triceratops]
        test_museum = Museum(expected_dinosaurs)
        museum_start = test_museum.get_dinosaurs()
        self.assertListEqual(museum_start, expected_dinosaurs)

    def test_check_dinosaur(self):
        test_museum = Museum([velociraptor])
        houses_tyrannosaurus = test_museum.check_for_dinosaur(triceratops)
        self.assertFalse(houses_tyrannosaurus)

    def test_adding_dinosaur(self):
        test_museum = Museum([])
        test_museum.add_dinosaur(triceratops)
        updated_museum = museum.get_dinosaurs()
        self.assertTrue(updated_museum.__contains__(triceratops))


if __name__ == '__main__':
    unittest.main()
