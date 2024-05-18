from email.policy import default
import psycopg2

conn = psycopg2.connect(database="python",user="postgres",password="postgres",host="localhost")

# cur = conn.cursor()

# # # select mata kuliah
# def read_mata_kuliah(cur):
#  query = "SELECT * FROM mata_kuliah"
#  cur.execute(query=query)
#  data= cur.fetchall()
#  for i in data:
#      print(i)
#  cur.close()
#  conn.close()

# # # select semester

# # query = "SELECT * FROM semester"
# # cur.execute(query)
# # data= cur.fetchall()
# # for i in data:
# #     print(i)
# # cur.close()
# # conn.close()

# # Dynamic Insert data 1
# # total_input = int(input(f"Mau menambahkan berapa data?: "))
# # for i in range(total_input):
# #     nama_mata_kuliah = input(f"Masukkan nama mata kuliah: ")
# #     sks = int(input(f"Masukkan jumlah sks: "))
# #     semester = int(input(f"Masukkan semester: "))
# #     query = f"insert into mata_kuliah(nama_mata_kuliah, sks, semester_id) values('{nama_mata_kuliah}, {sks}, {semester_id})"
# #     cur.execute(query, {nama_mata_kuliah, sks, semester_id})

# # conn.commit()
# # cur.close()
# # conn.close()


# query = f"UPDATE mata_kuliah SET nama_mata_kuliah = %s, sks = %s, semester_id = %s"
# # read_mata_kuliah(cur)
# #read mata kuliah

# query_select = "SELECT & FROM mata_kuliah"
# cur.execute()
# data = cur.fetchall()
# for i in data:
#    print(i)

# id_mata_kuliah = input(f"Masukkan id mata kulliah yang ingin di update: ")
# select_query = "SELECT * FROM mata-kuliah WHERE id_mata_kuliah +%s"
# cur.execute(select_query, (id_mata_kuliah))
# data2 = cur.fetchone()

# if data2:
#     print('Data saat ini:')
#     print(f'id mata kuliah saat ini: {data2[0]}')
#     print(f'nama mata kuliah saat ini: {data2[1]}')
#     print(f'sks mata kuliah saat ini: {data2[2]}')
#     print(f'semester mata kuliah saat ini: {data2[3]}')

# #UPDATE
# nama_mata_kuliah = input(f"Masukkan nama mata kuliah: ") or data2[1]
# sks = input(f"Masukkan jumlah sks: ") or data2[2]
# sks = int(sks)
# semester_id = int(input(f"Masukkan semester: ")) or data[3]

# query_update = f"UPDATE mata_kuliah SET nama_mata_kuliah = %s, sks = %s, semester_id = %s"
# cur.execute(query_update, (nama_mata_kuliah, sks, semester_id, id_mata_kuliah))

# conn.commit()
# # print("total baris yang diubah: {cur.rowcount{}}")

# cur.close()
# conn.close()

# -------------------   Rewrite Jadi Function   -------------------

def read_mata_kuliah_by_id(id):
    cur = conn.cursor()
    query = "SELECT * FROM mata_kuliah WHERE id_mata_kuliah = %s"
    cur.execute(query, (id,))
    row = cur.fetchone()
    if row is not None:
        print("\nID Mata Kuliah: ",row[0])
        print("Nama Mata Kuliah: ",row[1])
        print("SKS Mata Kuliah: ",row[2])
        print("Semester Mata Kuliah: ",row[3])
    else:
        print("Kosong :(")
    cur.close()

def read_mata_kuliah():
    cur = conn.cursor()
    query = "SELECT * FROM mata_kuliah"
    cur.execute(query)
    rows = cur.fetchall()
    print("\nID Mata Kuliah | Nama Mata Kuliah | SKS | Semester ID")
    for row in rows:
        print(row)
    print("Jumlah Row: ",cur.rowcount)
    cur.close()

def insert_mata_kuliah():
    total_imput = int(input("Maw input berapa data Le: "))
    for i in range(total_imput):
        cur = conn.cursor()
        nama_mata_kuliah = input("Masukkan Nama Matkul: ")
        sks = int(input("Masukkan Jumlah SKS: "))
        semester_id = int(input("Masukkan Semester Id: "))
        query = "INSERT INTO mata_kuliah(nama_mata_kuliah,sks,semester_id) VALUES(%s, %s, %s)"
        cur.execute(query, (nama_mata_kuliah, sks, semester_id))
    conn.commit()
    cur.close()

def update_mata_kuliah():
    cur = conn.cursor()
    id = int(input("Masukkan ID Matkul yang akan diupdate: "))
    nama_mata_kuliah = input("Masukkan Nama Matkul baru: ")
    sks = int(input("Masukkan Jumlah SKS baru: "))
    semester_id = int(input("Masukkan Semester Id baru: "))
    query = "UPDATE mata_kuliah SET nama_mata_kuliah = %s, sks = %s, semester_id = %s WHERE id_mata_kuliah = %s"
    cur.execute(query, (nama_mata_kuliah, sks, semester_id, id))
    conn.commit()
    cur.close()
    read_mata_kuliah_by_id(id)
    
def delete_mata_kuliah():
    id = int(input("Masukkan ID Matkul yang akan dihapus: "))
    cur = conn.cursor()
    query = "DELETE FROM mata_kuliah WHERE id_mata_kuliah = %s"
    cur.execute(query, (id,))
    conn.commit()
    cur.close()
    print(f"Matakuliah dengan id {id} sudah dihapus! .")
    
read_mata_kuliah()
print("\nMENU\n  1. Insert Mata Kuliah\n  2. Update Mata Kuliah\n  3. Delete Mata Kuliah\n  4. Exit\n")
menu = input("Pilih Menu: ")

match menu:
    case "1":
        insert_mata_kuliah()
    case "2":
        update_mata_kuliah()
    case "3":
        delete_mata_kuliah()
    case default:
        print("\n-- Keluar! --")


conn.close()