class Employee:
    def __init__(self, fun):
        self.emp = []
        self.f = -1
        self.g = -1
        self.fun = fun


# g(i) - najlepsza impreza, na którą i nie idzie
# f(i) - najlepsza impreza zrobiona z i i wszystkich podpracowników
# (podrzewo o root = i)
# rozw f(root)


def g(v):
    if v.g >= 0:
        return v.g
    v.g = 0
    for employee in v.emp:
        v.g += f(employee)
    return v.g


def f(v):
    if v.f >= 0:
        return v.f
    v.f = 0
    for employee in v.emp:
        v.f += g(employee)
    v.f = max(v.f, v.g)
    return v.f
