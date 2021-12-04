# Strategia: bierzemy ten klocek, który najbardziej zniweluje różnicę między naszą wieżą a najwyższą wieżą
# Najpierw liczymy wysokośc wiezy kazdego dziecka i sortujemy klocki w kazdej wiezy
# Iterujemy po dzieciach:
# Jeśli wieża rozpatrywanego dziecka nie jest najwyższa: liczymy różnicę: H_max - (nasza_wieża + najwiekszy klocek
#                                         dziecka, które rozpatrujemy)
# Jeśli jest najwyższa: Sprawdzamy, czy po wzięciu z niej najwiekszego klocka dalej jest najwyzsza, bo musimy
#                       sprawdzać zawsze do najwyższej, dalej wzór ten, co wyżej
# Bierzemy ten klocek, dla którego ta różnica jest najmniejsza
