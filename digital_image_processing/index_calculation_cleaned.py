





import numpy as np



class IndexCalculation:
    

    def __init__(self, red=None, green=None, blue=None, redEdge=None, nir=None):
        
        self.setMatrices(red=red, green=green, blue=blue, redEdge=redEdge, nir=nir)

    def setMatrices(self, red=None, green=None, blue=None, redEdge=None, nir=None):
        if red is not None:
            self.red = red
        if green is not None:
            self.green = green
        if blue is not None:
            self.blue = blue
        if redEdge is not None:
            self.redEdge = redEdge
        if nir is not None:
            self.nir = nir
        return True

    def calculation(
        self, index="", red=None, green=None, blue=None, redEdge=None, nir=None
    ):
        
        self.setMatrices(red=red, green=green, blue=blue, redEdge=redEdge, nir=nir)
        funcs = {
            "ARVI2": self.ARVI2,
            "CCCI": self.CCCI,
            "CVI": self.CVI,
            "GLI": self.GLI,
            "NDVI": self.NDVI,
            "BNDVI": self.BNDVI,
            "redEdgeNDVI": self.redEdgeNDVI,
            "GNDVI": self.GNDVI,
            "GBNDVI": self.GBNDVI,
            "GRNDVI": self.GRNDVI,
            "RBNDVI": self.RBNDVI,
            "PNDVI": self.PNDVI,
            "ATSAVI": self.ATSAVI,
            "BWDRVI": self.BWDRVI,
            "CIgreen": self.CIgreen,
            "CIrededge": self.CIrededge,
            "CI": self.CI,
            "CTVI": self.CTVI,
            "GDVI": self.GDVI,
            "EVI": self.EVI,
            "GEMI": self.GEMI,
            "GOSAVI": self.GOSAVI,
            "GSAVI": self.GSAVI,
            "Hue": self.Hue,
            "IVI": self.IVI,
            "IPVI": self.IPVI,
            "I": self.I,
            "RVI": self.RVI,
            "MRVI": self.MRVI,
            "MSAVI": self.MSAVI,
            "NormG": self.NormG,
            "NormNIR": self.NormNIR,
            "NormR": self.NormR,
            "NGRDI": self.NGRDI,
            "RI": self.RI,
            "S": self.S,
            "IF": self.IF,
            "DVI": self.DVI,
            "TVI": self.TVI,
            "NDRE": self.NDRE,
        }

        try:
            return funcs[index]()
        except KeyError:
            print("Index not in the list!")
            return False

    def ARVI2(self):
        
        return -0.18 + (1.17 * ((self.nir - self.red) / (self.nir + self.red)))

    def CCCI(self):
        
        return ((self.nir - self.redEdge) / (self.nir + self.redEdge)) / (
            (self.nir - self.red) / (self.nir + self.red)
        )

    def CVI(self):
        
        return self.nir * (self.red / (self.green**2))

    def GLI(self):
        
        return (2 * self.green - self.red - self.blue) / (
            2 * self.green + self.red + self.blue
        )

    def NDVI(self):
        
        return (self.nir - self.red) / (self.nir + self.red)

    def BNDVI(self):
        
        return (self.nir - self.blue) / (self.nir + self.blue)

    def redEdgeNDVI(self):
        
        return (self.redEdge - self.red) / (self.redEdge + self.red)

    def GNDVI(self):
        
        return (self.nir - self.green) / (self.nir + self.green)

    def GBNDVI(self):
        
        return (self.nir - (self.green + self.blue)) / (
            self.nir + (self.green + self.blue)
        )

    def GRNDVI(self):
        
        return (self.nir - (self.green + self.red)) / (
            self.nir + (self.green + self.red)
        )

    def RBNDVI(self):
        
        return (self.nir - (self.blue + self.red)) / (self.nir + (self.blue + self.red))

    def PNDVI(self):
        
        return (self.nir - (self.green + self.red + self.blue)) / (
            self.nir + (self.green + self.red + self.blue)
        )

    def ATSAVI(self, X=0.08, a=1.22, b=0.03):
        
        return a * (
            (self.nir - a * self.red - b)
            / (a * self.nir + self.red - a * b + X * (1 + a**2))
        )

    def BWDRVI(self):
        
        return (0.1 * self.nir - self.blue) / (0.1 * self.nir + self.blue)

    def CIgreen(self):
        
        return (self.nir / self.green) - 1

    def CIrededge(self):
        
        return (self.nir / self.redEdge) - 1

    def CI(self):
        
        return (self.red - self.blue) / self.red

    def CTVI(self):
        
        ndvi = self.NDVI()
        return ((ndvi + 0.5) / (abs(ndvi + 0.5))) * (abs(ndvi + 0.5) ** (1 / 2))

    def GDVI(self):
        
        return self.nir - self.green

    def EVI(self):
        
        return 2.5 * (
            (self.nir - self.red) / (self.nir + 6 * self.red - 7.5 * self.blue + 1)
        )

    def GEMI(self):
        
        n = (2 * (self.nir**2 - self.red**2) + 1.5 * self.nir + 0.5 * self.red) / (
            self.nir + self.red + 0.5
        )
        return n * (1 - 0.25 * n) - (self.red - 0.125) / (1 - self.red)

    def GOSAVI(self, Y=0.16):
        
        return (self.nir - self.green) / (self.nir + self.green + Y)

    def GSAVI(self, L=0.5):
        
        return ((self.nir - self.green) / (self.nir + self.green + L)) * (1 + L)

    def Hue(self):
        
        return np.arctan(
            ((2 * self.red - self.green - self.blue) / 30.5) * (self.green - self.blue)
        )

    def IVI(self, a=None, b=None):
        
        return (self.nir - b) / (a * self.red)

    def IPVI(self):
        
        return (self.nir / ((self.nir + self.red) / 2)) * (self.NDVI() + 1)

    def I(self):  
        
        return (self.red + self.green + self.blue) / 30.5

    def RVI(self):
        
        return self.nir / self.red

    def MRVI(self):
        
        return (self.RVI() - 1) / (self.RVI() + 1)

    def MSAVI(self):
        
        return (
            (2 * self.nir + 1)
            - ((2 * self.nir + 1) ** 2 - 8 * (self.nir - self.red)) ** (1 / 2)
        ) / 2

    def NormG(self):
        
        return self.green / (self.nir + self.red + self.green)

    def NormNIR(self):
        
        return self.nir / (self.nir + self.red + self.green)

    def NormR(self):
        
        return self.red / (self.nir + self.red + self.green)

    def NGRDI(self):
        
        return (self.green - self.red) / (self.green + self.red)

    def RI(self):
        
        return (self.red - self.green) / (self.red + self.green)

    def S(self):
        
        max = np.max([np.max(self.red), np.max(self.green), np.max(self.blue)])
        min = np.min([np.min(self.red), np.min(self.green), np.min(self.blue)])
        return (max - min) / max

    def IF(self):
        
        return (2 * self.red - self.green - self.blue) / (self.green - self.blue)

    def DVI(self):
        
        return self.nir / self.red

    def TVI(self):
        
        return (self.NDVI() + 0.5) ** (1 / 2)

    def NDRE(self):
        return (self.nir - self.redEdge) / (self.nir + self.redEdge)

