from rich.syntax import Syntax
syntax = Syntax(highlight_lines={2, 3}, line_range=(1, 5), code="print('hello world')", lexer_name='python', start_line=1, line_numbers=True, theme='monokai', dedent=False)
