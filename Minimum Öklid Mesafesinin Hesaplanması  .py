import math

# Kullanıcıdan nokta girişlerini alma
points = []
n = int(input("Kaç nokta gireceksiniz? "))
for i in range(n):
    x, y = map(float, input(f"{i+1}. noktanın koordinatlarını girin (x y): ").split())
    points.append((x, y))

# Öklid mesafesini hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Tüm nokta çiftleri arasındaki mesafeleri hesaplayıp minimum olanı bulma
min_distance = float('inf')
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        if distance < min_distance:
            min_distance = distance

# Sonucu yazdırma
if n > 1:
    print(f"Minimum Öklid mesafesi: {min_distance}")
else:
    print("Mesafe hesaplanacak yeterli nokta yok.")