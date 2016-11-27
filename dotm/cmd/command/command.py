import logging
from ... import util

#from argparse import ArgumentParser

log = logging.getLogger("dotm").getChild(__name__)
""" The List of possible commands supported by the program """
CommandList = []
""" The command that will be executed for the user based on program arguments """
ExecutingCommand = None

class ParseError(util.Error):
    def __init__(self, message):
        self.message = message

class Command:
    def __init__(self, name=None, parser=None, action=None, args=None):
        self.parser=parser
        self.name=name
        self.action=action
        self.args=args

    def execute(self):
        log.debug("{}.execute({})".format(self.name, self.args))
        self.action(self.args)

def parse(argv):
    """ Determine from argument vector the command to be executed """
    log.debug("parsin {}".format(argv))
    to_match = argv[1]
    for c in CommandList:
        if c.name == to_match:
            global ExecutingCommand
            ExecutingCommand = c
            ExecutingCommand.args = argv[2:]
            log.debug("Found {}".format(c.name))
            break
    else:
        raise ParseError("No match found for {}".format(to_match))

def execute():
    log.debug("executin {}".format(ExecutingCommand.name))
    ExecutingCommand.execute()

def list_commands():
    for c in CommandList:
        log.debug(c.name)

def add_command(command):
    validate_command(command)
    CommandList.append(command)

def validate_command(command):
    # Check to make sure its a valid command
    pass
