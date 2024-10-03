import math

def length_side_c(side_a, side_b):
    side_c = math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))
    return side_c

a = float(input("Podaj długość Boku A: "))
b = float(input("Podaj długość Boku B: "))
c = length_side_c(a, b)
print(f"Długość przeciwprostokątnej to: {c}.")