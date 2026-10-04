# Design Direction: Jungian MBTI Assessment (Claymorphism & Glassmorphism Hybrid)

## 1. Identitas & Karakter Produk
Instrumen evaluasi psikometrik dan arsitektur kognitif Carl Jung yang memadukan kedalaman analitis dengan atmosfer visual yang **berkarakter, hidup, ramah, dan taktil (*lively, tactile, & engaging*)** terinspirasi oleh standar arketipe visual modern ala `16Personalities`.

- **Aset Karakter:** Dilengkapi 16 avatar arketipe kepribadian visual berformat SVG lokal berkualitas tinggi yang dipetakan pada 4 kelompok temperamen utama.
- **Prinsip Estetika:** Perpaduan **Claymorphism** (volume 3D lembut bantal/clay dengan dual inset shadow) dan **Glassmorphism** (aksen frosted glass tembus pandang dengan backdrop-filter blur).
- **Integritas Copywriting & Anti-Slop:** Bahasa naratif yang mengalir, imersif, kreatif, dan kaya imajinasi tanpa istilah hiperbolis generik (*AI buzzwords*) dan tanpa tanda sambung panjang (em dash). Diksi tombol dan kontrol fungsional tetap lugas dan bersih (*clean CTAs*).

---

## 2. Palet Warna & Sistem 4 Kelompok Temperamen

Setiap tipe MBTI dikelompokkan ke dalam 4 kuadran temperamen klasik Keirsey/Jung:

| Kelompok Temperamen | Kode MBTI | Warna Primer | Tint Latar | Border Aksen |
|---|---|---|---|---|
| **Analis (Rational / NT)** | INTJ, INTP, ENTJ, ENTP | `#4F46E5` (Warm Indigo) | `#EEF2FF` | `#C7D2FE` |
| **Diplomat (Idealist / NF)** | INFJ, INFP, ENFJ, ENFP | `#059669` (Fresh Emerald) | `#ECFDF5` | `#A7F3D0` |
| **Pengawal (Sentinel / SJ)** | ISTJ, ISFJ, ESTJ, ESFJ | `#0284C7` (Sky Cerulean) | `#F0F9FF` | `#BAE6FD` |
| **Penjelajah (Explorer / SP)** | ISTP, ISFP, ESTP, ESFP | `#D97706` (Warm Ochre) | `#FFFBEB` | `#FDE68A` |

---

## 3. Sistem Desain: Claymorphism + Glassmorphism Hybrid

### A. Claymorphism Tokens (Volume & Taktilitas 3D)
- **Fondasi Permukaan:** `#FFFFFF` dengan lengkungan ramah (`border-radius: 20px - 24px`).
- **Dual Inset Shadow:**
  - Kiri-atas terang: `inset 4px 4px 8px rgba(255, 255, 255, 0.95)`
  - Kanan-bawah teduh: `inset -4px -4px 8px rgba(15, 23, 42, 0.035)`
- **Drop Shadow Mengapung:**
  - Normal: `0 14px 28px -4px rgba(79, 70, 229, 0.08), 0 4px 10px -2px rgba(15, 23, 42, 0.03)`
  - Hover: `0 18px 36px -4px rgba(79, 70, 229, 0.12)` dengan elevasi `translateY(-3px)` atau `translateY(-4px)`
- **Implementasi:**
  - Hero Card
  - Kartu Skenario Pilihan
  - Kartu Karakter Arketipe (Avatar Pod)
  - Pilihan Radio Jawaban

### B. Glassmorphism Tokens (Aksen Kaca Elegan)
- **Latar Kaca Frosted:** `background: rgba(255, 255, 255, 0.72)` dengan `backdrop-filter: blur(14px)`
- **Border Kaca Kilap:** `1px solid rgba(255, 255, 255, 0.65)`
- **Bayangan Halus:** `0 4px 14px rgba(31, 38, 135, 0.05)`
- **Implementasi:**
  - Badge Kategori & Metadata Butir
  - Pill Chips Fitur & Fungsi Kognitif Dominan
  - Bar Status Navigasi & Pintasan Keyboard
  - Kotak Tagline Arketipe

---

## 4. Tata Letak Desktop Proporsional & Responsif

- **Ukuran Kanvas:** Maksimal `880px` di desktop dengan margin yang lega dan simetris.
- **Kesejajaran Card:**
  - Menggunakan CSS Grid (`grid-template-columns: repeat(4, 1fr)` pada desktop dan `repeat(2, 1fr)` pada tablet) untuk showcase karakter.
  - Tiga pilar metodologi disusun dalam grid 3 kolom proporsional dengan tinggi seragam (`height: 100%`).
  - Hero Card Hasil menggunakan layout split 2 kolom: Identitas teks di sisi kiri dan Avatar Karakter dalam bingkai claymorphic di sisi kanan.

---

## 5. Diksi Tombol & Copywriting (Anti-Slop Clean Standard)

- **Tombol Utama (Clean CTAs):**
  - Beranda: `Mulai asesmen`
  - Kuis: `Sebelumnya`, `Berikutnya`, `Lihat hasil analisis`
  - Hasil: `Ulangi asesmen`, `Kembali ke beranda`, `Unduh dokumen laporan (.txt)`
- **Narasi & Arketipe:**
  - Setiap tipe memiliki nama julukan berbobot (misal: "INTJ · Sang Arsitek Strategis", "INFP · Sang Mediator Autentik").
  - Penjelasan kognitif menyajikan dinamika pemikiran secara imersif, manusiawi, dan terstruktur tanpa klaim hiperbolik klise.
  - Bebas dari tanda sambung panjang (em dash).
