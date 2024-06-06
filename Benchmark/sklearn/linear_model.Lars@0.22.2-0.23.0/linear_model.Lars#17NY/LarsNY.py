from sklearn import linear_model
reg = linear_model.Lars(True,  False,  True,  'auto', n_nonzero_coefs=500)
