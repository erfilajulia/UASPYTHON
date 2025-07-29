import streamlit as st

# 🌟 Styling Title
st.markdown("""
    <style>
    .title {
        font-size:40px !important;
        color:#6a1b9a;
        font-weight:bold;
    }
    .footer {
        position: fixed;
        bottom: 10px;
        font-size: 13px;
        color: grey;
        text-align: center;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

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
st.markdown("<div class='title'>📋 TaskMate - Manajemen Tugas Harian</div>", unsafe_allow_html=True)
st.sidebar.title("👥 Info Kelompok")
st.sidebar.write("👩 Nama: Fulanah\n🧑 Nama: Temanmu")

st.markdown("### 🛠️ Pilihan Menu:")
st.markdown("1. 🔍 Lihat Tugas")
st.markdown("2. ➕ Tambah Tugas")
st.markdown("3. ✏ Ubah Tugas")
st.markdown("4. 🗑 Hapus Tugas")

menu = st.text_input("Masukkan angka menu (1-4):")

# Menu 1 - Lihat
if menu == "1":
    st.subheader("🔍 Lihat Tugas")
    if st.session_state.tasks:
        for i, task in enumerate(st.session_state.tasks):
            st.success(f"{i+1}. {task}")
    else:
        st.info("📭 Belum ada tugas.")

# Menu 2 - Tambah
elif menu == "2":
    st.subheader("➕ Tambah Tugas")
    id = st.number_input("🆔 Masukkan ID", step=1)
    nama = st.text_input("✍ Masukkan Nama Tugas")
    deadline = st.text_input("📅 Masukkan Deadline (contoh: 30-07-2025)")
    if st.button("💾 Simpan"):
        if nama and deadline:
            new_task = Task(id, nama, deadline)
            st.session_state.tasks.append(new_task)
            st.success("✅ Tugas berhasil ditambahkan.")
        else:
            st.warning("⚠️ Semua kolom harus diisi.")
            
# Menu 3 - Ubah
elif menu == "3":
    st.subheader("✏ Ubah Tugas")
    if st.session_state.tasks:
        id_ubah = st.number_input("Masukkan ID tugas yang ingin diubah", step=1)
        for task in st.session_state.tasks:
            if task.id == id_ubah:
                nama_baru = st.text_input("Nama baru", task.nama)
                deadline_baru = st.text_input("Deadline baru", task.deadline)
                selesai_baru = st.checkbox("Sudah selesai?", task.selesai)
                if st.button("Update"):
                    task.nama = nama_baru
                    task.deadline = deadline_baru
                    task.selesai = selesai_baru
                    st.success("Tugas berhasil diperbarui.")
                break
        else:
            st.warning("ID tidak ditemukan.")
    else:
        st.info("Belum ada tugas.")

# Menu 4 - Hapus
elif menu == "4":
    st.subheader("🗑 Hapus Tugas")
    if st.session_state.tasks:
        id_hapus = st.number_input("Masukkan ID tugas yang ingin dihapus", step=1)
        if st.button("Hapus"):
            for i, task in enumerate(st.session_state.tasks):
                if task.id == id_hapus:
                    st.session_state.tasks.pop(i)
                    st.success("Tugas berhasil dihapus.")
                    break
            else:
                st.warning("ID tidak ditemukan.")
    else:
        st.info("Belum ada tugas.")

# Validasi input
elif menu != "":
    st.warning("Masukkan angka 1 - 4 sesuai menu.")
