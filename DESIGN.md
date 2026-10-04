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

## 5. Tata Letak Hasil Analisis & Segmented Tabs

- **Karakter Menyatu Alami (Seamless Avatar):**
  - Pada hero card hasil analisis, karakter SVG tidak lagi dibingkai oleh pod/card terpisah.
  - Karakter berdiri bebas secara organik berdampingan dengan identitas teks dan memiliki efek `drop-shadow` lembut sehingga menyatu harmonis dengan kanvas hero.
- **Tab Ringkas Bebas Scroll Horizontal:**
  - Label 4 tab analisa dibuat ringkas dan padat: `Pola pikir`, `Kelebihan`, `Gaya kerja`, dan `Sisi stres`.
  - Tab bar diformat sebagai segmented switch glass pill yang membagi kolom secara proporsional (`flex: 1 1 0`) sehingga muat sempurna pada desktop maupun ponsel tanpa memicu scroll horizontal.

---

## 6. Diksi Tombol & Copywriting (Clean Anti-Slop Standard)

- **Tombol Utama (Clean CTAs):**
  - Beranda: `Mulai asesmen`
  - Kuis: `Sebelumnya`, `Lihat hasil analisis`
  - Hasil: `Ulangi asesmen`, `Kembali ke beranda`, `Unduh dokumen laporan (.txt)`
- **Bebas Emoticon Slop:** Tidak menggunakan emoji generic (🤖, ✨, 🧠, 🚀). Mengutamakan Google Material Symbols untuk ikon fungsional.
