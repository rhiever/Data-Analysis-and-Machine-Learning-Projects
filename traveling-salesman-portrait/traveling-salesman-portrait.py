'''
This is a script written by Randal S. Olson (randalolson.com) for the Traveling Salesman Project.

More information on the project can be found here:  http://www.randalolson.com/2018/04/11/traveling-salesman-portrait-in-python/

Please check my project repository for information on how this script can be used and shared: https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects
'''

import os
import math
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
from PIL import Image
from itertools import combinations
from tsp_solver.greedy_numpy import solve_tsp

image_url = 'http://ereaderbackgrounds.com/movies/bw/Frankenstein.jpg'
image_path = 'Frankenstein.jpg'

if not os.path.exists(image_path):
    urllib.request.urlretrieve(image_url, image_path)

original_image = Image.open(image_path)
bw_image = original_image.convert('1', dither=Image.NONE)

bw_image_array = np.array(bw_image, dtype=np.int)
black_indices = np.argwhere(bw_image_array == 0)
chosen_black_indices = black_indices[np.random.choice(black_indices.shape[0], replace=False, size=10000)]

distance_lookup = {}

for (p1, p2) in combinations(range(len(chosen_black_indices)), r=2):
    p1 = tuple(chosen_black_indices[p1])
    p2 = tuple(chosen_black_indices[p2])
    x1, y1 = p1
    x2, y2 = p2
    distance_lookup[(p1, p2)] = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
distance_matrix = []
for row_num in range(0, len(chosen_black_indices)):
    row_list = []
    for col_num in range(0, row_num):
        p1 = tuple(chosen_black_indices[row_num])
        p2 = tuple(chosen_black_indices[col_num])
        if (p1, p2) in distance_lookup:
            row_list.append(distance_lookup[p1, p2])
        else:
            row_list.append(distance_lookup[p2, p1])
    distance_matrix.append(row_list)

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
