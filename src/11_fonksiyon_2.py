import cmath  # cmath, karmaşık sayıları destekler

def ikinci_dereceden_coz(a, b, c):
    # Delta hesaplama
    delta = cmath.sqrt(b**2 - 4*a*c)

    # Kökleri bulma
    x1 = (-b + delta) / (2*a)
    x2 = (-b - delta) / (2*a)

    return x1, x2

# Örnek kullanım
a = 1
b = -3
c = 2

kokler = ikinci_dereceden_coz(a, b, c)
print("Kökler:", kokler)
# Output: Kökler: (2+0j, 1+0j)

