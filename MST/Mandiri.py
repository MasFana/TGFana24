import random
import time
import tkinter as tk

root = tk.Tk()
root.title("Visualisasi Vertex")
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

def generate_vertex(num_vertices):
    vertices = []
    print("canvas = 500 x 500")
    UPTTI = input("Masukkan Koodinat UPTTI x y")
    UPTTI.split()
    vertices.append((UPTTI[0], UPTTI[1]))
    for i in range(num_vertices-1):
        x = input("Masukkan kordinat x: ")
        y = input("Masukkan kordinat y: ")
        vertices.append((x, y))
    return vertices

def draw_vertices(canvas, vertices):
    for vertex in vertices:
        x, y = vertex
        canvas.create_oval(x-5, y-5, x+5, y+5, fill="white")

def draw_edge(canvas, v1, v2, color="green", hilang=False, ms=500):
    x1, y1 = v1
    x2, y2 = v2
    if hilang == False: 
        return canvas.create_line(x1, y1, x2, y2, fill=color)
    else:
        ch = canvas.create_line(x1, y1, x2, y2, fill=color)
        canvas.after(ms, canvas.delete, ch)

def minimum_spanning_tree(vertices):
    mst = []
    visited = [False] * len(vertices)
    visited[0] = True
    e = None
    canvas.create_text(
        vertices[0],
    text="UPTTI",
    fill="white",
    font='tkDefaeultFont 12 bold'
    )
    while False in visited:
        min_edge = None
        min_dist = float('inf')
        for i in range(len(vertices)):
            if visited[i]:
                for j in range(len(vertices)):
                    if not visited[j]:
                        if min_edge is not None:
                            if e is not None:
                                canvas.delete(e)
                            e = draw_edge(canvas, vertices[min_edge[0]], vertices[min_edge[1]], "yellow")
                        root.update()
                        dist = (vertices[i][0] - vertices[j][0]) ** 2 + (vertices[i][1] - vertices[j][1]) ** 2
                        draw_edge(canvas, vertices[i], vertices[j], "red", True, 200)
                        root.update()
                        time.sleep(0.2)
                        if dist < min_dist:
                            min_dist = dist
                            min_edge = (i, j)
        mst.append(min_edge)
        visited[min_edge[1]] = True
        for edge in mst:
            draw_edge(canvas, vertices[edge[0]], vertices[edge[1]], "green")
        root.update()
    return mst

vertex = generate_vertex(10)
print(vertex)
draw_vertices(canvas, vertex)
mst = minimum_spanning_tree(vertex)

root.mainloop()