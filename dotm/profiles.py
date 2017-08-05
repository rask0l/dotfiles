import os
import subprocess
import logging
from .thirdparty import yaml

from . import config
from . import util
from .util import _abs, Link
from . import modules

log = logging.getLogger("dotm").getChild(__name__)

class ProfileError(util.Error):
    def __init__(self, message):
        self.message = message

class Profile():
    """ Profile used for selecting different modules for different
    environments or computers."""
    def __init__(self, name):
        self.name = name
        self.path = os.path.join(config.profiles_dir, name)
        self.test_path = os.path.join(self.path, 'test')
        self.config_path = os.path.join(self.path, "profile.yaml")
        self.links = self._get_links()

    def test(self):
        if os.path.isfile(self.test_path):
            executed = subprocess.run(self.test_path)
            log.debug('Testing Profile: {}, Test Return Code: {}'.format(self.name, executed.returncode))
            return executed.returncode
        else:
            log.debug("Profile {0} does not contain test script".format(self.name))
            return 1

    def modules(self):
        """ Return all modules in this profile. """
        with open(self.config_path, 'r') as f:
            yml = yaml.load(f)
            try:
                mods = yml["modules"]
            except KeyError as e:
                # No modules
                return []
            return [ modules.Module(m) for m in mods ]

    def link(self):
        """ Link all modules in profile. """
        for m in self.modules():
            module.link()

    def unlink(self):
        """ Unlink all modules in profile. """
        for m in self.modules():
            module.unlink()

    def _get_links(self):
        """ Profiles can have files and links embedded in them.  This allows for overriding or profile specific
        without creating an additional module. """
        try:
            with open(self.config_path, 'r') as f:
                yml = yaml.load(f)
                try:
                    links = yml["links"]
                except KeyError as e:
                    # No links in this profile
                    return []
                targets = links.keys()
                return [Link(
                        _abs(config.dotfiles_dir,"profiles",self.name,t),
                        _abs(os.path.join(config.home,links[t])))
                    for t
                    in targets]
        except (OSError, IOError) as e:
            log.error("Profile file error: {0}".format(e))
            return []


def avail():
    """ Returns list of available profiles as Profiles() """
    ignore = ['git']
    return [Profile(x) for x in util.list_dirs(config.profiles_dir, ignore)]


def select():
    profs = avail()
    profs.sort(key=lambda x:x.name)
    log.debug("Available profiles: {}".format([x.name for x in profs]))
    for profile in profs:
        if profile.test() == 0:
            return profile
    else:
        print("No profiles passed their test for this environment.")


