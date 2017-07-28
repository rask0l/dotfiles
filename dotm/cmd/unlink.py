import logging
import sys
from .. import profiles
from .. import modules

log = logging.getLogger("dotm").getChild(__name__)

# Unlink Command
def unlink(args):
    dry_run = args.dry_run
    if dry_run:
        log.info(" ============= DRY RUN ============= ")

    profile = profiles.select()
    if not profile:
        sys.exit(1)

    # for each desired module, create softlink
    mods = profile.modules()
    for m in mods:
        m.unlink(dry_run)
 

