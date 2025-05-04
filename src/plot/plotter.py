import matplotlib.pyplot as plt

def plot_container(xver, yver):
    plt.figure(figsize=(6, 4))
    for i in range(xver.shape[0]):
        plt.fill(xver[i], yver[i], color='gray', alpha=0.7, edgecolor='black')
    
    plt.gca().set_aspect('equal')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("DEM Container with Wall Thickness")
    plt.grid(True)
    plt.show()
