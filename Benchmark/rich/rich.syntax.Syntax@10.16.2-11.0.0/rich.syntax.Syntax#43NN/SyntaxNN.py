from rich.syntax import Syntax
syntax = Syntax("print('hello world')", lexer_name='python', start_line=1, line_numbers=True, highlight_lines={2, 3}, tab_size=4, line_range=(1, 5), background_color='yellow', dedent=False, theme='monokai', code_width=50, word_wrap=True)
