from subprocess import call
import os

def main():
    """
    Controls the flow of the program
    """
    createdb()
    deletedb()

def command_formater(command):
    """
    Formats the commands for the subprocess.call function
    """
    return command.split(" ")

def createdb():
    """
    Creates a test database
    """
    command = "createdb crazcalm"
    print(command_formater(command))
    call(command_formater(command))

def deletedb():
    """
    Deletes the test database
    """
    command = "dropdb crazcalm"
    print(command_formater(command))
    call(command_formater(command))

if __name__ == "__main__":
    main()
