import os
import logging
from .thirdparty import yaml

from . import config
from . import util
from .util import _abs, Link

log = logging.getLogger("dotm").getChild(__name__)

class ModuleError(util.Error):
    def __init__(self, message):
        self.message = message

class LinkError(ModuleError):
    def __init__(self, message):
        self.message = message

def avail():
    ignore = ['.git']
    module_dir = os.path.join(config.dotfiles_dir,'modules')
    return util.list_dirs(module_dir, ignore)
    
class Module():
    def __init__(self, name):
        self.name = name
        self.path = os.path.join(config.modules_dir, name)
        self._config_path = os.path.join(self.path, "module.yaml")

        self._config = self._get_config()
        self.links = self._get_links()
       
    """ Helper Functions """

    def _get_config(self):
        with open(self._config_path, 'r') as stream:
            return yaml.load(stream)


    def _get_links(self):
        if not self._config:
            raise ModuleError("Empty module config.")
        links = self._config['links']
        targets = links.keys()

        return [Link(
                    _abs(config.dotfiles_dir,"modules",self.name,t),
                    _abs(os.path.join(config.home,links[t]))) 
                for t 
                in targets]
        

    """ Public Functions """

    def config_path(self):
        return 

    def link(self, dry_run):
        """ Create links for this module. """
        log.debug("Linking module {}.".format(self.name))

        for l in self.links:
            l.create(dry_run)

    def unlink(self, dry_run):
        """ Remove links for this module. """
        log.debug("Unlinking module {}.".format(self.name))

        for l in self.links:
            l.remove(dry_run)
        
