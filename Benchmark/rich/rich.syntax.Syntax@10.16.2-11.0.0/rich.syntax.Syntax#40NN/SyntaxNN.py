from rich.syntax import Syntax
syntax = Syntax("print('hello world')", start_line=1, dedent=False, highlight_lines={2, 3}, code_width=50, theme='monokai', line_range=(1, 5), lexer_name='python', line_numbers=True)
