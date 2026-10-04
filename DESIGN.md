# Design Direction: Jungian MBTI Assessment (Lively & Tactile Glassmorphism)

## 1. Identitas & Karakter Produk
Instrumen evaluasi psikometrik dan arsitektur kognitif Carl Jung yang memadukan kedalaman analitis dengan atmosfer visual yang **berkarakter, hidup, ramah, dan taktil (*lively, tactile, & engaging*)** terinspirasi oleh standar arketipe visual modern ala `16Personalities`.

- **Aset Karakter:** Dilengkapi 16 avatar arketipe kepribadian visual berformat SVG lokal berkualitas tinggi yang dipetakan pada 4 kelompok temperamen utama.
- **Prinsip Estetika:** **Pure Glassmorphism & Tactile Interaction** (permukaan frosted glass tembus pandang dengan backdrop-filter blur, border kaca kilap elegan, ambient multi-point mesh gradient, dan mikro-interaksi taktil yang hidup).
- **Integritas Copywriting & Anti-Slop:** Bahasa naratif yang mengalir, imersif, kreatif, dan kaya imajinasi tanpa istilah hiperbolis generik (*AI buzzwords*), tanpa emoticon AI-slop, dan tanpa tanda sambung panjang (em dash). Diksi tombol dan kontrol fungsional tetap lugas dan bersih (*clean CTAs*).

---

## 2. Palet Warna & Sistem 4 Kelompok Temperamen

Setiap tipe MBTI dikelompokkan ke dalam 4 kuadran temperamen klasik Keirsey/Jung:

| Kelompok Temperamen | Kode MBTI | Warna Primer | Tint Glass Latar | Border Kaca Aksen |
|---|---|---|---|---|
| **Analis (Rational / NT)** | INTJ, INTP, ENTJ, ENTP | `#4F46E5` (Warm Indigo) | `rgba(238, 242, 255, 0.85)` | `#C7D2FE` |
| **Diplomat (Idealist / NF)** | INFJ, INFP, ENFJ, ENFP | `#059669` (Fresh Emerald) | `rgba(236, 253, 245, 0.85)` | `#A7F3D0` |
| **Pengawal (Sentinel / SJ)** | ISTJ, ISFJ, ESTJ, ESFJ | `#0284C7` (Sky Cerulean) | `rgba(240, 249, 255, 0.85)` | `#BAE6FD` |
| **Penjelajah (Explorer / SP)** | ISTP, ISFP, ESTP, ESFP | `#D97706` (Warm Ochre) | `rgba(255, 251, 235, 0.85)` | `#FDE68A` |

---

## 3. Sistem Desain: Glassmorphism & Tactile Tokens

### A. Glassmorphism Tokens
- **Latar Kaca Frosted:** `background: rgba(255, 255, 255, 0.78)` dengan `backdrop-filter: blur(16px - 18px)` dan `-webkit-backdrop-filter: blur(16px - 18px)`
- **Border Kaca Kilap:** `1.5px solid rgba(255, 255, 255, 0.85)`
- **Bayangan Halus & Refleksi Spekular:**
  - Normal: `0 14px 34px -4px rgba(31, 38, 135, 0.07), inset 0 1px 1.5px rgba(255, 255, 255, 0.95)`
  - Hover: `0 20px 42px -4px rgba(79, 70, 229, 0.14), inset 0 1px 1.5px rgba(255, 255, 255, 0.95)`
  - Soft: `0 8px 20px -3px rgba(31, 38, 135, 0.05), inset 0 1px 1px rgba(255, 255, 255, 0.9)`
- **Implementasi:**
  - Hero Card
  - Kartu Tiga Pilar Metodologi
  - Kartu Karakter Showcase
  - Kartu Skenario Soal Kuis
  - Kartu Opsi Pilihan Jawaban
  - Kartu Hasil Analisis Hero
  - Segmented Tab Switch Control

### B. Taktil & Mikro-Interaksi
- **Hover Elevation:** `transform: translateY(-2.5px) scale(1.002)` dengan peningkatan glow warna temperamen.
- **Active Click Press:** `transform: translateY(1px) scale(0.995)` memberikan sensasi fisik tombol saat ditekan.
- **Status Terpilih:** Border aksen warna primer 2px tebal dengan background tint hangat dan badge status `(Terpilih)`.

---

## 4. Alur & Efektivitas UI/UX Kuis (Compact & No-Scroll Mobile)

- **Layout Terpadu Bebas Scroll (Mobile-First):**
  - Mengeliminasi container bertingkat yang boros ruang vertikal. Header, nomor butir, persentase, dan popover daftar dirampingkan ke dalam satu baris fleksibel kompak.
  - Padding container utama di HP dipangkas menjadi `0.45rem 0.75rem` sehingga konten kuis langsung berada dalam pandangan mata (*above-the-fold*) tanpa perlu menggulir (*no scroll*).
