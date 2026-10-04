from __future__ import annotations
import base64
import os
from typing import Dict, List, Optional

PROFILES: Dict[str, Dict] = {
    "INTJ": {
        "code": "INTJ",
        "archetype": "Sang Arsitek Strategis",
        "title": "INTJ · Sang Arsitek Strategis",
        "tagline": "Melihat pola masa depan sebelum orang lain menyadarinya, merancang rencana matang, dan mengeksekusinya dengan tenang.",
        "summary": "Pikiranmu bekerja seperti ahli strategi di balik layar. Kamu jarang puas hanya melihat apa yang ada di permukaan; kamu selalu tertarik mencari tahu pola tersembunyi, memprediksi arah ke depan, dan merancang rencana jangka panjang yang rapi. Kamu mandiri, menghargai waktu fokus, dan lebih suka bergerak efisien tanpa terganggu drama atau basa-basi yang nggak perlu.",
        "avatar": "assets/avatars/intj.svg",
        "quick_dossier": {
            "superpower": "Visi Strategis & Pemecah Masalah Sistemik",
            "love_language": "Quality Time Mendalam & Tindakan Nyata",
            "pet_peeve": "Basa-basi kosong, inefisiensi, dan mikromanajemen",
            "emergency_recharge": "Waktu hening total tanpa interaksi untuk riset proyek pribadi"
        },
        "cognitive_roles": {
            "dominant": "Ni (Visi & Pola Masa Depan): Nalurimu tajam menghubungkan titik-titik fakta menjadi gambaran masa depan yang jelas. Kamu sering 'tahu' arah mana yang paling masuk akal sebelum orang lain menyadarinya.",
            "auxiliary": "Te (Logika & Eksekusi Praktis): Kamu nggak cuma bermimpi; kamu mengatur langkah konkret, waktu, dan sumber daya secara terstruktur biar rencanamu benar-benar terwujud di dunia nyata.",
            "tertiary": "Fi (Nilai & Prinsip Personal): Di balik penampilan luarmu yang tenang dan analitis, kamu punya kompas moral pribadi yang sangat dalam dan hanya kamu bagikan ke orang-orang terdekat.",
            "inferior": "Se (Sensorik Seketika): Mengingat kamu sering tenggelam di dunia pikiran, lingkungan yang terlalu bising, ramai, atau penuh kekacauan fisik bisa bikin energimu cepat terkuras habis."
        },
        "relatable_traits": {
            "daily_habits": [
                "Punya rencana cadangan (Plan B, C, sampai Z) bahkan untuk hal-hal sepele seperti rute jalan atau menu makan siang.",
                "Sering dikira judes atau sinis padahal aslinya cuma lagi asyik mikir dan bengong di kepala sendiri.",
                "Paling malas ikut rapat panjang yang intinya sebenarnya bisa diselesaikan lewat chat 2 kalimat.",
                "Kalau nemu topik baru yang bikin penasaran, bisa riset sampai subuh dan baca puluhan artikel dalam semalam."
            ],
            "pet_peeves": [
                "Orang yang mengulang-ulang penjelasan berputar-putar padahal kamu sudah paham dari kalimat pertama.",
                "Aturan kaku yang dipertahankan cuma karena 'dari dulu memang sudah begini' tanpa alasan logis.",
                "Didesak mengambil keputusan besar secara mendadak tanpa diberi waktu menganalisis data."
            ],
            "flow_triggers": [
                "Merancang arsitektur sistem, strategi bisnis, atau alur kerja dari nol sampai berjalan otomatis.",
                "Membaca buku atau membedah studi kasus rumit di pojokan kamar yang sunyi dengan lampu temaram."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Punya visi jangka panjang yang tajam, sangat mandiri dalam berpikir, dan cepat menemukan solusi sistemik saat terjadi inefisiensi yang bikin macet pekerjaan.",
            "blindspots": "Kadang terlalu perfeksionis, kurang sabar saat orang lain butuh waktu adaptasi lebih lama, dan sering lupa bahwa komunikasi yang hangat itu penting dalam kerja tim.",
            "superpower_list": [
                "Kemampuan membaca arah tren dan konsekuensi jangka panjang dengan akurasi tinggi.",
                "Kemandirian berpikir; tidak mudah terbawa opini mayoritas atau tekanan sosial.",
                "Kejelasan berpikir yang runtut dalam menyederhanakan masalah ruwet menjadi langkah terarah."
            ],
            "blindspot_list": [
                "Cenderung mengabaikan sinyal emosional orang lain dan menganggap semua hal harus selesai lewat logika murni.",
                "Standar tinggi yang kadang membuatmu sulit mendelegasikan tugas ke rekan lain.",
                "Mudah lelah secara fisik jika harus terus-menerus merespons stimulus mendadak di lingkungan ramai."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu bekerja berbasis sasaran dan hasil akhir, bukan jam duduk formal. Kamu menyukai kebebasan cara kerja selama target tercapai dengan standar keunggulan tinggi.",
            "ideal_env": "Lingkungan kerja profesional yang menghargai kompetensi, minim politik kantor, dengan target terukur dan ruang hening untuk fokus mendalam.",
            "team_role": "Arsitek strategi dan penjamin arah jangka panjang; orang yang memastikan tim tidak berjalan ke jalan buntu."
        },
        "love_relationships": {
            "love_style": "Kamu tidak suka drama asmara klise atau rayuan gombal. Kamu menunjukkan cinta lewat komitmen setia, kesiapan membantunya mencapai impian hidup, dan percakapan jujur tanpa topeng.",
            "green_flags": "Pasangan yang mandiri secara emosional, punya gairah intelektual, menghargai waktu me-time, dan bisa diajak diskusi kritis tanpa baper.",
            "red_flags": "Orang yang manipulatif, hobi menguji perasaan dengan drama pasif-agresif, atau menuntut kabar setiap sepuluh menit."
        },
        "friendship": {
            "circle_role": "Teman diskusi tepercaya dan pemecah masalah darurat saat sahabat terdekat sedang buntu menghadapi masalah hidup pelik.",
            "circle_style": "Lingkaran pertemananmu sangat kecil (2-4 orang), tapi ikatannya sangat kokoh dan bisa bertahan puluhan tahun tanpa perlu ketemu tiap minggu."
        },
        "interaction_guide": {
            "do": [
                "Langsung ke inti persoalan; sampaikan konteks dan ekspektasimu secara jelas dan to-the-point.",
                "Hargai batasan waktunya dan beri jeda waktu berpikir sebelum menuntut keputusan final.",
                "Dukung argumenmu dengan data atau logika yang masuk akal jika ingin berdiskusi dengannya."
            ],
            "dont": [
                "Jangan basa-basi kepanjangan atau berputar-putar tanpa arah jelas.",
                "Jangan mencoba mengatur rutinitas pribadinya dengan mikromanajemen detail sepele.",
                "Jangan menuntut respon instan saat dia sedang memakai headphones atau tenggelam dalam mode fokus."
            ]
        },
        "stress_dynamics": "Saat burnout parah, kamu bisa tiba-tiba jadi gampang kesal sama detail kecil atau malah overthinking hal-hal sepele. Cara paling pas buat recharge: sediakan waktu sendiri yang tenang, kurangi komitmen sosial sementara, dan tulis unek-unekmu di catatan pribadi.",
        "stress_recharge": {
            "burnout_triggers": [
                "Kelebihan beban sensorik (kebisingan, interupsi terus-menerus, kerumunan padat).",
                "Harus berurusan dengan orang-orang yang tidak kompeten tapi bersuara paling keras.",
                "Rencana matang yang berantakan karena kecerobohan atau keputusan impulsif pihak lain."
            ],
            "stress_signals": [
                "Menjadi sinis, berbicara sarkastik, dan menarik diri total dari semua interaksi.",
                "Tiba-tiba terobsesi pada detail fisik sepele (misal: membersihkan meja berkali-kali secara kompulsif).",
                "Merasa terjebak dan kehilangan keyakinan pada masa depan yang biasanya selalu terlihat jelas."
            ],
            "recharge_remedy": [
                "Isolasi tenang selama minimal setengah hari: matikan notifikasi chat dan jangan bicara dengan siapa pun.",
                "Lepaskan beban kendali: terima bahwa tidak semua hal di luar sana adalah tanggung jawabmu untuk dibereskan.",
                "Lakukan aktivitas fisik ringan terstruktur (jalan santai di alam terbuka atau stretching) untuk menurunkan ketegangan kepala."
            ]
        },
        "color": "#4338CA",
        "temperament": "Analis (Rational / NT)",
        "bg_tint": "#EEF2FF",
        "border_color": "#C7D2FE",
        "work_style": "Kamu bekerja berbasis sasaran dan hasil akhir, bukan jam duduk formal. Kamu menyukai kebebasan cara kerja selama target tercapai dengan standar keunggulan tinggi."
    },
    "INTP": {
        "code": "INTP",
        "archetype": "Sang Pemikir Logis",
        "title": "INTP · Sang Pemikir Logis",
        "tagline": "Menemukan kebenaran di balik teka-teki rumit, membedah ide dari berbagai sudut, dan selalu penasaran sama cara kerja dunia.",
        "summary": "Otakmu ibarat laboratorium ide yang nggak pernah tidur. Kamu suka membedah konsep sampai ke akar-akarnya, mencari celah logika yang sering dilewatkan orang lain, dan merangkai penjelasan yang elegan. Kamu nggak gampang percaya sama aturan kaku sebelum kamu sendiri yang menguji apakah aturan itu masuk akal dan konsisten.",
        "avatar": "assets/avatars/intp.svg",
        "quick_dossier": {
            "superpower": "Analisis Logika Murni & Pemecahan Masalah Abstrak",
            "love_language": "Diskusi Intelektual Lepas & Penerimaan Apa Adanya",
            "pet_peeve": "Argumen emosional tanpa logika, dan dipaksa mematuhi aturan tanpa alasan jelas",
            "emergency_recharge": "Tenggelam dalam rabbit-hole topik acak yang menarik tanpa batas waktu"
        },
        "cognitive_roles": {
            "dominant": "Ti (Akurasi Logika Internal): Standar logikamu sangat tinggi. Kamu otomatis memeriksa apakah setiap argumen dan ide itu konsisten, jujur secara intelektual, dan bebas dari kontradiksi.",
            "auxiliary": "Ne (Eksplorasi Kemungkinan): Pikiranmu senang melompat ke berbagai cabang ide baru, menghubungkan topik yang kelihatannya nggak nyambung, dan menikmati proses eksplorasi 'gimana kalau begini?'.",
            "tertiary": "Si (Rujukan Data & Pengalaman): Kamu mengumpulkan referensi fakta dan pengalaman masa lalu sebagai bahan bakar pembanding saat menganalisis topik baru.",
            "inferior": "Fe (Kepekaan Emosi Sosial): Kamu kadang merasa canggung atau serba salah saat harus membaca kode sosial yang berbelit-belit atau menghadapi luapan emosi orang lain yang nggak logis."
        },
        "relatable_traits": {
            "daily_habits": [
                "Punya 50+ tab browser terbuka sekaligus dan kamu merasa semuanya penting buat dibaca nanti.",
                "Sering mulai kalimat dengan 'Sebenarnya tergantung konteksnya sih...' karena selalu melihat banyak sisi.",
                "Tiba-tiba begadang sampai jam 3 pagi cuma gara-gara penasaran cara kerja reaktor nuklir atau asal-usul bahasa.",
                "Bisa lupa makan atau lupa waktu kalau lagi asyik ngoding, nulis teori, atau utak-atik proyek eksperimental."
            ],
            "pet_peeves": [
                "Orang yang ngotot pada pendapat yang jelas-jelas keliru secara fakta dan logika cuma karena gengsi.",
                "Birokrasi berbelit-belit yang membuang waktu dan tidak memberi nilai tambah apa pun.",
                "Dihakimi 'pemalas' cuma karena proses kerjamu lebih banyak berpikir konseptual daripada gerak fisik."
            ],
            "flow_triggers": [
                "Menemukan pola elegan yang memecahkan teka-teki logika yang bikin orang lain pusing berhari-hari.",
                "Mengembangkan teori atau model baru sambil mendengarkan musik lo-fi tanpa ada yang menginterupsi."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Kemampuan luar biasa memecahkan masalah rumit, objektif tanpa bias emosional, dan sangat terbuka terhadap sudut pandang alternatif yang segar.",
            "blindspots": "Kerap terjebak dalam siklus overthinking (analysis paralysis) sampai menunda eksekusi nyata, dan malas mengurusi urusan administrasi rutin yang membosankan.",
            "superpower_list": [
                "Ketajaman mendeteksi lubang logika dan inkonsistensi yang luput dari pandangan orang lain.",
                "Kemampuan berpikir orisinal tanpa terikat konvensi atau dogma lama.",
                "Objektivitas tinggi; mampu memisahkan opini dari ego pribadi."
            ],
            "blindspot_list": [
                "Kecenderungan menunda eksekusi akhir karena merasa model idenya masih bisa disempurnakan lagi.",
                "Kurang peka terhadap nuansa emosional lawan bicara sehingga terkadang terkesan terlalu blak-blakan.",
                "Cepat kehilangan minat begitu prinsip dasar masalah sudah terpecahkan, enggan menyelesaikan urusan finishing."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu bekerja paling produktif saat diberi otonomi penuh untuk bereksperimen. Kamu benci mikromanajemen dan aturan absensi kaku; kamu mengukur kerja dari kualitas ide dan solusinya.",
            "ideal_env": "Lingkungan riset, teknologi, sains, atau strategi yang mengutamakan meritokrasi intelektual dan kebebasan bereksplorasi.",
            "team_role": "Troubleshooter konseptual; orang yang dipanggil saat ada masalah teknis pelik yang belum pernah ada solusinya."
        },
        "love_relationships": {
            "love_style": "Kamu tidak romantis secara teatrikal, tapi sangat setia dan suportif. Kamu menunjukkan kasih sayang dengan berbagi pemikiran terdalam, mendengarkan argumennya, dan memecahkan masalahnya secara praktis.",
            "green_flags": "Seseorang yang menghargai keunikan cara berpikirmu, tidak memaksamu berubah jadi ekstrovert gaul, dan bisa diajak diskusi ngalor-ngidul dengan santai.",
            "red_flags": "Orang yang suka playing victim, menuntut validasi emosi tanpa logika, atau menuduhmu tidak peduli hanya karena kamu tidak puitis."
        },
        "friendship": {
            "circle_role": "Ensiklopedia berjalan dan teman ngobrol seru saat membahas topik-topik unik yang jarang diobrolkan di tongkrongan umum.",
            "circle_style": "Lebih suka nongkrong santai berdua atau bertiga di kedai kopi sepi daripada pesta ramai yang mengharuskan basa-basi."
        },
        "interaction_guide": {
            "do": [
                "Ajak diskusi dengan logika yang runtut dan terbuka terhadap argumen tandingan.",
                "Beri dia waktu untuk menyendiri dan mencerna ide sebelum menuntut respon instan.",
                "Hargai rasa ingin tahunya walau topik yang dibahas terdengar nyeleneh atau tidak biasa."
            ],
            "dont": [
                "Jangan gunakan argumen otoritas ('pokoknya ikut aturan!') tanpa alasan yang masuk akal.",
                "Jangan paksa dia berbicara banyak di forum sosial yang canggung baginya.",
                "Jangan menganggap keheningannya sebagai tanda marah; dia kemungkinan besar cuma lagi melamun."
            ]
        },
        "stress_dynamics": "Kalau lagi stres berat, kamu bisa merasa terasing, frustrasi karena merasa orang lain nggak paham, atau tiba-tiba sensitif soal penerimaan sosial. Cara recharge: cari topik baru yang bikin kamu penasaran tanpa ada tenggat waktu yang menekan.",
        "stress_recharge": {
            "burnout_triggers": [
                "Tuntutan administratif monoton yang tidak memberi ruang berpikir kreatif.",
                "Konflik interpersonal bernuansa emosional tinggi yang menolak diselesaikan lewat logika.",
                "Kelelahan sosial karena terlalu lama dipaksa beramah-tamah di lingkungan yang tidak akrab."
            ],
            "stress_signals": [
                "Tiba-tiba meledak emosional atau merasa sangat cemas terhadap apa yang dipikirkan orang lain tentang dirinya.",
                "Menjadi sangat ragu-ragu bahkan untuk keputusan paling sederhana sekalipun.",
                "Menarik diri ke dalam kamar dan mengabaikan semua pesan masuk selama berhari-hari."
            ],
            "recharge_remedy": [
                "Bebaskan diri dari semua tenggat waktu selama satu hari penuh dan tidur cukup.",
                "Tekuni proyek kreatif santai tanpa target hasil (gaming strategi, utak-atik coding, atau membaca komik/buku fiksi).",
                "Curhat singkat ke satu orang yang paling kamu percaya dan dijamin tidak akan menghakimimu."
            ]
        },
        "color": "#4F46E5",
        "temperament": "Analis (Rational / NT)",
        "bg_tint": "#EEF2FF",
        "border_color": "#C7D2FE",
        "work_style": "Kamu bekerja paling produktif saat diberi otonomi penuh untuk bereksperimen. Kamu benci mikromanajemen dan aturan absensi kaku; kamu mengukur kerja dari kualitas ide dan solusinya."
    },
    "ENTJ": {
        "code": "ENTJ",
        "archetype": "Sang Komandan Visioner",
        "title": "ENTJ · Sang Komandan Visioner",
        "tagline": "Mengubah ide ambisius jadi kenyataan nyata lewat ketegasan, strategi terarah, dan kepemimpinan yang berani ambil risiko.",
        "summary": "Kamu punya energi alami untuk memimpin dan menyelesaikan sesuatu. Saat melihat kekacauan atau inefisiensi, nalurimu langsung terpicu untuk merapikannya dan mengarahkan tim menuju target yang jelas. Kamu lugas, menghargai waktu, percaya diri mengambil keputusan sulit, dan selalu terdorong untuk mencapai hasil terbaik.",
        "avatar": "assets/avatars/entj.svg",
        "quick_dossier": {
            "superpower": "Kepemimpinan Eksekusi & Pengambilan Keputusan Cepat",
            "love_language": "Dukungan Ambisi Bersama & Loyalitas Tanpa Syarat",
            "pet_peeve": "Kemalasan, alasan tanpa solusi, dan ketidakefisienan yang dibiarkan",
            "emergency_recharge": "Olahraga intensitas tinggi, jeda dari koordinasi orang lain, dan menyusun roadmap baru"
        },
        "cognitive_roles": {
            "dominant": "Te (Efisiensi & Kepemimpinan Nyata): Naluri utamamu adalah menertibkan situasi, membagi tugas secara adil, dan memastikan semua orang bergerak menuju target yang jelas dan terukur.",
            "auxiliary": "Ni (Arah Visi Strategis): Kamu selalu punya pandangan beberapa langkah ke depan. Intuisi strategismu memandu ke mana organisasi atau proyek harus diarahkan agar relevan dalam jangka panjang.",
            "tertiary": "Se (Ketangkasan Aksi Nyata): Kamu responsif membaca peluang di lapangan dan berani mengambil langkah taktis saat momentumnya tepat tanpa ragu-ragu.",
            "inferior": "Fi (Ruang Hati & Refleksi Batin): Karena terbiasa fokus pada hasil, kamu rentan menekan rasa lelah batin sendiri atau mengabaikan kebutuhan emosional sampai tubuhmu protes."
        },
        "relatable_traits": {
            "daily_habits": [
                "Paling tidak tahan melihat orang rapat berlama-lama tanpa ada action items dan penanggung jawab yang jelas.",
                "Secara otomatis mengambil kendali saat kelompok atau tim kehilangan arah dan saling lempar tanggung jawab.",
                "Jadwal harian tertata rapi di kalender dan kamu merasa sangat puas saat semua target hari itu tercoret tuntas.",
                "Suka menantang diri sendiri dengan target yang menurut orang lain terlalu ambisius."
            ],
            "pet_peeves": [
                "Orang yang banyak mengeluh tapi tidak mau mencoba solusi yang sudah ditawarkan.",
                "Ketidaksiapan rekan kerja saat menghadiri presentasi atau rapat penting.",
                "Drama emosional di lingkungan profesional yang mengaburkan fokus pada tujuan bersama."
            ],
            "flow_triggers": [
                "Memimpin peluncuran proyek besar dengan tim yang solid dan melihat hasil angka tercapai melampaui target.",
                "Menyusun strategi kompetitif dan mengeksekusinya dengan presisi tinggi."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Ketegasan mengambil keputusan di masa krisis, kemampuan komunikasi yang meyakinkan, dan daya dorong tinggi untuk menyelesaikan proyek ambisius tepat waktu.",
            "blindspots": "Terkadang terkesan terlalu dominan atau kurang sabar menghadapi rekan kerja yang butuh ritme lebih perlahan, serta jarang memberi jeda istirahat untuk diri sendiri.",
            "superpower_list": [
                "Daya eksekusi tinggi; mampu mengubah konsep abstrak menjadi roadmap terukur.",
                "Ketegasan dalam mengambil keputusan berat tanpa ragu-ragu di bawah tekanan.",
                "Karisma kepemimpinan yang menginspirasi orang lain untuk melampaui batas kemampuan mereka."
            ],
            "blindspot_list": [
                "Kecenderungan menabrak pertimbangan emosional demi mencapai efisiensi target.",
                "Bisa bersikap intimidatif tanpa sadar saat rekan kerja tidak secepat ritmenya.",
                "Sulit mengakui rasa rapuh atau kelelahan batin kepada orang lain."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu adalah pekerja keras berorientasi target tinggi. Kamu menetapkan standar keunggulan bagi dirimu sendiri dan berharap rekan tim menunjukkan dedikasi yang setara.",
            "ideal_env": "Posisi manajerial, kewirausahaan, konsultasi strategi, atau industri berdaya saing tinggi yang memberi ruang untuk memimpin perubahan.",
            "team_role": "Kapten penggerak; orang yang menetapkan target, memangkas hambatan, dan menuntut akuntabilitas hasil."
        },
        "love_relationships": {
            "love_style": "Kamu mencari pasangan setara (power couple). Kamu menunjukkan cinta lewat komitmen yang kokoh, mendorong pasangan berkembang, dan melindungi masa depan bersama secara materi dan emosional.",
            "green_flags": "Pasangan yang percaya diri, punya tujuan hidup jelas, berani memberikan masukan jujur, dan tidak mudah terintimidasi oleh ketegasanmu.",
            "red_flags": "Orang yang pasif-agresif, tidak punya inisiatif, atau sering memainkan drama emosional untuk mencari perhatian."
        },
        "friendship": {
            "circle_role": "Penyemangat utama dan penasihat karier yang selalu siap memberi dorongan nyata saat teman sedang meragukan potensinya.",
            "circle_style": "Menghargai pertemanan yang saling membangun; kamu bangga melihat kawan-kawanmu sukses dan selalu siap membuka jaringan koneksi bagi mereka."
        },
        "interaction_guide": {
            "do": [
                "Datang dengan persiapan matang, sampaikan kesimpulan di awal sebelum menjabarkan detail pendukung.",
                "Bicaralah secara jujur, lugas, dan percaya diri; dia sangat menghargai keberanian berbicara terbuka.",
                "Tepati janji dan komitmen waktu tanpa mencari-cari alasan."
            ],
            "dont": [
                "Jangan bertele-tele atau menutup-nutupi kesalahan; akui secara profesional dan tawarkan rencana perbaikan.",
                "Jangan bersikap pasif dan menunggu disuapi instruksi terus-menerus.",
                "Jangan menyerang karakternya di depan forum; sampaikan kritik objektif secara privat."
            ]
        },
        "stress_dynamics": "Saat kelelahan mental memuncak, kamu bisa jadi sangat mengontrol hal-hal kecil atau merasa kehilangan arah makna. Cara recharge: delegasikan tugas, luangkan waktu buat olahraga fisik intensif, dan istirahat dari urusan koordinasi kerjaan.",
        "stress_recharge": {
            "burnout_triggers": [
                "Kehilangan kendali atas arah proyek karena campur tangan otoritas yang tidak kompeten.",
                "Terjebak dalam rutinitas tanpa progres nyata atau menghadapi kemandekan kerja tim.",
                "Kelelahan fisik akumulatif yang diabaikan terlalu lama demi mengejar tenggat waktu."
            ],
            "stress_signals": [
                "Tiba-tiba menjadi sangat reaktif, mudah marah pada kesalahan sepele, atau merasa dikhianati.",
                "Merasa hampa dan mempertanyakan apakah semua pencapaian yang diperjuangkan selama ini ada artinya.",
                "Memaksakan diri bekerja lebih keras lagi walau tubuh sudah memberikan sinyal drop."
            ],
            "recharge_remedy": [
                "Hentikan kontak kerja selama akhir pekan: serahkan mandat operasional kepada orang tepercaya.",
                "Lakukan aktivitas fisik yang memicu keringat dan adrenalin (fitnes, lari, atau olahraga kompetitif).",
                "Buka ruang hati untuk mengobrol santai tanpa membahas prestasi dengan orang terkasih."
            ]
        },
        "color": "#3730A3",
        "temperament": "Analis (Rational / NT)",
        "bg_tint": "#EEF2FF",
        "border_color": "#C7D2FE",
        "work_style": "Kamu adalah pekerja keras berorientasi target tinggi. Kamu menetapkan standar keunggulan bagi dirimu sendiri dan berharap rekan tim menunjukkan dedikasi yang setara."
    },
    "ENTP": {
        "code": "ENTP",
        "archetype": "Sang Pendebat Inovatif",
        "title": "ENTP · Sang Pendebat Inovatif",
        "tagline": "Menantang ide-ide lama dengan humor cerdas, melihat peluang di mana-mana, dan selalu punya cara tak terduga buat mecahin masalah.",
        "summary": "Bagi kamu, hidup terlalu seru buat diisi dengan hal-hal yang monoton. Kamu suka menguji asumsi orang lain lewat diskusi cerdas, menghubungkan ide-ide acak jadi terobosan baru, dan paling bersemangat saat memulai proyek yang menantang kreativitas. Kamu lincah, berani mencoba cara baru, dan nggak takut beda dari arus utama.",
        "avatar": "assets/avatars/entp.svg",
        "quick_dossier": {
            "superpower": "Inovasi Spontan, Fleksibilitas Ide & Retorika Cerdas",
            "love_language": "Bercanda Cerdas, Petualangan Spontan & Eksplorasi Bersama",
            "pet_peeve": "Kemonotonan, dogma kaku, dan orang yang mudah tersinggung saat diajak berdiskusi",
            "emergency_recharge": "Ngobrol santai tanpa batas topik dengan orang cerdas atau mencoba eksperimen baru"
        },
        "cognitive_roles": {
            "dominant": "Ne (Eksplorasi Peluang Baru): Matamu selalu melihat kemungkinan segar di setiap situasi. Kamu suka membongkar kebiasaan lama dan menciptakan alternatif yang lebih menarik.",
            "auxiliary": "Ti (Uji Logika Kritis): Setiap ide liar yang muncul langsung disaring oleh naluri analisismu untuk memastikan bahwa konsep tersebut punya dasar logika yang kokoh.",
            "tertiary": "Fe (Koneksi & Diplomasi Santai): Kamu punya karisma humoris dan luwes membaca audiens, membuat diskusi yang rumit jadi terasa seru dan hidup.",
            "inferior": "Si (Kepatuhan Rutinitas): Tugas-tugas administratif yang berulang, membosankan, dan minim ruang kreasi adalah hal yang paling cepat bikin energimu drop."
        },
        "relatable_traits": {
            "daily_habits": [
                "Sering memainkan peran devil's advocate (mengambil posisi lawan) dalam diskusi cuma buat menguji seberapa kuat argumen orang lain.",
                "Punya 10 ide bisnis atau proyek baru setiap minggu, tapi tantangan terbesarnya adalah menyelesaikan proyek yang pertama sampai tuntas.",
                "Bisa membaca situasi ruangan dengan cepat dan mencairkan suasana tegang lewat lelucon spontan yang tepat sasaran.",
                "Paling malas merapikan barang atau mengurus berkas formulir kertas yang terasa tidak ada nilainya."
            ],
            "pet_peeves": [
                "Orang yang menganggap perbedaan pendapat intelektual sebagai serangan pribadi.",
                "Lingkungan yang melarang pertanyaan kritis dan mengharuskan kepatuhan buta pada tradisi.",
                "Tenggat waktu kaku untuk pekerjaan kreatif yang sebenarnya butuh ruang eksplorasi."
            ],
            "flow_triggers": [
                "Sesi brainstorming tanpa batas di mana ide-ide liar saling bertabrakan dan melahirkan solusi orisinal.",
                "Menemukan celah cerdas (hack) yang membuat proses sulit menjadi jauh lebih cepat dan menyenangkan."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Kecerdasan adaptasi yang tinggi, lihai memecahkan kebuntuan ide, dan kemampuan retorika persuasif yang sanggup membuka wawasan baru bagi orang lain.",
            "blindspots": "Cepat bosan saat proyek sudah masuk ke tahap pemeliharaan rutin, dan kadang terlalu asyik mendebat hal-hal kecil sampai orang lain merasa tersudut.",
            "superpower_list": [
                "Kreativitas tak terbatas dalam menghubungkan domain ilmu yang berbeda menjadi solusi inovatif.",
                "Kemampuan beradaptasi dengan sangat cepat terhadap perubahan situasi mendadak.",
                "Karisma komunikasi yang hidup, humoris, dan tidak mudah panik menghadapi ketidakpastian."
            ],
            "blindspot_list": [
                "Kurang disiplin dalam menuntaskan detail administratif dan tindak lanjut jangka panjang.",
                "Terkadang terlihat tidak konsisten karena pandangannya terus berevolusi seiring masuknya data baru.",
                "Bisa membuat orang yang sensitif merasa kewalahan karena gaya debatnya yang terus menekan."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu adalah inovator fase awal (initiator). Kamu bersemangat saat memecahkan kebuntuan dan merancang konsep, namun lebih efektif jika berpartner dengan tipe eksekutor detail.",
            "ideal_env": "Start-up, inkubator bisnis, periklanan, hukum, riset produk, atau media yang dinamis dan mendorong pertukaran ide bebas.",
            "team_role": "Katalisator perubahan dan pembangkit ide; orang yang mencegah tim mandek dalam cara-cara usang."
        },
        "love_relationships": {
            "love_style": "Hubungan bagimu harus seru, dinamis, dan tidak monoton. Kamu menunjukkan cinta lewat obrolan mendalam, mengajak pasangan mencoba pengalaman baru, dan mendukung mimpinya secara antusias.",
            "green_flags": "Seseorang yang percaya diri, punya selera humor cerdas, tidak gampang baper saat diajak adu argumen santai, dan punya dunianya sendiri.",
            "red_flags": "Pasangan yang posesif, menuntut kepatuhan aturan kaku, atau merasa terancam saat kamu bergaul dengan banyak orang."
        },
        "friendship": {
            "circle_role": "Penyemarak tongkrongan yang selalu punya topik seru, ide jalan-jalan dadakan, dan pandangan segar tentang isu terkini.",
            "circle_style": "Punya kenalan di mana-mana dari berbagai kalangan, namun hanya berbagi isi hati terdalam dengan sedikit sahabat yang benar-benar memahaminya."
        },
        "interaction_guide": {
            "do": [
                "Tantang ide-idenya dengan argumen cerdas; dia sangat menikmati lawan bicara yang kritis.",
                "Beri dia ruang berimprovisasi tanpa membatasi cara kerjanya dengan aturan kaku.",
                "Tanggapilah leluconnya dan jangan buru-buru tersinggung saat dia mengeksplorasi sudut pandang kontroversial."
            ],
            "dont": [
                "Jangan memaksanya mengerjakan detail administratif yang monoton tanpa henti.",
                "Jangan menganggap perdebatan intelektualnya sebagai permusuhan pribadi.",
                "Jangan menuntut rencana hidup yang kaku dan tidak bisa diubah."
            ]
        },
        "stress_dynamics": "Saat terkungkung oleh aturan birokrasi yang kaku, kamu bisa jadi sinis dan kehilangan motivasi. Cara recharge: ngobrol santai tanpa agenda sama teman yang sefrekuensi, atau coba hobi baru yang menantang rasa ingin tahumu.",
        "stress_recharge": {
            "burnout_triggers": [
                "Terjebak dalam rutinitas birokrasi yang mematikan inisiatif dan kreativitas.",
                "Diperlakukan dengan mikromanajemen detail oleh atasan yang kaku.",
                "Kelelahan fisik akibat terlalu banyak memulai proyek sekaligus tanpa waktu jeda."
            ],
            "stress_signals": [
                "Kehilangan semangat ceria, menjadi cemas pada detail kesehatan atau kesalahan sepele di masa lalu.",
                "Menjadi sinis, apatis, dan menolak berdiskusi dengan siapa pun.",
                "Merasa kehilangan identitas diri sebagai sosok yang biasanya penuh ide dan optimis."
            ],
            "recharge_remedy": [
                "Tinggalkan sejenak rutinitas: jalan-jalan ke tempat baru tanpa rencana terikat.",
                "Kurangi komitmen aktif: pilih 1 proyek paling menyenangkan dan tuntaskan satu tahap saja.",
                "Ngobrol santai dan tertawa lepas bareng sahabat terdekat tanpa membicarakan urusan beban kerja."
            ]
        },
        "color": "#6366F1",
        "temperament": "Analis (Rational / NT)",
        "bg_tint": "#EEF2FF",
        "border_color": "#C7D2FE",
        "work_style": "Kamu adalah inovator fase awal (initiator). Kamu bersemangat saat memecahkan kebuntuan dan merancang konsep, namun lebih efektif jika berpartner dengan tipe eksekutor detail."
    },
    "INFJ": {
        "code": "INFJ",
        "archetype": "Sang Advokat Bijak",
        "title": "INFJ · Sang Advokat Bijak",
        "tagline": "Memahami kedalaman batin manusia, memegang teguh nilai idealis, dan membimbing orang lain dengan empati yang tenang.",
        "summary": "Kamu punya radar intuisi yang sangat peka terhadap perasaan dan motivasi orang lain. Di balik sifatmu yang tenang dan pendiam, ada idealisme kuat tentang dunia yang lebih baik dan kepedulian tulus pada pertumbuhan manusia di sekitarmu. Kamu reflektif, menyukai makna mendalam, dan setia pada prinsip moral pribadimu.",
        "avatar": "assets/avatars/infj.svg",
        "quick_dossier": {
            "superpower": "Intuisi Empati Mendalam & Visi Kemanusiaan",
            "love_language": "Koneksi Jiwa / Deep Talk & Kehadiran Tulus",
            "pet_peeve": "Kepalsuan, ketidakadilan sosial, dan basa-basi dangkal",
            "emergency_recharge": "Waktu hening total di alam atau ruang privat untuk memulihkan energi batin"
        },
        "cognitive_roles": {
            "dominant": "Ni (Visi & Pola Masa Depan): Matamu selalu menangkap makna tersirat dan pola jangka panjang dalam dinamika hubungan manusia.",
            "auxiliary": "Fe (Keharmonisan & Empati Sosial): Nalurimu secara alami menyelaraskan suasana, meredakan ketegangan, dan memastikan kebutuhan emosional orang lain terpenuhi.",
            "tertiary": "Ti (Penalaran Kritis Pribadi): Kamu punya kerangka berpikir logis yang rapi untuk menyaring dan memvalidasi apakah intuisimu masuk akal sebelum bertindak.",
            "inferior": "Se (Sensorik Seketika): Suasana fisik yang bising, terlalu banyak tuntutan visual, atau aktivitas mendadak tanpa persiapan bisa bikin energimu terkuras cepat."
        },
        "relatable_traits": {
            "daily_habits": [
                "Sering jadi tempat curhat andalan karena orang lain merasa sangat didengarkan dan tidak pernah dihakimi.",
                "Punya kemampuan 'membaca' suasana hati orang lain dalam hitungan detik bahkan sebelum orang itu bicara sepatah kata pun.",
                "Bisa sangat ramah dan hangat saat berinteraksi, lalu langsung 'menghilang' masuk mode bertapa selama beberapa hari buat ngecas energi.",
                "Overthinking sebelum tidur soal apakah perkataanmu tadi siang sempat menyakiti hati teman secara tidak sengaja."
            ],
            "pet_peeves": [
                "Orang yang berpura-pura baik di depan tapi suka menusuk dari belakang atau menyebarkan gosip jahat.",
                "Didesak terus-menerus untuk segera bersosialisasi padahal baterai jiwamu sedang benar-benar kosong.",
                "Ketidakadilan atau perlakuan semena-mena terhadap orang yang lemah atau tidak berdaya."
            ],
            "flow_triggers": [
                "Deep talk berdua hingga larut malam membahas makna hidup, mimpi masa depan, dan luka batin yang sedang disembuhkan.",
                "Menulis refleksi pribadi atau menuangkan ide kreatif yang membawa dampak positif nyata bagi orang lain."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Integritas moral yang tinggi, empati mendalam yang menyembuhkan, dan kemampuan luar biasa menginspirasi orang lain untuk menjadi versi terbaik dirinya.",
            "blindspots": "Cenderung memendam perasaan sendiri demi menjaga keharmonisan, rentan mengalami 'INFJ Door Slam' (memutus kontak total tiba-tiba) saat batas sabarnya habis.",
            "superpower_list": [
                "Kemampuan membaca motivasi terselubung dan dinamika emosional orang lain dengan sangat akurat.",
                "Komitmen teguh pada nilai-nilai kemanusiaan dan kebaikan jangka panjang.",
                "Daya diplomasi yang halus dan menenangkan saat meredakan perselisihan sengit."
            ],
            "blindspot_list": [
                "Kecenderungan memikul beban emosional orang lain sampai mengabaikan kesehatan fisik dan mental sendiri.",
                "Perfeksionisme idealis yang membuatmu merasa hasil kerjamu tidak pernah cukup sempurna.",
                "Sulit membuka ruang kerapuhan diri sendiri kepada orang lain karena terbiasa menjadi penopang."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu bekerja dengan hati dan tujuan bermakna (purpose-driven). Kamu sulit termotivasi oleh uang semata jika pekerjaan itu bertentangan dengan kompas moralmu.",
            "ideal_env": "Konseling, psikologi, penulisan, pendidikan, non-profit, atau desain yang memiliki misi sosial jelas dan atmosfer yang saling mendukung.",
            "team_role": "Penjaga nurani dan pemersatu tim; orang yang memastikan tujuan proyek tetap berpihak pada kesejahteraan manusia."
        },
        "love_relationships": {
            "love_style": "Cinta bagimu adalah koneksi batin yang suci dan mendalam. Kamu setia, penuh perhatian pada detail kecil pasangan, dan selalu berusaha memahami jiwanya secara utuh.",
            "green_flags": "Pasangan yang tulus, jujur apa adanya, menghargai waktu me-time, dan mau diajak bertumbuh bersama secara spiritual dan emosional.",
            "red_flags": "Orang yang manipulatif emosional, suka meremehkan perasaanmu, atau berorientasi pada pencitraan status sosial belaka."
        },
        "friendship": {
            "circle_role": "Sahabat setia seumur hidup dan tempat pulang yang aman saat teman terdekat butuh tempat berkeluh kesah tanpa dihakimi.",
            "circle_style": "Sangat selektif memilih teman akrab. Kamu lebih memilih punya 1-2 sahabat karib sejati daripada punya puluhan teman basa-basi."
        },
        "interaction_guide": {
            "do": [
                "Bicaralah dengan ketulusan dan keterbukaan emosional; dia sangat menghargai kejujuran batin.",
                "Beri dia ruang dan waktu saat dia butuh menyendiri untuk mengisi ulang baterai jiwanya.",
                "Apresiasi usaha dan kepedulian halusnya yang sering kali luput dari perhatian orang lain."
            ],
            "dont": [
                "Jangan memanfaatkan kebaikannya atau terus menuntut perhatiannya tanpa timbal balik.",
                "Jangan memaksanya membuka rahasia pribadinya sebelum dia merasa benar-benar aman.",
                "Jangan meremehkan intuisinya dengan alasan 'tidak ada bukti angka di atas kertas'."
            ]
        },
        "stress_dynamics": "Saat kelelahan mental, kamu bisa merasa terasing dan kewalahan oleh emosi sekitar. Cara recharge: cari ketenangan di alam terbuka, buat batasan tegas dari masalah orang lain, dan lakukan meditasi atau journaling.",
        "stress_recharge": {
            "burnout_triggers": [
                "Menjadi 'tempat sampah emosi' orang lain terlalu lama tanpa punya kesempatan untuk memulihkan diri.",
                "Lingkungan yang sarat konflik, kebencian, atau manipulasi yang mengikis rasa percaya.",
                "Tuntutan fisik dan sensorik yang berlebihan tanpa jeda waktu hening."
            ],
            "stress_signals": [
                "Menarik diri secara ekstrem dan berhenti merespons chat dari siapa pun ('door slam' mode).",
                "Tiba-tiba menjadi impulsif dalam urusan fisik (makan berlebihan atau belanja barang yang tidak perlu).",
                "Merasa kehilangan arah hidup dan merasa semua usahanya menolong orang lain sia-sia."
            ],
            "recharge_remedy": [
                "Tutup pintu kamar, pasang earphone kedap suara, dan nikmati hening total selama beberapa jam.",
                "Tuliskan semua emosi yang bukan milikmu di atas kertas lalu bakar atau buang sebagai simbol pelepasan.",
                "Berjalan santai di taman atau tempat hijau tanpa memegang ponsel."
            ]
        },
        "color": "#059669",
        "temperament": "Diplomat (Idealist / NF)",
        "bg_tint": "#ECFDF5",
        "border_color": "#A7F3D0",
        "work_style": "Kamu bekerja dengan hati dan tujuan bermakna (purpose-driven). Kamu sulit termotivasi oleh uang semata jika pekerjaan itu bertentangan dengan kompas moralmu."
    },
    "INFP": {
        "code": "INFP",
        "archetype": "Sang Mediator Puitis",
        "title": "INFP · Sang Mediator Puitis",
        "tagline": "Menjaga kejujuran rasa di dunia yang serba riuh, melihat keindahan tersembunyi, dan setia pada suara hati terdalam.",
        "summary": "Kamu adalah jiwa perasa yang peka dan penuh imajinasi. Kamu punya kompas nilai pribadi yang sangat kuat; kamu tidak bisa berpura-pura menjadi orang lain hanya demi diterima lingkungan. Kamu menghargai keaslian (autentisitas), punya dunia batin yang kaya dan indah, serta selalu berempati pada mereka yang terpinggirkan.",
        "avatar": "assets/avatars/infp.svg",
        "quick_dossier": {
            "superpower": "Autentisitas Sejati, Empati Hangat & Kreativitas Jiwa",
            "love_language": "Pengertian Batin, Waktu Berdua yang Manis & Dukungan Impian",
            "pet_peeve": "Ketidakjujuran, penghakiman sepihak, dan aturan kaku yang membunuh empati",
            "emergency_recharge": "Mendengarkan playlist musik favorit, menulis puisi/jurnal, atau menyendiri di sudut kamar"
        },
        "cognitive_roles": {
            "dominant": "Fi (Keaslian Nilai Batin): Panduan hidupmu adalah suara hati nurani. Kamu memeriksa apakah setiap tindakanmu jujur, autentik, dan selaras dengan prinsip moral pribadimu.",
            "auxiliary": "Ne (Eksplorasi Makna & Simbol): Imajinasi kreatifmu senang mengembara, menemukan metafora indah dalam kejadian sehari-hari, dan melihat potensi kebaikan dalam diri orang lain.",
            "tertiary": "Si (Kenangan & Kehangatan Masa Lalu): Kamu menyimpan memori emosional dengan sangat detail; lagu, aroma, atau foto lama bisa membangkitkan nostalgia yang begitu hidup.",
            "inferior": "Te (Ketegasan Struktur & Eksekusi Objektif): Menghadapi deadline kaku, kritik tajam di depan umum, atau konflik logika dingin adalah hal yang paling cepat bikin energimu drop."
        },
        "relatable_traits": {
            "daily_habits": [
                "Punya dunia imajinasi di kepala yang sering kali jauh lebih seru daripada kenyataan sehari-hari.",
                "Bisa membaca satu buku, mendengarkan satu lagu berulang-ulang, atau menatap langit jendela selama berjam-jam tanpa bosan.",
                "Sering merasa berbeda dari orang kebanyakan dan butuh waktu lama untuk menemukan orang yang benar-benar 'nyambung'.",
                "Paling tidak tegaan melihat orang atau hewan yang kesusahan, otomatis ingin membantu walau sedang repot sendiri."
            ],
            "pet_peeves": [
                "Orang yang menyuruhmu 'jangan baperan' saat kamu sedang merasakan sesuatu dengan sungguh-sungguh.",
                "Lingkungan yang munafik, penuh pencitraan palsu, dan mengorbankan empati demi kepentingan praktis.",
                "Kritik yang disampaikan secara kasar dan mempermalukan harga dirimu di hadapan orang lain."
            ],
            "flow_triggers": [
                "Menulis jurnal, menggambar, mendesain, atau mengekspresikan emosi lewat karya seni tanpa ada yang menilai.",
                "Mengobrol santai dari hati ke hati tentang mimpi, ketakutan, dan cinta sejati di bawah rintik hujan."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Kejujuran batin yang langka, kreativitas ekspresif yang menyentuh jiwa, dan kesetiaan mendalam kepada orang-orang yang kamu cintai.",
            "blindspots": "Rentan tenggelam dalam kesedihan (melankolis), sering menunda urusan praktis karena menunggu mood yang pas, dan terlalu memasukkan kritik ke dalam hati.",
            "superpower_list": [
                "Kemampuan berempati tanpa syarat dan membuat orang lain merasa diterima seutuhnya apa adanya.",
                "Orisinalitas ide dan kepekaan estetika seni yang bernyawa.",
                "Kesetiaan tanpa kompromi pada kebenaran nurani walau harus berdiri sendirian."
            ],
            "blindspot_list": [
                "Kecenderungan menarik diri ke dunia khayalan saat realita hidup terasa terlalu keras atau mengecewakan.",
                "Kesulitan mengambil keputusan praktis yang membutuhkan ketegasan dingin tanpa melibatkan perasaan.",
                "Menunda-nunda pekerjaan penting karena merasa energinya belum 'klik' dengan tugas tersebut."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu bekerja dengan inspirasi dan keterlibatan emosional. Saat kamu percaya pada misi pekerjaanmu, dedikasi dan kreativitasmu bisa mengalir tanpa batas.",
            "ideal_env": "Seni, sastra, psikologi, desain grafis, aktivisme kemanusiaan, atau kerja remote mandiri yang fleksibel dan bebas dari politik kantor.",
            "team_role": "Penyelaras nurani dan pemberi sentuhan humanis; orang yang mengingatkan tim bahwa di balik angka ada manusia nyata."
        },
        "love_relationships": {
            "love_style": "Kamu mencari cinta sejati yang puitis dan bermakna. Kamu setia, mencintai dengan segenap jiwa, dan selalu melihat sisi terbaik pasangan bahkan saat dia sedang merasa rendah diri.",
            "green_flags": "Seseorang yang lembut, sabar memahami naik-turunnya perasaanmu, menghargai kreativitasmu, dan tidak pernah memaksamu menjadi orang lain.",
            "red_flags": "Pasangan yang sinis, suka meremehkan impianmu, manipulatif, atau menuntutmu selalu bersikap logis dan menekan emosi."
        },
        "friendship": {
            "circle_role": "Pendengar yang penuh kasih dan sahabat yang selalu siap merangkulmu saat seluruh dunia seakan memusuhimu.",
            "circle_style": "Lingkaran pertemanan sangat intim; kamu menjaga pertemanan dengan ketulusan dan paling menghargai teman yang bisa diajak berbicara jujur tanpa kepalsuan."
        },
        "interaction_guide": {
            "do": [
                "Sampaikan masukan dengan nada hangat dan fokus pada perbaikan proses, bukan menyerang identitas pribadinya.",
                "Hargai keunikannya dan jangan pernah membanding-bandingkannya dengan orang lain.",
                "Beri dia waktu untuk menyesuaikan mood saat mengajaknya mengerjakan tugas baru."
            ],
            "dont": [
                "Jangan pernah meremehkan prinsip moral yang dia pegang teguh.",
                "Jangan menyuruhnya bersikap realistis dengan nada merendahkan impiannya.",
                "Jangan memaksa dia berbicara saat dia sedang butuh waktu mencerna perasaannya sendiri."
            ]
        },
        "stress_dynamics": "Saat kewalahan emosi, kamu bisa merasa tidak berdaya dan terpuruk dalam rasa bersalah. Cara recharge: dengarkan musik yang menenangkan, curahkan perasaanmu ke media kreatif, dan beri pelukan hangat pada dirimu sendiri.",
        "stress_recharge": {
            "burnout_triggers": [
                "Dipaksa bekerja di lingkungan yang beracun, penuh tipu daya, atau menuntut kompromi atas nilai moral.",
                "Kritik pedas yang meruntuhkan rasa percaya diri dan keyakinan akan nilai dirinya.",
                "Kelelahan mengurus urusan birokrasi kaku dan konflik interpersonal yang berlarut-larut."
            ],
            "stress_signals": [
                "Tiba-tiba menjadi sangat kritis, sarkastik, dan menyalahkan orang lain secara dingin (inferior Te grip).",
                "Merasa terasing total dari dunia luar dan tidak ingin melihat siapa pun.",
                "Mengabaikan makan, tidur, dan perawatan diri dasar karena tenggelam dalam kesedihan."
            ],
            "recharge_remedy": [
                "Curahkan isi hati ke dalam tulisan jurnal tanpa aturan tata bahasa atau ke kanvas gambar.",
                "Putar album musik favorit yang membangkitkan rasa damai di ruangan yang hangat dan nyaman.",
                "Ingatkan dirimu bahwa kamu berharga apa adanya dan tidak perlu sempurna untuk dicintai."
            ]
        },
        "color": "#10B981",
        "temperament": "Diplomat (Idealist / NF)",
        "bg_tint": "#ECFDF5",
        "border_color": "#A7F3D0",
        "work_style": "Kamu bekerja dengan inspirasi dan keterlibatan emosional. Saat kamu percaya pada misi pekerjaanmu, dedikasi dan kreativitasmu bisa mengalir tanpa batas."
    },
    "ENFJ": {
        "code": "ENFJ",
        "archetype": "Sang Protagonis Inspiratif",
        "title": "ENFJ · Sang Protagonis Inspiratif",
        "tagline": "Menggerakkan orang lain menuju potensi terbaiknya, merajut keharmonisan kelompok, dan memimpin dengan ketulusan hati.",
        "summary": "Kamu punya karisma alami yang hangat dan memikat. Kamu peduli tulus pada kebahagiaan dan masa depan orang-orang di sekitarmu, sering kali bisa melihat bakat tersembunyi seseorang bahkan sebelum orang itu menyadarinya sendiri. Kamu komunikatif, terorganisir, pandai menyatukan perbedaan, dan selalu terdorong untuk membawa perubahan positif.",
        "avatar": "assets/avatars/enfj.svg",
        "quick_dossier": {
            "superpower": "Kepemimpinan Empatik, Inspirasi Kelompok & Diplomasi Hangat",
            "love_language": "Kata-Kata Penguatan (Words of Affirmation) & Perhatian Nyata",
            "pet_peeve": "Ketidakpedulian, sikap egois yang merusak tim, dan pengabaian janji",
            "emergency_recharge": "Waktu tenang untuk merawat diri sendiri tanpa harus memikirkan kebutuhan orang lain"
        },
        "cognitive_roles": {
            "dominant": "Fe (Keharmonisan & Kepedulian Sosial): Nalurimu selalu peka pada kebutuhan kelompok. Kamu terdorong menciptakan suasana di mana semua orang merasa dihargai, aman, dan kompak.",
            "auxiliary": "Ni (Visi & Intuisi Makna): Kamu melihat potensi masa depan seseorang dan merancang langkah strategis untuk membimbing mereka bertumbuh.",
            "tertiary": "Se (Dinamika Sosial Nyata): Kamu luwes berinteraksi di atas panggung atau forum, tanggap membaca respon audiens, dan mampu mencairkan suasana dengan anggun.",
            "inferior": "Ti (Analisis Dingin Tanpa Perasaan): Menghadapi kritik pedas yang membongkar kekurangan logikamu secara blak-blakan bisa bikin kamu merasa cemas dan mempertanyakan kemampuanmu."
        },
        "relatable_traits": {
            "daily_habits": [
                "Secara otomatis mengecek kabar teman-teman di grup chat kalau ada yang kelihatan murung atau mendadak pendiam.",
                "Paling senang kalau berhasil mengenalkan dua orang kawan yang kemudian jadi sahabat akrab atau rekan bisnis sukses.",
                "Sering lupa makan atau istirahat karena terlalu asyik membantu menyelesaikan urusan orang lain.",
                "Punya kemampuan berbicara di depan umum yang bisa membuat orang lain tersentuh dan tergerak untuk bertindak."
            ],
            "pet_peeves": [
                "Orang yang memperlakukan pelayan atau staf junior dengan kasar dan meremehkan martabat mereka.",
                "Anggota tim yang pasif, melempar tanggung jawab, atau sengaja memicu konflik demi ego pribadi.",
                "Kebaikan dan ketulusanmu dianggap remeh atau dimanfaatkan demi keuntungan sepihak."
            ],
            "flow_triggers": [
                "Menjadi fasilitator atau mentor di mana kamu melihat seseorang berhasil mengatasi rasa takut dan meraih impiannya.",
                "Mengorganisasi acara sosial atau komunitas yang sukses menyatukan ratusan orang dalam energi positif."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Kecerdasan emosional tinggi, kemampuan diplomasi ulung, dan kepemimpinan yang merangkul semua orang menuju visi bersama.",
            "blindspots": "Terlalu memprioritaskan kebutuhan orang lain sampai burnout, sulit berkata 'tidak' (people pleaser), dan rentan stres saat ada anggota tim yang tidak bisa akur.",
            "superpower_list": [
                "Karisma persuasif yang tulus dan menggerakkan orang lain tanpa paksaan.",
                "Kepekaan luar biasa dalam mendeteksi dan menyelesaikan konflik kelompok secara damai.",
                "Kemampuan membimbing dan mengembangkan potensi terbaik rekan kerja."
            ],
            "blindspot_list": [
                "Kerap mengorbankan kebutuhan pribadi dan kesehatan demi menjaga kebahagiaan orang lain.",
                "Bisa menjadi terlalu protektif atau berusaha mengontrol jalannya hubungan demi menghindari konflik.",
                "Mudah merasa bersalah dan memikul beban saat ada rencana kelompok yang gagal."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu adalah organisator yang kolaboratif dan berdedikasi tinggi. Kamu paling bahagia saat bekerja bersama tim yang bersemangat dan saling mendukung.",
            "ideal_env": "Pendidikan, manajemen SDM (HR), pelatihan kepemimpinan, komunikasi publik, diplomasi, atau organisasi nirlaba yang berorientasi kemanusiaan.",
            "team_role": "Mentor penggerak dan lem perekat tim; orang yang menjaga motivasi dan keharmonisan kelompok tetap berkobar."
        },
        "love_relationships": {
            "love_style": "Kamu mencintai dengan penuh pengabdian dan kehangatan. Kamu sangat peka pada kebutuhan pasangan, selalu menyemangatinya, dan berusaha menciptakan hubungan yang penuh kasih sayang.",
            "green_flags": "Pasangan yang mengapresiasi ketulusanmu, bisa menjaga komunikasi terbuka, dan tidak segan memanjakanmu balik saat kamu sedang lelah.",
            "red_flags": "Orang yang narsistik, hanya mau menerima pengorbananmu tanpa timbal balik, atau suka memainkan perasaanmu dengan sikap dingin."
        },
        "friendship": {
            "circle_role": "Ibu/ayah baptis di circle pertemanan; orang yang selalu mengingat ulang tahun kawan, mengorganisasi reuni, dan ada saat teman butuh pelukan.",
            "circle_style": "Punya lingkaran pertemanan yang luas dan hangat, serta selalu berusaha memastikan tidak ada seorang pun di tongkrongan yang merasa diabaikan."
        },
        "interaction_guide": {
            "do": [
                "Apresiasi ketulusan dan usaha yang telah dia berikan; ucapan terima kasih yang tulus sangat bermakna baginya.",
                "Tanyakan kabarnya secara tulus dan ingatkan dia untuk meluangkan waktu istirahat bagi dirinya sendiri.",
                "Bicaralah dengan jujur dan terbuka tanpa menyembunyikan maksud di balik topeng."
            ],
            "dont": [
                "Jangan meremehkan kepeduliannya atau menganggap keramahannya sebagai kepalsuan.",
                "Jangan memanfaatkan kebaikannya untuk melimpahkan seluruh pekerjaan kotor kepadanya.",
                "Jangan memicu perselisihan sengit di depannya secara sengaja tanpa niat mencari solusi damai."
            ]
        },
        "stress_dynamics": "Saat kelelahan sosial melanda, kamu bisa merasa cemas dan tidak dihargai. Cara recharge: luangkan waktu khusus untuk memanjakan diri sendiri (spa, tidur pulas, atau me-time) tanpa harus meladeni chat urusan orang lain.",
        "stress_recharge": {
            "burnout_triggers": [
                "Terus-menerus menolong orang lain yang tidak tahu berterima kasih dan menguras energimu.",
                "Konflik antar orang terdekat yang tidak kunjung reda walau kamu sudah berusaha mendamaikan.",
                "Merasa tidak dihargai dan sendirian setelah sekian lama menjadi penopang bagi semua orang."
            ],
            "stress_signals": [
                "Tiba-tiba menjadi sangat kritis, sarkastik, dan menghakimi kesalahan orang lain secara pedas (Ti inferior).",
                "Merasa cemas berlebihan dan mempertanyakan apakah teman-temannya benar-benar menyukainya.",
                "Kelelahan fisik parah tapi tetap sulit menolak permintaan bantuan orang lain."
            ],
            "recharge_remedy": [
                "Tetapkan batasan tegas: matikan handphone selama satu hari dan katakan 'aku sedang tidak bisa diganggu'.",
                "Minta orang terdekat untuk merawat dan mendengarkanmu, bukan sebaliknya.",
                "Lakukan aktivitas yang memanjakan tubuh: mandi air hangat, pijat relaksasi, atau tidur siang panjang."
            ]
        },
        "color": "#047857",
        "temperament": "Diplomat (Idealist / NF)",
        "bg_tint": "#ECFDF5",
        "border_color": "#A7F3D0",
        "work_style": "Kamu adalah organisator yang kolaboratif dan berdedikasi tinggi. Kamu paling bahagia saat bekerja bersama tim yang bersemangat dan saling mendukung."
    },
    "ENFP": {
        "code": "ENFP",
        "archetype": "Sang Pejuang Antusias",
        "title": "ENFP · Sang Pejuang Antusias",
        "tagline": "Menyalakan percikan semangat di mana pun berada, penuh ide kreatif, dan selalu berani merayakan keunikan hidup.",
        "summary": "Kamu adalah sosok yang ceria, hangat, dan punya rasa ingin tahu tanpa batas. Kamu melihat dunia sebagai panggung luas yang penuh kemungkinan magis dan cerita manusia yang memikat. Kamu gampang akrab dengan siapa saja, berjiwa bebas, kreatif, dan paling tidak suka terkungkung dalam aturan yang monoton.",
        "avatar": "assets/avatars/enfp.svg",
        "quick_dossier": {
            "superpower": "Kreativitas Spontan, Optimisme Menular & Koneksi Manusiawi Hangat",
            "love_language": "Petualangan Seru, Obrolan Mendalam & Dukungan Penuh pada Kebebasan Jiwa",
            "pet_peeve": "Mikromanajemen, rutinitas membosankan, dan orang yang suka mengecilkan mimpi",
            "emergency_recharge": "Waktu hening untuk merenung di tempat estetik atau mengeksplorasi hobi baru yang seru"
        },
        "cognitive_roles": {
            "dominant": "Ne (Eksplorasi Peluang Baru): Pikiranmu adalah generator ide yang terus berputar, menemukan koneksi unik antar hal yang tampaknya tidak berkaitan.",
            "auxiliary": "Fi (Nilai Autentik Pribadi): Semangatmu dipandu oleh rasa empati dan kejujuran batin; kamu ingin menciptakan dampak yang selaras dengan nuranimu.",
            "tertiary": "Te (Dorongan Aksi Nyata): Saat sudah yakin pada suatu visi, kamu bisa mengumpulkan energi besar untuk mengajak orang lain bergerak bersama.",
            "inferior": "Si (Keterikatan Rutinitas & Detail): Mengurusi detail laporan keuangan, formulir administrasi, atau prosedur berulang adalah musuh terbesarmu."
        },
        "relatable_traits": {
            "daily_habits": [
                "Bisa berteman akrab dengan orang asing yang baru ditemui di kereta atau kafe dalam waktu 15 menit.",
                "Punya segudang rencana liburan atau proyek kreatif di kepalamu, walau yang beneran dieksekusi mungkin cuma sebagian.",
                "Mudah bersemangat pada hal baru, tapi begitu hal itu jadi rutinitas wajib yang monoton, energimu langsung anjlok.",
                "Sering ganti hobi setiap beberapa bulan sekali karena selalu penasaran ingin mencoba hal-hal baru."
            ],
            "pet_peeves": [
                "Orang yang selalu melihat sisi negatif dan langsung membunuh ide baru sebelum sempat dicoba.",
                "Dipaksa duduk diam mengerjakan pekerjaan administratif monoton selama 8 jam sehari.",
                "Hubungan yang terlalu menuntut kepatuhan kaku dan berusaha mengekang kebebasan berekspresi."
            ],
            "flow_triggers": [
                "Mendiskusikan ide proyek kreatif yang berpotensi mengubah hidup banyak orang bersama kawan-kawan yang sefrekuensi.",
                "Melakukan perjalanan spontan (road trip) ke tempat yang belum pernah dikunjungi sebelumnya."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Antusiasme yang menular, kemampuan adaptasi luar biasa, empati tulus, dan cara pandang inovatif yang memecahkan kebuntuan.",
            "blindspots": "Kesulitan menjaga konsistensi rutinitas, mudah terdistraksi oleh ide baru sebelum tugas lama selesai, dan overthinking soal penerimaan sosial.",
            "superpower_list": [
                "Kemampuan alami mencairkan suasana dan membuat siapa pun merasa nyaman berbicara dengannya.",
                "Daya cipta yang tidak pernah kering dalam memecahkan masalah dengan cara tak terduga.",
                "Optimisme tulus yang mampu membangkitkan semangat orang yang sedang putus asa."
            ],
            "blindspot_list": [
                "Cenderung menunda-nunda urusan praktis dan administrasi penting hingga detik-detik terakhir.",
                "Mudah merasa kewalahan karena terlalu banyak mengambil komitmen emosional dan sosial.",
                "Terkadang terlalu idealis dan terluka saat realitas dunia tidak seindah harapannya."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu adalah pencetus inspirasi yang fleksibel. Kamu bekerja paling maksimal saat diberi kebebasan bereksperimen dan berkolaborasi dalam lingkungan yang santai namun dinamis.",
            "ideal_env": "Industri kreatif, media, hubungan masyarakat (PR), konseling, kewirausahaan sosial, atau pemasaran digital yang dinamis.",
            "team_role": "Katalisator antusiasme dan pembuat ide; orang yang menjaga energi tim tetap ceria dan optimis."
        },
        "love_relationships": {
            "love_style": "Cinta bagimu adalah petualangan emosional yang indah. Kamu penuh kejutan romantis, selalu mendukung pasangan untuk menjadi dirinya sendiri, dan menginginkan ikatan batin yang hidup.",
            "green_flags": "Seseorang yang bisa menjadi 'jangkar' yang menenangkan tanpa mematikan api semangatmu, mau diajak berpetualang, dan setia.",
            "red_flags": "Pasangan yang posesif berlebihan, suka mengkritik sifat spontanmu, atau selalu memaksamu bersikap kaku dan formal."
        },
        "friendship": {
            "circle_role": "Pusat keceriaan dan teman curhat yang paling suportif; orang yang selalu siap menyemangati impian terliar teman-temannya.",
            "circle_style": "Punya teman dari berbagai latar belakang yang sangat beragam, dan selalu terbuka menyambut orang baru ke dalam lingkaran persahabatannya."
        },
        "interaction_guide": {
            "do": [
                "Dukung ide-idenya dengan antusias dan bantu dia merumuskan langkah konkret secara santai.",
                "Beri dia kebebasan untuk berekspresi tanpa menghakiminya dengan standar konvensional kaku.",
                "Ajaklah dia mencoba hal-hal baru dan dengarkan ceritanya dengan penuh perhatian."
            ],
            "dont": [
                "Jangan membatasi ruang geraknya dengan mikromanajemen detail yang berlebihan.",
                "Jangan membicarakan hal-hal negatif atau gosip menjatuhkan terus-menerus di depannya.",
                "Jangan memaksanya melakukan rutinitas yang monoton tanpa penjelasan makna tujuannya."
            ]
        },
        "stress_dynamics": "Saat stres berat, kamu bisa merasa terjebak, cemas, dan kehilangan percikan semangatmu. Cara recharge: luangkan waktu sendiri di alam terbuka, buat coretan kreatif tanpa beban, dan nikmati istirahat tanpa rasa bersalah.",
        "stress_recharge": {
            "burnout_triggers": [
                "Terjebak dalam pekerjaan kaku yang menuntut kepatuhan buta dan minim interaksi manusiawi.",
                "Kelelahan sosial akibat berusaha membuat semua orang senang sepanjang waktu.",
                "Tekanan tenggat waktu administratif yang menumpuk dan tidak teratur."
            ],
            "stress_signals": [
                "Kehilangan keceriaan, menjadi sangat cemas pada kesehatan tubuh atau kesalahan kecil di masa lalu (Si inferior).",
                "Merasa kehilangan makna hidup dan meragukan apakah dirinya memiliki masa depan yang cerah.",
                "Menjadi pasif, menarik diri dari pergaulan, dan malas merespons pesan masuk."
            ],
            "recharge_remedy": [
                "Ubah suasana: pindah tempat duduk ke kafe estetik atau pergi ke alam terbuka yang hijau.",
                "Tuliskan semua hal yang sedang membebani kepalamu ke dalam bentuk mind map acak lalu buang yang tidak perlu.",
                "Izinkan dirimu untuk tidak produktif selama sehari penuh tanpa merasa bersalah."
            ]
        },
        "color": "#059669",
        "temperament": "Diplomat (Idealist / NF)",
        "bg_tint": "#ECFDF5",
        "border_color": "#A7F3D0",
        "work_style": "Kamu adalah pencetus inspirasi yang fleksibel. Kamu bekerja paling maksimal saat diberi kebebasan bereksperimen dan berkolaborasi dalam lingkungan yang santai namun dinamis."
    },
    "ISTJ": {
        "code": "ISTJ",
        "archetype": "Sang Logistik Tepercaya",
        "title": "ISTJ · Sang Logistik Tepercaya",
        "tagline": "Menjaga keteraturan dengan integritas tinggi, tenang dalam ketelitian, dan selalu menepati janji dengan aksi nyata.",
        "summary": "Kamu adalah pilar keandalan yang bisa diandalkan kapan saja. Kamu menghargai fakta, ketertiban, dan kejujuran tanpa banyak drama. Saat kamu berjanji melakukan sesuatu, kamu akan menuntaskannya dengan cermat dan disiplin tinggi. Kamu lebih suka bukti kerja nyata daripada omong kosong atau teori muluk yang tidak bisa dipertanggungjawabkan.",
        "avatar": "assets/avatars/istj.svg",
        "quick_dossier": {
            "superpower": "Ketelitian Cermat, Keandalan Eksekusi & Integritas Nyata",
            "love_language": "Tindakan Nyata (Acts of Service) & Komitmen Setia",
            "pet_peeve": "Ketidaktepatan waktu, orang yang ingkar janji, dan perubahan mendadak tanpa rencana",
            "emergency_recharge": "Waktu hening di rumah yang rapi, menuntaskan to-do list pribadi tanpa gangguan"
        },
        "cognitive_roles": {
            "dominant": "Si (Memori Fakta & Pengalaman Nyata): Nalurimu sangat teliti mengamati detail, mengingat prosedur yang terbukti aman, dan menjaga stabilitas sistem.",
            "auxiliary": "Te (Logika & Efisiensi Sistemik): Kamu mengatur alur kerja secara runtut, membuat SOP yang jelas, dan memastikan tugas selesai tepat waktu.",
            "tertiary": "Fi (Nilai & Tanggung Jawab Pribadi): Kamu punya integritas moral yang teguh; rasa banggamu muncul saat kamu bisa memenuhi kewajiban dengan terhormat.",
            "inferior": "Ne (Imajinasi Peluang Tak Terduga): Menghadapi situasi kacau serba dadakan tanpa kejelasan data bisa memicu rasa cemas akan skenario terburuk."
        },
        "relatable_traits": {
            "daily_habits": [
                "Paling tepat waktu di tongkrongan; kalau janjian jam 10, kamu sudah sampai di lokasi jam 09.50.",
                "File di laptop atau lemari pakaian tertata rapi sesuai kategori dan fungsinya masing-masing.",
                "Merasa sangat terganggu kalau ada orang yang meminjam barang dan tidak mengembalikannya ke posisi semula.",
                "Selalu membaca instruksi atau syarat ketentuan dengan teliti sebelum menandatangani atau membeli sesuatu."
            ],
            "pet_peeves": [
                "Orang yang suka membatalkan janji secara sepihak di menit-menit terakhir tanpa alasan darurat.",
                "Rekan kerja yang ceroboh dan mengabaikan standar baku hanya demi buru-buru selesai.",
                "Perubahan instruksi yang mendadak dan berulang-ulang tanpa koordinasi matang."
            ],
            "flow_triggers": [
                "Merapikan data, menyusun laporan keuangan, atau mengorganisasi alur kerja hingga rapi dan seimbang.",
                "Menuntaskan proyek rumit langkah demi langkah sesuai checklist tanpa ada satu detail pun yang terlewat."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Tingkat akurasi dan keandalan luar biasa, loyalitas tinggi pada komitmen, dan ketenangan dalam menjaga keteraturan di tengah kekacauan.",
            "blindspots": "Terkadang terlalu kaku memegang aturan lama, sulit beradaptasi dengan perubahan metode mendadak, dan kurang fleksibel menerima ide spekulatif.",
            "superpower_list": [
                "Ketelitian tajam dalam mendeteksi kesalahan kecil yang terlewatkan oleh orang lain.",
                "Konsistensi etos kerja yang stabil dan tidak mudah terpengaruh fluktuasi suasana hati.",
                "Kejujuran dan integritas yang membuat orang lain merasa sangat aman mempercayakan tanggung jawab kepadamu."
            ],
            "blindspot_list": [
                "Kecenderungan menolak cara baru sebelum ada bukti riil yang teruji selama bertahun-tahun.",
                "Bisa terlihat dingin atau terlalu kaku saat harus menyampaikan evaluasi kepada rekan kerja.",
                "Rentan stres dan cemas berlebihan saat rencana matang tiba-tiba harus diubah total di tengah jalan."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu adalah pekerja berdedikasi tinggi yang menghormati struktur dan kejelasan wewenang. Kamu bangga menghasilkan pekerjaan yang presisi dan bebas dari cacat.",
            "ideal_env": "Keuangan, akuntansi, hukum, logistik, administrasi data, rekayasa teknik, atau operasional yang menuntut akurasi dan kepatuhan standar tinggi.",
            "team_role": "Penjaga standar mutu dan fondasi stabilitas; orang yang memastikan semua aturan dipatuhi dan tenggat waktu terpenuhi."
        },
        "love_relationships": {
            "love_style": "Kamu menunjukkan cinta lewat kesetiaan seumur hidup, memberikan kepastian masa depan, dan merawat kebutuhan praktis pasangan secara konsisten setiap hari.",
            "green_flags": "Pasangan yang menepati janji, bertanggung jawab, menghargai rutinitas yang tenang, dan bisa diajak merencanakan masa depan bersama dengan matang.",
            "red_flags": "Orang yang tidak bertanggung jawab secara finansial, hidup serba impulsif tanpa arah, atau suka mempermainkan komitmen hubungan."
        },
        "friendship": {
            "circle_role": "Teman yang paling bisa diandalkan saat butuh pertolongan nyata; kawan yang selalu datang tepat waktu dan tidak pernah mengumbar janji palsu.",
            "circle_style": "Lingkaran pertemananmu stabil dan tidak banyak berganti; kamu lebih nyaman berkumpul dengan sahabat lama yang sudah kamu kenal karakternya selama bertahun-tahun."
        },
        "interaction_guide": {
            "do": [
                "Tepati janji dan datang tepat waktu; jika ada perubahan, beri kabar seawal mungkin beserta alasannya.",
                "Sampaikan informasi berbasis fakta konkret dan data riil, bukan sekadar asumsi atau gosip.",
                "Hargai prosedur dan ketertiban kerja yang sudah dia bangun dengan rapi."
            ],
            "dont": [
                "Jangan mengubah rencana yang sudah disepakati bersama secara mendadak tanpa konsultasi.",
                "Jangan bersikap meremehkan detail atau aturan keselamatan kerja di depannya.",
                "Jangan memaksa dia mengambil risiko spekulatif yang tidak jelas dasar perhitungannya."
            ]
        },
        "stress_dynamics": "Saat rencana berantakan total, kamu bisa merasa cemas dan membayangkan kemungkinan terburuk (catastrophizing). Cara recharge: rapikan kembali ruang fisikmu, susun ulang rencana langkah demi langkah, dan istirahat dari urusan yang serba tak pasti.",
        "stress_recharge": {
            "burnout_triggers": [
                "Lingkungan kerja yang semrawut tanpa aturan jelas dan dipimpin oleh pihak yang tidak konsisten.",
                "Dikelilingi oleh orang-orang yang sering ingkar janji dan lepas tangan dari tanggung jawab.",
                "Beban kerja berlebih yang mengorbankan waktu istirahat dan ketelitian standarmu."
            ],
            "stress_signals": [
                "Mengalami 'Ne inferior grip': tiba-tiba diliputi rasa cemas ekstrem bahwa malapetaka besar akan menimpa.",
                "Menjadi sangat sinis, menuduh orang lain tidak becus, dan menarik diri ke tempat aman.",
                "Mengalami keluhan fisik seperti insomnia, sakit kepala tegang, atau gangguan pencernaan."
            ],
            "recharge_remedy": [
                "Lakukan kegiatan fisik sederhana yang terstruktur: mencuci mobil, menata rak buku, atau menyapu halaman.",
                "Kembalilah ke rutinitas harian yang membuatmu merasa memegang kendali atas hidupmu.",
                "Fokuslah hanya pada apa yang bisa kamu selesaikan hari ini, dan lepaskan hal-hal di luar kuasamu."
            ]
        },
        "color": "#0284C7",
        "temperament": "Pengawal (Sentinel / SJ)",
        "bg_tint": "#F0F9FF",
        "border_color": "#BAE6FD",
        "work_style": "Kamu adalah pekerja berdedikasi tinggi yang menghormati struktur dan kejelasan wewenang. Kamu bangga menghasilkan pekerjaan yang presisi dan bebas dari cacat."
    },
    "ISFJ": {
        "code": "ISFJ",
        "archetype": "Sang Pembela Setia",
        "title": "ISFJ · Sang Pembela Setia",
        "tagline": "Merawat dengan kehangatan tulus, teliti menjaga kenyamanan sesama, dan selalu setia mendampingi dalam suka maupun duka.",
        "summary": "Kamu adalah sosok pelindung yang berhati lembut dan penuh dedikasi. Kamu punya ingatan luar biasa tentang detail-detail kecil yang penting bagi orang yang kamu sayangi, mulai dari makanan favorit sampai tanggal berharga. Kamu sabar, dapat diandalkan, tidak suka mencari sorotan panggung, dan selalu berusaha memastikan orang di sekitarmu merasa aman dan nyaman.",
        "avatar": "assets/avatars/isfj.svg",
        "quick_dossier": {
            "superpower": "Kepedulian Praktis, Kesetiaan Tanpa Pamrih & Ketelitian Rawat",
            "love_language": "Perhatian Sehari-hari, Melayani dengan Tulus & Sentuhan Hangat",
            "pet_peeve": "Kekasaran, ketidaksopanan, dan orang yang melupakan kebaikan sesama",
            "emergency_recharge": "Waktu tenang di rumah yang nyaman, memasak resep favorit, atau istirahat bersama keluarga terdekat"
        },
        "cognitive_roles": {
            "dominant": "Si (Memori Kasih & Detail Praktis): Nalurimu menyimpan kenangan berharga dan detail kebiasaan orang terdekat untuk melayani mereka dengan penuh perhatian.",
            "auxiliary": "Fe (Keharmonisan & Kepedulian Sosial): Kamu peka membaca kebutuhan orang lain dan secara aktif menciptakan suasana hangat yang bebas dari konflik.",
            "tertiary": "Ti (Penalaran Praktis Mandiri): Di balik kelembutanmu, kamu punya logika sehat yang cermat dalam menyelesaikan masalah sehari-hari secara efisien.",
            "inferior": "Ne (Kekhawatiran akan Perubahan): Dihadapkan pada ketidakpastian masa depan atau perubahan besar yang tidak terduga bisa memicu kekhawatiran batin yang mendalam."
        },
        "relatable_traits": {
            "daily_habits": [
                "Selalu ingat makanan kesukaan teman, alergi mereka, atau topik sensitif yang sebaiknya tidak diungkit di tongkrongan.",
                "Sering menyiapkan camilan, payung ekstra, atau tisu di tas untuk berjaga-jaga kalau ada teman yang membutuhkan.",
                "Paling sulit menolak permintaan bantuan orang lain walau badan sendiri sebenarnya sudah sangat lelah.",
                "Merasa senang saat orang lain menikmati masakan atau bantuan yang kamu berikan dengan tulus."
            ],
            "pet_peeves": [
                "Orang yang sombong, kasar pada orang lain, atau tidak menghargai tata krama sopan santun dasar.",
                "Kebaikan hatimu dimanfaatkan oleh orang yang hanya datang saat butuh lalu menghilang.",
                "Suasana keluarga atau tim yang dipenuhi pertengkaran sengit yang saling melukai perasaan."
            ],
            "flow_triggers": [
                "Menyiapkan kejutan hangat untuk orang terkasih dan melihat senyum bahagia di wajah mereka.",
                "Merapikan rumah, merawat tanaman, atau membuat kerajinan tangan yang estetik dan menenangkan hati."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Kesetiaan tanpa batas, kepekaan emosional yang membumi, ketelitian cermat dalam melayani, dan keandalan luar biasa dalam menjaga keharmonisan.",
            "blindspots": "Cenderung memendam kekecewaan hingga menumpuk jadi rasa dongkol, terlalu enggan berubah dari zona nyaman, dan sering mengabaikan kebutuhan diri sendiri.",
            "superpower_list": [
                "Daya ingat emosional yang tinggi dalam mengingat kebutuhan dan kenyamanan orang lain.",
                "Ketenangan dan kesabaran luar biasa dalam mendampingi orang yang sedang sakit atau berduka.",
                "Dedikasi tanpa pamrih yang menjaga keutuhan komunitas atau keluarga tetap erat."
            ],
            "blindspot_list": [
                "Kesulitan mengekspresikan kemarahan secara terbuka sehingga terkadang menjadi pasif-agresif.",
                "Terlalu cemas menghadapi perubahan yang belum teruji keamanannya di masa depan.",
                "Bisa merasa sangat terluka jika pengorbanan tulusnya tidak dihargai sama sekali."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu adalah pekerja berhati mulia yang teliti dan bertanggung jawab. Kamu lebih memilih bekerja di balik layar memastikan segalanya berjalan lancar daripada berebut sorotan panggung.",
            "ideal_env": "Kesehatan, keperawatan, pendidikan anak, administrasi personalia, perhotelan, atau layanan sosial yang menuntut ketulusan dan ketelitian tinggi.",
            "team_role": "Penjaga kesejahteraan tim; orang yang memastikan semua orang merasa didukung dan kebutuhan logistik kerja terpenuhi."
        },
        "love_relationships": {
            "love_style": "Kamu mencintai dengan kelembutan yang nyata dan langgeng. Kamu menunjukkan kasih sayang lewat tindakan merawat sehari-hari, mendengarkan pasangan dengan sabar, dan setia mendampingi.",
            "green_flags": "Pasangan yang sopan, menghargai nilai keluarga, tulus berterima kasih atas hal-hal kecil, dan memberikan rasa aman emosional.",
            "red_flags": "Orang yang kasar, egois, suka meremehkan keluargamu, atau memperlakukan hubungan seperti permainan tanpa komitmen."
        },
        "friendship": {
            "circle_role": "Sahabat yang paling perhatian dan tempat berlindung yang menyejukkan hati saat teman sedang terluka atau tertekan.",
            "circle_style": "Menjaga pertemanan jangka panjang dengan penuh kesetiaan; kamu selalu hadir di momen-momen penting sahabatmu tanpa perlu diminta."
        },
        "interaction_guide": {
            "do": [
                "Ucapkan terima kasih dan apresiasi atas bantuannya secara tulus; pengakuan hangat itu sangat membahagiakannya.",
                "Bicaralah dengan nada santun dan penuh rasa hormat.",
                "Bantulah dia untuk meluangkan waktu merawat dirinya sendiri dan ingatkan dia untuk berani berkata tidak."
            ],
            "dont": [
                "Jangan memanfaatkan kerelaannya membantu sampai dia jatuh sakit kelelahan.",
                "Jangan bersikap kasar atau memicu pertengkaran di depannya secara terang-terangan.",
                "Jangan memaksanya melakukan perubahan drastis tanpa memberinya waktu beradaptasi secara bertahap."
            ]
        },
        "stress_dynamics": "Saat kelelahan batin menumpuk, kamu bisa merasa tidak berdaya dan terpuruk dalam kecemasan akan masa depan. Cara recharge: istirahat tenang di rumah, nikmati makanan hangat yang kamu sukai, dan luangkan waktu santai tanpa kewajiban melayani orang lain.",
        "stress_recharge": {
            "burnout_triggers": [
                "Terus-menerus mengurus orang lain tanpa pernah ada yang menanyakan 'kamu sendiri apa kabar?'.",
                "Konflik berkepanjangan di rumah atau kantor yang merusak rasa damai dan keharmonisan.",
                "Perubahan hidup mendadak yang meruntuhkan rasa kepastian dan stabilitas yang sudah dibangun."
            ],
            "stress_signals": [
                "Tiba-tiba merasa sangat cemas bahwa hal-hal buruk akan menimpa orang-orang terkasihnya (Ne inferior).",
                "Menjadi sensitif, mudah menangis, atau merasa pengorbanannya selama ini sia-sia.",
                "Mengisolasi diri di kamar dan menolak berbicara karena merasa energinya sudah terkuras habis."
            ],
            "recharge_remedy": [
                "Izinkan orang lain untuk merawatmu hari ini: pesan makanan enak tanpa harus repot memasak sendiri.",
                "Tonton film keluarga atau serial nostalgia yang menghangatkan hati di bawah selimut hangat.",
                "Curhatkan unek-unek yang selama ini kamu pendam kepada satu sahabat yang paling tulus mendengarkan."
            ]
        },
        "color": "#0284C7",
        "temperament": "Pengawal (Sentinel / SJ)",
        "bg_tint": "#F0F9FF",
        "border_color": "#BAE6FD",
        "work_style": "Kamu adalah pekerja berhati mulia yang teliti dan bertanggung jawab. Kamu lebih memilih bekerja di balik layar memastikan segalanya berjalan lancar daripada berebut sorotan panggung."
    },
    "ESTJ": {
        "code": "ESTJ",
        "archetype": "Sang Eksekutif Tegas",
        "title": "ESTJ · Sang Eksekutif Tegas",
        "tagline": "Menegakkan keteraturan dan disiplin nyata, memimpin dengan ketegasan logis, dan memastikan setiap target tuntas terwujud.",
        "summary": "Kamu adalah pemimpin operasional yang berani, tertib, dan berintegritas tinggi. Kamu menghargai aturan yang jelas, kejujuran langsung, dan kerja keras yang nyata. Kamu tidak suka membuang-buang waktu dengan keraguan atau basa-basi; bagimu, tugas yang diemban harus diselesaikan dengan standar terbaik dan dapat dipertanggungjawabkan di hadapan semua orang.",
        "avatar": "assets/avatars/estj.svg",
        "quick_dossier": {
            "superpower": "Manajemen Operasional Tangguh, Ketegasan Regulasi & Disiplin Eksekusi",
            "love_language": "Tindakan Bertanggung Jawab, Komitmen Nyata & Waktu Bersama yang Teratur",
            "pet_peeve": "Ketidakdisiplinan, alasan berulang-ulang, dan kekacauan organisasi yang dibiarkan",
            "emergency_recharge": "Aktivitas fisik teratur, berkumpul santai dengan keluarga/kawan setia, dan menyelesaikan rencana kerja minggu depan"
        },
        "cognitive_roles": {
            "dominant": "Te (Efisiensi & Ketertiban Operasional): Nalurimu secara otomatis mengorganisasi sumber daya, menegakkan SOP, dan menuntut akuntabilitas hasil kerja.",
            "auxiliary": "Si (Rujukan Fakta & Prosedur Teruji): Kamu mengandalkan bukti masa lalu dan metode yang terbukti berhasil untuk meminimalkan risiko kegagalan.",
            "tertiary": "Ne (Inovasi Praktis Terukur): Kamu terbuka pada ide baru selama gagasan tersebut punya dasar implementasi yang masuk akal dan efisien.",
            "inferior": "Fi (Nilai Personal & Kepekaan Rasa Batin): Kamu merasa tidak nyaman dan canggung saat harus menghadapi drama emosional subjektif yang tidak berpijak pada fakta konkret."
        },
        "relatable_traits": {
            "daily_habits": [
                "Paling geram kalau melihat antrean yang diserobot atau aturan bersama yang dilanggar begitu saja tanpa sanksi.",
                "Secara otomatis mengambil peran mengatur susunan acara liburan keluarga atau agenda rapat kantor agar tidak berantakan.",
                "Bicara lugas, tegas, dan langsung pada intinya tanpa suka menutup-nutupi masalah dengan kata-kata manis palsu.",
                "Merasa puas saat melihat ruang kerja atau rumah tertata rapi, bersih, dan semua barang berfungsi dengan baik."
            ],
            "pet_peeves": [
                "Orang yang terlambat dan menganggap enteng waktu orang lain yang sudah menunggu.",
                "Karyawan atau rekan yang banyak alasan saat target tidak tercapai tapi enggan meminta bantuan sejak awal.",
                "Ketidakpastian aturan hukum atau SOP yang berubah-ubah sesuka hati tanpa kejelasan resmi."
            ],
            "flow_triggers": [
                "Menertibkan proyek yang tadinya kacau balau menjadi sistematis dan selesai tepat sebelum batas waktu.",
                "Memimpin tim yang berdisiplin tinggi dalam mencapai target produksi atau kinerja yang memecahkan rekor."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Dedikasi kerja luar biasa, ketegasan mengambil keputusan di lapangan, kepemimpinan yang dapat diandalkan, dan integritas tinggi.",
            "blindspots": "Terkadang terkesan terlalu otoriter atau kaku, kurang peka pada kebutuhan emosional anggota tim yang lebih perasa, dan sulit menerima kritik atas metodenya.",
            "superpower_list": [
                "Keberanian menegakkan kebenaran aturan dan memimpin pembenahan sistem tanpa gentar.",
                "Kemampuan manajemen waktu dan logistik yang sangat efisien dalam skala besar.",
                "Kesetiaan dan tanggung jawab penuh dalam menjaga kesejahteraan tim atau keluarga yang dipimpinnya."
            ],
            "blindspot_list": [
                "Bisa bersikap terlalu keras dan menghakimi orang lain yang ritme kerjanya lebih lambat.",
                "Kecenderungan menolak pendekatan baru hanya karena belum terdaftar dalam standar operasional konvensional.",
                "Sulit mengekspresikan rasa empati atau apresiasi hangat secara verbal kepada orang terdekat."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu adalah teladan etos kerja disiplin. Kamu datang tepat waktu, bekerja dengan fokus penuh, dan memastikan setiap rupiah dan jam kerja membuahkan hasil nyata.",
            "ideal_env": "Manajemen operasional, militer/kepolisian, teknik sipil, hukum, perbankan, manufaktur, atau pemerintahan yang terstruktur rapi.",
            "team_role": "Komandan operasional; orang yang membagi tugas secara adil, memastikan disiplin, dan menuntaskan target sesuai anggaran."
        },
        "love_relationships": {
            "love_style": "Kamu menunjukkan cinta lewat komitmen yang kokoh, memberikan perlindungan dan stabilitas materi, serta merawat masa depan keluarga dengan penuh rasa tanggung jawab.",
            "green_flags": "Pasangan yang setia, menghargai komitmen keluarga, punya etos kerja yang baik, dan bisa diajak berdiskusi secara terbuka tanpa drama.",
            "red_flags": "Orang yang tidak bertanggung jawab, hobi bermain api dalam komitmen, atau mengabaikan kewajiban moral terhadap keluarga."
        },
        "friendship": {
            "circle_role": "Koordinator utama dan teman yang selalu siap sedia membantu dengan aksi konkret saat sahabat sedang tertimpa musibah nyata.",
            "circle_style": "Menghargai persahabatan yang kokoh dan setia kawan; kamu suka mengadakan acara kumpul makan bersama atau olahraga bareng teman lama."
        },
        "interaction_guide": {
            "do": [
                "Datanglah tepat waktu dan sampaikan laporan atau usulanmu secara runtut dan berbasis data riil.",
                "Bersikaplah jujur dan bertanggung jawab atas tugas yang telah kamu sepakati.",
                "Hargai pengorbanan dan kepemimpinannya dalam menjaga kestabilan organisasi atau tim."
            ],
            "dont": [
                "Jangan mencoba mengakali aturan atau mencari-cari alasan klise saat melakukan kesalahan.",
                "Jangan menguji kesabarannya dengan sikap acuh tak acuh atau menunda-nunda pekerjaan penting.",
                "Jangan membawa gosip pribadi atau drama yang tidak relevan ke dalam rapat kerja dengannya."
            ]
        },
        "stress_dynamics": "Saat berada di bawah tekanan ekstrem dan merasa usahanya tidak dihargai, kamu bisa menjadi emosional dan merasa sendirian. Cara recharge: lepaskan sementara beban kepemimpinan, lakukan olahraga fisik, dan nikmati waktu santai bersama keluarga terkasih.",
        "stress_recharge": {
            "burnout_triggers": [
                "Menghadapi ketidaktertiban sistem yang kronis dan orang-orang yang menolak untuk bekerja sama secara bertanggung jawab.",
                "Merasa memikul semua beban tanggung jawab sendirian tanpa ada rekan yang sanggup mengimbangi standarmu.",
                "Pengkhianatan atas komitmen kesetiaan dari pihak yang selama ini kamu bela mati-matian."
            ],
            "stress_signals": [
                "Mengalami 'Fi inferior grip': tiba-tiba merasa sangat terluka, merasa tidak ada yang menghargainya, dan menarik diri dalam kemarahan batin.",
                "Menjadi sangat reaktif secara emosional dan melontarkan kritik keras tanpa filter kesabaran.",
                "Merasa kehilangan kendali dan frustrasi karena rencananya yang rapi dipatahkan oleh pihak luar."
            ],
            "recharge_remedy": [
                "Delegasikan tugas operasional harian kepada staf tepercaya dan ambil cuti pendek untuk rehat total.",
                "Lakukan aktivitas fisik di luar ruangan (golf, bersepeda, mendaki santai, atau bekerja di kebun).",
                "Habiskan waktu bersama orang-orang tercinta yang menerimamu apa adanya sebagai manusia, bukan hanya sebagai pemimpin."
            ]
        },
        "color": "#0369A1",
        "temperament": "Pengawal (Sentinel / SJ)",
        "bg_tint": "#F0F9FF",
        "border_color": "#BAE6FD",
        "work_style": "Kamu adalah teladan etos kerja disiplin. Kamu datang tepat waktu, bekerja dengan fokus penuh, dan memastikan setiap rupiah dan jam kerja membuahkan hasil nyata."
    },
    "ESFJ": {
        "code": "ESFJ",
        "archetype": "Sang Konsul Hangat",
        "title": "ESFJ · Sang Konsul Hangat",
        "tagline": "Menghadirkan kehangatan di setiap pertemuan, peka menjaga perasaan sesama, dan setia merajut kebersamaan yang kompak.",
        "summary": "Kamu adalah sosok yang ramah, penuh perhatian, dan sangat menghargai keharmonisan sosial. Kamu punya bakat alami membuat siapa pun merasa disambut dan diakui. Kamu menghormati tradisi kebersamaan, setia pada keluarga dan sahabat, terorganisir rapi dalam mengurus kebutuhan kelompok, dan selalu terdorong untuk memberikan yang terbaik bagi kebahagiaan orang-orang di sekitarmu.",
        "avatar": "assets/avatars/esfj.svg",
        "quick_dossier": {
            "superpower": "Hospitality Alami, Membangun Komunitas Hangat & Keteraturan Sosial",
            "love_language": "Perhatian Detail, Waktu Bersama yang Hangat & Kata-Kata Apresiasi",
            "pet_peeve": "Sikap dingin meremehkan, orang yang merusak suasana kebersamaan, dan ketidaksopanan",
            "emergency_recharge": "Kumpul santai bareng orang terkasih yang tulus, atau merawat diri di rumah yang rapi"
        },
        "cognitive_roles": {
            "dominant": "Fe (Keharmonisan Sosial & Kasih Nyata): Nalurimu selalu aktif membaca kebutuhan orang lain dan memastikan semua orang merasa nyaman, akrab, dan dihargai.",
            "auxiliary": "Si (Ketelitian Tradisi & Detail Kenangan): Kamu mengingat tanggal ulang tahun, kebiasaan keluarga, dan tata krama yang menjaga hubungan tetap harmonis.",
            "tertiary": "Ne (Kreativitas Hiburan Sosial): Kamu punya ide-ide seru untuk meramaikan acara kumpul bareng, menyiapkan hidangan lezat, dan mendekorasi ruangan.",
            "inferior": "Ti (Kritik Logika Dingin Tanpa Empati): Menghadapi kritik pedas yang membongkar argumenmu di depan umum bisa bikin kamu merasa ditolak dan terluka batin."
        },
        "relatable_traits": {
            "daily_habits": [
                "Paling pertama yang berinisiatif patungan kado atau memesankan kue saat ada teman atau rekan kerja yang berulang tahun.",
                "Tidak bisa tenang kalau melihat ada anggota keluarga atau teman yang pulang ke rumah dalam keadaan lapar dan murung.",
                "Senang sekali menjadi tuan rumah acara kumpul-kumpul; memastikan meja makan penuh hidangan lezat dan minuman segar.",
                "Sering menjadi penengah saat ada dua teman yang sedang salah paham agar mereka bisa segera baikan lagi."
            ],
            "pet_peeves": [
                "Orang yang datang ke acara dengan wajah cemberut dan menyebarkan aura negatif ke seluruh ruangan.",
                "Tamu yang tidak menghargai usaha tuan rumah yang sudah bersusah payah menyiapkan segalanya.",
                "Pengabaian terhadap norma kesopanan dan etika dasar dalam pergaulan masyarakat."
            ],
            "flow_triggers": [
                "Menyelenggarakan acara keluarga atau reuni komunitas yang berjalan sangat sukses, hangat, dan penuh tawa.",
                "Mendengarkan ucapan 'terima kasih banyak, berkat kamu segalanya jadi menyenangkan' dari orang-orang tersayang."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Kecerdasan interpersonal luar biasa, loyalitas mendalam, kemampuan organisasi acara yang cermat, dan kehangatan yang tulus.",
            "blindspots": "Terlalu bergantung pada validasi atau pujian orang lain, mudah merasa terluka oleh penolakan, dan kadang terlalu ikut campur dalam urusan orang lain demi niat baik.",
            "superpower_list": [
                "Kemampuan luar biasa menyatukan orang-orang dari berbagai latar belakang menjadi satu keluarga yang kompak.",
                "Ketelitian tinggi dalam merawat kebutuhan fisik dan emosional orang-orang di sekitarnya.",
                "Integritas kesetiaan dalam menjaga janji dan komitmen pertemanan seumur hidup."
            ],
            "blindspot_list": [
                "Kecenderungan merasa cemas berlebihan saat ada orang yang tidak menyukainya walau tanpa alasan jelas.",
                "Sulit menerima kritik yang disampaikan secara dingin tanpa memperhatikan perasaannya.",
                "Kerap memaksakan bantuan atau nasihat yang tidak diminta karena merasa dirinya tahu apa yang terbaik untuk orang lain."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu adalah pekerja yang berdedikasi dan kooperatif. Kamu paling produktif saat bekerja dalam lingkungan tim yang saling menghargai dan punya kejelasan tugas yang teratur.",
            "ideal_env": "Hubungan masyarakat, administrasi pendidikan, manajemen acara, keperawatan, konseling keluarga, atau customer relations yang berfokus pada pelayanan manusia.",
            "team_role": "Tuan rumah dan koordinator kebersamaan tim; orang yang memastikan semangat kerja tim tetap positif dan saling peduli."
        },
        "love_relationships": {
            "love_style": "Kamu mencintai dengan segenap hati dan perhatian nyata. Kamu selalu ingin membuat pasangan merasa istimewa lewat kejutan manis, masakan favorit, dan dukungan setia dalam suka maupun duka.",
            "green_flags": "Pasangan yang ekspresif menunjukkan kasih sayang, menghargai keluargamu, setia, dan tidak segan memuji usaha yang kamu lakukan.",
            "red_flags": "Orang yang dingin emosional, cuek saat kamu sedang bersedih, atau suka mempermalukanmu di hadapan kawan-kawanmu."
        },
        "friendship": {
            "circle_role": "Jantung kehangatan pertemanan; orang yang selalu menyapa duluan di grup, merencanakan liburan bareng, dan memastikan semua kawan tetap saling terhubung.",
            "circle_style": "Punya lingkaran kawan yang luas dan erat; kamu memperlakukan sahabatmu seperti keluarga kandung sendiri."
        },
        "interaction_guide": {
            "do": [
                "Tunjukkan apresiasi dan ucapkan terima kasih atas perhatian tulusnya; kata-kata manis itu sangat berarti baginya.",
                "Bicaralah dengan nada ramah, santun, dan hargai perasaannya.",
                "Libatkan dia dalam acara sosial atau tanyakan pendapatnya seputar kenyamanan bersama."
            ],
            "dont": [
                "Jangan mengkritik usahanya secara kasar di hadapan orang lain tanpa memuji niat baiknya terlebih dahulu.",
                "Jangan mengabaikan pesan atau sapaan hangatnya dengan sikap dingin yang tidak beralasan.",
                "Jangan merusak suasana acara kumpul bersama dengan drama ego pribadi."
            ]
        },
        "stress_dynamics": "Saat merasa ditolak atau tidak dihargai oleh lingkungan sosialnya, kamu bisa merasa sangat terpuruk dan meragukan nilai dirimu. Cara recharge: cari lingkungan yang hangat dan suportif, curhat dengan sahabat paling terpercaya, dan istirahat dari urusan melayani orang lain.",
        "stress_recharge": {
            "burnout_triggers": [
                "Pengorbanan dan pelayanan tulusmu diabaikan atau bahkan dianggap sebagai hal yang biasa saja tanpa ada terima kasih.",
                "Konflik berkepanjangan antar orang-orang yang kamu cintai yang menolak untuk berdamai.",
                "Kritik pedas yang meremehkan kompetensi atau niat baikmu di depan umum."
            ],
            "stress_signals": [
                "Mengalami 'Ti inferior grip': tiba-tiba menjadi sangat kritis, mencari-cari kesalahan orang lain secara pedas, dan bersikap dingin.",
                "Merasa sangat kesepian dan yakin bahwa tidak ada seorang pun yang benar-benar peduli padanya.",
                "Tenggelam dalam siklus overthinking memikirkan di mana letak kesalahannya dalam bergaul."
            ],
            "recharge_remedy": [
                "Kunjungi sahabat atau anggota keluarga yang paling tulus menyayangimu dan biarkan mereka yang memanjakanmu hari ini.",
                "Matikan notifikasi grup sementara waktu dan fokuslah merawat dirimu sendiri (perawatan kulit, makan enak, tidur cukup).",
                "Ingatkan dirimu bahwa kebahagiaan orang lain bukanlah tanggung jawabmu sepenuhnya."
            ]
        },
        "color": "#0284C7",
        "temperament": "Pengawal (Sentinel / SJ)",
        "bg_tint": "#F0F9FF",
        "border_color": "#BAE6FD",
        "work_style": "Kamu adalah pekerja yang berdedikasi dan kooperatif. Kamu paling produktif saat bekerja dalam lingkungan tim yang saling menghargai dan punya kejelasan tugas yang teratur."
    },
    "ISTP": {
        "code": "ISTP",
        "archetype": "Sang Pengrajin Cekatan",
        "title": "ISTP · Sang Pengrajin Cekatan",
        "tagline": "Membedah dunia lewat aksi nyata, tenang dalam krisis tak terduga, dan selalu punya solusi praktis paling tak terduga.",
        "summary": "Kamu adalah pemecah masalah alami yang mengamati dunia dengan mata kritis dan tangan terampil. Kamu tenang, mandiri, tidak suka banyak bicara jika tidak perlu, tapi sangat tanggap saat terjadi situasi darurat yang membutuhkan tindakan cepat. Kamu belajar paling baik lewat praktik langsung dan paling tidak suka diikat oleh teori kaku yang tidak bisa diterapkan.",
        "avatar": "assets/avatars/istp.svg",
        "quick_dossier": {
            "superpower": "Respons Taktis Darurat, Logika Mekanis Praktis & Ketenangan di Bawah Tekanan",
            "love_language": "Bantuan Praktis, Kebersamaan Santai & Memberi Kebebasan Penuh",
            "pet_peeve": "Drama emosional berlebihan, orang yang banyak omong tapi nol tindakan, dan mikromanajemen",
            "emergency_recharge": "Waktu menyendiri mengutak-atik mesin, coding, merakit barang, atau olahraga motorik mandiri"
        },
        "cognitive_roles": {
            "dominant": "Ti (Akurasi Logika Mekanis): Nalurimu secara otomatis membedah cara kerja alat, sistem, atau situasi sampai ke komponen terkecilnya.",
            "auxiliary": "Se (Ketangkasan Sensorik Nyata): Refleks fisik dan inderamu sangat tajam membaca dinamika lingkungan seketika dan langsung bertindak tepat sasaran.",
            "tertiary": "Ni (Firasat & Pola Taktis): Di balik ketenanganmu, kamu punya insting bawah sadar yang tajam dalam memprediksi momen paling pas untuk melangkah.",
            "inferior": "Fe (Kepekaan Emosi Sosial): Kamu merasa serba salah dan sangat canggung saat harus merespons luapan drama emosional atau obrolan basa-basi sosial yang berbelit-belit."
        },
        "relatable_traits": {
            "daily_habits": [
                "Kalau barang elektronik atau perabot di rumah rusak, refleks pertamamu adalah membongkarnya sendiri sebelum panggil tukang servis.",
                "Di tongkrongan bicaranya paling santai dan irit kata-kata, tapi sekali nyeletuk komentarnya selalu tepat sasaran dan bikin ngakak.",
                "Paling tenang saat semua orang panik (misal: ban bocor di tengah jalan malam-malam, listrik padam, atau sistem mendadak eror).",
                "Suka belajar skill baru lewat coba-coba langsung (trial & error) daripada harus membaca buku manual tebal dari halaman pertama."
            ],
            "pet_peeves": [
                "Orang yang menceritakan masalah hidupnya sambil menangis histeris tapi menolak semua solusi praktis yang ditawarkan.",
                "Atasan atau rekan yang suka berdiri di belakangmu mengawasi setiap ketukan jarimu (mikromanajemen).",
                "Dipaksa membuat komitmen jangka panjang yang kaku dan mematikan kebebasan spontanitasmu."
            ],
            "flow_triggers": [
                "Membongkar dan memperbaiki sistem rumit (mesin motor, coding debug, perangkat keras, atau alat olahraga) sampai berfungsi sempurna.",
                "Melakukan aktivitas motorik yang menuntut fokus refleks tinggi (mengendarai motor di jalur menantang, panjat tebing, atau gaming taktis)."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Efisiensi pemecahan masalah tanpa tanding, ketenangan luar biasa di bawah tekanan krisis, dan kemampuan adaptasi fisik yang lincah.",
            "blindspots": "Cenderung terlalu cuek atau dingin terhadap perasaan orang lain, cepat bosan dengan rutinitas jangka panjang, dan enggan mengekspresikan komitmen emosional secara verbal.",
            "superpower_list": [
                "Ketepatan refleks taktis dalam mengatasi situasi darurat tanpa panik.",
                "Keahlian mendalam dalam memahami cara kerja fisik dan mekanis dari suatu sistem rumit.",
                "Kemandirian tinggi; tidak pernah merepotkan orang lain untuk urusan yang bisa diselesaikan sendiri."
            ],
            "blindspot_list": [
                "Kerap dianggap tidak peduli atau acuh tak acuh padahal sebenarnya hanya sedang fokus pada fakta teknis.",
                "Kecenderungan mengambil risiko fisik atau finansial yang impulsif saat merasa bosan.",
                "Sulit diajak berbicara serius mengenai perasaan dan rencana hubungan jangka panjang."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu adalah eksekutor taktis yang hemat energi. Kamu tidak suka membuang tenaga untuk formalitas; kamu mencari jalan pintas paling efisien untuk menuntaskan masalah.",
            "ideal_env": "Teknik mesin, software engineering, penerbangan, forensik, paramedis gawat darurat, arsitektur lanskap, atau operasi lapangan yang mengutamakan hasil nyata.",
            "team_role": "Troubleshooter lapangan; orang yang paling diandalkan saat rencana di atas kertas hancur dan butuh improvisasi darurat seketika."
        },
        "love_relationships": {
            "love_style": "Kamu tidak romantis dengan puisi atau kata-kata manis, tapi cintamu nyata dalam perbuatan. Kamu menunjukkan kasih sayang dengan memperbaiki barangnya yang rusak, mengantarnya dengan aman, dan memberinya ruang bernapas yang leluasa.",
            "green_flags": "Pasangan yang mandiri, santai, tidak suka drama, menghargai hobimu, dan tidak menuntut laporan chat setiap jam.",
            "red_flags": "Orang yang posesif, suka mengontrol, hobi mengetes kesetiaan dengan kode-kode berbelit, atau menuntutmu mengekspresikan cinta setiap hari."
        },
        "friendship": {
            "circle_role": "Teman nongkrong yang asyik tanpa tuntutan; kawan yang selalu siap diajak jalan dadakan, riding malam, atau sekadar duduk santai ngopi tanpa harus ngobrol non-stop.",
            "circle_style": "Pertemanan berbasis aktivitas bersama (shared hobbies); kamu lebih suka melakukan sesuatu bareng kawan daripada cuma duduk berjam-jam saling curhat."
        },
        "interaction_guide": {
            "do": [
                "Bicaralah secara ringkas, to the point, dan langsung ke akar masalah yang ingin diselesaikan.",
                "Beri dia ruang kebebasan dan jangan mendesaknya berbicara saat dia sedang butuh hening.",
                "Hargai keahlian praktisnya dan percayakan solusi teknis kepadanya tanpa banyak intervensi."
            ],
            "dont": [
                "Jangan memaksanya terlibat dalam gosip kantor atau drama pertemanan yang tidak ada gunanya.",
                "Jangan mencoba mendikte cara kerjanya; biarkan dia menemukan metodenya sendiri.",
                "Jangan menuntut janji emosional jangka panjang secara terburu-buru."
            ]
        },
        "stress_dynamics": "Saat tertekan oleh aturan yang mengekang dan beban emosi yang menumpuk, kamu bisa meledak secara emosional atau menjadi sangat impulsif. Cara recharge: menyendiri mengerjakan hobi mekanis atau fisik, matikan ponsel, dan nikmati waktu di alam tanpa ada yang mengatur.",
        "stress_recharge": {
            "burnout_triggers": [
                "Terperangkap dalam lingkungan yang terlalu banyak aturan birokrasi kaku dan minim ruang gerak.",
                "Tuntutan sosial yang memaksa untuk terus-menerus ramah tamah dan mengekspresikan emosi palsu.",
                "Konflik interpersonal yang berlarut-larut tanpa adanya solusi nyata."
            ],
            "stress_signals": [
                "Mengalami 'Fe inferior grip': tiba-tiba meledak secara emosional, merasa semua orang membencinya, atau bersikap sangat sinis pada norma sosial.",
                "Menjadi sangat ceroboh dan mengambil risiko berbahaya untuk mencari pelampiasan sensorik.",
                "Menghilang total tanpa kabar dan mematikan semua saluran komunikasi."
            ],
            "recharge_remedy": [
                "Lakukan aktivitas motorik mandiri: naik motor keliling kota di malam sepi, bersepeda di jalur alam, atau merakit PC/alat.",
                "Hindari pertemuan sosial dan habiskan satu hari penuh mengerjakan proyek fisik pribadimu.",
                "Istirahatkan pikiran dari urusan logika dengan menonton film aksi atau bermain game yang memuaskan refleksmu."
            ]
        },
        "color": "#D97706",
        "temperament": "Penjelajah (Artisan / SP)",
        "bg_tint": "#FFFBEB",
        "border_color": "#FDE68A",
        "work_style": "Kamu adalah eksekutor taktis yang hemat energi. Kamu tidak suka membuang tenaga untuk formalitas; kamu mencari jalan pintas paling efisien untuk menuntaskan masalah."
    },
    "ISFP": {
        "code": "ISFP",
        "archetype": "Sang Petualang Estetik",
        "title": "ISFP · Sang Petualang Estetik",
        "tagline": "Mengekspresikan keindahan rasa lewat karya nyata, lembut dalam kepedulian, dan menikmati pesona momen saat ini.",
        "summary": "Kamu adalah jiwa seniman yang membumi, lembut, dan menghargai keindahan dalam setiap detik kehidupan. Kamu punya kepekaan estetika alami dan memegang teguh kejujuran batinmu. Kamu tidak suka berkonflik, menyukai kebebasan ruang pribadi, ramah tanpa banyak menuntut, dan menunjukkan kasih sayang lewat tindakan nyata yang penuh rasa.",
        "avatar": "assets/avatars/isfp.svg",
        "quick_dossier": {
            "superpower": "Kepekaan Estetika, Empati Lembut & Spontanitas Bernyawa",
            "love_language": "Waktu Bersama yang Santai, Sentuhan Kasih & Kejutan Manis",
            "pet_peeve": "Penghakiman sepihak, kepalsuan, dan lingkungan yang kaku serta tidak ramah",
            "emergency_recharge": "Waktu santai di ruangan estetik, menikmati musik favorit, atau merawat karya seni tanpa dinilai"
        },
        "cognitive_roles": {
            "dominant": "Fi (Keaslian Nilai Batin): Panduan hidupmu adalah nurani yang jujur dan rasa hormat yang mendalam pada individualitas setiap manusia.",
            "auxiliary": "Se (Pengalaman Sensorik Indah): Inderamu sangat peka menikmati warna, rasa, tekstur, melodi, dan keindahan alam sekitar secara langsung.",
            "tertiary": "Ni (Firasat & Visi Tersembunyi): Kamu punya intuisi batin yang halus dalam merasakan arah perubahan dan makna tersirat di balik kejadian.",
            "inferior": "Te (Ketegasan Logika Objektif & Kritik Keras): Menghadapi konfrontasi argumen yang agresif, jadwal kaku, atau kritik dingin bisa membuatmu merasa terluka dan menutup diri."
        },
        "relatable_traits": {
            "daily_habits": [
                "Punya selera musik, gaya berpakaian, atau dekorasi kamar yang sangat khas dan mencerminkan suasana hatimu.",
                "Sering jalan santai sendirian sambil memotret hal-hal kecil yang indah di jalanan: kucing tidur, bayangan pohon, atau langit senja.",
                "Paling malas kalau diajak berdebat kusir yang cuma buang-buang energi; kamu lebih memilih mengalah atau menyingkir diam-diam.",
                "Bisa sangat asyik tenggelam dalam dunia seni, musik, atau kerajinan tangan sampai lupa waktu makan siang."
            ],
            "pet_peeves": [
                "Orang yang suka mengatur-atur penampilan, gaya hidup, atau pilihan pribadimu dengan standar mereka.",
                "Ketidakadilan, kekejaman terhadap hewan, atau orang yang meremehkan perasaan sesama.",
                "Lingkungan kerja yang penuh persaingan saling menjatuhkan dan minim empati kemanusiaan."
            ],
            "flow_triggers": [
                "Melukis, bermusik, memasak dengan sentuhan estetika, atau menata interior ruangan hingga terasa sangat nyaman dan berjiwa.",
                "Menikmati konser musik intim atau jalan-jalan santai di pantai saat matahari terbenam bersama orang terkasih."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Kehangatan empati yang tulus, kepekaan seni yang bernyawa, toleransi tinggi pada perbedaan, dan kemampuan menikmati keindahan saat ini.",
            "blindspots": "Cenderung menghindari konflik sampai merugikan diri sendiri, sulit membuat rencana jangka panjang yang kaku, dan mudah merasa rendah diri saat dikritik.",
            "superpower_list": [
                "Kemampuan alami menciptakan atmosfer yang hangat, santai, dan estetik di mana pun berada.",
                "Kebaikan hati yang tidak menghakimi dan menerima orang lain seutuhnya apa adanya.",
                "Kreativitas praktis yang sanggup mengubah benda biasa menjadi karya yang bernilai seni."
            ],
            "blindspot_list": [
                "Kerap memendam rasa sakit hati demi menghindari konfrontasi langsung dengan orang lain.",
                "Kesulitan menegakkan batasan tegas saat ada pihak yang memanfaatkan kebaikannya.",
                "Mudah menyerah pada komitmen jangka panjang jika suasana emosionalnya terasa tidak lagi sehat."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu bekerja dengan rasa dan sentuhan personal. Kamu membutuhkan otonomi dan atmosfer kerja yang santai agar inspirasi kreatifmu bisa mekar dengan indah.",
            "ideal_env": "Desain interior, tata busana, seni visual, kuliner kreatif, fotografi, kedokteran hewan, atau pekerjaan sosial yang membumi.",
            "team_role": "Penyelaras rasa dan penenang suasana; orang yang membawa kehangatan dan sentuhan artistik ke dalam hasil karya tim."
        },
        "love_relationships": {
            "love_style": "Kamu mencintai dengan penuh kelembutan dan kesetiaan yang tenang. Kamu menunjukkan kasih sayang lewat perlakuan manis sehari-hari, selalu mendampingi di masa sulit, dan menerima pasangan seutuhnya.",
            "green_flags": "Pasangan yang lembut, setia, menghargai keunikanmu, tidak suka memaksakan kehendak, dan bisa menikmati keheningan yang nyaman bersamamu.",
            "red_flags": "Orang yang suka membentak, agresif secara verbal, suka mengkritik penampilanmu, atau membatasi kebebasan berekspresimu."
        },
        "friendship": {
            "circle_role": "Kawan yang paling menenangkan dan tidak pernah menghakimi; teman yang selalu asyik diajak nongkrong santai, berburu kuliner enak, atau menikmati seni bersama.",
            "circle_style": "Lingkaran pertemananmu santai dan hangat; kamu lebih menghargai kenyamanan rasa daripada status sosial atau popularitas."
        },
        "interaction_guide": {
            "do": [
                "Bicaralah dengan nada ramah dan sampaikan masukan secara halus empat mata.",
                "Apresiasi sentuhan estetika dan karya yang dia hasilkan dengan penuh ketulusan.",
                "Beri dia kebebasan untuk mengambil keputusan sesuai dengan apa yang terasa benar di hatinya."
            ],
            "dont": [
                "Jangan membentak atau menggunakan nada suara tinggi yang mengintimidasi perasaannya.",
                "Jangan memaksanya terlibat dalam perdebatan logika yang agresif dan menyudutkannya.",
                "Jangan meremehkan kebiasaannya menikmati waktu santai sebagai bentuk kemalasan."
            ]
        },
        "stress_dynamics": "Saat kewalahan oleh konflik atau kritik pedas, kamu bisa merasa terpuruk dan sangat rapuh. Cara recharge: cari perlindungan di tempat yang aman dan estetik, putar musik yang menenangkan, dan buat karya seni tanpa memikirkan hasilnya.",
        "stress_recharge": {
            "burnout_triggers": [
                "Terjebak dalam lingkungan yang penuh teriakan, konflik panas, dan saling serang.",
                "Kritik pedas yang meruntuhkan rasa percaya diri dan menolak sentuhan kreatifnya.",
                "Tuntutan jadwal yang terlalu padat dan menuntut kepatuhan kaku tanpa ada jeda bernapas."
            ],
            "stress_signals": [
                "Mengalami 'Te inferior grip': tiba-tiba menjadi sangat reaktif, melontarkan kritik keras dan menyalahkan orang lain secara kasar.",
                "Merasa kehilangan harapan dan yakin bahwa dirinya tidak memiliki bakat atau masa depan.",
                "Menarik diri ke dalam kamar dan menolak makan atau merawat diri secara wajar."
            ],
            "recharge_remedy": [
                "Habiskan waktu bersama hewan peliharaan atau jalan-jalan santai di tengah rimbunnya pepohonan alam.",
                "Ciptakan sesuatu dengan tanganmu sendiri (memasak makanan enak, melukis, atau merangkai tanaman).",
                "Izinkan dirimu menangis untuk melepaskan beban emosi yang menumpuk tanpa merasa lemah."
            ]
        },
        "color": "#EA580C",
        "temperament": "Penjelajah (Artisan / SP)",
        "bg_tint": "#FFFBEB",
        "border_color": "#FDE68A",
        "work_style": "Kamu bekerja dengan rasa dan sentuhan personal. Kamu membutuhkan otonomi dan atmosfer kerja yang santai agar inspirasi kreatifmu bisa mekar dengan indah."
    },
    "ESTP": {
        "code": "ESTP",
        "archetype": "Sang Pengusaha Dinamis",
        "title": "ESTP · Sang Pengusaha Dinamis",
        "tagline": "Melangkah berani di garis terdepan, menangkap peluang seketika, dan mengubah tantangan jadi kemenangan nyata.",
        "summary": "Kamu adalah sosok yang penuh energi, berani ambil risiko, dan punya karisma panggung yang memukau. Kamu hidup seutuhnya di momen saat ini; kamu tidak suka berlama-lama terjebak dalam teori abstrak yang bertele-tele. Kamu membaca situasi lapangan dengan sangat cepat, tangkas bernegosiasi, luwes menyelesaikan krisis nyata, dan selalu menikmati adrenalin tantangan.",
        "avatar": "assets/avatars/estp.svg",
        "quick_dossier": {
            "superpower": "Reaksi Taktis Seketika, Negosiasi Lapangan & Keberanian Ambil Risiko",
            "love_language": "Petualangan Seru, Aksi Nyata Spontan & Menikmati Momen Berdua",
            "pet_peeve": "Teori berbelit tanpa aksi nyata, kelambatan birokrasi, dan aturan kaku yang menghambat hasil",
            "emergency_recharge": "Olahraga beradrenalin tinggi, kumpul seru bareng kawan aktif, atau perjalanan spontan"
        },
        "cognitive_roles": {
            "dominant": "Se (Ketangkasan Aksi & Peluang Nyata): Nalurimu menangkap peluang nyata seketika, membaca bahasa tubuh audiens, dan bertindak cepat tanpa ragu.",
            "auxiliary": "Ti (Logika Taktis & Efisiensi): Setiap tindakan spontanmu disaring oleh pertimbangan logika yang tajam untuk memastikan langkahmu memberi hasil paling optimal.",
            "tertiary": "Fe (Karisma & Pesona Sosial): Kamu punya daya tarik alami yang supel, humoris, dan mudah membuat orang lain merasa senang berada di dekatmu.",
            "inferior": "Ni (Visi Abstrak Jangka Panjang): Menghadapi analisis filosofis mendalam yang rumit atau dipaksa memikirkan skenario abstrak 10 tahun ke depan bisa bikin kamu merasa jenuh dan cemas."
        },
        "relatable_traits": {
            "daily_habits": [
                "Paling tidak betah duduk diam mendengarkan ceramah atau kuliah panjang tanpa ada praktik langsungnya.",
                "Kalau diajak pergi liburan atau tanding olahraga dadakan, jawabanmu hampir selalu 'Gas, berangkat sekarang!'.",
                "Punya insting negosiasi yang luar biasa; bisa menawar barang atau meyakinkan orang lain dengan santai sambil tersenyum.",
                "Belajar paling cepat dari kesalahan langsung di lapangan daripada harus membaca teori dari buku teks tebal."
            ],
            "pet_peeves": [
                "Orang yang terlalu banyak overthinking dan menganalisis hal sepele sampai peluang emas di depan mata hilang.",
                "Rapat berjam-jam yang cuma mendiskusikan konsep tanpa ada satu pun keputusan tindakan nyata yang diambil.",
                "Dilarang mencoba sesuatu yang baru cuma karena 'belum ada contoh preseden sebelumnya'."
            ],
            "flow_triggers": [
                "Menutup kesepakatan bisnis penting (closing deals) atau menyelesaikan masalah darurat di lapangan yang menuntut kecepatan berpikir.",
                "Berolahraga kompetitif yang memicu adrenalin tinggi dan menuntut respons fisik seketika."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Keberanian bertindak tanpa gentar, kecerdasan taktis di situasi krisis, karisma sosial yang persuasif, dan ketangkasan membaca momentum.",
            "blindspots": "Cenderung bertindak impulsif tanpa memikirkan konsekuensi jangka panjang, cepat bosan dengan rutinitas pemeliharaan, dan terkadang terkesan tidak peka pada perasaan orang lain.",
            "superpower_list": [
                "Keberanian mengambil keputusan berisiko tinggi dengan perhitungan taktis yang cepat dan tepat.",
                "Karisma komunikasi yang meyakinkan dan sanggup menghidupkan suasana di mana pun berada.",
                "Daya tahan tinggi menghadapi stres di garis depan operasional tanpa mudah panik."
            ],
            "blindspot_list": [
                "Kerap meremehkan risiko jangka panjang demi mengejar kepuasan atau hasil instan hari ini.",
                "Bisa melukai perasaan rekan yang lebih sensitif dengan gaya bicara yang terlalu blak-blakan.",
                "Kesulitan menjaga komitmen pada tugas administratif rutin yang membosankan."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu adalah eksekutor berorientasi hasil cepat. Kamu menyukai tantangan dinamis, persaingan sehat, dan imbalan nyata yang sepadan dengan kinerjamu.",
            "ideal_env": "Penjualan (sales), kewirausahaan, trading, manajemen krisis, paramedis darurat, atletik, atau pemasaran lapangan yang dinamis.",
            "team_role": "Pemberi gebrakan dan pengambil risiko; orang yang mendorong tim berani keluar dari zona nyaman dan mengeksekusi peluang."
        },
        "love_relationships": {
            "love_style": "Cinta bagimu harus seru, penuh tawa, dan bersemangat. Kamu menunjukkan cinta lewat mengajak pasangan menikmati pengalaman hidup terbaik, memanjakannya dengan aksi nyata, dan menjadi pelindung yang berani.",
            "green_flags": "Pasangan yang percaya diri, mandiri, suka petualangan, punya selera humor santai, dan tidak mudah cemas berlebihan.",
            "red_flags": "Orang yang terlalu posesif, suka mengontrol setiap gerak-gerikmu, atau hobi membuat drama emosional yang menguras energi."
        },
        "friendship": {
            "circle_role": "Pusat keseruan tongkrongan; kawan yang selalu punya ide gila buat liburan, olahraga bareng, dan membela teman saat ada masalah di luar.",
            "circle_style": "Punya jaringan pertemanan yang sangat luas di berbagai tempat; kamu mudah akrab dengan siapa saja dari kalangan mana pun."
        },
        "interaction_guide": {
            "do": [
                "Bicaralah secara santai, langsung ke poin utama, dan fokus pada apa yang bisa segera dikerjakan sekarang.",
                "Ikutlah menikmati keseruan bersamanya dan jangan ragu mengutarakan pikiranmu secara terbuka.",
                "Hargai keberanian dan ketangkasannya dalam menyelesaikan masalah lapangan."
            ],
            "dont": [
                "Jangan mengikatnya dengan teori abstrak yang bertele-tele tanpa contoh aplikatif.",
                "Jangan mencoba membatasinya dengan aturan mikromanajemen yang mengekang geraknya.",
                "Jangan membicarakan drama emosional yang berputar-putar tanpa menawarkan solusi tindakan."
            ]
        },
        "stress_dynamics": "Saat terkungkung dalam situasi monoton tanpa aksi nyata dan dihadapkan pada ketidakpastian yang mengambang, kamu bisa merasa cemas dan curiga pada orang lain. Cara recharge: olahraga fisik intensif, ubah suasana lingkungan, dan ambil aksi nyata kecil yang segera membuahkan hasil.",
        "stress_recharge": {
            "burnout_triggers": [
                "Terjebak di ruangan tertutup mengerjakan administrasi kertas yang monoton berhari-hari.",
                "Dilarang mengambil aksi nyata dan dipaksa menunggu keputusan birokrasi yang lambat.",
                "Menghadapi kegagalan besar yang membuatmu merasa kehilangan kendali atas momentum hidupmu."
            ],
            "stress_signals": [
                "Mengalami 'Ni inferior grip': tiba-tiba diliputi rasa curiga bahwa ada konspirasi atau orang lain berniat menjatuhkannya.",
                "Kehilangan rasa percaya diri dan membayangkan skenario masa depan yang gelap dan buntu.",
                "Menjadi sangat gelisah, sulit tidur, dan melampiaskan stres pada perilaku impulsif yang berisiko."
            ],
            "recharge_remedy": [
                "Keluarkan energi fisik yang tertumpuk: bermain futsal, tinju, angkat beban, atau berenang.",
                "Pergilah keluar ke tempat terbuka yang ramai dan nikmati suasana dinamis sekitar untuk mengalihkan pikiran.",
                "Fokuslah pada satu kemenangan taktis kecil hari ini untuk memulihkan kembali rasa percaya dirimu."
            ]
        },
        "color": "#C2410C",
        "temperament": "Penjelajah (Artisan / SP)",
        "bg_tint": "#FFFBEB",
        "border_color": "#FDE68A",
        "work_style": "Kamu adalah eksekutor berorientasi hasil cepat. Kamu menyukai tantangan dinamis, persaingan sehat, dan imbalan nyata yang sepadan dengan kinerjamu."
    },
    "ESFP": {
        "code": "ESFP",
        "archetype": "Sang Penghibur Karismatik",
        "title": "ESFP · Sang Penghibur Karismatik",
        "tagline": "Menghidupkan setiap ruangan dengan tawa dan energi positif, hangat merangkul sesama, dan merayakan indahnya kebersamaan.",
        "summary": "Kamu adalah sosok yang penuh pesona, ramah, dan punya energi positif yang memancar secara alami. Kamu mencintai kehidupan dan senang berbagi kebahagiaan dengan orang-orang di sekitarmu. Kamu tidak tahan melihat suasana canggung atau murung; nalurimu selalu tergerak untuk membuat semua orang tersenyum, merasa nyaman, dan menikmati momen kebersamaan saat ini.",
        "avatar": "assets/avatars/esfp.svg",
        "quick_dossier": {
            "superpower": "Karisma Sosial Memikat, Keceriaan Spontan & Kepekaan Panggung",
            "love_language": "Perhatian Hangat, Waktu Bersenang-senang Bersama & Kejutan Manis",
            "pet_peeve": "Suasana muram kaku, orang yang suka menghakimi keceriaan orang lain, dan kemonotonan",
            "emergency_recharge": "Kumpul seru dengan sahabat terdekat yang suportif, mendengarkan musik asyik, atau belanja/manjakan diri"
        },
        "cognitive_roles": {
            "dominant": "Se (Pengalaman Sensorik & Semangat Spontan): Nalurimu selalu hadir penuh di momen sekarang, menyerap keindahan dan energi di sekelilingmu.",
            "auxiliary": "Fi (Nilai & Kehangatan Rasa): Keceriaanmu berakar dari hati yang tulus; kamu ingin semua orang merasa diterima tanpa perlu berpura-pura.",
            "tertiary": "Te (Ketegasan Aksi Praktis): Saat keadaan menuntut, kamu bisa bersikap tegas dan mencari solusi praktis untuk membantu kawan yang sedang kesusahan.",
            "inferior": "Ni (Visi Filosofis & Ramalan Masa Depan): Memikirkan konsekuensi abstrak yang rumit atau dipaksa merencanakan hidup secara kaku bisa memicu rasa cemas yang membingungkan."
        },
        "relatable_traits": {
            "daily_habits": [
                "Paling pertama yang mencairkan suasana saat kumpul keluarga atau kantor terasa kaku dan garing.",
                "Gaya pakaian atau aksesorismu selalu menarik perhatian dan kamu punya bakat alami tampil fotogenik.",
                "Tidak tahan berada di ruangan sepi terlalu lama; kamu butuh musik yang menyala atau suara obrolan agar merasa hidup.",
                "Sangat murah hati; suka mentraktir teman atau membelikan oleh-oleh lucu saat pulang dari bepergian."
            ],
            "pet_peeves": [
                "Orang yang suka mengeluh dan menyebarkan aura negatif ke mana pun mereka pergi.",
                "Acara kumpul yang dipenuhi orang-orang sok jaim (jaga image) dan sibuk bermain ponsel sendiri-sendiri.",
                "Dilarang mengekspresikan kegembiraan dan dipaksa bersikap kaku tanpa alasan yang jelas."
            ],
            "flow_triggers": [
                "Tampil di atas panggung, bernyanyi, memandu acara (MC), atau menghibur audiens dan melihat mereka tertawa lepas.",
                "Merencanakan pesta kejutan atau liburan seru bareng sahabat dan melihat semua orang menikmati setiap detiknya."
            ]
        },
        "strengths_blindspots": {
            "strengths": "Karisma interpersonal yang luar biasa, keberanian berekspresi, kemurahan hati yang tulus, dan kemampuan membuat hidup terasa berwarna.",
            "blindspots": "Cenderung menghindari pembicaraan serius atau konflik yang tidak menyenangkan, mudah tergoda belanja impulsif, dan kesulitan membuat perencanaan jangka panjang.",
            "superpower_list": [
                "Kemampuan luar biasa menyebarkan kebahagiaan dan mencairkan kebekuan sosial seketika.",
                "Kecerdasan estetika dan daya tarik panggung yang membuat orang lain terpikat.",
                "Ketulusan hati dalam merangkul orang yang sedang merasa kesepian atau tersisihkan."
            ],
            "blindspot_list": [
                "Kecenderungan menolak melihat tanda-tanda bahaya masa depan demi menjaga suasana hati tetap senang hari ini.",
                "Bisa merasa sangat terluka dan kehilangan percaya diri jika merasa diabaikan oleh lingkungannya.",
                "Kesulitan mempertahankan disiplin anggaran keuangan karena sifatnya yang impulsif dan royal."
            ]
        },
        "career_work": {
            "work_ethic": "Kamu adalah pekerja yang bersemangat dan interaktif. Kamu paling produktif dalam lingkungan yang dinamis, kolaboratif, dan melibatkan interaksi langsung dengan manusia.",
            "ideal_env": "Industri hiburan, perhotelan, pramugari/pramugara, event organizer, pemasaran media sosial, public relations, atau konseling anak.",
            "team_role": "Penyemarak energi dan duta hubungan masyarakat; orang yang menjaga moral tim tetap tinggi dan membangun relasi hangat dengan klien."
        },
        "love_relationships": {
            "love_style": "Kamu mencintai dengan penuh gairah, keceriaan, dan kemurahan hati. Kamu selalu ingin membuat pasangan merasa bahagia, dimanjakan dengan hadiah manis, dan menikmati petualangan hidup berdua.",
            "green_flags": "Pasangan yang ekspresif memuji, suka bersenang-senang bareng, setia, dan bisa menjadi pendengar yang aman saat kamu sedang merasa sedih.",
            "red_flags": "Orang yang pelit, suka mengkritik sifat ramahmu dengan rasa cemburu buta, atau selalu menuntutmu bersikap serius sepanjang waktu."
        },
        "friendship": {
            "circle_role": "Bintang pergaulan dan sahabat yang paling seru diajak ke mana saja; orang yang selalu memastikan kawan-kawannya tidak pernah merasa bosan.",
            "circle_style": "Memiliki lingkaran sahabat yang sangat luas dan beragam; kamu selalu menyambut siapa saja dengan tangan terbuka dan senyuman hangat."
        },
        "interaction_guide": {
            "do": [
                "Tunjukkan apresiasi dan tertawalah bersamanya; dia sangat senang saat usahanya menghibur dihargai.",
                "Bicaralah dengan nada ceria, santai, dan penuh kehangatan emosional.",
                "Ajaklah dia menikmati aktivitas seru di luar ruangan atau mencoba kuliner baru bersama."
            ],
            "dont": [
                "Jangan mengabaikan kehadirannya atau bersikap cuek saat dia sedang berusaha ramah kepadamu.",
                "Jangan memaksanya mendengarkan kuliah teori abstrak yang membosankan.",
                "Jangan mengkritik sifat spontan atau gaya berpakaiannya di hadapan orang lain."
            ]
        },
        "stress_dynamics": "Saat merasa terisolasi, ditolak, atau menghadapi beban hidup yang berat tanpa pelarian positif, kamu bisa merasa cemas dan putus asa. Cara recharge: kumpul santai dengan orang terkasih yang tulus, manjakan dirimu dengan perawatan tubuh, dan dengarkan lagu-lagu ceria favoritmu.",
        "stress_recharge": {
            "burnout_triggers": [
                "Terisolasi sendirian dalam jangka waktu lama tanpa ada interaksi manusiawi yang hangat.",
                "Konflik berkepanjangan dengan orang yang dicintai yang menolak diajak bicara secara baik-baik.",
                "Kritik pedas yang meruntuhkan rasa percaya dirinya dan membuatnya merasa tidak diinginkan."
            ],
            "stress_signals": [
                "Mengalami 'Ni inferior grip': tiba-tiba merasa sangat cemas bahwa masa depannya hancur dan diliputi pikiran negatif yang suram.",
                "Kehilangan senyuman cerianya, menjadi pendiam, dan menarik diri ke tempat tidur seharian.",
                "Merasa sangat rendah diri dan yakin bahwa orang-orang hanya berpura-pura baik kepadanya."
            ],
            "recharge_remedy": [
                "Temui sahabat terdekat yang paling bisa membuatmu tertawa dan tumpahkan semua unek-unekmu sambil berpelukan.",
                "Manjakan inderamu: makan makanan favorit yang lezat, dengarkan musik up-beat, atau jalan-jalan santai di mall/taman.",
                "Ingatkan dirimu bahwa hari buruk bukan berarti hidup yang buruk; esok hari selalu membawa peluang baru yang menyenangkan."
            ]
        },
        "color": "#D97706",
        "temperament": "Penjelajah (Artisan / SP)",
        "bg_tint": "#FFFBEB",
        "border_color": "#FDE68A",
        "work_style": "Kamu adalah pekerja yang bersemangat dan interaktif. Kamu paling produktif dalam lingkungan yang dinamis, kolaboratif, dan melibatkan interaksi langsung dengan manusia."
    }
}


def get_profile(mbti_code: str) -> Dict:
    code = (mbti_code or '').upper().strip()
    return PROFILES.get(code, {
        'code': code,
        'archetype': 'Kepribadian Adaptif',
        'title': f'{code} · Kepribadian Adaptif',
        'tagline': 'Profil hasil evaluasi arsitektur kognitif yang memetakan caramu berpikir dan bertindak.',
        'summary': 'Kombinasi proses berpikir dan orientasi adaptasi yang memandu tindakanmu sehari-hari.',
        'avatar': 'assets/avatars/intj.svg',
        'quick_dossier': {
            'superpower': 'Adaptasi Kognitif Mandiri',
            'love_language': 'Kejujuran & Waktu Berkualitas',
            'pet_peeve': 'Ketidakteraturan & Asumsi Tanpa Dasar',
            'emergency_recharge': 'Waktu hening dan istirahat tanpa gangguan'
        },
        'cognitive_roles': {
            'dominant': 'Fungsi utama yang memandu keputusan sadar sehari-hari.',
            'auxiliary': 'Pemandu pendukung yang bikin kamu tetap seimbang.',
            'tertiary': 'Sisi santai yang muncul pas lagi rileks.',
            'inferior': 'Sisi yang paling rentan capek atau bikin overthinking saat stres berat.'
        },
        'relatable_traits': {
            'daily_habits': ['Mengambil jeda sebelum memutuskan hal penting.'],
            'pet_peeves': ['Janji yang tidak ditepati tanpa kejelasan.'],
            'flow_triggers': ['Menuntaskan tantangan praktis dengan fokus penuh.']
        },
        'strengths_blindspots': {
            'strengths': 'Kapasitas adaptif dalam menyelesaikan tantangan nyata.',
            'blindspots': 'Area kerentanan yang perlu kamu perhatikan secara sadar.',
            'superpower_list': ['Ketahanan dan pemecahan masalah.'],
            'blindspot_list': ['Kelelahan saat memaksakan diri tanpa jeda.']
        },
        'career_work': {
            'work_ethic': 'Gaya kerja yang seimbang antara otonomi dan kolaborasi.',
            'ideal_env': 'Lingkungan yang transparan dan menghargai hasil nyata.',
            'team_role': 'Kontributor andal dalam pemecahan masalah.'
        },
        'love_relationships': {
            'love_style': 'Membangun koneksi saling percaya dan suportif.',
            'green_flags': 'Keterbukaan emosional dan saling menghargai waktu.',
            'red_flags': 'Ketidakjujuran dan sikap pasif-agresif.'
        },
        'friendship': {
            'circle_role': 'Sahabat setia yang siap mendengarkan.',
            'circle_style': 'Lingkaran pertemanan yang hangat dan bermakna.'
        },
        'interaction_guide': {
            'do': ['Berkomunikasi lugas dan saling menghargai.'],
            'dont': ['Memaksa atau mengabaikan batasan pribadi.']
        },
        'work_style': 'Gaya kerja yang seimbang antara otonomi dan kolaborasi.',
        'stress_dynamics': 'Manajemen energi yang sehat dan ruang pemulihan yang cukup.',
        'stress_recharge': {
            'burnout_triggers': ['Kelebihan beban mental atau interaksi berlebihan.'],
            'stress_signals': ['Menarik diri atau merasa kewalahan.'],
            'recharge_remedy': ['Istirahat tenang di ruang nyaman tanpa tuntutan.']
        },
        'color': '#4F46E5',
        'temperament': 'Tipologi kognitif',
        'bg_tint': '#EEF2FF',
        'border_color': '#C7D2FE'
    })


def get_all_profiles() -> Dict[str, Dict]:
    return PROFILES


_AVATAR_CACHE: Dict[str, str] = {}


def get_avatar_base64(mbti_code: str) -> str:
    code = mbti_code.lower().strip()
    if code in _AVATAR_CACHE:
        return _AVATAR_CACHE[code]

    file_path = os.path.join(os.path.dirname(__file__), 'assets', 'avatars', f'{code}.svg')
    if not os.path.exists(file_path):
        return ''

    try:
        with open(file_path, 'rb') as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
            _AVATAR_CACHE[code] = encoded
            return encoded
    except Exception:
        return ''
