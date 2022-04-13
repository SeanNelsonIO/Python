import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


from sklearn.model_selection import train_test_split


from sklearn.preprocessing import PolynomialFeatures


dataset = pd.read_csv(
    "https://s3.us-west-2.amazonaws.com/public.gamelab.fun/dataset/"
    "position_salaries.csv"
)
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y)



def viz_polymonial():
    plt.scatter(X, y, color="red")
    plt.plot(X, pol_reg.predict(poly_reg.fit_transform(X)), color="blue")
    plt.title("Truth or Bluff (Linear Regression)")
    plt.xlabel("Position level")
    plt.ylabel("Salary")
    plt.show()
    return


if __name__ == "__main__":
    viz_polymonial()

    
    pol_reg.predict(poly_reg.fit_transform([[5.5]]))
    
