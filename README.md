# Pertemuan 02 - Dasar Python dan Pengumpulan GitHub

Identitas Mahasiswa

* **Nama :** Maila Andira Putri
* **NIM :** 2225250126
* **Kelas :** 3A

---

## Deskripsi Repositori

Repositori ini berisi latihan dasar pemrograman Python (variabel, tipe data, input-output, operator) serta tugas kalkulator koordinat untuk Pertemuan 02.

## Struktur Berkas

* `latihan/01_biodata.py` : Latihan variabel dan tipe data string.
* `latihan/02_persegi_panjang.py` : Latihan menghitung luas persegi panjang.
* `latihan/03_konversi_suhu.py` : Latihan konversi Celsius ke Fahrenheit.
* `latihan/04_nilai_akhir.py` : Latihan menghitung bobot nilai.
* `tugas/kalkulator_koordinat.py` : Menghitung dx, dy, jarak Euclidean, dan titik tengah dua titik.

## Cara Menjalankan Program

## 1. Menjalankan Berkas Latihan

```bash
python latihan/01_biodata.py
python latihan/02_persegi_panjang.py
python latihan/03_konversi_suhu.py
python latihan/04_nilai_akhir.py

## 2. Menjalankan Tugas Utama

```bash
python tugas/kalkulator_koordinat.py

## Flowchart Program
graph TD
    Start([Start]) --> Input1[/Input x1, y1/]
    Input1 --> Input2[/Input x2, y2/]
    Input2 --> Process1[Hitung dx = x2 - x1<br>Hitung dy = y2 - y1]
    Process1 --> Process2["Hitung Jarak = √(dx² + dy²)"]
    Process2 --> Process3["Hitung Midpoint:<br>xm = (x1 + x2) / 2<br>ym = (y1 + y2) / 2"]
    Process3 --> Output[/Tampilkan dx, dy, Jarak, Midpoint/]
    Output --> End([End])
    