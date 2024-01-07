'''
klasa dom
input:
--> długość
--> rozdzielczość
--> indeksy graniczne
output:
--> mini macierze (na rozwiązanie)
--> maski (na pozostałe)


class dom:
    def __init__(self, params):
        self.macierze = {}

        for key in params["indeksy_graniczne"].keys():
            coordinates = params["indeksy_graniczne"][key]
            ind_row_min = min([for tup[0] in params["indeksy_graniczne"][key]])
            ind_row_max = max([for tup[0] in params["indeksy_graniczne"][key]])
            ind_col_min = min([for tup[0] in params["indeksy_graniczne"][key]])
            ind_col_max = max([for tup[0] in params["indeksy_graniczne"][key]])
            self.macierze[key] = np.zeros((ind_row_max - ind_row_min, ind_col_max - ind_col_min ))
            self.macierze[key] = params["maska"[key]]


        ind_row_min = min(
            [for tup[0] in params["indeksy_graniczne"][key]])

        return self

if __name__== "main":
    dom1 = Dom()

    params = {
        "indeksy_graniczne" : {
            I : [(0,0), (0,50), (50,0), (50,50)],
            II : [(0,50), (0,100),(50,50), (50,100)],
            III : [(50,0), (50,50), (100,0), (100,50)],
            IV : [(50,50), (50,100), (100,50), (100,100)]
        },
        "rozdzielczosc" : {},
        "maska" : {
            "I":1,
            "II":1,
            "III": 1,
            "IV": 0}
    }

    plt.inshow(M)

    '''


import numpy as np
import matplotlib.pyplot as plt 

class dom:
    def __init__(self, params):
        self.macierze = {}  

        for key in params["indeksy_graniczne"].keys():  
            coordinates = params["indeksy_graniczne"][key]
            ind_row_min = min(tup[0] for tup in coordinates)
            ind_row_max = max(tup[0] for tup in coordinates)
            ind_col_min = min(tup[1] for tup in coordinates)
            ind_col_max = max(tup[1] for tup in coordinates)
            
            self.macierze[key] = np.zeros((ind_row_max - ind_row_min, ind_col_max - ind_col_min))
            self.macierze[key][:] = params["maska"][key] 

        self.draw_square(params)

    def draw_square(self, params):
        square = np.zeros((100, 100)) 


        square[:50, :50] = params["maska"]["I"] 
        square[:50, 50:] = params["maska"]["II"] 
        square[50:, :50] = params["maska"]["III"]  
        square[50:, 50:] = params["maska"]["IV"]  


        plt.imshow(square, cmap='summer', interpolation='nearest')
        plt.title('Plan domu')  
        plt.show()

if __name__ == "__main__":
    params = {
        "indeksy_graniczne": {
            "I": [(0, 0), (0, 50), (50, 0), (50, 50)],
            "II": [(0, 50), (0, 100), (50, 50), (50, 100)],
            "III": [(50, 0), (50, 50), (100, 0), (100, 50)],
            "IV": [(50, 50), (50, 100), (100, 50), (100, 100)]
        },
        "rozdzielczosc": {},
        "maska": {
            "I": 1,
            "II": 1,
            "III": 1,
            "IV": 0
        }
    }

    dom1 = dom(params) 
