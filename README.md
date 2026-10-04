# MBTI Assessment: Clinical Psychometrics & Jungian Cognitive Stack

Aplikasi asesmen kepribadian spektrum MBTI berbasis web interaktif dengan **Streamlit**, berlandaskan 8 fungsi kognitif Carl Jung dan pendekatan psikometri non-ekstrem.

---

## Fitur Utama
1. **24 Skenario Realistis & Non-Ekstrem**: Dilema interaksi sosial dan profesional yang seimbang tanpa opsi jebakan/klise.
2. **Spektrum Kontinu (0–100%)**: Menghitung persentase presisi untuk 4 dimensi utama:
   - Mind: *Extraversion (E) vs Introversion (I)*
   - Energy: *Sensing (S) vs Intuition (N)*
   - Nature: *Thinking (T) vs Feeling (F)*
   - Tactics: *Judging (J) vs Prospecting (P)*
3. **Deteksi Borderline Trait (47%–53%)**: Mengidentifikasi spektrum seimbang di mana pengguna memiliki adaptabilitas luwes antar mode.
4. **Bedah 4 Lapisan Fungsi Kognitif**:
   - Dominant (Driver Utama)
   - Auxiliary (Co-Pilot)
   - Tertiary (Mode Rekreasi)
   - Inferior (Titik Buta / Stres)
5. **Optimasi UX & Aksesibilitas**:
   - **Randomisasi Opsi Butir**: Urutan letak opsi jawaban diacak secara dinamis per sesi asesmen.
   - **Auto-Advance Cerdas**: Pilihan toggle di header kuis dengan jeda perpindahan yang mulus.
   - **Responsivitas Mobile**: Target sentuh tombol (min 48px) dan tata letak popover yang pas di layar sentuh HP.
6. **Ekspor Laporan**: Salin atau unduh ringkasan hasil evaluasi dalam format `.txt`.

---

## Cara Menjalankan

### 1. Prasyarat
Pastikan Python 3.9+ sudah terpasang di perangkat.

### 2. Instalasi Dependensi
```bash
pip install -r requirements.txt
```

### 3. Menjalankan Aplikasi
- **Windows (Sekali Klik)**: Buka file `run.bat` atau shortcut `Jalankan MBTI.lnk`.
- **Terminal / CLI**:
  ```bash
  python -m streamlit run app.py
  ```
Aplikasi akan otomatis terbuka di browser pada URL default `http://localhost:8501`.

---

## Struktur Berkas
- `app.py`: Antarmuka UI Streamlit, state management kuis, styling responsif kustom (Claymorphism & Glassmorphism).
- `engine.py`: Scoring engine psikometri, pemetaan dimensi spektrum, dan penentu fungsi kognitif.
- `profiles.py`: Basis data deskripsi komprehensif ke-16 tipe kepribadian.
- `questions.json`: Bank data 24 butir soal skenario realistis.
- `run.bat`: Skrip runner sekali klik untuk lingkungan Windows.