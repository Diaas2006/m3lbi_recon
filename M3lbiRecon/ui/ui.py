from ui.help import __help; from ui.banner import __banner
import modules.enumeration as enum

def UI(arguments):
    if arguments.help:
        __help()
        return
    else:
        __banner()
        url = arguments.target
        modes = arguments.mode

        modes_recon = {
            "dir": enum.__dir,
            "sub": enum.__sub,
            "all": enum.__all
        }
        
        for mode in modes:
            modes_recon.get(mode)(url)
    return