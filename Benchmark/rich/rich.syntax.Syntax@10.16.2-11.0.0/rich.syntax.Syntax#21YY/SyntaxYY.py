from rich.syntax import Syntax
syntax = Syntax("print('hello world')",  'python', tab_size=4, theme='monokai', code_width=50, line_numbers=True, dedent=False, highlight_lines={2, 3}, start_line=1, background_color='yellow', line_range=(1, 5), word_wrap=True)
