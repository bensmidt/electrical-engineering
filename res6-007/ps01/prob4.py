"""
Author: Benjamin Smidt
Course: RES.6-007: Signals and Systems
Professor: Alan V. Oppenheim
Date: 08/28/2020
Assignment: Problem Set 1, Problem 4
"""
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


def main() -> None:
    r = 2/3
    theta = np.pi/6

    radii = [r, r**2, r, r**2, 1, 1/r]
    thetas = [-theta, 2*theta, theta+np.pi/2, 0, 2*theta, -theta]
    colors = ['r', 'g', 'b', 'y', 'm', 'c']
    labels = ['i', 'ii', 'iii', 'iv', 'v', 'vi']

    # create polar plot
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    # plot coordinates as vectors
    for i in range(len(radii)):
        arrowprops = dict(arrowstyle="->", linewidth=2, color=colors[i])
        ax.annotate(
            '', xy=(thetas[i], radii[i]), xytext=(0, 0), arrowprops=arrowprops
        )

    # Add a legend
    legend_handles = []
    for i in range(len(colors)):
        legend_handles.append(
            mpatches.Patch(color=colors[i], label=labels[i])
        )
    ax.legend(handles=legend_handles, title='Vectors')
    # other graph settings
    ax.set_rmax(max(radii))
    ax.set_rticks(np.arange(0, max(radii), 1/4))
    ax.set_rlabel_position(-22.5)
    ax.grid(True)
    ax.set_title("Problem 4")
    plt.savefig('images/prob4.png')
    plt.show()


if __name__ == "__main__":
    main()
