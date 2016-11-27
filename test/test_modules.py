import mock
import unittest

def avail_modules(d):
    ignore = ['.git']
    dirs = []
    entries = os.listdir(d)
    for e in entries:
        d = os.path.join(d, e)
        if os.path.isdir(d) and e not in ignore:
            dirs.append(e)
    print(dirs)
    return dirs

class TestModules(unittest.TestCase):
    
    @patch(
    def test_avail_modules(self):
        mods = avail_modules("/test")
        self.assertEqual(1, 1)

    def test_isupper(self):
        self.assertTrue(True)
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()
