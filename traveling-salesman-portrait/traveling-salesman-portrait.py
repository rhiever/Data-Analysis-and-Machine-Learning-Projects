'''
This is a script written by Randal S. Olson (randalolson.com) for the Traveling Salesman Portrait project.

More information on the project can be found on my blog:

http://www.randalolson.com/2018/04/11/traveling-salesman-portrait-in-python/

Please check my project repository for information on how this script can be used and shared:

https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects
'''

import os
import math
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
from PIL import Image
from tsp_solver.greedy_numpy import solve_tsp
from scipy.spatial.distance import pdist, squareform

image_url = 'http://ereaderbackgrounds.com/movies/bw/Frankenstein.jpg'
image_path = 'Frankenstein.jpg'

if not os.path.exists(image_path):
    urllib.request.urlretrieve(image_url, image_path)

original_image = Image.open(image_path)
bw_image = original_image.convert('1', dither=Image.NONE)

bw_image_array = np.array(bw_image, dtype=np.int)
black_indices = np.argwhere(bw_image_array == 0)
chosen_black_indices = black_indices[np.random.choice(black_indices.shape[0], replace=False, size=10000)]

distances = pdist(chosen_black_indices)
distance_matrix = squareform(distances)

optimized_path = solve_tsp(distance_matrix)

optimized_path_points = [chosen_black_indices[x] for x in optimized_path]

plt.figure(figsize=(8, 10), dpi=100)
plt.plot([x[1] for x in optimized_path_points], [x[0] for x in optimized_path_points], color='black', lw=1)
plt.xlim(0, 600)
plt.ylim(0, 800)
plt.gca().invert_yaxis()
plt.xticks([])
plt.yticks([])
plt.savefig('traveling-salesman-portrait.png', bbox_inches='tight')
