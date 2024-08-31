import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def vecinos(x, y):
    vec = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    return [(i % N, j % N) for i, j in vec]

def actualizar(frameNum, img, tabla, N):
    nueva_tabla = np.copy(tabla)
    for i in range(N):
        for j in range(N):
            total = int((tabla[i, (j-1)%N] + tabla[i, (j+1)%N] +
                         tabla[(i-1)%N, j] + tabla[(i+1)%N, j] +
                         tabla[(i-1)%N, (j-1)%N] + tabla[(i-1)%N, (j+1)%N] +
                         tabla[(i+1)%N, (j-1)%N] + tabla[(i+1)%N, (j+1)%N]) / 255)
            if tabla[i, j]  == ON:
                if (total < 2) or (total > 3):
                    nueva_tabla[i, j] = OFF
            else:
                if total == 3:
                    nueva_tabla[i, j] = ON
    img.set_data(nueva_tabla)
    tabla[:] = nueva_tabla
    return img,

# Tamaño de la cuadrícula
N = 100
ON = 255
OFF = 0

# Estado inicial aleatorio
tabla = np.random.choice([ON, OFF], N*N, p=[0.2, 0.8]).reshape(N, N)

fig, ax = plt.subplots()
img = ax.imshow(tabla, interpolation='nearest')
ani = animation.FuncAnimation(fig, actualizar, fargs=(img, tabla, N),
                              frames=10,
                              interval=50,
                              save_count=50)

plt.show()