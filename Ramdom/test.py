import random
import tkinter as tk
import time
# Create tkinter window
root = tk.Tk()
root.title("Visualisasi Vertex")
# Create canvas for drawing vertices
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def generate_vertex(num_vertices):
    vertices = []
    for _ in range(num_vertices):
        x = random.randint(1, 450)  # Generate random x coordinate
        y = random.randint(1, 450)  # Generate random y coordinate
        vertices.append((x, y))  # Add new vertex to the list
    return vertices

def draw_vertices(canvas, vertices):
    for vertex in vertices:
        x, y = vertex
        canvas.create_rectangle(x-2, y-2, x+2, y+2, fill="white")  # Draw small rectangles as vertices

def draw_edge(canvas, v1, v2, color="blue", hilang=False, ms=500):
    x1, y1 = v1
    x2, y2 = v2
    if hilang == False: 
        canvas.create_line(x1, y1, x2, y2, fill=color)
    else:
        ch = canvas.create_line(x1, y1, x2, y2, fill=color)
        canvas.after(ms, canvas.delete, ch)

def minimum_spanning_tree(vertices):
    edges = []
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            dist = (vertices[i][0] - vertices[j][0]) ** 2 + (vertices[i][1] - vertices[j][1]) ** 2 / 2
            edges.append((dist, i, j))
    edges.sort()
    print(edges)
    mst_edges = []
    parent = [i for i in range(len(vertices))]
    rank = [0] * len(vertices)

    for edge in edges:
        dist, v1, v2 = edge
        root1 = find(parent, v1)
        root2 = find(parent, v2)
        if root1 != root2:
            mst_edges.append((v1, v2))
            union(parent, rank, root1, root2)
            e = draw_edge(canvas, vertices[v1], vertices[v2], "green")  # Highlight edges in the MST
            root.update()  # Update the canvas to visualize changes

        else:
            em = draw_edge(canvas, vertices[v1], vertices[v2], "red",True,200)  # Highlight edges in the MST
            root.update()  # Update the canvas to visualize changes
        time.sleep(0.2)
            

    return mst_edges

vertex = generate_vertex(10)
draw_vertices(canvas, vertex)
mst = minimum_spanning_tree(vertex)

root.mainloop()
