from rich.syntax import Syntax
syntax = Syntax("print('hello world')", line_range=(1, 5), highlight_lines={2, 3}, line_numbers=True, tab_size=4, start_line=1, code_width=50, dedent=False, lexer_name='python', theme='monokai', word_wrap=True)
