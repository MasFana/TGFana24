import random
import time
import tkinter as tk

# Membuat jendela GUI dan canvas untuk menggambar
root = tk.Tk()
root.title("Visualisasi Vertex")
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

# Fungsi untuk membuat titik-titik (vertex) secara acak
def generate_vertex(num_vertices):
    vertices = []
    for _ in range(num_vertices):
        x = random.randint(1, 450)
        y = random.randint(1, 450)
        vertices.append((x, y))  # koordinat titik
    return vertices

# Fungsi untuk menggambar titik pada canvas
def draw_vertices(canvas, vertices):
    for vertex in vertices:
        x, y = vertex
        canvas.create_rectangle(x-2, y-2, x+2, y+2, fill="white")  # titik berwarna putih

# Fungsi untuk menggambar garis (edge) antara dua titik
# Bisa juga diatur agar garis menghilang setelah beberapa saat (hilang=True)
def draw_edge(canvas, v1, v2, color="green", hilang=False, ms=500):
    x1, y1 = v1
    x2, y2 = v2
    if not hilang: 
        return canvas.create_line(x1, y1, x2, y2, fill=color)
    else:
        ch = canvas.create_line(x1, y1, x2, y2, fill=color)
        canvas.after(ms, canvas.delete, ch)  # hilangkan garis setelah 'ms' milidetik

# Fungsi utama: membangun Minimum Spanning Tree menggunakan algoritma Prim
def minimum_spanning_tree(vertices):
    mst = []  # list untuk menyimpan edge yang termasuk MST
    visited = [False] * len(vertices)  # penanda node yang sudah dikunjungi
    visited[0] = True  # mulai dari node pertama
    e = None  # untuk menyimpan edge sementara yang digambar kuning

    # Selama masih ada vertex yang belum dikunjungi
    while False in visited:
        min_edge = None
        min_dist = float('inf')  # jarak minimum sementara
        for i in range(len(vertices)):
            if visited[i]:  # hanya cari dari node yang sudah masuk MST
                for j in range(len(vertices)):
                    if not visited[j]:  # ke node yang belum dikunjungi
                        # Jika sudah ada edge minimum sebelumnya, hapus visualisasinya
                        if min_edge is not None:
                            if e is not None:
                                canvas.delete(e)
                            e = draw_edge(canvas, vertices[min_edge[0]], vertices[min_edge[1]], "yellow", True, 200)

                        root.update()

                        # Hitung jarak kuadrat antar dua titik (tanpa akar karena tidak perlu)
                        dist = (vertices[i][0] - vertices[j][0]) ** 2 + (vertices[i][1] - vertices[j][1]) ** 2
                        
                        # Gambarkan edge yang sedang dievaluasi
                        draw_edge(canvas, vertices[i], vertices[j], "red", True, 200)
                        root.update()
                        time.sleep(0.2)  # delay untuk visualisasi

                        # Simpan edge dengan jarak terkecil
                        if dist < min_dist:
                            min_dist = dist
                            min_edge = (i, j)
        
        # Tambahkan edge terbaik ke MST
        mst.append(min_edge)
        visited[min_edge[1]] = True  # tandai node tujuan sebagai sudah dikunjungi

        print(visited)
        print(min_edge)

        # Gambar ulang semua edge dalam MST dengan warna hijau
        for edge in mst:
            draw_edge(canvas, vertices[edge[0]], vertices[edge[1]], "green")
        root.update()

    return mst  # kembalikan list edge yang termasuk MST

# Eksekusi program
vertex = generate_vertex(10)  # buat 10 titik acak
draw_vertices(canvas, vertex)  # gambar titik-titik tersebut
mst = minimum_spanning_tree(vertex)  # buat dan visualisasi MST-nya

# Jalankan loop utama Tkinter
root.mainloop()
