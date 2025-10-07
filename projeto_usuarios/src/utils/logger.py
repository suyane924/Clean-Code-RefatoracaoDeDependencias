
from rich.console import Console
from datetime import datetime

console = Console()

def log_info(msg: str):
    console.print(f"[bold green]{msg}[/bold green]")

def log_warning(msg: str):
    console.print(f"[bold yellow]{msg}[/bold yellow]")

def log_error(msg: str):
    console.print(f"[bold red]{msg}[/bold red]")

def salvar_log_email(email: str, mensagem: str):
    with open("log_email.txt", "a") as f:
        f.write(f"{datetime.now()} - {email} - {mensagem}\n")
