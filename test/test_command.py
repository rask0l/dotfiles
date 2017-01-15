import logging
#import mock
import unittest

from dotm.cmd.command import Command

class TestCommand(unittest.TestCase):

    def test_parse(self):
        log = logging.getLogger('TestCommand.test_parse')
           
        args = ['test','--foo','--bar']
        c = Command('test')
        c.add_argument('--foo')
        c.add_argument('--bar')
        a, rest = c.parse(args)

        self.assertListEqual(a, args)
        

if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger("TestCommand.test_parse").setLevel(logging.DEBUG)
    unittest.main()
