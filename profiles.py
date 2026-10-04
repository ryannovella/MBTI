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
        "cognitive_roles": {
            "dominant": "Ni (Visi & Pola Masa Depan): Nalurimu tajam menghubungkan titik-titik fakta menjadi gambaran masa depan yang jelas. Kamu sering 'tahu' arah mana yang paling masuk akal sebelum orang lain menyadarinya.",
            "auxiliary": "Te (Logika & Eksekusi Praktis): Kamu nggak cuma bermimpi; kamu mengatur langkah konkret, waktu, dan sumber daya secara terstruktur biar rencanamu benar-benar terwujud di dunia nyata.",
            "tertiary": "Fi (Nilai & Prinsip Personal): Di balik penampilan luarmu yang tenang dan analitis, kamu punya kompas moral pribadi yang sangat dalam dan hanya kamu bagikan ke orang-orang terdekat.",
            "inferior": "Se (Sensorik Seketika): Mengingat kamu sering tenggelam di dunia pikiran, lingkungan yang terlalu bising, ramai, atau penuh kekacauan fisik bisa bikin energimu cepat terkuras habis."
        },
        "strengths_blindspots": {
            "strengths": "Punya visi jangka panjang yang tajam, sangat mandiri dalam berpikir, dan cepat menemukan solusi sistemik saat terjadi inefisiensi yang bikin macet pekerjaan.",
            "blindspots": "Kadang terlalu perfeksionis, kurang sabar saat orang lain butuh waktu adaptasi lebih lama, dan sering lupa bahwa komunikasi yang hangat itu penting dalam kerja tim."
        },
        "work_style": "Paling produktif saat diberi kepercayaan penuh dan otonomi tanpa mikromanajemen. Kamu menyukai komunikasi tertulis yang jelas, target terukur, dan waktu hening buat fokus mendalam.",
        "stress_dynamics": "Saat burnout parah, kamu bisa tiba-tiba jadi gampang kesal sama detail kecil atau malah overthinking hal-hal sepele. Cara paling pas buat recharge: sediakan waktu sendiri yang tenang, kurangi komitmen sosial sementara, dan tulis unek-unekmu di catatan pribadi.",
        "color": "#4338CA",
        "temperament": "Analis (Rational / NT)",
        "bg_tint": "#EEF2FF",
        "border_color": "#C7D2FE"
    },
    "INTP": {
        "code": "INTP",
        "archetype": "Sang Pemikir Logis",
        "title": "INTP · Sang Pemikir Logis",
        "tagline": "Menemukan kebenaran di balik teka-teki rumit, membedah ide dari berbagai sudut, dan selalu penasaran sama cara kerja dunia.",
        "summary": "Otakmu ibarat laboratorium ide yang nggak pernah tidur. Kamu suka membedah konsep sampai ke akar-akarnya, mencari celah logika yang sering dilewatkan orang lain, dan merangkai penjelasan yang elegan. Kamu nggak gampang percaya sama aturan kaku sebelum kamu sendiri yang menguji apakah aturan itu masuk akal dan konsisten.",
        "avatar": "assets/avatars/intp.svg",
        "cognitive_roles": {
            "dominant": "Ti (Akurasi Logika Internal): Standar logikamu sangat tinggi. Kamu otomatis memeriksa apakah setiap argumen dan ide itu konsisten, jujur secara intelektual, dan bebas dari kontradiksi.",
            "auxiliary": "Ne (Eksplorasi Kemungkinan): Pikiranmu senang melompat ke berbagai cabang ide baru, menghubungkan topik yang kelihatannya nggak nyambung, dan menikmati proses eksplorasi 'gimana kalau begini?'.",
            "tertiary": "Si (Rujukan Data & Pengalaman): Kamu mengumpulkan referensi fakta dan pengalaman masa lalu sebagai bahan bakar pembanding saat menganalisis topik baru.",
            "inferior": "Fe (Kepekaan Emosi Sosial): Kamu kadang merasa canggung atau serba salah saat harus membaca kode sosial yang berbelit-belit atau menghadapi luapan emosi orang lain yang nggak logis."
        },
        "strengths_blindspots": {
            "strengths": "Kemampuan luar biasa memecahkan masalah rumit, objektif tanpa bias emosional, dan sangat terbuka terhadap sudut pandang alternatif yang segar.",
            "blindspots": "Kerap terjebak dalam siklus overthinking (analysis paralysis) sampai menunda eksekusi nyata, dan malas mengurusi urusan administrasi rutin yang membosankan."
        },
        "work_style": "Nyaman di lingkungan fleksibel yang menghargai kebebasan intelektual. Kamu butuh ruang buat bereksperimen dengan berbagai pendekatan sebelum memutuskan cara eksekusi final.",
        "stress_dynamics": "Kalau lagi stres berat, kamu bisa merasa terasing, frustrasi karena merasa orang lain nggak paham, atau tiba-tiba sensitif soal penerimaan sosial. Cara recharge: cari topik baru yang bikin kamu penasaran tanpa ada tenggat waktu yang menekan.",
        "color": "#4F46E5",
        "temperament": "Analis (Rational / NT)",
        "bg_tint": "#EEF2FF",
        "border_color": "#C7D2FE"
    },
    "ENTJ": {
        "code": "ENTJ",
        "archetype": "Sang Komandan Visioner",
        "title": "ENTJ · Sang Komandan Visioner",
        "tagline": "Mengubah ide ambisius jadi kenyataan nyata lewat ketegasan, strategi terarah, dan kepemimpinan yang berani ambil risiko.",
        "summary": "Kamu punya energi alami untuk memimpin dan menyelesaikan sesuatu. Saat melihat kekacauan atau inefisiensi, nalurimu langsung terpicu untuk merapikannya dan mengarahkan tim menuju target yang jelas. Kamu lugas, menghargai waktu, percaya diri mengambil keputusan sulit, dan selalu terdorong untuk mencapai hasil terbaik.",
        "avatar": "assets/avatars/entj.svg",
        "cognitive_roles": {
            "dominant": "Te (Efisiensi & Kepemimpinan Nyata): Naluri utamamu adalah menertibkan situasi, membagi tugas secara adil, dan memastikan semua orang bergerak menuju target yang jelas dan terukur.",
            "auxiliary": "Ni (Arah Visi Strategis): Kamu selalu punya pandangan beberapa langkah ke depan. Intuisi strategismu memandu ke mana organisasi atau proyek harus diarahkan agar relevan dalam jangka panjang.",
            "tertiary": "Se (Ketangkasan Aksi Nyata): Kamu responsif membaca peluang di lapangan dan berani mengambil langkah taktis saat momentumnya tepat tanpa ragu-ragu.",
            "inferior": "Fi (Ruang Hati & Refleksi Batin): Karena terbiasa fokus pada hasil, kamu rentan menekan rasa lelah batin sendiri atau mengabaikan kebutuhan emosional sampai tubuhmu protes."
        },
        "strengths_blindspots": {
            "strengths": "Ketegasan mengambil keputusan di masa krisis, kemampuan komunikasi yang meyakinkan, dan daya dorong tinggi untuk menyelesaikan proyek ambisius tepat waktu.",
            "blindspots": "Terkadang terkesan terlalu dominan atau kurang sabar menghadapi rekan kerja yang butuh ritme lebih perlahan, serta jarang memberi jeda istirahat untuk diri sendiri."
        },
        "work_style": "Unggul di lingkungan yang dinamis dengan tanggung jawab yang jelas. Menyukai pertemuan yang to-the-point, laporan berbasis data nyata, dan rekan kerja yang berkomitmen tinggi.",
        "stress_dynamics": "Saat kelelahan mental memuncak, kamu bisa jadi sangat mengontrol hal-hal kecil atau merasa kehilangan arah makna. Cara recharge: delegasikan tugas, luangkan waktu buat olahraga fisik intensif, dan istirahat dari urusan koordinasi kerjaan.",
        "color": "#3730A3",
        "temperament": "Analis (Rational / NT)",
        "bg_tint": "#EEF2FF",
        "border_color": "#C7D2FE"
    },
    "ENTP": {
        "code": "ENTP",
        "archetype": "Sang Pendebat Inovatif",
        "title": "ENTP · Sang Pendebat Inovatif",
        "tagline": "Menantang ide-ide lama dengan humor cerdas, melihat peluang di mana-mana, dan selalu punya cara tak terduga buat mecahin masalah.",
        "summary": "Bagi kamu, hidup terlalu seru buat diisi dengan hal-hal yang monoton. Kamu suka menguji asumsi orang lain lewat diskusi cerdas, menghubungkan ide-ide acak jadi terobosan baru, dan paling bersemangat saat memulai proyek yang menantang kreativitas. Kamu lincah, berani mencoba cara baru, dan nggak takut beda dari arus utama.",
        "avatar": "assets/avatars/entp.svg",
        "cognitive_roles": {
            "dominant": "Ne (Eksplorasi Peluang Baru): Matamu selalu melihat kemungkinan segar di setiap situasi. Kamu suka membongkar kebiasaan lama dan menciptakan alternatif yang lebih menarik.",
            "auxiliary": "Ti (Uji Logika Kritis): Setiap ide liar yang muncul langsung disaring oleh naluri analisismu untuk memastikan bahwa konsep tersebut punya dasar logika yang kokoh.",
            "tertiary": "Fe (Koneksi & Diplomasi Santai): Kamu punya karisma humoris dan luwes membaca audiens, membuat diskusi yang rumit jadi terasa seru dan hidup.",
            "inferior": "Si (Kepatuhan Rutinitas): Tugas-tugas administratif yang berulang, membosankan, dan minim ruang kreasi adalah hal yang paling cepat bikin energimu drop."
        },
        "strengths_blindspots": {
            "strengths": "Kecerdasan adaptasi yang tinggi, lihai memecahkan kebuntuan ide, dan kemampuan retorika persuasif yang sanggup membuka wawasan baru bagi orang lain.",
            "blindspots": "Cepat bosan saat proyek sudah masuk ke tahap pemeliharaan rutin, dan kadang terlalu asyik mendebat hal-hal kecil sampai orang lain merasa tersudut."
        },
        "work_style": "Paling bersinar dalam fase inisiasi proyek, riset inovasi, strategi produk, atau sesi brainstorming lepas. Butuh fleksibilitas jam kerja dan lingkungan yang merayakan pertukaran gagasan.",
        "stress_dynamics": "Saat terkungkung oleh aturan birokrasi yang kaku, kamu bisa jadi sinis dan kehilangan motivasi. Cara recharge: ngobrol santai tanpa agenda sama teman yang sefrekuensi, atau coba hobi baru yang menantang rasa ingin tahumu.",
        "color": "#6366F1",
        "temperament": "Analis (Rational / NT)",
        "bg_tint": "#EEF2FF",
        "border_color": "#C7D2FE"
    },
    "INFJ": {
        "code": "INFJ",
        "archetype": "Sang Advokat Humanis",
        "title": "INFJ · Sang Advokat Humanis",
        "tagline": "Punya intuisi tajam membaca perasaan orang lain, berpegang teguh pada prinsip hidup, dan tulus ingin membawa perubahan positif.",
        "summary": "Kamu adalah pendengar yang luar biasa dan sering kali bisa merasakan apa yang sedang dialami orang lain bahkan sebelum mereka cerita. Di balik sifatmu yang tenang dan santun, kamu punya idealisme yang kokoh dan dedikasi sunyi untuk membantu sesama. Kamu menghargai percakapan yang mendalam daripada obrolan basa-basi yang dangkal.",
        "avatar": "assets/avatars/infj.svg",
        "cognitive_roles": {
            "dominant": "Ni (Intuisi Makna & Karakter): Kamu otomatis menangkap esensi di balik kata-kata orang lain, motif tersembunyi, dan gambaran besar tentang bagaimana hubungan antarmanusia saling terikat.",
            "auxiliary": "Fe (Empati & Harmoni Sosial): Kamu peka menjaga keharmonisan kelompok, memastikan orang lain merasa dihargai, dan mengutarakan masukan dengan kelembutan yang menyentuh hati.",
            "tertiary": "Ti (Analisis Struktur Logis): Diam-diam kamu menguji ide-ide empatimu dengan pemikiran logis mandiri agar rencanamu tetap masuk akal dan realistis.",
            "inferior": "Se (Beban Sensorik Lingkungan): Suara bising, keramaian terus-menerus, atau lingkungan yang berantakan bisa bikin kamu gampang kewalahan dan lelah mental."
        },
        "strengths_blindspots": {
            "strengths": "Wawasan psikologis yang mendalam, integritas etika yang tulus, dan kemampuan merajut hubungan persahabatan yang kuat dan bermakna.",
            "blindspots": "Rentan mengalami kelelahan empati karena terlalu menyerap beban emosi orang lain, sulit bilang 'tidak', dan kadang punya ekspektasi kesempurnaan yang bikin diri sendiri stres."
        },
        "work_style": "Bekerja paling baik di tempat yang tenang dengan tujuan kerja yang selaras sama nilai moral pribadimu. Sangat cocok dalam peran mentoring, strategi konten, konsultasi, dan psikologi.",
        "stress_dynamics": "Kalau sudah kewalahan parah, kamu bisa tiba-tiba menarik diri total dari lingkungan sosial (doorslam). Cara recharge: nikmati kesendirian yang utuh, jalan-jalan santai di alam terbuka, dan detoks sejenak dari media sosial.",
        "color": "#047857",
        "temperament": "Diplomat (Idealist / NF)",
        "bg_tint": "#ECFDF5",
        "border_color": "#A7F3D0"
    },
    "INFP": {
        "code": "INFP",
        "archetype": "Sang Mediator Autentik",
        "title": "INFP · Sang Mediator Autentik",
        "tagline": "Menjaga kejujuran hati nurani, menghargai keunikan tiap insan, dan selalu mencari makna mendalam di setiap perjalanan hidup.",
        "summary": "Kamu hidup dipandu oleh kompas nilai batin yang sangat peka. Keaslian adalah segalanya buatmu; kamu paling nggak nyaman kalau harus berpura-pura atau mengikuti hal-hal yang bertentangan dengan kata hatimu. Kamu punya empati yang lembut, daya imajinasi kreatif yang kaya, dan selalu siap membela orang-orang yang merasa terpinggirkan.",
        "avatar": "assets/avatars/infp.svg",
        "cognitive_roles": {
            "dominant": "Fi (Keaslian Nilai Nurani): Hatimu tahu persis apa yang benar dan tulus bagi dirimu. Setiap keputusan disaring lewat rasa keselarasan moral batin yang nggak bisa ditawar.",
            "auxiliary": "Ne (Imajinasi & Eksplorasi Makna): Pikiranmu kaya akan simbol, cerita, dan sudut pandang puitis. Kamu suka membayangkan berbagai skenario masa depan yang penuh harapan dan kebaikan.",
            "tertiary": "Si (Kenangan & Rasa Nostalgia): Kamu menghargai momen masa lalu yang bermakna dan sering menyimpan memori sentimental dari tempat atau orang-orang yang kamu sayangi.",
            "inferior": "Te (Penegakan Efisiensi Kaku): Kamu kurang nyaman jika dituntut membuat aturan yang serba kaku, mengejar metrik angka tanpa jiwa, atau menghadapi perdebatan agresif."
        },
        "strengths_blindspots": {
            "strengths": "Empati yang tulus tanpa menghakimi, kreativitas artistik yang khas, dan keteguhan hati membela keadilan bagi mereka yang lemah.",
            "blindspots": "Sering menunda pekerjaan kalau mood belum pas, gampang kepikiran atau merasa tersinggung saat dikritik, dan cenderung menghindari konfrontasi langsung."
        },
        "work_style": "Berkembang pesat di lingkungan yang fleksibel, minim kompetisi saling sikut, dan memiliki dampak sosial yang nyata. Butuh otonomi untuk mengatur cara kerjanya sendiri.",
        "stress_dynamics": "Di bawah tekanan berat, kamu bisa merasa putus asa atau tiba-tiba jadi gampang mengkritik orang lain dengan nada tajam. Cara recharge: habiskan waktu untuk membuat karya kreatif (menulis, menggambar, dengerin musik) sendirian tanpa target penilaian orang lain.",
        "color": "#059669",
        "temperament": "Diplomat (Idealist / NF)",
        "bg_tint": "#ECFDF5",
        "border_color": "#A7F3D0"
    },
    "ENFJ": {
        "code": "ENFJ",
        "archetype": "Sang Protagonis Katalisator",
        "title": "ENFJ · Sang Protagonis Katalisator",
        "tagline": "Membangun semangat tim lewat kehangatan tulus, peka terhadap potensi orang lain, dan pandai menyatukan perbedaan.",
        "summary": "Karisma alamimu lahir dari kepedulian yang nyata. Kamu pandai membaca dinamika kelompok, menyemangati teman yang lagi down, dan membuat setiap orang di sekitarmu merasa didengar dan dirangkul. Kamu adalah pemimpin yang memotivasi lewat kehangatan, inspirasi positif, dan dedikasi tulus untuk kemajuan bersama.",
        "avatar": "assets/avatars/enfj.svg",
        "cognitive_roles": {
            "dominant": "Fe (Koneksi & Harmoni Kolektif): Nalurimu otomatis merawat atmosfer emosi kelompok. Kamu tahu persis apa yang perlu dikatakan untuk menenangkan hati atau menyatukan orang yang berselisih.",
            "auxiliary": "Ni (Wawasan Pertumbuhan Masa Depan): Kamu punya insting tajam melihat potensi tersembunyi dalam diri seseorang, bahkan saat orang itu sendiri belum menyadarinya.",
            "tertiary": "Se (Antusiasme Momen Nyata): Kamu tampil percaya diri dalam interaksi tatap muka, presentasi publik, dan pandai merespon situasi ruang secara spontan.",
            "inferior": "Ti (Analisis Kritis Dingin): Kamu kadang merasa bimbang saat harus mengambil keputusan logis yang objektif tapi berisiko melukai perasaan orang lain di tim."
        },
        "strengths_blindspots": {
            "strengths": "Kemampuan komunikasi yang memotivasi, kepemimpinan inklusif yang mempersatukan, dan kepekaan tinggi dalam mengembangkan potensi rekan kerja.",
            "blindspots": "Sering mengorbankan waktu dan kesehatan sendiri demi mengurusi masalah orang lain, dan terlalu memikirkan kritik atau pendapat orang lain tentang dirimu."
        },
        "work_style": "Sangat efektif dalam peran kepemimpinan tim, manajemen komunitas, pendidikan, dan hubungan masyarakat. Membutuhkan atmosfer kerja yang saling menghargai dan mendukung.",
        "stress_dynamics": "Saat kehabisan energi emosional, kamu bisa jadi sangat cemas atau merasa kerja kerasmu nggak dihargai. Cara recharge: tetapkan batasan tegas untuk diri sendiri, tolak ajakan kumpul untuk sementara waktu, dan istirahat santai di rumah.",
        "color": "#065F46",
        "temperament": "Diplomat (Idealist / NF)",
        "bg_tint": "#ECFDF5",
        "border_color": "#A7F3D0"
    },
    "ENFP": {
        "code": "ENFP",
        "archetype": "Sang Juru Kampanye Eksploratif",
        "title": "ENFP · Sang Juru Kampanye Eksploratif",
        "tagline": "Energi ceria yang menular, penuh rasa ingin tahu pada kehidupan, dan selalu melihat kebaikan serta kemungkinan baru dalam diri sesama.",
        "summary": "Kamu adalah pembawa angin segar di mana pun kamu berada. Rasa ingin tahumu luas, mudah akrab dengan siapa saja, dan selalu antusias mencoba pengalaman baru. Kamu melihat dunia sebagai tempat penuh kemungkinan seru, menghubungkan orang-orang dari latar belakang berbeda, dan menolak hidup yang cuma diisi rutinitas membosankan.",
        "avatar": "assets/avatars/enfp.svg",
        "cognitive_roles": {
            "dominant": "Ne (Imajinasi & Peluang Tanpa Batas): Matamu selalu melihat potensi baru di mana-mana. Kamu suka menghubungkan ide-ide segar dan menyalakan percikan antusiasme di sekitarmu.",
            "auxiliary": "Fi (Resonansi Nilai Otentik): Di balik sifat ceriamu, kamu punya perasaan batin yang dalam dan komitmen kuat pada nilai-nilai keadilan serta keaslian personal.",
            "tertiary": "Te (Pengorganisasian Aksi Taktis): Saat ada ide yang benar-benar kamu yakini maknanya, kamu bisa sangat tangkas menyusun rencana aksi buat mewujudkannya.",
            "inferior": "Si (Tugas Administratif Berulang): Menangani berkas rutin, detail administrasi harian, atau aturan kaku tanpa variasi adalah hal yang paling cepat bikin kamu mati gaya."
        },
        "strengths_blindspots": {
            "strengths": "Kreativitas yang melimpah, kemampuan adaptasi instan terhadap suasana baru, dan bakat alami menyemangati orang lain agar percaya diri.",
            "blindspots": "Sering memulai banyak proyek seru tapi kesulitan menuntaskannya sampai selesai (gampang teralihkan ide baru), dan sering salah memperkirakan waktu luang."
        },
        "work_style": "Butuh atmosfer kerja yang merayakan inovasi, kolaborasi terbuka, dan kebebasan bereksplorasi. Paling produktif dalam proyek kreatif, komunikasi kreatif, dan perintisan inisiatif baru.",
        "stress_dynamics": "Saat terkunci dalam rutinitas mekanis yang monoton, kamu bisa merasa overthinking dan meragukan kemampuan diri sendiri. Cara recharge: ngobrol lepas sama teman dekat, ganti suasana kerja ke kafe atau alam, dan tunda tugas rutin sejenak.",
        "color": "#10B981",
        "temperament": "Diplomat (Idealist / NF)",
        "bg_tint": "#ECFDF5",
        "border_color": "#A7F3D0"
    },
    "ISTJ": {
        "code": "ISTJ",
        "archetype": "Sang Inspektur Andal",
        "title": "ISTJ · Sang Inspektur Andal",
        "tagline": "Jangkar terpercaya yang selalu menepati janji, kerja rapi berdasarkan fakta, dan menjaga komitmen sampai tuntas.",
        "summary": "Kalau kamu sudah berjanji, orang lain tahu tugas itu pasti beres tanpa perlu diawasi. Kamu menghargai ketertiban, kejelasan tugas, dan metode kerja yang sudah terbukti andal. Kamu adalah sosok yang tenang, teliti, dan bisa diandalkan dalam kondisi apa pun karena tindakanmu selalu konsisten dan berakar pada kenyataan.",
        "avatar": "assets/avatars/istj.svg",
        "cognitive_roles": {
            "dominant": "Si (Ketelitian Fakta & Pengalaman Teruji): Kamu punya ingatan operasional yang sangat rapi. Kamu menghargai preseden yang berhasil dan memastikan setiap langkah dikerjakan sesuai standar terbaik.",
            "auxiliary": "Te (Pengaturan Logika Efisien): Kamu mengelola pekerjaan dengan jadwal teratur, to-the-point, dan berorientasi pada pencapaian hasil yang nyata dan terukur.",
            "tertiary": "Fi (Loyalitas Prinsip Sunyi): Kesetiaanmu pada komitmen dan tanggung jawab dipegang secara mendalam dan dibuktikan lewat tindakan nyata, bukan sekadar janji manis.",
            "inferior": "Ne (Kecemasan Terhadap Hal Tak Pasti): Disrupsi mendadak, perubahan arah tanpa alasan jelas, atau skenario spekulatif liar bisa bikin kamu merasa risih dan waswas."
        },
        "strengths_blindspots": {
            "strengths": "Keandalan tinggi yang nggak perlu diragukan, ketelitian luar biasa terhadap data, dan dedikasi menjaga sistem kerja tetap berjalan tertib.",
            "blindspots": "Cenderung skeptis terhadap metode baru yang belum teruji, agak kaku saat menghadapi perubahan dadakan, dan terkadang terkesan terlalu formal."
        },
        "work_style": "Berkinerja optimal di lingkungan dengan ekspektasi jelas, peran yang terdefinisi, dan parameter sukses yang transparan. Sangat menghargai ketepatan waktu dan profesionalisme.",
        "stress_dynamics": "Saat menghadapi kekacauan arahan atau lingkungan yang serba berantakan, kamu bisa merasa terbebani dan terpaku pada detail minor. Cara recharge: rapikan kembali ruang kerjamu, nikmati rutinitas yang tenang, dan ambil istirahat tanpa gangguan orang lain.",
        "color": "#0369A1",
        "temperament": "Pengawal (Sentinel / SJ)",
        "bg_tint": "#F0F9FF",
        "border_color": "#BAE6FD"
    },
    "ISFJ": {
        "code": "ISFJ",
        "archetype": "Sang Pelindung Setia",
        "title": "ISFJ · Sang Pelindung Setia",
        "tagline": "Merawat orang-orang tersayang dengan perhatian praktis, menjaga keharmonisan, dan selalu hadir tanpa pamrih.",
        "summary": "Kebaikan hatimu terlihat jelas dari hal-hal kecil sehari-hari: mengingat detail kesukaan teman, sigap membantu di balik layar, dan memastikan suasana kerja tetap nyaman serta tenteram. Kamu adalah figur penyangga yang setia dan tulus, menjaga kestabilan tim tanpa pernah menuntut sorotan panggung.",
        "avatar": "assets/avatars/isfj.svg",
        "cognitive_roles": {
            "dominant": "Si (Perhatian Detail & Konsistensi Nyata): Kamu mengingat kebutuhan orang lain dengan teliti dan setia menjalankan kebiasaan baik yang menjaga keharmonisan lingkungan.",
            "auxiliary": "Fe (Kehangatan & Kepedulian Sosial): Kamu peka terhadap kenyamanan orang lain, sigap menawarkan bantuan konkret, dan selalu berusaha meredam friksi interpersonal.",
            "tertiary": "Ti (Analisis Masalah Praktis): Diam-diam kamu memikirkan cara kerja yang paling efisien agar bantuan yang kamu berikan tepat sasaran dan nggak merepotkan orang lain.",
            "inferior": "Ne (Kekhawatiran Masa Depan): Perubahan besar yang mendadak atau ketidakpastian rencana jangka panjang bisa bikin kamu merasa cemas berlebihan."
        },
        "strengths_blindspots": {
            "strengths": "Dedikasi kerja yang konsisten, ketelitian tinggi dalam urusan logistik dan kebutuhan tim, serta kesetiaan luar biasa pada hubungan pertemanan.",
            "blindspots": "Sering memendam perasaan sendiri demi menjaga suasana damai, susah menolak permintaan tolong orang lain sampai diri sendiri kecapekan, dan enggan menerima perubahan mendadak."
        },
        "work_style": "Paling produktif dalam lingkungan yang suportif, teratur, dan saling menghargai. Berkontribusi besar dalam koordinasi operasional, layanan pendukung, dan administrasi tim.",
        "stress_dynamics": "Saat kelelahan menumpuk karena terlalu sering memprioritaskan orang lain, kamu bisa merasa tertekan dan overthinking skenario terburuk. Cara recharge: luangkan waktu khusus buat memanjakan diri sendiri di rumah, istirahat tenang, dan belajar bilang 'tidak' tanpa rasa bersalah.",
        "color": "#0284C7",
        "temperament": "Pengawal (Sentinel / SJ)",
        "bg_tint": "#F0F9FF",
        "border_color": "#BAE6FD"
    },
    "ESTJ": {
        "code": "ESTJ",
        "archetype": "Sang Eksekutif Pengarah",
        "title": "ESTJ · Sang Eksekutif Pengarah",
        "tagline": "Merapikan hal yang berantakan, menegakkan kejelasan aturan, dan menggerakkan tim dengan aksi nyata yang terukur.",
        "summary": "Kamu adalah sosok penggerak yang tegas, praktis, dan berorientasi pada hasil nyata. Kamu nggak suka buang-buang waktu dengan keraguan; kalau ada masalah, kamu langsung buat rencana aksi, membagi tugas dengan jelas, dan memastikan target tuntas tepat waktu. Kamu menghargai kerja keras, kejujuran, dan akuntabilitas profesional.",
        "avatar": "assets/avatars/estj.svg",
        "cognitive_roles": {
            "dominant": "Te (Tata Kelola & Eksekusi Tegas): Naluri utamamu adalah menegakkan standar kerja yang jelas, menertibkan proses yang lamban, dan memastikan setiap orang tahu tanggung jawabnya.",
            "auxiliary": "Si (Prosedur & Pengalaman Terbaik): Kamu berpegang pada fakta yang terbukti berhasil dan memastikan aturan yang berlaku dijalankan secara konsisten dan adil.",
            "tertiary": "Ne (Solusi Taktis Alternatif): Kamu cukup fleksibel mencari jalan pintas yang masuk akal ketika cara baku menemui hambatan teknis di lapangan.",
            "inferior": "Fi (Kepekaan Emosi Pribadi): Karena terbiasa to-the-point, kamu kadang lupa memperhatikan perasaan orang lain atau merasa canggung saat harus membahas masalah yang bernuansa emosional."
        },
        "strengths_blindspots": {
            "strengths": "Kepemimpinan operasional yang kokoh, kejelasan dalam delegasi tugas, dan kemampuan luar biasa membereskan situasi kerja yang kacau balau.",
            "blindspots": "Bisa terkesan terlalu keras atau kaku bagi rekan kerja yang lebih sensitif, dan kurang sabar menghadapi orang yang kerjanya lamban atau bertele-tele."
        },
        "work_style": "Menyukai lingkungan kerja yang jelas hierarkinya, disiplin waktu, dan menghargai hasil kerja terukur. Mengutamakan komunikasi langsung yang jujur dan ringkas.",
        "stress_dynamics": "Saat menghadapi rekan kerja yang nggak disiplin atau proyek yang berantakan di luar kendalimu, kamu bisa jadi sangat gampang marah dan tertekan. Cara recharge: delegasikan sebagian beban kerja, lakukan aktivitas fisik untuk menyalurkan energi, dan ambil jeda dari posisi koordinasi.",
        "color": "#075985",
        "temperament": "Pengawal (Sentinel / SJ)",
        "bg_tint": "#F0F9FF",
        "border_color": "#BAE6FD"
    },
    "ESFJ": {
        "code": "ESFJ",
        "archetype": "Sang Konsul Pengayom",
        "title": "ESFJ · Sang Konsul Pengayom",
        "tagline": "Paling jago bikin suasana kumpul jadi hangat, memastikan nggak ada yang merasa ditinggal, dan setia menjaga persahabatan.",
        "summary": "Kamu adalah perekat sosial yang bikin suasana di mana pun jadi terasa akrab dan hangat. Kamu peka terhadap kebutuhan orang-orang di sekitarmu, suka mengorganisir acara kumpul bareng, dan selalu siap jadi teman curhat yang suportif. Kesuksesan bagimu adalah saat seluruh anggota tim atau lingkaran pertemanan bisa maju bareng dalam suasana rukun.",
        "avatar": "assets/avatars/esfj.svg",
        "cognitive_roles": {
            "dominant": "Fe (Kehangatan & Keharmonisan Relasi): Kamu otomatis menjaga agar semua orang merasa nyaman, didengar, dan terlibat dalam perbincangan tanpa ada yang merasa dikucilkan.",
            "auxiliary": "Si (Perhatian Praktis & Ketertiban): Kamu mengingat kebiasaan dan kebutuhan teman-temanmu secara detail, serta teliti mengurus kebutuhan logistik sehari-hari.",
            "tertiary": "Ne (Keterbukaan Ide Kolaborasi): Kamu terbuka menyambut ide-ide baru yang bisa membuat kegiatan bersama terasa lebih menyenangkan dan bervariasi.",
            "inferior": "Ti (Kritik Logis Dingin): Kamu rentan merasa terserang atau sedih saat menerima kritik yang disampaikan tanpa nada empati atau saat harus berhadapan dengan konflik terbuka."
        },
        "strengths_blindspots": {
            "strengths": "Kecerdasan sosial yang tinggi, pandai membangun solidaritas tim, dan sangat bisa diandalkan dalam memfasilitasi kebutuhan bersama.",
            "blindspots": "Gampang kepikiran kalau ada orang yang kelihatan nggak suka sama kamu, cenderung menghindari konflik yang sebenarnya perlu dibicarakan, dan terlalu bergantung pada validasi luar."
        },
        "work_style": "Sangat produktif dalam peran yang melibatkan interaksi langsung, koordinasi acara, hubungan masyarakat, dan pelayanan. Membutuhkan atmosfer kerja yang ramah dan saling menghargai.",
        "stress_dynamics": "Saat terjadi perselisihan sengit di sekitarmu, kamu bisa merasa cemas dan menyalahkan diri sendiri. Cara recharge: ngobrol santai dari hati ke hati sama sahabat terpercaya yang suportif, dan ingat bahwa kamu nggak bisa membahagiakan semua orang sekaligus.",
        "color": "#0EA5E9",
        "temperament": "Pengawal (Sentinel / SJ)",
        "bg_tint": "#F0F9FF",
        "border_color": "#BAE6FD"
    },
    "ISTP": {
        "code": "ISTP",
        "archetype": "Sang Virtuoso Teknis",
        "title": "ISTP · Sang Virtuoso Teknis",
        "tagline": "Kepala dingin di saat genting, jago utak-atik cara kerja alat atau sistem, dan bergerak efektif tanpa drama.",
        "summary": "Kamu tenang, observatif, dan sangat pragmatis. Di saat orang lain panik menghadapi masalah teknis mendadak, kamu santai menganalisis akar masalahnya dan langsung menemukan solusi jitu dengan tangan dinginmu. Kamu suka kebebasan bertindak, hemat energi bicara, dan lebih memilih membuktikan kemampuan lewat hasil nyata daripada banyak teori.",
        "avatar": "assets/avatars/istp.svg",
        "cognitive_roles": {
            "dominant": "Ti (Bedah Logika & Mekanisme): Kamu otomatis membedah cara kerja suatu hal di kepalamu untuk menemukan cara paling efisien dan cerdas buat menyelesaikannya.",
            "auxiliary": "Se (Respons Taktis Real-Time): Pengamatanmu tajam membaca kondisi fisik sekitar. Kamu sangat tangkas mengambil tindakan cepat dan tepat saat terjadi situasi darurat.",
            "tertiary": "Ni (Insting Pola Tersembunyi): Kamu punya firasat kuat yang membantumu menemukan jalan keluar cerdik saat cara standar menemui jalan buntu.",
            "inferior": "Fe (Basa-Basi Sosial): Kamu paling malas kalau harus meladeni obrolan basa-basi yang berputar-putar, drama emosional, atau protokol formalitas yang kaku."
        },
        "strengths_blindspots": {
            "strengths": "Ketenangan luar biasa di bawah tekanan, keahlian alami dalam pemecahan masalah teknis (troubleshooting), dan efisiensi kerja tanpa buang energi percuma.",
            "blindspots": "Cenderung terlalu tertutup sehingga rekan kerja susah membaca pikiranmu, enggan terikat komitmen yang terlalu kaku, dan kadang kurang peka sama perasaan orang lain."
        },
        "work_style": "Membutuhkan kebebasan kerja tanpa mikromanajemen, fokus pada penyelesaian masalah konkret daripada rapat panjang yang teoritis. Sangat unggul dalam rekayasa sistem, investigasi masalah, dan operasi lapangan.",
        "stress_dynamics": "Saat terjebak dalam birokrasi berbelit atau lingkungan yang penuh drama sosial, kamu bisa menarik diri total atau melontarkan komentar sarkas yang pedas. Cara recharge: luangkan waktu sendiri buat utak-atik proyek pribadi, main game, atau olahraga fisik di luar ruangan.",
        "color": "#B45309",
        "temperament": "Penjelajah (Explorer / SP)",
        "bg_tint": "#FFFBEB",
        "border_color": "#FDE68A"
    },
    "ISFP": {
        "code": "ISFP",
        "archetype": "Sang Seniman Autentik",
        "title": "ISFP · Sang Seniman Autentik",
        "tagline": "Menikmati keindahan momen sekarang, punya cita rasa estetika yang halus, dan hidup selaras dengan kata hati tanpa kepura-puraan.",
        "summary": "Kamu bersahaja, ramah, dan punya pandangan hidup yang damai. Kamu menikmati hal-hal yang menyentuh panca indera: musik yang pas, visual yang estetik, atau suasana yang nyaman. Kamu nggak suka mendikte orang lain, menghargai ruang pribadi masing-masing, dan mengekspresikan jati dirimu lewat karya atau perbuatan nyata daripada banyak bicara.",
        "avatar": "assets/avatars/isfp.svg",
        "cognitive_roles": {
            "dominant": "Fi (Integritas Hati Nurani): Kamu menilai segala hal berdasarkan kecocokan batin dan prinsip moral pribadimu. Keaslian diri adalah prinsip hidup yang kamu pegang teguh tanpa perlu koar-koar.",
            "auxiliary": "Se (Kepekaan Estetika & Momen Nyata): Panca inderamu sangat peka terhadap warna, tekstur, nada, dan suasana sekitar. Kamu menikmati setiap momen hidup dengan intens dan apa adanya.",
            "tertiary": "Ni (Wawasan Intuitif Perlahan): Seiring waktu, kamu mulai melihat arah gambaran besar dari pengalaman hidupmu dan mengembangkan insting yang semakin matang.",
            "inferior": "Te (Perencanaan Birokrasi Kaku): Menyusun jadwal jangka panjang yang kaku, laporan formal yang berbelit, atau harus bersikap mendikte orang lain adalah hal yang paling bikin kamu tertekan."
        },
        "strengths_blindspots": {
            "strengths": "Kepekaan rasa dan estetika yang tinggi, kepribadian yang ramah tanpa menghakimi, dan kemampuan adaptasi yang tenang menghadapi kenyataan.",
            "blindspots": "Cenderung menghindari perselisihan atau negosiasi batas kerja sampai dirugikan, susah membuat perencanaan jangka panjang yang terstruktur, dan gampang meragukan karya sendiri."
        },
        "work_style": "Bekerja paling optimal dalam ruang yang fleksibel, santai, dan minim tekanan kompetisi agresif. Sangat bersinar dalam bidang desain kreatif, seni terapan, penulisan, dan pemulihan kesehatan.",
        "stress_dynamics": "Saat ditekan oleh target yang terlalu agresif atau lingkungan yang kaku dan munafik, kamu bisa menutup diri rapat-rapat. Cara recharge: nikmati keindahan alam, dengarkan musik favorit, dan habiskan waktu hening tanpa tuntutan ekspektasi dari orang lain.",
        "color": "#D97706",
        "temperament": "Penjelajah (Explorer / SP)",
        "bg_tint": "#FFFBEB",
        "border_color": "#FDE68A"
    },
    "ESTP": {
        "code": "ESTP",
        "archetype": "Sang Pengusaha Responsif",
        "title": "ESTP · Sang Pengusaha Responsif",
        "tagline": "Cepat membaca momentum lapangan, berani ambil risiko cerdas, dan selalu punya akal buat mengatasi rintangan langsung.",
        "summary": "Hidupmu penuh warna, energi, dan aksi nyata. Daripada cuma berteori lama-lama di atas kertas, kamu lebih suka langsung terjun ke lapangan dan belajar sambil jalan. Kamu punya insting sosial dan taktis yang tajam, sangat adaptif saat ada perubahan mendadak, dan suka tantangan seru yang memacu adrenalin.",
        "avatar": "assets/avatars/estp.svg",
        "cognitive_roles": {
            "dominant": "Se (Aksi Taktis & Refleks Cepat): Kamu menyerap data langsung dari lingkungan sekitar secara instan. Kamu tangkas memanfaatkan peluang nyata di depan mata tanpa banyak ragu.",
            "auxiliary": "Ti (Kalkulasi Cepat & Masuk Akal): Di balik aksimu yang spontan, otakmu terus mengkalkulasi risiko secara logis agar manuver yang kamu ambil tetap efektif dan menguntungkan.",
            "tertiary": "Fe (Persuasi & Negosiasi Santai): Kamu punya gaya komunikasi yang santai, karismatik, dan luwes meyakinkan orang lain agar mau diajak kerja sama.",
            "inferior": "Ni (Analisis Teori Abstrak Jangka Panjang): Kamu cepat bosan dengan perdebatan teoritis yang bertele-tele atau perencanaan spekulatif yang nggak punya relevansi praktis saat ini."
        },
        "strengths_blindspots": {
            "strengths": "Keberanian mengambil keputusan cepat di saat genting, ketahanan mental yang tinggi menghadapi krisis, dan kepiawaian negosiasi yang langsung ke sasaran.",
            "blindspots": "Terkadang terlalu impulsif tanpa memikirkan konsekuensi jangka panjang, cepat bosan saat situasi sudah stabil tanpa tantangan baru, dan kurang sabar dengan aturan birokrasi."
        },
        "work_style": "Menyukai ritme kerja yang dinamis, menantang, dan memberikan keleluasaan buat bermanuver langsung. Sangat efektif dalam manajemen krisis, negosiasi komersial, operasi lapangan, dan kewirausahaan.",
        "stress_dynamics": "Saat dipaksa duduk diam mengerjakan urusan administratif yang monoton, kamu bisa merasa gelisah dan bertindak terlalu nekat. Cara recharge: lakukan aktivitas olahraga fisik yang memacu keringat, ambil tantangan taktis jangka pendek, dan cari suasana baru di luar ruangan.",
        "color": "#92400E",
        "temperament": "Penjelajah (Explorer / SP)",
        "bg_tint": "#FFFBEB",
        "border_color": "#FDE68A"
    },
    "ESFP": {
        "code": "ESFP",
        "archetype": "Sang Penghibur Karismatik",
        "title": "ESFP · Sang Penghibur Karismatik",
        "tagline": "Membawa tawa dan energi positif di mana pun berada, spontan, dan membuat setiap momen terasa seperti perayaan bersama.",
        "summary": "Bersamamu, suasana nggak pernah terasa membosankan. Kamu menikmati hidup dengan sepenuh hati, peka terhadap perasaan orang-orang di sekitarmu, dan senang bikin teman-temanmu tersenyum. Kamu spontan, fleksibel, punya gaya yang ekspresif, dan selalu siap menyambut petualangan seru hari ini tanpa beban berlebihan.",
        "avatar": "assets/avatars/esfp.svg",
        "cognitive_roles": {
            "dominant": "Se (Antusiasme Momen & Kegembiraan Nyata): Kamu hidup sepenuhnya di momen sekarang. Kamu pandai menciptakan atmosfer interaktif yang menyenangkan dan menghidupkan suasana ruangan.",
            "auxiliary": "Fi (Kehangatan & Ketulusan Hati): Kamu peduli secara tulus pada orang lain dan memastikan interaksi yang kamu bangun tetap berlandaskan kejujuran dan rasa saling menghargai.",
            "tertiary": "Te (Aksi Nyata & Eksekusi Cepat): Saat ingin mewujudkan rencana yang seru, kamu bisa sangat gesit mengatur hal-hal praktis biar acaranya berjalan lancar.",
            "inferior": "Ni (Kekhawatiran Rumit Masa Depan): Memikirkan ramalan masa depan yang suram atau analisis konsep yang terlalu abstrak bisa bikin energimu cepat drop dan merasa tertekan."
        },
        "strengths_blindspots": {
            "strengths": "Kemampuan luar biasa menyatukan kelompok secara organik, antusiasme yang menular, dan kepekaan tinggi dalam membaca suasana hati teman atau klien.",
            "blindspots": "Cenderung menghindari obrolan konflik yang berat, malas mengurusi urusan perencanaan jangka panjang, dan kadang terlalu mementingkan kesenangan sesaat dibanding masa depan."
        },
        "work_style": "Berkembang pesat di lingkungan yang interaktif, terbuka, dan kolaboratif. Sangat efektif dalam representasi brand, fasilitasi pelatihan publik, manajemen komunitas, hiburan, dan layanan kreatif.",
        "stress_dynamics": "Saat merasa terisolasi secara sosial atau terkekang oleh aturan yang membatasi spontanitas, kamu bisa merasa cemas dan putus asa. Cara recharge: kumpul santai dengan teman-teman terdekat yang ceria, lakukan aktivitas seru di luar ruangan, dan lepaskan beban pikiran sementara waktu.",
        "color": "#F59E0B",
        "temperament": "Penjelajah (Explorer / SP)",
        "bg_tint": "#FFFBEB",
        "border_color": "#FDE68A"
    }
}


