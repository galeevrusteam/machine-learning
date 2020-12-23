from kmeans_task.kmeans import generate_points, get_optimal_clusters, draw_points, draw_clusters

points = generate_points(500)
draw_points(points)
clusters = get_optimal_clusters(points)
draw_clusters(clusters)
