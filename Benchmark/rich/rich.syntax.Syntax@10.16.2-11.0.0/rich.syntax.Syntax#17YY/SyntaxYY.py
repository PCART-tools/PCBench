from rich.syntax import Syntax
syntax = Syntax("print('hello world')",  'python', start_line=1, line_numbers=True, theme='monokai', line_range=(1, 5), dedent=False, highlight_lines={2, 3})
