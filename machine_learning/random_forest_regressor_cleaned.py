
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


def main():

    

    
    boston = load_boston()
    print(boston.keys())

    
    X = boston["data"]  
    Y = boston["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.3, random_state=1
    )

    
    rand_for = RandomForestRegressor(random_state=42, n_estimators=300)
    rand_for.fit(x_train, y_train)

    
    predictions = rand_for.predict(x_test)
    predictions = predictions.reshape(len(predictions), 1)

    
    print(f"Mean Absolute Error:\t {mean_absolute_error(y_test, predictions)}")
    print(f"Mean Square Error  :\t {mean_squared_error(y_test, predictions)}")


if __name__ == "__main__":
    main()
