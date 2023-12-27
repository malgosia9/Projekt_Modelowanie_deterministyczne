'''
klasa dom
input:
--> długość
--> rozdzielczość
--> indeksy graniczne
output:
--> mini macierze (na rozwiązanie)
--> maski (na pozostałe)
'''

class dom:
    def __init__(self, params):
        self.macierze = {}

        for key in params["indeksy_graniczne"].keys():
            ind_row_min = min([for tup[0] in params["indeksy_graniczne"][key]])
            ind_row_max = max([for tup[0] in params["indeksy_graniczne"][key]])
            ind_col_min = min([for tup[0] in params["indeksy_graniczne"][key]])
            ind_col_max = max([for tup[0] in params["indeksy_graniczne"][key]])
            self.macierze[key] = np.zeros((ind_row_max - ind_row_min, ind_col_max - ind_col_min ))
            self.macierze[key] = params["maska"[key]]


        ind_row_min = min(
            [for tup[0] in params["indeksy_graniczne"][key]]
        )

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