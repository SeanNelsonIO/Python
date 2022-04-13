

import mpmath  
import numpy as np


class FFT:
    

    def __init__(self, polyA=None, polyB=None):
        
        self.polyA = list(polyA or [0])[:]
        self.polyB = list(polyB or [0])[:]

        
        while self.polyA[-1] == 0:
            self.polyA.pop()
        self.len_A = len(self.polyA)

        while self.polyB[-1] == 0:
            self.polyB.pop()
        self.len_B = len(self.polyB)

        
        self.C_max_length = int(
            2 ** np.ceil(np.log2(len(self.polyA) + len(self.polyB) - 1))
        )

        while len(self.polyA) < self.C_max_length:
            self.polyA.append(0)
        while len(self.polyB) < self.C_max_length:
            self.polyB.append(0)
        
        self.root = complex(mpmath.root(x=1, n=self.C_max_length, k=1))

        
        self.product = self.__multiply()

    
    def __DFT(self, which):
        if which == "A":
            dft = [[x] for x in self.polyA]
        else:
            dft = [[x] for x in self.polyB]
        
        if len(dft) <= 1:
            return dft[0]
        
        next_ncol = self.C_max_length // 2
        while next_ncol > 0:
            new_dft = [[] for i in range(next_ncol)]
            root = self.root**next_ncol

            
            current_root = 1
            for j in range(self.C_max_length // (next_ncol * 2)):
                for i in range(next_ncol):
                    new_dft[i].append(dft[i][j] + current_root * dft[i + next_ncol][j])
                current_root *= root
            
            current_root = 1
            for j in range(self.C_max_length // (next_ncol * 2)):
                for i in range(next_ncol):
                    new_dft[i].append(dft[i][j] - current_root * dft[i + next_ncol][j])
                current_root *= root
            
            dft = new_dft
            next_ncol = next_ncol // 2
        return dft[0]

    
    def __multiply(self):
        dftA = self.__DFT("A")
        dftB = self.__DFT("B")
        inverseC = [[dftA[i] * dftB[i] for i in range(self.C_max_length)]]
        del dftA
        del dftB

        
        if len(inverseC[0]) <= 1:
            return inverseC[0]
        
        next_ncol = 2
        while next_ncol <= self.C_max_length:
            new_inverseC = [[] for i in range(next_ncol)]
            root = self.root ** (next_ncol // 2)
            current_root = 1
            
            for j in range(self.C_max_length // next_ncol):
                for i in range(next_ncol // 2):
                    
                    new_inverseC[i].append(
                        (
                            inverseC[i][j]
                            + inverseC[i][j + self.C_max_length // next_ncol]
                        )
                        / 2
                    )
                    
                    new_inverseC[i + next_ncol // 2].append(
                        (
                            inverseC[i][j]
                            - inverseC[i][j + self.C_max_length // next_ncol]
                        )
                        / (2 * current_root)
                    )
                current_root *= root
            
            inverseC = new_inverseC
            next_ncol *= 2
        
        inverseC = [round(x[0].real, 8) + round(x[0].imag, 8) * 1j for x in inverseC]

        
        while inverseC[-1] == 0:
            inverseC.pop()
        return inverseC

    
    def __str__(self):
        A = "A = " + " + ".join(
            f"{coef}*x^{i}" for coef, i in enumerate(self.polyA[: self.len_A])
        )
        B = "B = " + " + ".join(
            f"{coef}*x^{i}" for coef, i in enumerate(self.polyB[: self.len_B])
        )
        C = "A*B = " + " + ".join(
            f"{coef}*x^{i}" for coef, i in enumerate(self.product)
        )

        return "\n".join((A, B, C))



if __name__ == "__main__":
    import doctest

    doctest.testmod()
