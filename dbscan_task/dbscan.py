import numpy as np

from kmeans_task.kmeans import draw_clusters, calculate_distance_between
from kmeans_task.point import Point

e = 5
m = 2
not_neighbour_key = -1


def get_neighbours(p):
    return [other for other in points if calculate_distance_between(p, other) < e]


def form_cluster_points(clusters: {}, cluster_id, visited_points, clustered_points, current_point, neighbours):
    if cluster_id not in clusters:
        clusters.update({cluster_id: []})
    curr_array = clusters.get(cluster_id)
    curr_array.append(current_point)
    clusters.update({cluster_id: curr_array})
    clustered_points.add(current_point)
    while neighbours:
        neighbour = neighbours.pop()
        if neighbour not in visited_points:
            visited_points.add(neighbour)
            neighbours_of_neighbour = get_neighbours(neighbour)
            if len(neighbours_of_neighbour) > m:
                neighbours.extend(neighbours_of_neighbour)
        if neighbour not in clustered_points:
            clustered_points.add(neighbour)
            neighbour_cluster = clusters.get(cluster_id)
            neighbour_cluster.append(neighbour)
            clusters.update({cluster_id: neighbour_cluster})
            if neighbour in clusters.get(not_neighbour_key):
                clusters.get(not_neighbour_key).remove(neighbour)


def get_clusters(points: []):
    cluster_id = 0
    visited_points = set()
    clustered_points = set()
    clusters = {}
    clusters.update({not_neighbour_key: []})
    for point in points:
        if point not in visited_points:
            visited_points.add(point)
            neighbours = get_neighbours(point)
            if len(neighbours) < m:
                clusters.get(not_neighbour_key).append(point)
            else:
                cluster_id += 1
                form_cluster_points(clusters, cluster_id, visited_points, clustered_points, point, neighbours)
    return clusters


def generate_points_in_range(n, x_low, x_high, y_low, y_high):
    return [Point(np.random.randint(low=x_low, high=x_high), np.random.randint(low=y_low, high=y_high)) for i in
            range(n)]


n = 250
points = generate_points_in_range(n, 0, 40, 0, 40)
points.extend(generate_points_in_range(n, 60, 100, 60, 100))
points.extend(generate_points_in_range(n, 0, 20, 80, 100))
points.extend(generate_points_in_range(n, 70, 100, 0, 30))
clusters = get_clusters(points)
draw_clusters(clusters)
