from rich.console import Console
console = Console()
json_data = '{"name": "John", "age": 30, "city": "New York"}'
console.print_json(data=None, indent=4, json=json_data)
