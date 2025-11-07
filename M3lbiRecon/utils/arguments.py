import argparse

class SafeArgument(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)

def arguments():
    args = SafeArgument(add_help=False)

    args.add_argument(
        "--help", "-h",
        action="store_true",
    )
    args.add_argument(
        "--target", "-t",
        default="",
    )
    args.add_argument(
        "--mode", "-m",
        nargs="+",
        choices=["dir", "sub", "all"],
        default=["all"],
    )
    args.add_argument(
        "--silence", "-s",
        default=""
    )

    try:
        return args.parse_args()
    except ValueError:
        raise ValueError(
            "[bold red]An error occurred. Please check if you entered the arguments correctly, or use \"-h\" to open the help menu.[/bold red]"
        )
