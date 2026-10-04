# Design Direction: Jungian MBTI Assessment (Friendly & Crafted)

## 1. Identitas & Karakter Produk
Instrumen evaluasi psikometrik dan arsitektur kognitif Carl Jung yang memadukan ketelitian klinis dengan atmosfer yang **ramah, hangat, dan memberdayakan (*friendly, warm, & lively*)**. Menghindari tampilan kaku korporat, warna monokrom dingin (*sterile default*), maupun efek visual klise generik (*AI slop*).

- **Mood:** Ramah, hangat, terpercaya, reflektif, dan modern (*welcoming & encouraging*).
- **Prinsip Utama:** Kejujuran data (evidence over claims), kemudahan navigasi yang santai, serta tipografi yang nyaman di mata.

---

## 2. Palet Warna & Sistem Tipologi

### A. Fondasi Kanvas
| Token | Nilai Hex | Peran & Tujuan |
|---|---|---|
| `--bg-canvas` | `#F8FAFC` | Latar kanvas utama yang sejuk, bersih, dan ramah mata |
| `--surface-card` | `#FFFFFF` | Permukaan kartu skenario, panel hasil, dan opsi pilihan |
| `--surface-subtle` | `#F1F5F9` | Latar sekunder untuk kontainer pendukung dan keyboard hints |
| `--border-light` | `#E2E8F0` | Garis batas kontainer yang rapi dan halus |
| `--border-hover` | `#A5B4FC` | Aksen visual lembut saat kartu pilihan disorot kursor |
| `--border-primary` | `#4F46E5` | Indikator pilihan aktif dan tombol utama warna warm indigo |
| `--text-title` | `#1E1B4B` | Teks judul utama bernuansa deep indigo hangat |
| `--text-main` | `#1E293B` | Teks utama dengan kontras rasio > 15:1 (WCAG AAA) |
| `--text-body` | `#475569` | Teks paragraf, skenario, dan penjelasan yang nyaman dibaca |
| `--text-muted` | `#64748B` | Label metadata, persentase sekunder, dan caption |

### B. Palet 4 Temperamen MBTI (David Keirsey / Carl Jung)
Setiap tipe MBTI memiliki identitas warna tematik yang cerah dan bersahabat pada halaman hasil:
- **Analis (Rational / NT):** `#4F46E5` (Warm Indigo), latar `#EEF2FF`, garis `#C7D2FE`. Mewakili visi strategis, pemodelan sistemik, dan penalaran logis (INTJ, INTP, ENTJ, ENTP).
- **Diplomat (Idealist / NF):** `#059669` (Fresh Emerald), latar `#ECFDF5`, garis `#A7F3D0`. Mewakili empati mendalam, inspirasi humanistik, dan kohesi nilai (INFJ, INFP, ENFJ, ENFP).
- **Pengawal (Sentinel / SJ):** `#0284C7` (Sky Cerulean), latar `#F0F9FF`, garis `#BAE6FD`. Mewakili keandalan operasional, dedikasi preseden, dan tanggung jawab prosedural (ISTJ, ISFJ, ESTJ, ESFJ).
- **Penjelajah (Explorer / SP):** `#D97706` (Warm Ochre), latar `#FFFBEB`, garis `#FDE68A`. Mewakili ketangkasan taktis langsung, kreativitas spontan, dan optimisme lapangan (ISTP, ISFP, ESTP, ESFP).

### C. Aksen Status & Zona Ekuilibrium
- **Zona Ekuilibrium (Borderline 47%–53%):** Latar `#FEF3C7`, teks `#92400E`, garis `#FDE68A`. Menandai fleksibilitas adaptif alami pada dimensi yang seimbang.

---

## 3. Sistem Tipografi

- **Font Utama (Body & Narasi):** `Plus Jakarta Sans` (Bobot: 400, 500, 600, 700, 800). Memberikan kenyamanan visual saat membaca skenario dan deskripsi profil.
- **Font Judul & Kode Hero:** `Space Grotesk` (Bobot: 600, 700, 800). Memberikan karakter terstruktur dan percaya diri pada judul serta badge singkatan kognitif (`[Ni]`, `[Te]`, dll.).
- **Font Monospace (Data Export):** `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas`. Khusus untuk area teks salinan hasil laporan.

---

## 4. Geometri, Elevasi & Mikro-Interaksi

- **Border Radius:**
  - Kartu Hero & Skenario: `18px` (`--radius-xl`)
  - Opsi Radio: `14px` (`--radius-lg`)
  - Tombol Navigasi: `10px` (`--radius-md`)
  - Status Tag & Rel Spektrum: `9999px` (`--radius-pill`)
- **Bayangan & Kedalaman (Shadows):**
  - Dasar: `0 2px 4px 0 rgba(79, 70, 229, 0.04)`
  - Kartu: `0 4px 12px -2px rgba(79, 70, 229, 0.06), 0 2px 6px -1px rgba(15, 23, 42, 0.03)`
  - Hover: `0 12px 24px -4px rgba(79, 70, 229, 0.10), 0 4px 8px -2px rgba(15, 23, 42, 0.04)`
- **Mikro-Interaksi:**
  - Kartu pilihan radio terangkat lembut saat disorot kursor (`translateY(-2px)`) dengan latar ungu lembut (`#FAF5FF`).
  - Tombol utama menggunakan gradien warm indigo (`linear-gradient(135deg, #4F46E5 0%, #4338CA 100%)`) dengan bayangan halus.
  - Visualizer spektrum memiliki penanda garis tengah (50%) untuk menunjukkan letak keseimbangan kontinu.

---

## 5. Dials & Parameter Anti-Slop

- **ENERGY (2/3 - Balanced & Warm):** Tampilan cerah dan bersahabat melalui aksen warna temperamen dan penataan kartu yang hangat.
- **RHYTHM (2/3 - Structured with Contextual Variety):** Alur 3 tahap (Beranda -> Kuis 24 Skenario -> Laporan Analisis Tabular) dengan variasi komposisi yang jelas.
- **MOTION (2/3 - Responsive Micro-Transitions):** Transisi hover taktil (180ms) dan animasi visualizer bar width easing (600ms).
