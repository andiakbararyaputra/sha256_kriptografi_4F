# 🔐 SHA-256 Password Hashing — Sistem Registrasi & Login

> Tugas Mata Kuliah Kriptografi

---

## 📋 Nama

| | |
|---|---|
| **Nama Lengkap** | Andi Akbar Arya Putra |
| **No. Urut** | 03 |
| **Mata Kuliah** | Kriptografi |
| **Universitas** | Universitas Muhammadiyah Makassar |

---

## 📖 Deskripsi

Program ini mengimplementasikan sistem **registrasi dan login user** dengan menggunakan **SHA-256** untuk mengamankan password. Password tidak pernah disimpan dalam bentuk asli (plaintext), melainkan diubah menjadi nilai hash sebelum disimpan ke database.

---

## ✅ Fitur

- [x] Registrasi user baru
- [x] Mengubah password menjadi hash SHA-256
- [x] Menyimpan username dan hash password ke file JSON
- [x] Menampilkan hasil Hash Password
- [x] Login user
- [x] Memverifikasi password saat login
- [x] Menampilkan status login (berhasil / gagal)
- [x] Demo konversi teks ke SHA-256 *(bonus)*

---

## 🛠️ Yang Digunakan di Dalam Program

- **Bahasa** : Python 3
- **Library** : `hashlib` (built-in), `json` (built-in), `os` (built-in)
- **Algoritma** : SHA-256 (Secure Hash Algorithm 256-bit)

> Tidak memerlukan instalasi library tambahan.

---

## 🚀 Cara Menjalankan

**1. Clone repository ini**
```bash
git clone https://github.com/andiakbararyaputra/sha256_kriptografi_4F.git
cd sha256_kriptografi_4F
```

**2. Jalankan program**
```bash
python3 sha256_login_andi_akbar_03.py
```

---

## 🔄 Alur Kerja

### Registrasi
```
Password (plaintext)
        │
        ▼
  hashlib.sha256()
        │
        ▼
  Hash SHA-256 (64 karakter hex)
        │
        ▼
  Disimpan ke users_db.json
```

### Login
```
Password Input (plaintext)
        │
        ▼
  hashlib.sha256()
        │
        ▼
  Hash SHA-256
        │
        ▼
  Dibandingkan dengan hash tersimpan
        │
     ┌──┴──┐
   Cocok  Tidak Cocok
     │        │
  ✅ Login  ❌ Gagal
  Berhasil
```

---

## 📚 Konsep SHA-256

**SHA-256** (Secure Hash Algorithm 256-bit) adalah fungsi hash kriptografis yang menghasilkan output sepanjang **256 bit (64 karakter hexadecimal)**. Sifat-sifatnya:

| Sifat | Keterangan |
|-------|------------|
| **Deterministik** | Input yang sama selalu menghasilkan hash yang sama |
| **One-way** | Tidak bisa dikembalikan ke bentuk asli (irreversible) |
| **Avalanche Effect** | Perubahan kecil pada input menghasilkan hash yang sangat berbeda |
| **Collision Resistant** | Hampir mustahil dua input berbeda menghasilkan hash yang sama |

---

## 📝 Tugas

Dibuat untuk keperluan tugas akademik mata kuliah Kriptografi.
