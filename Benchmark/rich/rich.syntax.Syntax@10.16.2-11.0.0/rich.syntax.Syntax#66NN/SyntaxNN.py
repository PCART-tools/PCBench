from rich.syntax import Syntax
syntax = Syntax(start_line=1, line_range=(1, 5), dedent=False, tab_size=4, background_color='yellow', indent_guides=True, highlight_lines={2, 3}, code_width=50, word_wrap=True, lexer_name='python', code="print('hello world')", line_numbers=True, theme='monokai')
