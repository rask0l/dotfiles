import os
import logging
import yaml

from . import config
from . import util

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

class Link():
    def __init__(self, target, link):
        """ Represents a softlink

        target: The link source
        link: The filename of the link
        """
        self.target = target
        self.link = link

    def create(self):
        log.debug("link {} -> target {}".format(self.link, self.target))
        path, f = os.path.split(self.link)
        if not util.path_exists(path):
            os.makedirs(path)
        if os.path.isfile(self.link):
            log.debug(config.red + "Skipping " + config.color_end + self.link + ", it already exists") 
        else:
            os.symlink(self.target, self.link)
            log.debug(config.green + "+ Success!" + config.color_end) 

    def remove(self):
        log.debug("removing link {} -> target {}".format(self.link, self.target))
        if os.path.lexists(self.link):
            os.unlink(self.link)
            log.debug(config.green + "+ Success!" + config.color_end) 
        else:
            log.debug(config.red + "- Skipping " + config.color_end + dest + ", it does not exist") 


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

        def _abs(*args):
            return os.path.abspath(os.path.join(*args))

        return [Link(
                    _abs(config.dotfiles_dir,"modules",self.name,t),
                    _abs(os.path.join(config.home,links[t]))) 
                for t 
                in targets]
        

    """ Public Functions """

    def config_path(self):
        return 

    def link(self):
        """ Create links for this module. """
        log.debug("Linking module {}.".format(self.name))

        for l in self.links:
            l.create()

    def unlink(self):
        """ Remove links for this module. """
        log.debug("Unlinking module {}.".format(self.name))

        for l in self.links:
            l.remove()
        
