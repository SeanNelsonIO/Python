from sklearn import svm
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split



def NuSVC(train_x, train_y):
    svc_NuSVC = svm.NuSVC()
    svc_NuSVC.fit(train_x, train_y)
    return svc_NuSVC


def Linearsvc(train_x, train_y):
    svc_linear = svm.LinearSVC(tol=10e-2)
    svc_linear.fit(train_x, train_y)
    return svc_linear


def SVC(train_x, train_y):
    
    
    
    
    
    SVC = svm.SVC(gamma="auto")
    SVC.fit(train_x, train_y)
    return SVC


def test(X_new):
    
    iris = load_iris()
    
    train_x, test_x, train_y, test_y = train_test_split(
        iris["data"], iris["target"], random_state=4
    )
    
    
    
    current_model = Linearsvc(train_x, train_y)
    prediction = current_model.predict([X_new])
    return iris["target_names"][prediction][0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
