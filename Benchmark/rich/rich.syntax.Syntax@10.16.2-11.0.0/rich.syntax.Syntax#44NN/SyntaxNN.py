from rich.syntax import Syntax
syntax = Syntax("print('hello world')", code_width=50, background_color='yellow', theme='monokai', indent_guides=True, tab_size=4, line_range=(1, 5), word_wrap=True, line_numbers=True, start_line=1, highlight_lines={2, 3}, lexer_name='python', dedent=False)
