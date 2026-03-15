from rich.console import Console
from rich.table import Table

console = Console()

def print_report(entropy, score, strength, crack_times, attack_results, suggestions):

    console.print("\n[bold cyan]Password Security Report[/bold cyan]\n")

    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("Metric")
    table.add_column("Result")

    table.add_row("Entropy", str(entropy))
    table.add_row("Score", f"{score}/100")
    table.add_row("Strength", strength)

    console.print(table)

    console.print("\n[bold yellow]Crack Time Estimates[/bold yellow]")

    for device, years in crack_times.items():
        console.print(f"{device}: {years} years")

    console.print("\n[bold red]Attack Simulation[/bold red]")

    for attack, result in attack_results.items():

        if result in ["COMPROMISED", "HIGH RISK", "LIKELY"]:
            console.print(f"{attack}: [bold red]{result}[/bold red]")
        else:
            console.print(f"{attack}: [bold green]{result}[/bold green]")

    console.print("\n[bold green]Security Suggestions[/bold green]")

    if suggestions:
        for s in suggestions:
            console.print(f"- {s}")
    else:
        console.print("No suggestions. Password looks strong.")