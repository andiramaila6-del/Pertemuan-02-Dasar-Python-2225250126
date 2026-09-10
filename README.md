# Pertemuan 02 - Dasar Python

**Nama:** Maila Andira Putri  
**NIM:** 2225250126  
**Kelas:** 3A  
**Mata Kuliah:** Algoritma dan Pemrograman  

---

## Deskripsi Repository
Repository ini berisi latihan dasar pemrograman Python (variabel, tipe data, input-output, operator) serta tugas utama berupa kalkulator koordinat dua titik.

---

## Struktur Berkas
- `Latihan/`: Berisi kode latihan dasar Python.
  - `01_Biodata.py`: Menghitung umur berdasarkan tahun lahir.
  - `02_Persegi_Panjang.py`: Menghitung luas dan keliling persegi panjang.
  - `03_Konversi_Suhu.py`: Konversi suhu Celsius ke Fahrenheit dan Kelvin.
  - `04_Nilai_Akhir.py`: Menghitung nilai akhir berbobot.
- `Tugas/`:
  - `Kalkulator_Koordinat.py`: Menghitung $dx$, $dy$, jarak Euclidean, dan titik tengah dari dua koordinat.

---

## Cara Menjalankan Program
Jalankan perintah berikut di terminal VS Code:

```bash
# Menjalankan latihan
python Latihan/01_Biodata.py

# Menjalankan tugas utama
python Tugas/Kalkulator_Koordinat.py

## Flowchart Program

mermaid
graph TD
    A([Start]) --> B[/Input x1, y1/]
    B --> C[/Input x2, y2/]
    C --> D[Hitung dx = x2 - x1<br>Hitung dy = y2 - y1]
    D --> E["Hitung Jarak = √(dx² + dy²)"]
    E --> F["Hitung Midpoint:<br>xm = (x1 + x2) / 2<br>ym = (y1 + y2) / 2"]
    F --> G[/Tampilkan dx, dy, Jarak, Midpoint/]
    G --> H([End])
