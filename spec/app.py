"""
Features and requirements for the smallest libspec example 
"""

from err import Feat, Req

class App(Req):
    '''This program found in project-root/main.py should emit the
    string "Hello, world!" to the terminal.
    '''

class CmdLine(Feat):
    '''
    This program does not take any command line arguments.
    '''
