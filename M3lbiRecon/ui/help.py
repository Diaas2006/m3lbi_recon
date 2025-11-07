from utils.clear import clear

from rich.console import Console;
from rich.panel import Panel

console = Console()

def __help():
    clear()
    help_text = (
        "[bold #6930c3]Usage:[/bold #6930c3]\n"
        "   m3lbi_recon.py -t <target>\n\n"

        "[bold #6930c3]Example:[/bold #6930c3]\n"
        "   python m3lbi_recon.py -t https://example.com\n\n"

        "[bold #6930c3]Options:[/bold #6930c3]\n"
        "   -h, --help      Show this help message\n"
        "   -t, --target    Target URL\n"
        "   -m, --mode      <dir, sub, all> \"all\" is default"
    )

    console.print(
        Panel.fit(
            help_text,
            border_style="bold #00ffd5",
            padding=(1, 3),
            title="[bold #00ffd5]M3lbiRecon Help[/bold #00ffd5]",
            title_align="center",
        )
    )