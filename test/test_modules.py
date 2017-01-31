import logging
import mock
import unittest

import dotm

class TestModules(unittest.TestCase):

    @mock.patch('dotm.util.list_dirs')
    def test_avail_modules(self, patch_list_dirs):
        dirs = ['bla','foo']
        patch_list_dirs.return_value = ['bla','foo']
        
        avail = dotm.modules.avail()
        self.assertListEqual(dirs, avail)

if __name__ == '__main__':
    unittest.main()
