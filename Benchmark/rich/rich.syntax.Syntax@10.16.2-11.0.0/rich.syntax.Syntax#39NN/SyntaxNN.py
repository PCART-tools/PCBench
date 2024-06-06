from rich.syntax import Syntax
syntax = Syntax("print('hello world')", theme='monokai', start_line=1, lexer_name='python', dedent=False, highlight_lines={2, 3}, line_numbers=True, line_range=(1, 5))
