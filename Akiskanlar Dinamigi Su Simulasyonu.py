import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Grid boyutu
N = 120

# Dalga alanları
h = np.zeros((N, N))
h_prev = np.zeros((N, N))

# Fizik parametreleri
c = 0.3
damping = 0.996

# Tekne başlangıç konumu
boat_x = 20
boat_y = N // 2

# Başlangıç dalgası (çok önemli!)
h[N//2, N//2] = 5

# Görselleştirme
fig, ax = plt.subplots()
im = ax.imshow(h, cmap="coolwarm", vmin=-5, vmax=5)
ax.set_title("Su Dalga + Tekne Simülasyonu")

def update(frame):
    global h, h_prev, boat_x

    h_new = np.zeros_like(h)

    # Dalga denklemi (discrete Laplacian)
    for i in range(1, N-1):
        for j in range(1, N-1):

            laplacian = (
                h[i+1, j] +
                h[i-1, j] +
                h[i, j+1] +
                h[i, j-1] -
                4 * h[i, j]
            )

            h_new[i, j] = (
                2 * h[i, j]
                - h_prev[i, j]
                + c**2 * laplacian
            )

    # Tekne etkisi (wake oluşturur)
    for dx in range(-3, 4):
        for dy in range(-3, 4):
            x = boat_x + dx
            y = boat_y + dy

            if 0 <= x < N and 0 <= y < N:
                h_new[x, y] -= 6.0  # güçlü etki

    # Damping (enerji kaybı)
    h_new *= damping

    # Zaman güncelleme
    h_prev[:] = h
    h[:] = h_new

    # Tekne hareketi
    boat_x += 1
    if boat_x > N - 10:
        boat_x = 10

    # Görüntü güncelle
    im.set_array(h)

    return [im]

ani = animation.FuncAnimation(
    fig,
    update,
    frames=300,
    interval=30,
    blit=True
)

plt.show()
