from rich.syntax import Syntax
syntax = Syntax(tab_size=4, highlight_lines={2, 3}, line_range=(1, 5), start_line=1, code_width=50, line_numbers=True, dedent=False, word_wrap=True, code="print('hello world')", lexer_name='python', background_color='yellow', theme='monokai')
