from sklearn import linear_model
reg = linear_model.LassoLars(1.0,  True,  False,  True,  'auto', max_iter=500, eps=2.220446049250313e-16, copy_X=True)
