from rich.syntax import Syntax
syntax = Syntax(theme='monokai', line_range=(1, 5), highlight_lines={2, 3}, code="print('hello world')", line_numbers=True, start_line=1, lexer_name='python', dedent=False, tab_size=4, code_width=50)
