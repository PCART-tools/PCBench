from rich.syntax import Syntax
syntax = Syntax("print('hello world')", tab_size=4, dedent=False, lexer_name='python', theme='monokai', line_range=(1, 5), line_numbers=True, start_line=1, code_width=50, highlight_lines={2, 3})
