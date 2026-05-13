import hashlib
import json
import os

# Database untuk menyimpan user dan password (dalam bentuk hash)
DATABASE_FILE = "users_db.json"

# Fungsi Utilitas
def hash_password_sha256(password: str) -> str:
    """Mengubah password menjadi hash SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def load_database() -> dict:
    """Memuat database user dari file JSON."""
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_database(users: dict) -> None:
    """Menyimpan database user ke file JSON."""
    with open(DATABASE_FILE, "w") as f:
        json.dump(users, f, indent=4)


def print_separator(char="─", length=55):
    print(char * length)


def print_header():
    print_separator("═")
    print("  SISTEM REGISTRASI & LOGIN — SHA-256 KRIPTOGRAFI")
    print(f"  Nama    : Andi Akbar Arya Putra")
    print(f"  No. Urut: 03")
    print_separator("═")

# Fitur 1: Registrasi User
def registrasi_user():
    """Melakukan registrasi user baru dengan password ter-hash SHA-256."""
    print("\n" + "─" * 55)
    print("  📝  REGISTRASI USER BARU")
    print_separator()

    users = load_database()

    username = input("  Masukkan username : ").strip()
    if not username:
        print("  ❌ Username tidak boleh kosong!")
        return

    if username in users:
        print(f"  ❌ Username '{username}' sudah terdaftar.")
        return

    password = input("  Masukkan password  : ").strip()
    if not password:
        print("  ❌ Password tidak boleh kosong!")
        return

    # Mengubah password menjadi hash SHA-256
    hashed = hash_password_sha256(password)

    # Menyimpan username dan hash password
    users[username] = {"hash_password": hashed}
    save_database(users)

    # Menampilkan hasil Hash Password
    print_separator()
    print(f"  ✅ Registrasi berhasil!")
    print(f"  👤 Username       : {username}")
    print(f"  🔑 Password asli  : {'*' * len(password)}")
    print(f"  🔐 Hash SHA-256   :")
    print(f"     {hashed}")
    print_separator()

# Fitur 2: Login User
def login_user():
    """Melakukan login dengan memverifikasi hash password."""
    print("\n" + "─" * 55)
    print("  🔓  LOGIN USER")
    print_separator()

    users = load_database()

    username = input("  Masukkan username : ").strip()
    if not username:
        print("  ❌ Username tidak boleh kosong!")
        return

    password = input("  Masukkan password  : ").strip()

    # Mengubah input password menjadi hash SHA-256
    input_hash = hash_password_sha256(password)

    print_separator()
    print(f"  👤 Username         : {username}")
    print(f"  🔐 Hash Input       :")
    print(f"     {input_hash}")

    # Memverifikasi password login
    if username not in users:
        print_separator()
        print(f"  ❌ STATUS LOGIN : GAGAL")
        print(f"  ℹ️  Username '{username}' tidak ditemukan.")
        print_separator()
        return

    stored_hash = users[username]["hash_password"]
    print(f"  🗄️  Hash Tersimpan  :")
    print(f"     {stored_hash}")
    print_separator()

    # Menampilkan status login
    if input_hash == stored_hash:
        print(f"  ✅ STATUS LOGIN : BERHASIL")
        print(f"  🎉 Selamat datang, {username}!")
    else:
        print(f"  ❌ STATUS LOGIN : GAGAL")
        print(f"  ⚠️  Password yang Anda masukkan salah.")
    print_separator()

# Fitur 3: Lihat Semua User
def lihat_semua_user():
    """Menampilkan daftar user dan hash password yang tersimpan."""
    print("\n" + "─" * 55)
    print("  📋  DAFTAR USER TERDAFTAR")
    print_separator()

    users = load_database()

    if not users:
        print("  ℹ️  Belum ada user yang terdaftar.")
        print_separator()
        return

    for i, (uname, data) in enumerate(users.items(), 1):
        print(f"  [{i}] Username : {uname}")
        print(f"      Hash     : {data['hash_password']}")
        print()

    print_separator()

# Fitur 4: Tes SHA-256
def demo_sha256():
    """Menampilkan test konversi password ke SHA-256."""
    print("\n" + "─" * 55)
    print("  🧪  TEST SHA-256 HASHING")
    print_separator()

    teks = input("  Masukkan teks/password : ").strip()
    if not teks:
        print("  ❌ Teks tidak boleh kosong!")
        return

    hasil = hash_password_sha256(teks)
    print_separator()
    print(f"  Input     : {teks}")
    print(f"  Algoritma : SHA-256")
    print(f"  Output    :")
    print(f"  {hasil}")
    print(f"\n  Panjang hash : {len(hasil)} karakter ({len(hasil)*4} bit)")
    print_separator()

# Halaman Utama
def main():
    print_header()

    while True:
        print("\n  MENU UTAMA:")
        print("  [1] Registrasi User")
        print("  [2] Login User")
        print("  [3] Lihat Semua User")
        print("  [4] Test SHA-256")
        print("  [0] Keluar")
        print_separator()

        pilihan = input("  Pilih menu [0-4] : ").strip()

        if pilihan == "1":
            registrasi_user()
        elif pilihan == "2":
            login_user()
        elif pilihan == "3":
            lihat_semua_user()
        elif pilihan == "4":
            demo_sha256()
        elif pilihan == "0":
            print("\n  👋 Terima kasih. Program selesai.")
            print_separator("═")
            break
        else:
            print("  ⚠️  Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
