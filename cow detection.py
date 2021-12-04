"""Jako że obszary krowopodobne są tylko i wyłącznie liniami, możemy dla każdego
 niezerowego punktu tablicy sprawdzić kolumnę w dół i wiersz w prawo, czy długość tej
 linii zaczynającej się w tym punkcie to 2 lub 3. Następnie zerujemy te wszystkie
 znalezione pola niezależnie od długości linii, by nie liczyć kilka razy tego
 samego pola jako krowę (lub stwierdzić w drugim napotkaniu 4-jednostkowej linii, że
 teraz ma 3 jednostki i jest krową).
 Złożoność algorytmu liniowa względem rozmiaru tablicy, bo do każdego elementu tablicy wejdziemy
 nie więcej niż 2 razy, zatem O(2xy) = O(xy)"""

"""WARIACJA:
W przypadku, gdyby obszary miały dowolny kształt, i 3-polowe obszary (literka L w tablicy) byłyby
klasyfikowane jako krowa, to z każdego niezerowego punktu należałoby puścić algorytm BFS/DFS (dowolnie),
odwiedzający i liczący niezerowych sąsiadów danego punktu (policzenie rozmiaru plamy), następnie analogicznie 
zerujący odwiedzone miejsca w celu niepowtarzania wywołań na tej samej plamie"""


def count_cows(arr, x, y):  # x - szerokość, y - długość tablicy
    res_count = 0  # wynik
    for i in range(y):  # i to obecny indeks wiersza
        for j in range(x):  # j to obecny indeks kolumny

            if arr[i][j] == 1:  # "==1" tylko dla czytelności, mamy obszar krowopodobny
                curr_count = 1

                vertical = i + 1  # sprawdzamy kolumnę w dół
                while vertical <= y - 1:
                    if arr[vertical][j] == 1:
                        arr[vertical][j] = 0
                        curr_count += 1
                        vertical += 1
                    else:
                        break

                # nie musimy sprowadzać curr_count do 1, bo tylko jedna z tych dwóch sytuacji może wystąpić,
                # tj albo jest linia w dół, albo w prawo, zaczynająca się w tym punkcie, z zał zadania

                horizontal = j + 1  # sprawdzamy wiersz w prawo
                while horizontal <= x - 1:
                    if arr[i][horizontal] == 1:
                        arr[i][horizontal] = 0
                        curr_count += 1
                        horizontal += 1
                    else:
                        break

                if 2 <= curr_count <= 3:
                    res_count += 1

                arr[i][j] = 0

    return res_count


def func(arr):
    arr[0] = 3


if __name__ == '__main__':
    t = [1, 2]
    func(t)
    print(t)
