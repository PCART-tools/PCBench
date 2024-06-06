from rich.syntax import Syntax
syntax = Syntax("print('hello world')",  'python', start_line=1, theme='monokai', dedent=False, code_width=50, line_range=(1, 5), line_numbers=True, highlight_lines={2, 3})
