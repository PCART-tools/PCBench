from rich.syntax import Syntax
syntax = Syntax("print('hello world')",  'python', theme='monokai', line_numbers=True, start_line=1, background_color='yellow', highlight_lines={2, 3}, tab_size=4, dedent=False, code_width=50, indent_guides=True, word_wrap=True, line_range=(1, 5))
