from rich.syntax import Syntax
syntax = Syntax("print('hello world')",  'python', tab_size=4, dedent=False, line_range=(1, 5), line_numbers=True, start_line=1, theme='monokai', code_width=50, highlight_lines={2, 3})
