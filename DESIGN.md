# Design Direction: Jungian MBTI Assessment

## 1. Identitas & Karakter Produk
Instrumen evaluasi psikometrik dan arsitektur kognitif Carl Jung yang memadukan ketelitian klinis, kejelasan analitis, dan estetika visual yang hidup serta berkarakter (lively & crafted). Menghindari gaya korporat kaku, tampilan monokrom hambar (sterile default), maupun estetika futuristik klise (AI slop).

- **Mood:** Klinis, terpercaya, berkarakter, reflektif, dan modern.
- **Prinsip Utama:** Kejujuran data (evidence over claims), navigasi spontan dan ergonomis, serta tipografi yang nyaman dibaca.

---

## 2. Palet Warna & Sistem Tipologi

### A. Fondasi Kanvas
| Token | Nilai Hex | Peran & Tujuan |
|---|---|---|
| `--bg-main` | `#F8FAFC` | Latar kanvas utama yang sejuk dan ramah mata |
| `--surface-card` | `#FFFFFF` | Permukaan kartu skenario, panel hasil, dan opsi pilihan |
| `--surface-subtle` | `#F1F5F9` | Latar sekunder untuk kontainer pendukung dan keyboard hints |
| `--border-subtle` | `#E2E8F0` | Garis batas kontainer yang rapi dan halus |
| `--border-hover` | `#CBD5E1` | Indikasi visual saat elemen pilihan disorot kursor |
| `--border-focus` | `#0F172A` | Indikator pilihan aktif dan fokus kontras tinggi |
| `--text-primary` | `#0F172A` | Teks judul dan opsi utama (> 17:1 rasio kontras WCAG AAA) |
| `--text-secondary` | `#334155` | Teks paragraf, skenario, dan penjelasan |
| `--text-muted` | `#64748B` | Label metadata, persentase sekunder, dan caption |

### B. Palet 4 Temperamen MBTI (David Keirsey / Carl Jung)
Setiap tipe MBTI memiliki identitas warna tematik yang hidup pada halaman hasil:
- **Analis (Rational / NT):** `#4338CA` (Indigo), latar `#EEF2FF`, garis `#C7D2FE`. Mewakili strategi konseptual, pemodelan sistemik, dan penalaran logis (INTJ, INTP, ENTJ, ENTP).
- **Diplomat (Idealist / NF):** `#047857` (Emerald), latar `#ECFDF5`, garis `#A7F3D0`. Mewakili wawasan humanistik, empati mendalam, dan kohesi nilai (INFJ, INFP, ENFJ, ENFP).
- **Pengawal (Sentinel / SJ):** `#0369A1` (Ocean Slate), latar `#F0F9FF`, garis `#BAE6FD`. Mewakili keandalan operasional, ketelitian preseden, dan tanggung jawab prosedural (ISTJ, ISFJ, ESTJ, ESFJ).
- **Penjelajah (Explorer / SP):** `#B45309` (Warm Ochre), latar `#FFFBEB`, garis `#FDE68A`. Mewakili ketangkasan taktis langsung, eksperimen dinamis, dan responsivitas lapangan (ISTP, ISFP, ESTP, ESFP).

### C. Aksen Status & Zona Ekuilibrium
- **Zona Ekuilibrium (Borderline 47%–53%):** Latar `#FEF3C7`, teks `#92400E`, garis `#FDE68A`. Menandai fleksibilitas adaptif situasional pada dimensi yang seimbang.

---

## 3. Sistem Tipografi

- **Font Utama (Body & Narasi):** `Plus Jakarta Sans` (Bobot: 400, 500, 600, 700). Memberikan keterbacaan optimal pada teks skenario dan deskripsi profil.
- **Font Judul & Kode Hero:** `Space Grotesk` (Bobot: 600, 700). Memberikan karakter kuat dan tegas pada kode tipe MBTI, judul halaman, dan badge singkatan fungsi kognitif (`[Ni]`, `[Te]`, dll.).
- **Font Monospace (Data Export):** `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas`. Digunakan khusus untuk area teks salinan hasil laporan.

---

## 4. Geometri, Elevasi & Mikro-Interaksi

- **Border Radius:**
  - Kartu & Hero: `14px` (`--radius-lg`)
  - Tombol & Opsi Radio: `10px` (`--radius-md`)
  - Status Tag & Rel Spektrum: `9999px` (`--radius-pill`)
- **Bayangan & Kedalaman (Shadows):**
  - Dasar: `0 1px 3px 0 rgba(15, 23, 42, 0.04)`
  - Kartu: `0 4px 6px -1px rgba(15, 23, 42, 0.05), 0 2px 4px -2px rgba(15, 23, 42, 0.03)`
  - Hover: `0 10px 18px -3px rgba(15, 23, 42, 0.07), 0 4px 6px -2px rgba(15, 23, 42, 0.04)`
- **Mikro-Interaksi:**
  - Kartu pilihan radio terangkat halus saat kursor mengambang (`translateY(-2px)`) dengan transisi kubik natural.
  - Opsi terpilih menampilkan border kontras ganda yang presisi.
  - Visualizer spektrum memiliki penanda garis tengah (50%) untuk menunjukkan letak keseimbangan kontinu.

---

## 5. Dials & Parameter Anti-Slop

- **ENERGY (2/3 - Balanced & Expressive):** Desain memiliki karakter kuat melalui aksen warna temperamen dan penataan kartu yang berwibawa, tanpa terjebak dalam efek glow atau warna neon sembarangan.
- **RHYTHM (2/3 - Structured with Contextual Variety):** Alur 3 tahap (Beranda -> Kuis 24 Skenario -> Laporan Analisis Tabular) dengan variasi komposisi yang jelas antara skenario, spektrum batang, dan kartu 4 lapisan fungsi kognitif.
- **MOTION (2/3 - Responsive Micro-Transitions):** Transisi hover taktil (180ms), visualizer bar width easing (600ms), dan tombol interaktif yang responsif terhadap ketukan/klik. Bebas dari animasi pulse atau looping tanpa akhir.
