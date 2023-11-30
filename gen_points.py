import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gen_torus_points(num_points, major_radius, minor_radius):
    theta = 2 * np.pi * np.random.rand(num_points)
    phi = 2 * np.pi * np.random.rand(num_points)

    x = (major_radius + minor_radius * np.cos(phi)) * np.cos(theta)
    y = (major_radius + minor_radius * np.cos(phi)) * np.sin(theta)
    z = minor_radius * np.sin(phi)

    return x, y, z

def gen_sphere_points(num_points, radius):
    theta = 2 * np.pi * np.random.rand(num_points)
    phi = np.pi * np.random.rand(num_points)

    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    return x, y, z

def gen_outliers(num_outliers):
    x = np.random.uniform(-1, 1, num_outliers)
    y = np.random.uniform(-1, 1, num_outliers)
    z = np.random.uniform(-1, 1, num_outliers)

    return x, y, z

def plot_torus(x_torus,y_torus,z_torus, x_outliers, y_outliers, z_outliers):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_torus, y_torus, z_torus, c='r', marker='o', label='Torus Points')
    ax.scatter(x_outliers, y_outliers, z_outliers, c='b', marker='o', label='Outliers')

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Random points on a torus with outliers')

    plt.show()

def plot_sphere(x_sphere,y_sphere,z_sphere, x_outliers, y_outliers, z_outliers):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_sphere, y_sphere, z_sphere, c='r', marker='o', label='sphere Points')
    ax.scatter(x_outliers, y_outliers, z_outliers, c='b', marker='o', label='Outliers')

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Random points on a sphere with outliers')

    plt.show()

def gen_torus(num_points, num_outliers = 0, 
              major_radius = 0.7, minor_radius = 0.3
              ,plot = False):
    x_torus, y_torus, z_torus = gen_torus_points(num_points, major_radius, minor_radius)
    x_outliers, y_outliers, z_outliers = gen_outliers(num_outliers)

    pts_torus = []
    for i in range(len(x_torus)):
        pts_torus.append(np.array((x_torus[i], y_torus[i], z_torus[i])))
    for i in range(len(x_outliers)):
        pts_torus.append(np.array((x_outliers[i], y_outliers[i], z_outliers[i])))
    pts_torus = np.array(pts_torus)

    grades_torus = np.floor(np.random.rand(num_outliers + num_points)*10)

    if plot:
        plot_torus(x_torus,y_torus,z_torus,x_outliers,y_outliers,z_outliers)
    return pts_torus, grades_torus

def gen_sphere(num_points, num_outliers = 0, 
              radius = 0.7 ,plot = False):
    x_sphere, y_sphere, y_sphere = gen_sphere_points(num_points, radius)
    x_outliers, y_outliers, z_outliers = gen_outliers(num_outliers)

    pts_sphere = []
    for i in range(len(x_sphere)):
        pts_sphere.append(np.array((x_sphere[i], y_sphere[i], y_sphere[i])))
    for i in range(len(x_outliers)):
        pts_sphere.append(np.array((x_outliers[i], y_outliers[i], z_outliers[i])))
    pts_sphere = np.array(pts_sphere)

    grades_sphere = np.floor(np.random.rand(num_outliers + num_points)*10)

    if plot:
        plot_sphere(x_sphere,y_sphere,y_sphere,x_outliers,y_outliers,z_outliers)
    return pts_sphere, grades_sphere