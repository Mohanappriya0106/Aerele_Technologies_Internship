"""
Day 1 Exercise
Java-style Python vs Pythonic Python
"""

from rich.console import Console

console = Console()

students = [
    {"name": "Alice", "marks": 90},
    {"name": "Bob", "marks": 82},
    {"name": "Charlie", "marks": 95},
]

console.rule("[bold red]Java-style Python")

# Java-style (Index based loop)
names = []

for i in range(len(students)):
    student = students[i]
    names.append(student["name"])

console.print(names)

console.rule("[bold green]Pythonic Version")

# Pythonic (Direct iteration + List comprehension)
names = [student["name"] for student in students]

console.print(names)