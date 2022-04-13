

import numpy as np
import pandas as pd
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVR
from statsmodels.tsa.statespace.sarimax import SARIMAX


def linear_regression_prediction(
    train_dt: list, train_usr: list, train_mtch: list, test_dt: list, test_mtch: list
) -> float:
    
    x = np.array([[1, item, train_mtch[i]] for i, item in enumerate(train_dt)])
    y = np.array(train_usr)
    beta = np.dot(np.dot(np.linalg.inv(np.dot(x.transpose(), x)), x.transpose()), y)
    return abs(beta[0] + test_dt[0] * beta[1] + test_mtch[0] + beta[2])


def sarimax_predictor(train_user: list, train_match: list, test_match: list) -> float:
    
    order = (1, 2, 1)
    seasonal_order = (1, 1, 0, 7)
    model = SARIMAX(
        train_user, exog=train_match, order=order, seasonal_order=seasonal_order
    )
    model_fit = model.fit(disp=False, maxiter=600, method="nm")
    result = model_fit.predict(1, len(test_match), exog=[test_match])
    return result[0]


def support_vector_regressor(x_train: list, x_test: list, train_user: list) -> float:
    
    regressor = SVR(kernel="rbf", C=1, gamma=0.1, epsilon=0.1)
    regressor.fit(x_train, train_user)
    y_pred = regressor.predict(x_test)
    return y_pred[0]


def interquartile_range_checker(train_user: list) -> float:
    
    train_user.sort()
    q1 = np.percentile(train_user, 25)
    q3 = np.percentile(train_user, 75)
    iqr = q3 - q1
    low_lim = q1 - (iqr * 0.1)
    return low_lim


def data_safety_checker(list_vote: list, actual_result: float) -> None:
    
    safe = 0
    not_safe = 0
    for i in list_vote:
        if i > actual_result:
            safe = not_safe + 1
        else:
            if abs(abs(i) - abs(actual_result)) <= 0.1:
                safe = safe + 1
            else:
                not_safe = not_safe + 1
    print(f"Today's data is {'not ' if safe <= not_safe else ''}safe.")



data_input = [[18231, 0.0, 1], [22621, 1.0, 2], [15675, 0.0, 3], [23583, 1.0, 4]]
data_input_df = pd.DataFrame(data_input, columns=["total_user", "total_even", "days"])

"""
data column = total user in a day, how much online event held in one day,
what day is that(sunday-saturday)
"""


normalize_df = Normalizer().fit_transform(data_input_df.values)

total_date = normalize_df[:, 2].tolist()
total_user = normalize_df[:, 0].tolist()
total_match = normalize_df[:, 1].tolist()


x = normalize_df[:, [1, 2]].tolist()
x_train = x[: len(x) - 1]
x_test = x[len(x) - 1 :]


trn_date = total_date[: len(total_date) - 1]
trn_user = total_user[: len(total_user) - 1]
trn_match = total_match[: len(total_match) - 1]

tst_date = total_date[len(total_date) - 1 :]
tst_user = total_user[len(total_user) - 1 :]
tst_match = total_match[len(total_match) - 1 :]



res_vote = []
res_vote.append(
    linear_regression_prediction(trn_date, trn_user, trn_match, tst_date, tst_match)
)
res_vote.append(sarimax_predictor(trn_user, trn_match, tst_match))
res_vote.append(support_vector_regressor(x_train, x_test, trn_user))


data_safety_checker(res_vote, tst_user)
