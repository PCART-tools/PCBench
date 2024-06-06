from rich.syntax import Syntax
syntax = Syntax(dedent=False, start_line=1, line_range=(1, 5), theme='monokai', code_width=50, highlight_lines={2, 3}, line_numbers=True, lexer_name='python', code="print('hello world')")
