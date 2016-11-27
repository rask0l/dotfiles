import sys
import logging
log = logging.getLogger("dotm").getChild(__name__)

from .link import LinkCmd
from .unlink import UnlinkCmd
from .command import add_command
from .command import ParseError

add_command(LinkCmd)
add_command(UnlinkCmd)

from .command import parse
from .command import execute
from .command import list_commands

def run(argv):
    list_commands()
    
    try:
        parse(argv)
    except ParseError as e:
        log.error("Parse failed: {}".format(e.message))
        sys.exit(1)
    execute()

__all__ = ['run']
