
import numpy as np

try:
    import skfuzzy as fuzz
except ImportError:
    fuzz = None

if __name__ == "__main__":
    
    X = np.linspace(start=0, stop=75, num=75, endpoint=True, retstep=False)

    
    
    abc1 = [0, 25, 50]
    abc2 = [25, 50, 75]
    young = fuzz.membership.trimf(X, abc1)
    middle_aged = fuzz.membership.trimf(X, abc2)

    
    one = np.ones(75)
    zero = np.zeros((75,))
    
    union = fuzz.fuzzy_or(X, young, X, middle_aged)[1]
    
    intersection = fuzz.fuzzy_and(X, young, X, middle_aged)[1]
    
    complement_a = fuzz.fuzzy_not(young)
    
    difference = fuzz.fuzzy_and(X, young, X, fuzz.fuzzy_not(middle_aged)[1])[1]
    
    alg_sum = young + middle_aged - (young * middle_aged)
    
    alg_product = young * middle_aged
    
    bdd_sum = fuzz.fuzzy_and(X, one, X, young + middle_aged)[1]
    
    bdd_difference = fuzz.fuzzy_or(X, zero, X, young - middle_aged)[1]

    
    

    
    from matplotlib import pyplot as plt

    plt.figure()

    plt.subplot(4, 3, 1)
    plt.plot(X, young)
    plt.title("Young")
    plt.grid(True)

    plt.subplot(4, 3, 2)
    plt.plot(X, middle_aged)
    plt.title("Middle aged")
    plt.grid(True)

    plt.subplot(4, 3, 3)
    plt.plot(X, union)
    plt.title("union")
    plt.grid(True)

    plt.subplot(4, 3, 4)
    plt.plot(X, intersection)
    plt.title("intersection")
    plt.grid(True)

    plt.subplot(4, 3, 5)
    plt.plot(X, complement_a)
    plt.title("complement_a")
    plt.grid(True)

    plt.subplot(4, 3, 6)
    plt.plot(X, difference)
    plt.title("difference a/b")
    plt.grid(True)

    plt.subplot(4, 3, 7)
    plt.plot(X, alg_sum)
    plt.title("alg_sum")
    plt.grid(True)

    plt.subplot(4, 3, 8)
    plt.plot(X, alg_product)
    plt.title("alg_product")
    plt.grid(True)

    plt.subplot(4, 3, 9)
    plt.plot(X, bdd_sum)
    plt.title("bdd_sum")
    plt.grid(True)

    plt.subplot(4, 3, 10)
    plt.plot(X, bdd_difference)
    plt.title("bdd_difference")
    plt.grid(True)

    plt.subplots_adjust(hspace=0.5)
    plt.show()
