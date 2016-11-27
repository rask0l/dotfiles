import logging
from .. import profiles
from .. import modules
from .command import Command
from argparse import ArgumentParser

log = logging.getLogger("dotm").getChild(__name__)

# Unlink Command
def unlink(args):
    log.debug('CALLED UNLINK FANCY')
    log.debug("args: {}".format(args))

    profile = profiles.select()

    # for each desired module, create softlink
    mods = profile.modules()
    for m in mods:
        m.unlink()
 

unlinkParser = ArgumentParser()
unlinkParser.add_argument("--dry-run")
UnlinkCmd = Command(name='unlink', parser=unlinkParser, action=unlink)
