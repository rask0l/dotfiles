import sys
import logging
import argparse
log = logging.getLogger('dotm').getChild(__name__)

# import cmds
from .link import link
from .unlink import unlink
from .sync import sync

parser = argparse.ArgumentParser()
parser.add_argument('--dry-run', action='store_true')
#subparsers = parser.add_subparsers(help='sub-command help')
subparsers = parser.add_subparsers()

link_parser = subparsers.add_parser('link')
link_parser.set_defaults(func=link)

unlink_parser = subparsers.add_parser('unlink')
unlink_parser.set_defaults(func=unlink)

sync_parser = subparsers.add_parser('sync')
sync_parser.add_argument('--dirs', '-l')
sync_parser.add_argument('--depth', '-d', type=int)
sync_parser.set_defaults(func=sync, depth=1, dirs='~,~/.config,~/.config/rc.d,~/.config/zshrc.d')

def run(argv):
    args = parser.parse_args(argv[1:])

    if hasattr(args, 'func'):
        args.func(args)
    else:
        log.error("You must provide a subcommand.")
        print(parser.format_help())


__all__ = ['run']
