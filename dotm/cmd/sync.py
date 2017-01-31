import logging
import os
import re

from .. import profiles
from .. import modules
from .. import config
from ..util import _usr, Link

log = logging.getLogger("dotm").getChild(__name__)

# Sync Command
def sync(args):
    dry_run = args.dry_run
    if dry_run:
        log.info(" ============= DRY RUN ============= ")
    
    profile = profiles.select()

    # args.depth has default, safe to use
    src_dir = config.dotfiles_dir
    dirs = args.dirs
    found_links = set()
    for dir in dirs.split(','):
        links = find_links_from(dir, args.depth, src_dir)
        found_links |= links
    mods = profile.modules()
    desired_links = set()
    for p in profile.links:
        desired_links.add(p)
    for m in mods:
        for l in m.links:
            desired_links.add(l)
    
    # Delete links that are present on filesystem but not in module
    delete_links = found_links - desired_links
    for l in delete_links:
        l.remove(dry_run)
    
    # Add links that are present in module but not on filesystem
    add_links = desired_links - found_links
    for l in add_links:
        l.create(dry_run)
 

def find_links_from(dir, depth, src_dir):
    found_links = set()
    nodes = os.listdir(os.path.expanduser(dir))
    for n in nodes: 
        check_node(_usr(dir, n), depth, src_dir, found_links)
    return found_links
        

def check_node(node, depth, src_dir, found_links):
    if depth == 0:
        return 
    if os.path.islink(node) and not os.path.isdir(node):
        if check_link(node, src_dir):
            # link target is in src_dir, we want to prune it if its not
            # in a module currently referenced in a profile
            found_links.add(Link(os.readlink(node), os.path.abspath(node)))
    elif os.path.isdir(node):
        check_node(node, depth-1, src_dir, found_links)


def check_link(link, src_dir):
    # if link path points to anything inside dotfiles dir then we pop 
    # it in a stack so that we can 
    target = os.readlink(link)
    result = re.match(src_dir, target)
    if result:
        return True
    return False

