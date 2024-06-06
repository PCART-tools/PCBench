from rich.syntax import Syntax
syntax = Syntax("print('hello world')",  'python', line_numbers=True, highlight_lines={2, 3}, word_wrap=True, tab_size=4, theme='monokai', line_range=(1, 5), dedent=False, start_line=1, code_width=50)
