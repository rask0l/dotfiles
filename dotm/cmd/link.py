import logging
from .. import profiles
from .. import modules
from .command import Command
from argparse import ArgumentParser

log = logging.getLogger("dotm").getChild(__name__)

# Link Command
def link(args):
    log.debug('CALLED LINK FANCY')
    log.debug("args: {}".format(args))

    profile = profiles.select()

    # for each desired module, create softlink
    mods = profile.modules()
    for m in mods:
        m.link()
 

linkParser = ArgumentParser()
linkParser.add_argument('--dry-run')
LinkCmd = Command(name='link', parser=linkParser, action=link)
