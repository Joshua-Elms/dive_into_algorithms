from ast import increment_lineno
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from pathlib import PurePath


def main(
    n=10,
    grid_size=10,
    start=1,
    seed=420,
    savepath=PurePath("chapter_6/img_output/"),
    incrementor_path=PurePath("chapter_6/incrementor.txt"),
):
    iter = get_iter(incrementor_path, inc=True)

    rng = np.random.default_rng(seed)

    points = gen_points(rng, n, grid_size, start)

    

def get_iter(path, inc):
    # read in iter
    with open(path, "r") as f:
        content = f.readline()
        if content == "":
            this_iter = 1

        else:
            this_iter = int(content.strip())

    # increment if inc
    if inc:
        with open(path, "w") as f:
            f.write(str(this_iter + 1))

    return this_iter


def gen_points(rng, n, grid_side_len, start):

    ax_range = range(start, start + grid_side_len)
    all_points = [(x, y) for x in ax_range for y in ax_range]
    cm_points = rng.choice(a=all_points, size=n, replace=False)

    return cm_points


if __name__ == "__main__":
    main()
