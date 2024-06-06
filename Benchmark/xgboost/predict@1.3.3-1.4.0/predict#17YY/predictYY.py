import xgboost as xgb
import numpy as np
X_train = np.array([[1, 2], [3, 4], [5, 6]])
y_train = np.array([0, 1, 0])
X_test = np.array([[2, 2], [4, 4]])
model = xgb.XGBClassifier(max_depth=3, n_estimators=100, learning_rate=0.1, objective='binary:logistic', eval_metric='logloss')
model.fit(X_train, y_train)
y_pred = model.predict(X_test,  False,  None, validate_features=True, base_margin=None)
