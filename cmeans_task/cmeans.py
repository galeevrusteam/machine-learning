import numpy as np

from kmeans_task.point import Point
from kmeans_task.kmeans import get_clusters, draw_clusters, generate_points, calculate_distance_between

n = 300
points = generate_points(n)
k = 3
clusters = get_clusters(points, k)
draw_clusters(clusters)

weight = np.random.dirichlet(np.ones(k), size=n)
centers = clusters.keys()
center_points = []
for center in centers:
    center_points.append(center)

centroids = []
for i in range(k):
    centroids.append(Point(0, 0))

p = 2
new_difference = 0
old_difference = 0
while new_difference == 0 or new_difference > old_difference:

    for j in range(k):
        nom_sum_x = 0
        nom_sum_y = 0
        denominator_sum = 0
        for i in range(n):
            pow_sum = pow(weight[i, j], p)
            nom_sum_x += pow_sum * points[i].x
            nom_sum_y += pow_sum * points[i].y
            denominator_sum += pow_sum
        centroids[j] = Point(nom_sum_x / denominator_sum, nom_sum_y / denominator_sum)

    for i in range(n):
        denominator_value = 0
        for j in range(k):
            denominator_value += pow(1 / calculate_distance_between(points[i], centroids[j]), 1 / (p - 1))
        for j in range(k):
            new_weight = pow(1 / calculate_distance_between(points[i], centroids[j]),
                             1 / (p - 1)) / denominator_value
            weight[i, j] = new_weight

    new_difference = 0
    for j in range(k):
        for i in range(n):
            new_difference += pow(weight[i, j], p) * calculate_distance_between(points[i], centroids[j])

    old_difference = new_difference

new_clusters = {}
for j in range(k):
    new_clusters.update({centroids[j]: []})
for i in range(n):
    index = np.where(weight[i] == max(weight[i, :]))[0][0]
    current_cluster = new_clusters.get(centroids[index])
    current_cluster.append(points[i])
    new_clusters.update({centroids[index]: current_cluster})

draw_clusters(new_clusters)
