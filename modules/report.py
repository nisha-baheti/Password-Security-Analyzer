from rich.console import Console
from rich.table import Table

console = Console()

def print_report(entropy, score, strength, crack_times, attack_results):

    console.print("\n[bold cyan]Password Security Report[/bold cyan]\n")

    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("Metric")
    table.add_column("Result")

    table.add_row("Entropy", str(entropy))
    table.add_row("Score", f"{score}/100")
    table.add_row("Strength", strength)

    console.print(table)

    console.print("\n[bold yellow]Crack Time Estimates[/bold yellow]")

    console.print(f"Estimated crack time: {crack_times} years")

    console.print("\n[bold red]Attack Simulation[/bold red]")

    for attack, result in attack_results.items():
        console.print(f"{attack}: {result}")