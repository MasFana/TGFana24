import random
import time
import tkinter as tk

# Membuat jendela GUI dan canvas untuk menggambar
root = tk.Tk()
root.title("Visualisasi Kruskal")
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

# Fungsi untuk membuat titik-titik (vertex) secara acak
def generate_vertex(num_vertices):
    vertices = []
    for _ in range(num_vertices):
        x = random.randint(1, 450)  # Koordinat x acak antara 1-450
        y = random.randint(1, 450)  # Koordinat y acak antara 1-450
        vertices.append((x, y))     # Tambahkan koordinat ke list vertices
    return vertices

# Fungsi untuk menggambar titik pada canvas
def draw_vertices(canvas, vertices):
    for vertex in vertices:
        x, y = vertex
        # Gambar kotak kecil sebagai representasi vertex
        canvas.create_rectangle(x-2, y-2, x+2, y+2, fill="white")

# Fungsi untuk menggambar garis (edge) antara dua titik
def draw_edge(canvas, v1, v2, color="green", hilang=False, ms=500):
    x1, y1 = v1
    x2, y2 = v2
    if not hilang: 
        return canvas.create_line(x1, y1, x2, y2, fill=color)
    else:
        ch = canvas.create_line(x1, y1, x2, y2, fill=color)
        canvas.after(ms, canvas.delete, ch)  # Hilangkan garis setelah 'ms' milidetik

# Fungsi untuk mencari parent dari suatu node (dengan path compression)
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # Path compression
    return parent[x]

# Fungsi untuk menggabungkan dua set (dengan union by rank)
def union(parent, rank, x, y):
    xroot = find(parent, x)  # Cari root dari x
    yroot = find(parent, y)  # Cari root dari y
    
    # Union by rank
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# Fungsi utama: membangun MST menggunakan algoritma Kruskal
def minimum_spanning_tree(vertices):
    mst = []  # List untuk menyimpan edge MST
    edges = []  # List untuk menyimpan semua edge
    
    # 1. Bangun semua kemungkinan edge dan hitung jaraknya
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):  # Hindari duplikat edge
            # Hitung jarak kuadrat (tidak perlu akar untuk perbandingan)
            dist = (vertices[i][0] - vertices[j][0])**2 + (vertices[i][1] - vertices[j][1])**2
            edges.append((dist, i, j))  # Simpan sebagai (jarak, vertex1, vertex2)
    
    # 2. Urutkan edge berdasarkan jarak terkecil ke terbesar
    edges.sort()
    
    # Inisialisasi struktur data Union-Find
    parent = list(range(len(vertices)))  # Setiap vertex adalah parent dirinya sendiri
    rank = [0] * len(vertices)          # Rank awal 0 untuk semua vertex
    
    # 3. Proses setiap edge secara berurutan
    for dist, u, v in edges:
        # Visualisasi: tampilkan edge yang sedang diproses (merah)
        draw_edge(canvas, vertices[u], vertices[v], "red", True, 300)
        root.update()
        time.sleep(0.2)  # Delay untuk visualisasi
        
        # Cari root dari kedua vertex
        u_root = find(parent, u)
        v_root = find(parent, v)
        
        # Jika root berbeda, tidak membentuk siklus
        if u_root != v_root:
            # Gabungkan kedua set
            union(parent, rank, u, v)
            # Tambahkan edge ke MST
            mst.append((u, v))
            # Visualisasi: tampilkan edge MST (hijau)
            draw_edge(canvas, vertices[u], vertices[v], "green")
            root.update()
        
        # Hentikan jika sudah cukup edge (n-1 edge untuk n vertex)
        if len(mst) == len(vertices) - 1:
            break
    
    return mst

# Eksekusi program
vertex = generate_vertex(10)  # Generate 10 vertex acak
draw_vertices(canvas, vertex)  # Gambar vertex di canvas
mst = minimum_spanning_tree(vertex)  # Bangun MST dengan Kruskal

# Jalankan loop utama Tkinter
root.mainloop()