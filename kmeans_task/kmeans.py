import matplotlib.pyplot as plt
import numpy as np
import random

from kmeans_task.point import Point


def calculate_distance_between(point_1: Point, point_2: Point):
    return np.math.sqrt(pow(point_1.x - point_2.x, 2) + pow(point_1.y - point_2.y, 2))


def generate_points(size):
    points = []
    for j in range(0, size):
        point = Point(random.randint(1, 100), random.randint(1, 100))
        points.append(point)
    return points


def get_centers(points: [], k: int) -> []:
    max_distance = 0
    center_1 = None
    center_2 = None
    centers = []
    for i in range(0, len(points)):
        point_from = points[i]
        for j in range(i + 1, len(points)):
            point_to = points[j]
            distance = calculate_distance_between(point_from, point_to)
            if distance > max_distance:
                max_distance = distance
                center_1 = point_from
                center_2 = point_to

    centers.append(center_1)
    centers.append(center_2)
    points.remove(center_1)
    points.remove(center_2)

    for i in range(0, k - len(centers)):
        max_distance = 0
        new_center = None
        for j in range(0, len(points)):
            point = points[j]
            min_distance = 0
            for l in range(0, len(centers)):
                center = centers[l]
                distance = calculate_distance_between(point, center)
                if min_distance == 0 or distance < min_distance:
                    min_distance = distance
            if max_distance < min_distance:
                max_distance = min_distance
                new_center = point
        centers.append(new_center)
        points.remove(new_center)

    return centers


def get_clusters_by_centers(points: [], centers: []):
    clusters = {}
    for point in points:
        min_distance = 0
        cluster = None
        for center in centers:
            distance = calculate_distance_between(point, center)
            if min_distance == 0 or distance < min_distance:
                min_distance = distance
                cluster = center
                if clusters.get(cluster) is None:
                    clusters.update({cluster: []})
        cluster_points = clusters.get(cluster)
        cluster_points.append(point)
        clusters.update({cluster: cluster_points})
    return clusters

def get_new_centers(clusters: {}) -> []:
    centers = clusters.keys()
    new_clusters = []
    for center in centers:
        cluster_points = clusters.get(center)
        mean_x = 0
        mean_y = 0
        for point in cluster_points:
            mean_x += point.x
            mean_y += point.y
        mean_x = mean_x / len(cluster_points)
        mean_y = mean_y / len(cluster_points)
        new_clusters.append(Point(x=mean_x, y=mean_y))
    return new_clusters


def get_clusters(points: [], k: int):
    centers = get_centers(points.copy(), k)
    fin_clusters = get_clusters_by_centers(points.copy(), centers.copy())
    new_centers = get_new_centers(fin_clusters)
    while centers != new_centers:
        fin_clusters = get_clusters_by_centers(points.copy(), new_centers.copy())
        centers = new_centers
        new_centers = get_new_centers(fin_clusters)
    return fin_clusters


def get_sum_distance(clusters: {}):
    sum_distance = 0
    for center in clusters.keys():
        points = clusters.get(center)
        for point in points:
            sum_distance += calculate_distance_between(point, center)
    return sum_distance


def get_optimal_clusters(points: []) -> {}:
    c = 9
    k = 2
    sum_distances = [None] * c
    d = [None] * c
    clusters_arr = [None] * c

    has_next = True
    while has_next:
        clusters_arr[k] = get_clusters(points.copy(), k)
        sum_distance = get_sum_distance(clusters_arr[k])
        sum_distances[k] = sum_distance
        if k >= 4:
            d[k - 1] = np.math.fabs((sum_distances[k - 1] - sum_distances[k]) / (sum_distances[k - 2] - sum_distances[k - 1]))
        k += 1
        has_next = k < c

    d_without_none = []
    for i in range(0, c):
        if d[i] is not None:
            d_without_none.append(d[i])
    idx = d.index(min(d_without_none))
    return clusters_arr[idx]


def draw_points(points: []):
    x = []
    y = []
    for o in range(0, len(points)):
        x.append(points[o].x)
        y.append(points[o].y)
    plt.scatter(x, y)
    plt.show()


def draw_clusters(clusters: {}):
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
    i = 0
    for k in clusters.keys():
        points = clusters.get(k)
        x = []
        y = []
        for point in points:
            x.append(point.x)
            y.append(point.y)
        plt.scatter(x, y, color=colors[i])
        i = i + 1
    plt.show()