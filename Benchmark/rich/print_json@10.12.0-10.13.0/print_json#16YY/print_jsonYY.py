from rich.console import Console
console = Console()
json_data = '{"name": "John", "age": 30, "city": "New York"}'
console.print_json(highlight=True, json=json_data)