def get_profile(mbti_type: str) -> Dict:
    code = mbti_type.upper().strip()
    return PROFILES.get(code, {
        "code": code,
        "archetype": "Tipologi Kognitif",
        "title": f"{code} · Analisis Tipologi",
        "tagline": "Profil hasil evaluasi arsitektur kognitif yang memetakan caramu berpikir dan bertindak.",
        "summary": "Kombinasi proses berpikir dan orientasi adaptasi yang memandu tindakanmu sehari-hari.",
        "avatar": "assets/avatars/intj.svg",
        "cognitive_roles": {
            "dominant": "Fungsi utama yang memandu keputusan sadar sehari-hari.",
            "auxiliary": "Pemandu pendukung yang bikin kamu tetap seimbang.",
            "tertiary": "Sisi santai yang muncul pas lagi rileks.",
            "inferior": "Sisi yang paling rentan capek atau bikin overthinking saat stres berat."
        },
        "strengths_blindspots": {
            "strengths": "Kapasitas adaptif dalam menyelesaikan tantangan nyata.",
            "blindspots": "Area kerentanan yang perlu kamu perhatikan secara sadar."
        },
        "work_style": "Gaya kerja yang seimbang antara otonomi dan kolaborasi.",
        "stress_dynamics": "Manajemen energi yang sehat dan ruang pemulihan yang cukup.",
        "color": "#4F46E5",
        "temperament": "Tipologi kognitif",
        "bg_tint": "#EEF2FF",
        "border_color": "#C7D2FE"
    })


def get_all_profiles() -> Dict[str, Dict]:
    return PROFILES


_AVATAR_CACHE: Dict[str, str] = {}


def get_avatar_base64(mbti_code: str) -> str:
    code = mbti_code.lower().strip()
    if code in _AVATAR_CACHE:
        return _AVATAR_CACHE[code]

    file_path = os.path.join(os.path.dirname(__file__), "assets", "avatars", f"{code}.svg")
    if not os.path.exists(file_path):
        return ""

    try:
        with open(file_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            _AVATAR_CACHE[code] = encoded
            return encoded
    except Exception:
        return ""
