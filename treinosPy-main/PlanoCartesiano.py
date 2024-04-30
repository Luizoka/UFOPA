import matplotlib.pyplot as plt

def plot_cartesian_plane(x, y):
    plt.scatter(x, y)
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.show()

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plot_cartesian_plane(x, y)