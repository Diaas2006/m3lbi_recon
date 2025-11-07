from utils.clear import clear

from rich.console import Console
from rich.panel import Panel
import pyfiglet

from time import sleep

console = Console()

def __banner():
    texto = "M3LBI L4W"
    banner = pyfiglet.figlet_format(texto)
    
    clear()

    console.print(
        Panel.fit(
            f"[bold #FF170F]{banner}[/bold #FF170F]",
            border_style="#ff00ea",
        )
    )
    sleep(3)
    clear()