from rich.syntax import Syntax
syntax = Syntax(line_numbers=True, code_width=50, theme='monokai', highlight_lines={2, 3}, dedent=False, tab_size=4, code="print('hello world')", line_range=(1, 5), word_wrap=True, lexer_name='python', start_line=1)
