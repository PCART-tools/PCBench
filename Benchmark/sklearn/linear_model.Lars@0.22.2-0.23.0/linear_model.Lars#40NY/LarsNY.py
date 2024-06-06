from sklearn import linear_model
reg = linear_model.Lars(True,  False,  True,  'auto',  500, eps=2.220446049250313e-16, copy_X=True, fit_path=True)
