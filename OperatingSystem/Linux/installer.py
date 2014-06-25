"""
  I am using this file as an attempt to refactor the installation process. I
want to write the function here and then import them when needed.
"""
from subprocess import call


def command_formater(command):
    """
    Formats the commands for the subprocess.call function
    """
    return command.split(" ")

def install(packages):
    """
    Makes terminal commands to install packages
    """
    command = "sudo apt-get install " + packages
    call(command_formater(command))