- **Opsi Jawaban Sekali Klik (Instant Advance):**
  - Opsi jawaban berupa kartu tombol taktil full-width dengan tinggi kompak (`min-height: 44px - 48px`, padding `0.65rem 0.9rem`).
  - Memilih opsi langsung mencatat jawaban ke session state dan secara otomatis beralih ke butir soal berikutnya tanpa butuh tombol "Berikutnya".
  - Fitur toggle manual "Lanjut otomatis" dihilangkan karena mode langsung maju sudah menjadi perilaku bawaan (default).
- **Bar Progresi Ramping & Real-Time:**
  - Bar progresi disematkan tepat di bawah bar navigasi dengan ketebalan ramping (`6px`) tanpa pembungkus card tebal.
  - Transisi CSS halus `transition: width 0.35s cubic-bezier(0.16, 1, 0.3, 1)` bergerak realtime seketika saat opsi dipilih tanpa lag, glitch, atau jeda waktu `time.sleep`.
- **Navigasi Fleksibel:**
  - Tombol `Sebelumnya` selalu tersedia untuk meninjau atau mengubah jawaban butir sebelumnya.
  - Mengklik kembali opsi yang telah dipilih langsung memvalidasi dan memajukan soal tanpa terjebak.
  - Popover `Daftar butir` memungkinkan lompatan instan ke nomor butir manapun.
  - Di butir terakhir (24/24), setelah semua soal terjawab, tombol utama `Lihat hasil analisis` aktif dengan visual gradient yang menonjol.

---

## 5. Tata Letak Hasil Analisis, Spektrum 4 Dimensi & Segmented Tabs

- **Karakter Menyatu Alami (Seamless Avatar):**
  - Pada hero card hasil analisis, karakter SVG tidak lagi dibingkai oleh pod/card terpisah.
  - Karakter berdiri bebas secara organik berdampingan dengan identitas teks dan memiliki efek `drop-shadow` lembut sehingga menyatu harmonis dengan kanvas hero.
- **Spektrum Kecenderungan 4 Dimensi (Dual-Color & Anti Bar Kosong):**
  - **Pill Kategori Simetris:** Pill penanda kutub kiri dan kanan (misal Ekstraversi vs Introversi) memiliki lebar identik (50% dari row), tinggi seragam, dan tata letak simetris dengan indikator persentase serta tag dominan.
  - **Bar Dua Warna Penuh:** Menggantikan track abu-abu kosong dengan bar split dua warna yang terisi penuh 100% secara proporsional sesuai rasio persentase kedua kutub, dilengkapi marker tengah putih di titik seimbang 50%.
  - **Kartu Penjelasan Kompak:** Di bawah setiap bar spektrum, disematkan kartu penjelasan ringkas dan rapi dua kolom yang menguraikan definisi kognitif masing-masing kutub kecenderungan dengan penekanan visual pada sisi dominan.
- **Tab Simetris & Proporsional:**
  - Tombol tab di beranda (`Analis (NT)`, `Diplomat (NF)`, `Pengawal (SJ)`, `Penjelajah (SP)`) dan di halaman hasil (`Pola pikir`, `Kelebihan`, `Gaya kerja`, `Sisi stres`) diatur dengan lebar simetris dan proporsional (25% per tombol), sejajar presisi dengan lebar card di bawahnya.
  - Dilengkapi optimasi media query untuk resolusi mobile dan tablet agar tidak memicu scroll horizontal dan tetap terbaca jernih.

---

## 6. Fitur Mode Tampilan (Light & Dark Mode) & Standar Kontras Tinggi (WCAG AA/AAA)

- **Default Otomatis Mengikuti Device:**
  - Secara bawaan (*default*), tema menggunakan deteksi otomatis preferensi perangkat pengguna melalui `@media (prefers-color-scheme: dark)`.
- **Selector Manual di Top Bar:**
  - Kontrol ringkas `Auto`, `Terang`, `Gelap` di bar navigasi atas menggunakan `st.segmented_control` yang terintegrasi langsung dengan session state.
