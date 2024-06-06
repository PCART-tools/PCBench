from matplotlib.cbook import normalize_kwargs
kw = {'alpha': 0.5, 'linestyle': 'dashed', 'linewidth': 2}
alias_mapping = {'alpha': 'a', 'linestyle': 'ls'}
result = normalize_kwargs(kw, alias_mapping=alias_mapping, required=['alpha', 'linestyle', 'linewidth'], forbidden=[], allowed=[])
print(result)
