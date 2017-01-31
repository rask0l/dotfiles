import os
import logging

from . import config

log = logging.getLogger("dotm").getChild(__name__)

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

def list_dirs(dirname, ignore):
    """ List dirs in dirname that are not in ignore """
    dirs = []
    entries = os.listdir(dirname)
    for e in entries:
        d = os.path.join(dirname, e)
        if os.path.isdir(d) and e not in ignore:
            dirs.append(e)
    return dirs

def _abs(*args):
    return os.path.abspath(os.path.join(*args))

def _usr(*args):
    return os.path.expanduser(os.path.join(*args))

class Link():
    def __init__(self, target, link):
        """ Represents a softlink

        target: The link source
        link: The filename of the link
        """
        self.target = target
        self.link = link

    def __eq__(self, other):
        return ((_abs(self.target), _abs(self.link)) == 
                (_abs(other.target), _abs(other.link)))

    def __hash__(self):
        return hash((self.target,self.link))


    def create(self, dry_run):
        log.debug("link {} -> target {}".format(self.link, self.target))
        path, f = os.path.split(self.link)
        if not os.path.exists(path):
            if not dry_run: 
                os.makedirs(path)
        if os.path.isfile(self.link):
            log.debug(config.red + "Skipping " + config.color_end + self.link + ", it already exists") 
        else:
            if not dry_run: 
                os.symlink(self.target, self.link)
            log.debug(config.green + "+ Success!" + config.color_end) 

    def remove(self, dry_run):
        log.debug("removing link {} -> target {}".format(self.link, self.target))
        if os.path.lexists(self.link):
            if not dry_run: 
                os.unlink(self.link)
            log.debug(config.green + "+ Success!" + config.color_end) 
        else:
            log.debug(config.red + "- Skipping " + config.color_end + dest + ", it does not exist") 


