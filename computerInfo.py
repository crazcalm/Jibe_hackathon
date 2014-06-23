import sys

def info():
    """
    Returns the operating system name and the version of python in use.
    """
    python_version = sys.version_info
    operating_system = sys.platform
    return (python_version, operating_system)

if __name__ == "__main__":
    print(info())
