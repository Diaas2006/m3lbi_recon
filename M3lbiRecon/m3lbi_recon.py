import sys;
from rich.console import Console;
from utils.arguments import arguments as args
from utils.validate_url import validUrl; from ui.ui import UI

console = Console()

def main():
    try:
        argv = args()
        if not validUrl(argv.target) and not argv.help:
            console.print("[bold red]Invalid URL.[/bold red]")
            return
        else:
            UI(argv)
            return
        
    except (KeyboardInterrupt, EOFError):
        console.print("[bold red]Operation cancelled by user.[/bold red]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[bold red]An error occurred:[/bold red] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()