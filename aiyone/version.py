__version__ = '0.0.0'

__dev_status__ = "dev" 

if __dev_status__ != "stable":
    __full_version__ = f"{__version__}-{__dev_status__}"
else:
    __full_version__ = __version__
    
def get_version():
    return __version__

def get_full_version():
    return __full_version__