- **Standar Kontras Bebas Teks Bentrok (Anti Light-on-Light & Dark-on-Dark):**
  - **Eliminasi Teks Terang di Latar Terang:**
    - Pada Mode Terang, seluruh teks utama, judul, dan persentase spektrum menggunakan rona pekat (`#0F172A`, `#1E293B`, `#334155`, `#475569`) dengan rasio kontras 7.5:1 hingga 17.8:1 (Standar WCAG AAA).
    - Opsi kuis yang terpilih di mode terang menampilkan border primer tegas dengan teks gelap pekat berbobot bold (`font-weight: 700`) sehingga tidak lagi memicu teks putih di atas latar lavender muda.
    - Warna aksen dimensi spektrum dan temperamen disesuaikan dengan saturasi mendalam (misal Pemikiran `#0369A1` dan Eksplorasi `#065F46`), bukan warna pucat yang memudar di latar putih.
  - **Eliminasi Teks Gelap di Latar Gelap:**
    - Pada Mode Gelap, seluruh teks Streamlit (`p`, `span`, `div[data-testid="stMarkdownContainer"]`, `div[data-testid="stCaptionContainer"]`, label, dan header) diikat ketat ke token kontras terang (`#F8FAFC`, `#F1F5F9`, `#CBD5E1`, `#94A3B8`) dengan rasio kontras 6.7:1 hingga 18.5:1 (Standar WCAG AAA).
    - Opsi kuis yang belum terpilih menggunakan teks terang (`#F1F5F9`) di atas latar obsidian glass, mengeliminasi teks abu-abu gelap default Streamlit.
    - Kode MBTI dan nama temperamen menggunakan warna berpendar terang (`#A5B4FC`, `#6EE7B7`, `#7DD3FC`, `#FCD34D`) dengan rasio kontras > 8.5:1 pada latar gelap.
  - **Kontras Khusus Komponen Interaktif (Tombol Tema, Unduh, dan Kembali ke Beranda):**
    - **Pengatur Pilihan Tema (`st.segmented_control`):**
      - Menggunakan selektor komprehensif Streamlit 1.65 (`div[data-testid="stButtonGroup"]`, `button[data-variant="segmented_control"]`, dan state `[data-selected]`).
      - Mode Terang: Track bernuansa abu-abu sejuk (`#F1F5F9`), opsi pasif berwarna slate (`#475569`, 5.5:1), dan opsi aktif putih solid (`#FFFFFF`) dengan teks indigo (`#4F46E5`, 8.5:1).
      - Mode Gelap: Track slate gelap (`#1E293B`), opsi pasif terang (`#94A3B8`, 5.2:1), dan opsi aktif indigo vibrant (`#4F46E5`) dengan teks putih solid (`#FFFFFF`, 8.5:1) berborder `#818CF8`.
    - **Tombol Sekunder & Tombol Unduh (`st.download_button` & `Kembali ke beranda`):**
      - Ditargetkan secara spesifik melalui `div[data-testid="stDownloadButton"] button`, `button[data-testid*="secondary"]`, dan child icon material.
      - Mode Terang: Latar putih padat `#FFFFFF`, border tegas `#CBD5E1`, teks dan ikon pekat `#0F172A` (16.1:1 AAA).
      - Mode Gelap: Latar dark slate `#1E293B`, border kilap halus `rgba(255, 255, 255, 0.22)`, teks dan ikon putih bersih `#F8FAFC` (11.4:1 AAA), tidak lagi bentrok dengan latar default Streamlit.
- **Harmoni Desain Kaca di Kedua Mode:**
  - **Mode Terang:** Kanvas off-white sejuk (`#F8FAFC`), permukaan kaca putih susu transparan, border halus, teks slate pekat berdaya baca tinggi.
  - **Mode Gelap:** Kanvas deep navy charcoal (`#090D16`), permukaan obsidian glass semi-transparan, border kaca bercahaya lembut, teks kontras tinggi (`#F8FAFC`).

---

## 7. Diksi Tombol & Copywriting (Clean Anti-Slop Standard)

- **Tombol Utama (Clean CTAs):**
  - Beranda: `Mulai asesmen`
  - Kuis: `Sebelumnya`, `Lihat hasil analisis`
  - Hasil: `Ulangi asesmen`, `Kembali ke beranda`, `Unduh dokumen laporan (.txt)`
- **Bebas Emoticon Slop:** Tidak menggunakan emoji generic (🤖, ✨, 🧠, 🚀). Mengutamakan Google Material Symbols untuk ikon fungsional.

---

## 8. Indikator Visual Keseimbangan (Balanced / Adaptive Traits)

Ketika skor dimensi berada di rentang tengah yang seimbang (50% : 50% atau 47%–53%), antarmuka secara otomatis mengaktifkan visual khusus keseimbangan adaptif alih-alih memaksakan salah satu kutub sebagai dominan:

1. **Badge Keseimbangan di Hero Identity:**
   - Ditampilkan chip `⚖️ {n} Dimensi Seimbang` mendampingi kode MBTI dan arketipe utama.
2. **Kartu Khusus Analisis Seimbang (Balanced Advisory Card):**
   - Kartu kaca bergradien aksen menampilkan penjelasan konsep *psychological adaptability* (keluwesan adaptif Carl Jung).
   - Chip visual tiap dimensi seimbang: misal `⚖️ Mind: Ekstraversi 50% ⇄ 50% Introversi (Ambivert)`.
3. **Pills Spektrum Co-Equal:**
   - Kedua pill kutub (kiri dan kanan) aktif bersamaan dengan styling `balanced` bergaris aksen putus-putus (`1.5px dashed var(--border-primary)`).
   - Label persentase menyematkan tag `· Seimbang` pada kedua sisi, mengeliminasi status "dimmed / muted".
4. **Pin Keseimbangan Luminous (Gold Marker):**
   - Garis pemisah tengah di track spektrum bertransformasi menjadi pin emas menyala (`#FFB800`) berikon `⚖` di atasnya.
5. **Catatan Adaptif pada Kartu Penjelasan:**
   - Kedua kartu penjelasan definisi kognitif diaktifkan secara simetris, disertai panel catatan: *"Kedua Kutub Seimbang: Kamu tidak terkunci pada satu kutub dominan, melainkan memiliki keluwesan alami beralih mode berpikir sesuai situasi nyata."*
