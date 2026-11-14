#viewing a mandelbrot fractal through a python program


#z_{n+1}=z_n^2+c
import matplotlib
matplotlib.use("MacOSX")


import numpy as np 
import matplotlib.pyplot as plt 

#image parameters 


width = 2400
height = 2400 
max_iterations = 200

#zoom parameters 

zoom = 1.0 
center_x = -0.5
center_y = 0.0

def julia(width, height, zoom, center_x, center_y, max_iterations):

    scale = 1.5 / zoom

    x_min = center_x - scale
    x_max = center_x + scale

    y_min = center_y - scale
    y_max = center_y + scale

    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)

    X, Y = np.meshgrid(x, y)

    Z = X + 1j * Y

    c = -0.7 + 0.27015j

    iterations = np.zeros(Z.shape, dtype=int)

    active = np.ones(Z.shape, dtype=bool)

    for i in range(max_iterations):

        Z[active] = Z[active] ** 2 + c

        escaped = (np.abs(Z) > 2) & active

        iterations[escaped] = i + 1

        active[escaped] = False

    iterations[active] = max_iterations

    return iterations


# Generate the fractal

fig, ax = plt.subplots()

image = julia(
    width, height, zoom,
    center_x, center_y, max_iterations
)

display = ax.imshow(
    image,
    cmap="inferno",
    origin="lower"
)

ax.axis("off")


def update():

    image = julia(
        width, height, zoom,
        center_x, center_y, max_iterations
    )

    display.set_data(image)

    ax.set_title(f"Zoom: {zoom:.2f}x")

    fig.canvas.draw_idle()


def on_scroll(event):

    global zoom

    if event.button == "up":
        zoom *= 1.5

    elif event.button == "down":
        zoom /= 1.5

    update()


fig.canvas.mpl_connect("scroll_event", on_scroll)

plt.show()


