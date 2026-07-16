from rich.console import Console

console = Console()

"""Reads the content from file called filename that contains integers and return the list """
def readFromFile (filename:str) -> list[int]:
    with open(filename) as file:
        return [int(line.strip()) for line in file]
    

"""Takes a list of integers and return a transformed list that contains the squares of all the numbers """
def squaredList (numbers:list[int]) -> list[int]:
    return [n*n for n in numbers]


def main() -> None:
    numbers = readFromFile("sample.txt")
    squares = squaredList(numbers)

    console.rule("[bold blue]Day 1 Python Exercise")
    console.print(f"[green]Original Numbers:[/green] {numbers}")
    console.print(f"[cyan]Squared Numbers:[/cyan] {squares}")


if __name__ == "__main__":
    main()