import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_id(self):
        r1 = Rectangle(2, 10)
        r2 = Rectangle(10, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_value_getter(self):
        rec = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.height, 2)

    def test_assign_errors(self):
        self.assertRaises(TypeError, Rectangle, "feranmi", "sharon")
        self.assertRaises(ValueError, Rectangle, 0, 3)
        self.assertRaises(ValueError, Rectangle, 3, 0)
        self.assertRaises(ValueError, Rectangle, 2, 3, -1, 3)
        self.assertRaises(ValueError, Rectangle,  -2, 0)

if __name__ == "__main__":
    unittest.main()
