import streamlit as st

# Kelas Tugas
class Task:
    def __init__(self, id, nama, deadline, selesai=False):
        self.id = id
        self.nama = nama
        self.deadline = deadline
        self.selesai = selesai

    def __str__(self):
        status = "✅" if self.selesai else "❌"
        return f"ID: {self.id}, Tugas: {self.nama}, Deadline: {self.deadline}, Status: {status}"

# Inisialisasi session_state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Judul dan Menu
st.title("📋 TaskMate - Manajemen Tugas Harian")
st.write("### Pilihan Menu:")
st.write("1. Lihat Tugas")
st.write("2. Tambah Tugas")
st.write("3. Ubah Tugas")
st.write("4. Hapus Tugas")

menu = st.text_input("Masukkan angka menu (1-4):")

# Menu 1 - Lihat
if menu == "1":
    st.subheader("📄 Daftar Tugas")
    if st.session_state.tasks:
        for i, task in enumerate(st.session_state.tasks):
            st.write(f"{i+1}. {task}")
    else:
        st.info("Belum ada tugas.")

# Menu 2 - Tambah
elif menu == "2":
    st.subheader("➕ Tambah Tugas")
    id = st.number_input("Masukkan ID", step=1)
    nama = st.text_input("Masukkan Nama Tugas")
    deadline = st.text_input("Masukkan Deadline (contoh: 30-07-2025)")
    if st.button("Simpan"):
        if nama and deadline:
            new_task = Task(id, nama, deadline)
            st.session_state.tasks.append(new_task)
            st.success("Tugas berhasil ditambahkan.")
        else:
            st.warning("Semua kolom harus diisi.")
