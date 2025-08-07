import unittest
from app import main

class TestApp(unittest.TestCase):
    def test_main(self):
        # This test just checks if main() runs without error
        try:
            main()
        except Exception as e:
            self.fail(f"main() raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
