from __future__ import annotations
import base64
import os
from typing import Dict, List, Optional

PROFILES: Dict[str, Dict] = {
    "INTJ": {
        "code": "INTJ",
        "archetype": "Sang Arsitek Strategis",
        "title": "INTJ · Sang Arsitek Strategis",
        "tagline": "Merancang cetak biru masa depan dengan kalkulasi tajam, visi jangka panjang, dan ketahanan independen yang kokoh.",
        "summary": "Pikiran seorang INTJ bekerja seperti ruang simulasi taktis. Mereka tidak sekadar melihat apa yang ada di depan mata, melainkan membaca pola tersembunyi, memprediksi skenario bertahun-tahun ke depan, dan menyusun arsitektur sistem yang efisien untuk mencapai tujuan ambisius tanpa terpengaruh oleh kebisingan opini publik.",
        "avatar": "assets/avatars/intj.svg",
        "cognitive_roles": {
            "dominant": "Ni (Introverted Intuition): Pemetaan pola makro dan proyeksi kemungkinan masa depan secara konvergen. Mengabstraksikan realitas ke dalam kerangka model konseptual.",
            "auxiliary": "Te (Extraverted Thinking): Pengorganisasian sumber daya objektif, penataan logika eksternal, dan penegakan metrik keberhasilan yang terstruktur.",
            "tertiary": "Fi (Introverted Feeling): Kompas etika internal dan keselarasan nilai personal yang dipegang secara mendalam dan privat.",
            "inferior": "Se (Extraverted Sensing): Pengolahan data sensoris seketika. Di bawah tekanan berkepanjangan, dapat mengalami kepekaan berlebih terhadap lingkungan fisik atau kelelahan sensorik."
        },
        "strengths_blindspots": {
            "strengths": "Kemampuan luar biasa dalam merancang arsitektur sistem jangka panjang, berpikir independen tanpa bias konsensus, serta ketajaman diagnostik terhadap inefisiensi prosedural.",
            "blindspots": "Kecenderungan mengabaikan kebutuhan konsensus emosional tim, ekspektasi perfeksionisme yang kaku, serta potensi memandang remeh dinamika interpersonal."
        },
        "work_style": "Berkinerja optimal dalam blok waktu fokus mandiri (deep work), komunikasi asinkron yang terstruktur, dan lingkungan yang memberikan otonomi strategis penuh tanpa mikromanajemen.",
        "stress_dynamics": "Saat mengalami kejenuhan akut, cenderung mengisolasi diri, menjadi terlampau kritis terhadap detail kecil, atau terdistraksi oleh impuls sensorik. Pemulihan memerlukan ruang kesendirian terstruktur, refleksi tertulis, dan eliminasi komitmen sosial yang tidak esensial.",
        "color": "#4338CA",
        "temperament": "Analis (Rational / NT)",
        "bg_tint": "#EEF2FF",
        "border_color": "#C7D2FE"
    },
    "INTP": {
        "code": "INTP",
        "archetype": "Sang Pemikir Teoretis",
        "title": "INTP · Sang Pemikir Teoretis",
        "tagline": "Membedah setiap lapis realitas untuk menemukan prinsip kebenaran fundamental yang berdiri kokoh tanpa kontradiksi.",
        "summary": "Bagi seorang INTP, dunia adalah sebuah teka-teki intelektual yang tak pernah selesai dikaji. Mereka terdorong untuk menelusuri akar dari setiap konsep, menguji logika di balik asumsi umum, dan membangun teori elegan yang sanggup menjelaskan fenomena paling rumit dengan presisi konseptual yang tinggi.",
        "avatar": "assets/avatars/intp.svg",
        "cognitive_roles": {
            "dominant": "Ti (Introverted Thinking): Penataan kerangka berpikir logis internal yang presisi. Menguji keabsahan setiap premis berdasarkan konsistensi rasional tanpa kompromi.",
            "auxiliary": "Ne (Extraverted Intuition): Eksplorasi kemungkinan lintas domain, identifikasi relasi abstrak antar konsep yang tampak tidak saling berhubungan.",
            "tertiary": "Si (Introverted Sensing): Rujukan komparatif terhadap data faktual historis dan preseden yang telah teruji.",
            "inferior": "Fe (Extraverted Feeling): Keselarasan emosional antarpribadi. Pada kondisi tertekan, dapat merasa canggung dalam memproses ekspektasi sosial atau menjadi sangat reaktif terhadap penerimaan kelompok."
        },
        "strengths_blindspots": {
            "strengths": "Kapasitas dekonstruksi masalah kompleks ke komponen fundamental, objektivitas intelektual murni, serta toleransi tinggi terhadap ambiguitas teoritis.",
            "blindspots": "Kecenderungan menunda finalisasi akibat siklus analisis berkelanjutan, keengganan mengeksekusi aspek administratif rutin, dan komunikasi yang terkadang terlalu abstrak bagi audiens umum."
        },
        "work_style": "Bekerja paling produktif dalam lingkungan non-kaku yang mengutamakan otonomi intelektual. Membutuhkan ruang eksplorasi eksperimental sebelum berkomitmen pada satu jalur implementasi.",
        "stress_dynamics": "Di bawah stres berat, dapat terjebak dalam perenungan berulang tanpa aksi (analysis paralysis) atau ledakan emosi sosial yang tidak terduga. Pemulihan dicapai melalui eksplorasi topik baru secara bebas tanpa target tenggat waktu.",
        "color": "#4F46E5",
        "temperament": "Analis (Rational / NT)",
        "bg_tint": "#EEF2FF",
        "border_color": "#C7D2FE"
    },
    "ENTJ": {
        "code": "ENTJ",
        "archetype": "Sang Komandan Visioner",
        "title": "ENTJ · Sang Komandan Visioner",
        "tagline": "Mengubah visi strategis menjadi realitas nyata melalui komando terarah dan orkestrasi sumber daya tanpa kompromi.",
        "summary": "ENTJ dilahirkan untuk memimpin dan membangun. Mereka memiliki bakat alami dalam mengenali potensi efisiensi, memetakan langkah aksi, dan menggalang sumber daya untuk menaklukkan tantangan skala besar. Keraguan dan kemalasan segera diubah menjadi momentum eksekusi yang penuh energi dan kejelasan arah.",
        "avatar": "assets/avatars/entj.svg",
        "cognitive_roles": {
            "dominant": "Te (Extraverted Thinking): Penataan dunia eksternal melalui struktur logis, penetapan target terukur, dan eliminasi hambatan birokrasi secara tegas.",
            "auxiliary": "Ni (Introverted Intuition): Pandangan strategis masa depan yang memandu arah aksi jangka panjang dan mengantisipasi disrupsi pasar.",
            "tertiary": "Se (Extraverted Sensing): Ketangkasan memanfaatkan peluang nyata di lapangan dan keterlibatan aktif dengan realitas konkret.",
            "inferior": "Fi (Introverted Feeling): Integrasi keselarasan emosional personal. Rentan mengesampingkan kelelahan emosional pribadi demi pencapaian objektif eksternal."
        },
        "strengths_blindspots": {
            "strengths": "Ketegasan pengambilan keputusan dalam situasi krisis, artikulasi visi strategis yang persuasif, serta kemampuan mengonsolidasikan tim menuju target ambisius.",
            "blindspots": "Potensi mengesampingkan kapasitas adaptasi rekan kerja yang memerlukan ritme lebih hati-hati, intoleransi terhadap ambiguitas proses, dan minimnya ruang jeda reflektif."
        },
        "work_style": "Menguasai lingkungan berisiko tinggi dengan target jelas dan tanggung jawab terdefinisi. Lebih menyukai komunikasi ringkas, berbasis data, dan pertemuan yang memiliki tujuan terukur.",
        "stress_dynamics": "Saat kelelahan melampaui batas, dapat beralih menjadi terlampau mengontrol atau justru merasa teralienasi dari tujuan internalnya. Pemulihan membutuhkan pelepasan kendali operasional sementara, latihan fisik intens, dan peninjauan kembali prinsip dasar personal.",
        "color": "#3730A3",
        "temperament": "Analis (Rational / NT)",
        "bg_tint": "#EEF2FF",
        "border_color": "#C7D2FE"
    },
    "ENTP": {
        "code": "ENTP",
        "archetype": "Sang Pendebat Inovatif",
        "title": "ENTP · Sang Pendebat Inovatif",
        "tagline": "Menantang kemapanan lewat percikan ide berani, dekonstruksi paradigma usang, dan navigasi kemungkinan tanpa batas.",
        "summary": "Bagi ENTP, tidak ada batas pemikiran yang tidak boleh dijelajahi. Mereka adalah katalisator perubahan yang gemar membedah argumen dari segala sudut pandang, merangkai hubungan tak terduga antara ide-ide yang saling terpisah, dan menyalakan percakapan intelektual yang memicu gebrakan baru.",
        "avatar": "assets/avatars/entp.svg",
        "cognitive_roles": {
            "dominant": "Ne (Extraverted Intuition): Penjelajahan hipotesis alternatif dan potensi inovatif. Terampil melihat koneksi di luar kelaziman yang membuka paradigma baru.",
            "auxiliary": "Ti (Introverted Thinking): Penyaringan rasional terhadap ide-ide baru guna memastikan integritas logika dan viabilitas teknis sebelum dieksekusi.",
            "tertiary": "Fe (Extraverted Feeling): Kemampuan diplomasi persuasif dan pembacaan dinamika audiensi saat mempresentasikan konsep.",
            "inferior": "Si (Introverted Sensing): Kepatuhan terhadap prosedur berulang dan dokumentasi terperinci. Cenderung merasa terkekang oleh protokol operasional yang kaku."
        },
        "strengths_blindspots": {
            "strengths": "Kecerdasan dialektis tinggi, kemampuan adaptasi instan terhadap skenario dinamis, dan ketajaman dalam mengidentifikasi kelemahan mendasar dalam suatu sistem.",
            "blindspots": "Penurunan motivasi ketika fase inisiasi konseptual berganti ke fase pemeliharaan rutin, serta kecenderungan mendebat asumsi orang lain melampaui kebutuhan praktis."
        },
        "work_style": "Membutuhkan ritme kerja yang fleksibel dan sarat pertukaran gagasan intelektual. Paling efektif dalam peran riset, inisiasi proyek baru, strategi produk, atau pemecahan kebuntuan operasional.",
        "stress_dynamics": "Saat tertekan oleh beban administratif monoton, dapat menjadi sinis, kehilangan arah prioritas, atau terjebak kekhawatiran berlebih terhadap detail historis. Pemulihan optimal melalui diskusi brainstorming lepas dan pergantian konteks masalah.",
        "color": "#6366F1",
        "temperament": "Analis (Rational / NT)",
        "bg_tint": "#EEF2FF",
        "border_color": "#C7D2FE"
    },
    "INFJ": {
        "code": "INFJ",
        "archetype": "Sang Advokat Humanis",
        "title": "INFJ · Sang Advokat Humanis",
        "tagline": "Membaca denyut jiwa manusia di balik kata-kata, merajut visi transformasi batin dengan keteguhan prinsip yang tenang.",
        "summary": "INFJ bergerak di dunia dengan kombinasi langka antara visi idealis mendalam dan determinasi sunyi. Mereka mampu memahami motif tersembunyi orang lain hampir secara naluriah, mendedikasikan energi mereka untuk menolong sesama, dan memperjuangkan nilai-nilai kemanusiaan yang berakar kuat pada integritas etika personal.",
        "avatar": "assets/avatars/infj.svg",
        "cognitive_roles": {
            "dominant": "Ni (Introverted Intuition): Persepsi konvergen terhadap motif tersembunyi, visi kemanusiaan jangka panjang, dan integrasi makna esensial di balik gejala permukaan.",
            "auxiliary": "Fe (Extraverted Feeling): Rekayasa keharmonisan interpersonal, artikulasi empati terarah, dan kepedulian aktif terhadap kesejahteraan komunitas.",
            "tertiary": "Ti (Introverted Thinking): Analisis struktural mandiri yang membedah koherensi argumen di balik keyakinan intuitif.",
            "inferior": "Se (Extraverted Sensing): Interaksi dengan beban sensoris fisik. Rentan mengalami kejenuhan lingkungan akibat overstimulasi kebisingan atau kerumunan."
        },
        "strengths_blindspots": {
            "strengths": "Kapasitas luar biasa dalam memahami kompleksitas psikologis individu, perancangan visi strategis yang berbobot etis, serta integritas dedikatif terhadap misi jangka panjang.",
            "blindspots": "Kerentanan terhadap kelelahan empati (compassion fatigue), kesulitan menetapkan batasan beban kerja pribadi, dan perfeksionisme ekspektasi yang sulit diimbangi realitas."
        },
        "work_style": "Memerlukan ruang kerja tenang dengan tujuan institusional yang selaras dengan nilai moral personal. Efektif dalam konsultasi strategis, perumusan kebijakan, kepemimpinan transformatif, dan pendampingan profesional.",
        "stress_dynamics": "Saat kewalahan emosional, cenderung menarik diri secara drastis (doorslam mode) atau menjadi terobsesi dengan keteraturan detail fisik. Pemulihan membutuhkan keheningan total, koneksi dengan alam, dan jeda tanpa tanggung jawab interpersonal.",
        "color": "#047857",
        "temperament": "Diplomat (Idealist / NF)",
        "bg_tint": "#ECFDF5",
        "border_color": "#A7F3D0"
    },
    "INFP": {
        "code": "INFP",
        "archetype": "Sang Mediator Autentik",
        "title": "INFP · Sang Mediator Autentik",
        "tagline": "Menjaga api integritas nurani di tengah bising dunia, menyuarakan keindahan makna dan empati yang murni.",
        "summary": "INFP adalah penjaga keaslian jiwa. Dipandu oleh kompas moral batin yang sangat peka, mereka selalu mencari kebenaran yang bermakna dan keindahan di tempat-tempat yang sering dilewatkan orang lain. Karya dan tindakan mereka memancarkan empati yang tulus serta apresiasi hangat terhadap keunikan setiap insan.",
        "avatar": "assets/avatars/infp.svg",
        "cognitive_roles": {
            "dominant": "Fi (Introverted Feeling): Penyelarasan batin dengan nilai-nilai kemanusiaan inti. Menilai keputusan berdasarkan keaslian motif, integritas moral, dan harmoni internal.",
            "auxiliary": "Ne (Extraverted Intuition): Penjelajahan perspektif imajinatif, simbolisme konseptual, dan keterbukaan terhadap berbagai kemungkinan alternatif.",
            "tertiary": "Si (Introverted Sensing): Penataan memori pengalaman subjektif dan apresiasi terhadap tradisi personal yang bermakna.",
            "inferior": "Te (Extraverted Thinking): Penegakan efisiensi eksternal yang kaku. Di bawah stres akut, dapat tiba-tiba bertindak menuntut atau menghakimi secara terburu-buru."
        },
        "strengths_blindspots": {
            "strengths": "Empati autentik tanpa penghakiman, orisinalitas perspektif konseptual, dan keteguhan membela prinsip-prinsip kemanusiaan yang sering terabaikan.",
            "blindspots": "Kecenderungan menunda eksekusi menunggu kondisi emosional yang ideal, kesulitan menerima kritik objektif tanpa merasa terserang secara personal, dan keengganan berhadapan dengan konflik terbuka."
        },
        "work_style": "Berkembang dalam lingkungan kerja yang menghormati otonomi individual dan memiliki misi sosial jelas. Menghindari atmosfer kompetitif agresif atau protokol yang terasa mekanistik semata.",
        "stress_dynamics": "Di bawah tekanan berat, dapat merasa terisolasi, putus asa terhadap realitas pragmatis, atau memunculkan kritik logis yang kaku terhadap rekan kerja. Pemulihan tercapai melalui ekspresi kreatif mandiri dan jeda refleksi bebas ekspektasi eksternal.",
        "color": "#059669",
        "temperament": "Diplomat (Idealist / NF)",
        "bg_tint": "#ECFDF5",
        "border_color": "#A7F3D0"
    },
    "ENFJ": {
        "code": "ENFJ",
        "archetype": "Sang Protagonis Katalisator",
        "title": "ENFJ · Sang Protagonis Katalisator",
        "tagline": "Menyalakan api potensi dalam diri orang lain, memimpin lewat ketulusan empati dan orkestrasi harmoni kolektif.",
        "summary": "ENFJ memiliki karisma hangat yang mampu menyatukan berbagai lapisan orang menuju tujuan bersama yang mulia. Mereka membaca kebutuhan emosional kelompok dengan cepat, memotivasi rekan kerja dengan ketulusan yang menggetarkan, dan membangun lingkungan di mana setiap individu merasa memiliki peran yang bernilai.",
        "avatar": "assets/avatars/enfj.svg",
        "cognitive_roles": {
            "dominant": "Fe (Extraverted Feeling): Pembacaan dinamika sosial kelompok secara akurat serta pemfasilitasan dialog yang membangun keselarasan dan kohesi tim.",
            "auxiliary": "Ni (Introverted Intuition): Pemahaman prediktif terhadap lintasan pertumbuhan potensi individu serta arah perkembangan organisasi.",
            "tertiary": "Se (Extraverted Sensing): Keterlibatan responsif dalam momentum komunikasi langsung dan manajemen presentasi publik.",
            "inferior": "Ti (Introverted Thinking): Evaluasi logis imparsial. Pada kondisi lelah berkepanjangan, rentan merasa bingung saat menghadapi keputusan rasional yang bertentangan dengan harmoni sosial."
        },
        "strengths_blindspots": {
            "strengths": "Kemampuan artikulasi inspiratif, kepekaan terhadap kebutuhan perkembangan orang lain, serta dedikasi tinggi dalam menciptakan kultur kolaborasi yang inklusif.",
            "blindspots": "Kecenderungan mengorbankan kesejahteraan pribadi demi memenuhi ekspektasi lingkungan, resistensi terhadap konfrontasi yang memecah konsensus, dan potensi memaksakan apa yang dianggap terbaik bagi orang lain."
        },
        "work_style": "Sangat efektif dalam kepemimpinan organisasi, manajemen sumber daya manusia, edukasi, dan fasilitasi program strategis. Memerlukan interaksi tim yang terbuka dan umpan balik yang konstruktif.",
        "stress_dynamics": "Saat kehabisan cadangan emosional, dapat menjadi cemas berlebih terhadap persepsi publik atau bersikap defensif. Pemulihan memerlukan pembatasan keterlibatan sosial dan alokasi waktu tenang untuk evaluasi diri secara objektif.",
        "color": "#065F46",
        "temperament": "Diplomat (Idealist / NF)",
        "bg_tint": "#ECFDF5",
        "border_color": "#A7F3D0"
    },
    "ENFP": {
        "code": "ENFP",
        "archetype": "Sang Juru Kampanye Eksploratif",
        "title": "ENFP · Sang Juru Kampanye Eksploratif",
        "tagline": "Menghubungkan titik-titik kemungkinan dengan antusiasme menular, melihat keajaiban dalam potensi setiap manusia.",
        "summary": "Energi seorang ENFP bagaikan percikan listrik yang menyulut inspirasi di sekitarnya. Penuh rasa ingin tahu dan keterbukaan hati, mereka gemar menelusuri gagasan baru, merangkul perspektif yang berbeda, dan merajut jalinan relasi yang hangat serta penuh harapan akan masa depan yang lebih baik.",
        "avatar": "assets/avatars/enfp.svg",
        "cognitive_roles": {
            "dominant": "Ne (Extraverted Intuition): Persepsi cepat terhadap pola peluang baru dan artikulasi berbagai kemungkinan inovatif yang menghubungkan disiplin ilmu berbeda.",
            "auxiliary": "Fi (Introverted Feeling): Penapisan ide berdasarkan resonansi etis dan keaslian nilai personal yang mendalam.",
            "tertiary": "Te (Extraverted Thinking): Penataan rencana aksi terstruktur saat mengeksekusi proyek yang memiliki signifikansi personal tinggi.",
            "inferior": "Si (Introverted Sensing): Penanganan detail administratif berulang. Rentan merasa kelelahan saat dituntut menjaga kepatuhan prosedural harian tanpa variasi."
        },
        "strengths_blindspots": {
            "strengths": "Kreativitas konseptual yang tinggi, adaptabilitas luar biasa terhadap perubahan konteks, serta kepiawaian dalam membangun jembatan kolaborasi antardisiplin.",
            "blindspots": "Kecenderungan memulai inisiatif baru sebelum menuntaskan implementasi inisiatif sebelumnya, estimasi waktu yang kerap terlalu optimistik, dan resistensi terhadap tugas pemeliharaan rutin."
        },
        "work_style": "Membutuhkan kebebasan mengeksplorasi metodologi pemecahan masalah dengan batasan birokrasi minimal. Sangat produktif dalam lingkungan yang merayakan inovasi, iterasi cepat, dan pertukaran gagasan lintas fungsi.",
        "stress_dynamics": "Saat terjebak dalam rutinitas mekanis tanpa stimulasi mental, dapat menjadi hiperkritis terhadap diri sendiri dan meragukan kompetensi dasarnya. Pemulihan diperoleh melalui dialog eksploratif dengan lingkaran terpercaya dan pengurangan beban administratif jangka pendek.",
        "color": "#10B981",
        "temperament": "Diplomat (Idealist / NF)",
        "bg_tint": "#ECFDF5",
        "border_color": "#A7F3D0"
    },
    "ISTJ": {
        "code": "ISTJ",
        "archetype": "Sang Inspektur Berdedikasi",
        "title": "ISTJ · Sang Inspektur Berdedikasi",
        "tagline": "Menjadi jangkar kestabilan dunia dengan kedisiplinan tanpa cela, ketelitian fakta, dan komitmen yang tak pernah goyah.",
        "summary": "ISTJ adalah benteng keandalan dalam setiap organisasi. Mereka berpegang pada fakta terverifikasi, menghormati aturan yang terbukti efektif, dan menyelesaikan setiap kewajiban dengan dedikasi penuh. Tanpa perlu banyak bicara, hasil kerja mereka menjadi standar kepastian dan kualitas yang menopang sistem.",
        "avatar": "assets/avatars/istj.svg",
        "cognitive_roles": {
            "dominant": "Si (Introverted Sensing): Pengorganisasian memori institusional, rujukan preseden empiris yang solid, dan konsistensi operasional berstandar tinggi.",
            "auxiliary": "Te (Extraverted Thinking): Penerapan proses logis yang teratur, penjadwalan efisien, dan pengukuran hasil kerja berbasis metrik objektif.",
            "tertiary": "Fi (Introverted Feeling): Loyalitas prinsipil yang tenang terhadap tanggung jawab dan komitmen yang telah disepakati.",
            "inferior": "Ne (Extraverted Intuition): Adaptasi terhadap disrupsi tak terduga. Di bawah tekanan krisis, rentan mencemaskan kemungkinan terburuk secara berlebihan."
        },
        "strengths_blindspots": {
            "strengths": "Keandalan luar biasa dalam menjaga kesinambungan operasional, ketelitian data tingkat tinggi, dan dedikasi tak tergoyahkan terhadap kepatuhan standar profesional.",
            "blindspots": "Resistensi terhadap perubahan metodologi yang belum memiliki riwayat keberhasilan terbukti, serta kecenderungan bersikap skeptis terhadap inovasi yang bersifat spekulatif."
        },
        "work_style": "Berkinerja optimal dalam organisasi dengan rantai komando yang jelas, deskripsi tugas definitif, dan parameter kesuksesan yang terukur secara transparan.",
        "stress_dynamics": "Saat menghadapi kekacauan struktural atau ambiguitas arahan yang berkepanjangan, dapat menjadi kaku atau terpaku pada detail minoritas. Pemulihan membutuhkan pemulihan keteraturan lingkungan kerja dan penugasan yang memiliki batas waktu jelas.",
        "color": "#0369A1",
        "temperament": "Pengawal (Sentinel / SJ)",
        "bg_tint": "#F0F9FF",
        "border_color": "#BAE6FD"
    },
    "ISFJ": {
        "code": "ISFJ",
        "archetype": "Sang Pelindung Setia",
        "title": "ISFJ · Sang Pelindung Setia",
        "tagline": "Merawat harmoni dan kebutuhan sesama dengan kehangatan tanpa pamrih, ketelitian praktis, dan kesetiaan yang kokoh.",
        "summary": "Kebaikan hati seorang ISFJ selalu berwujud aksi konkret. Mereka mengingat detail kecil tentang preferensi orang lain, sigap menyediakan dukungan logistik di balik layar, dan menjaga stabilitas lingkungan kerja dengan kelembutan yang menenteramkan tanpa pernah menuntut sorotan panggung.",
        "avatar": "assets/avatars/isfj.svg",
        "cognitive_roles": {
            "dominant": "Si (Introverted Sensing): Retensi memori operasional yang terperinci dan kepatuhan cermat terhadap protokol yang telah teruji efektivitasnya.",
            "auxiliary": "Fe (Extraverted Feeling): Responsivitas tinggi terhadap kebutuhan logistik dan emosional lingkungan kerja demi menjaga kestabilan tim.",
            "tertiary": "Ti (Introverted Thinking): Analisis pragmatis mandiri guna memastikan bahwa setiap langkah penanganan masalah berjalan efisien.",
            "inferior": "Ne (Extraverted Intuition): Antisipasi ketidakpastian masa depan. Rentan merasa kewalahan saat dihadapkan pada restrukturisasi besar yang mendadak."
        },
        "strengths_blindspots": {
            "strengths": "Dedikasi kerja yang konsisten, ketelitian luar biasa terhadap kebutuhan detail operasional, dan kesetiaan menjaga kesinambungan kultur kerja yang sehat.",
            "blindspots": "Kecenderungan menanggung beban kerja melampaui kapasitas demi menghindari mengecewakan pihak lain, keengganan mendelegasikan tugas, dan kesulitan menyuarakan ketidaksetujuan secara terbuka."
        },
        "work_style": "Paling produktif dalam lingkungan yang stabil, suportif, dan terorganisir dengan rapi. Memberikan kontribusi signifikan dalam peran manajemen proses, administrasi terpadu, dan koordinasi layanan.",
        "stress_dynamics": "Saat kelelahan kronis melanda akibat beban akumulatif, dapat memendam kekecewaan mendalam atau mencemaskan skenario risiko secara tidak rasional. Pemulihan membutuhkan pembagian beban tugas yang tegas, apresiasi yang tulus, dan istirahat tanpa gangguan pekerjaan.",
        "color": "#0284C7",
        "temperament": "Pengawal (Sentinel / SJ)",
        "bg_tint": "#F0F9FF",
        "border_color": "#BAE6FD"
    },
    "ESTJ": {
        "code": "ESTJ",
        "archetype": "Sang Eksekutif Pengarah",
        "title": "ESTJ · Sang Eksekutif Pengarah",
        "tagline": "Menegakkan keteraturan dan efisiensi operasional dengan kepemimpinan nyata yang menghargai akuntabilitas dan hasil terukur.",
        "summary": "ESTJ adalah penggerak roda tata kelola yang tangkas dan tegas. Mereka melihat kekacauan sebagai panggilan tugas untuk menertibkan, membagi peran secara proporsional, dan memastikan setiap target selesai tepat waktu dengan kualitas standar profesional tanpa kompromi.",
        "avatar": "assets/avatars/estj.svg",
        "cognitive_roles": {
            "dominant": "Te (Extraverted Thinking): Penegakan standar operasional, alokasi sumber daya yang optimal, dan penuntasan target melalui sistematika kerja yang teruji.",
            "auxiliary": "Si (Introverted Sensing): Penerapan tata kelola berbasis preseden terbaik, dokumentasi regulasi, dan konsistensi kepatuhan prosedural.",
            "tertiary": "Ne (Extraverted Intuition): Fleksibilitas dalam mengevaluasi solusi taktis ketika metode baku menemui kendala praktis di lapangan.",
            "inferior": "Fi (Introverted Feeling): Kesadaran emosional personal. Rentan mengabaikan dampak emosional dari keputusan administratif terhadap dinamika individu."
        },
        "strengths_blindspots": {
            "strengths": "Kepemimpinan operasional yang kokoh, kejelasan dalam delegasi dan penegakan akuntabilitas, serta efisiensi tinggi dalam menertibkan proses kerja yang kacau.",
            "blindspots": "Kecenderungan memaksakan keseragaman metode kerja tanpa mempertimbangkan gaya individu, minimnya toleransi terhadap kekeliruan pemula, dan komunikasi yang terkadang terkesan terlalu lugas."
        },
        "work_style": "Menyukai lingkungan kerja profesional berstruktur hierarkis dengan wewenang proporsional terhadap tanggung jawab. Menghargai profesionalisme tepat waktu, integritas data, dan pelaporan yang ringkas.",
        "stress_dynamics": "Di bawah stres tinggi akibat inefisiensi tim atau ketidakpatuhan aturan, dapat menjadi teramat mengendalikan atau bereaksi defensif secara emosional. Pemulihan menuntut delegasi beban kerja secara terukur dan rehat sementara dari tanggung jawab supervisi langsung.",
        "color": "#075985",
        "temperament": "Pengawal (Sentinel / SJ)",
        "bg_tint": "#F0F9FF",
        "border_color": "#BAE6FD"
    },
    "ESFJ": {
        "code": "ESFJ",
        "archetype": "Sang Konsul Pengayom",
        "title": "ESFJ · Sang Konsul Pengayom",
        "tagline": "Merajut kehangatan komunitas dengan kepedulian aktif, memastikan setiap orang merasa dihargai, didengar, dan terhubung.",
        "summary": "ESFJ adalah perekat sosial sejati. Dengan intuisi hubungan yang peka dan keterampilan organisasi yang rapi, mereka memastikan dinamika tim berjalan hangat dan selaras. Bagi mereka, kesuksesan sejati adalah ketika seluruh anggota kelompok maju bersama dalam suasana persaudaraan yang rukun.",
        "avatar": "assets/avatars/esfj.svg",
        "cognitive_roles": {
            "dominant": "Fe (Extraverted Feeling): Penyelarasan relasi antarpribadi dalam kelompok, pemastian terpenuhinya kebutuhan anggota tim, dan penciptaan lingkungan kerja yang inklusif.",
            "auxiliary": "Si (Introverted Sensing): Penyelenggaraan prosedur operasional harian yang tertib berlandaskan kebiasaan kerja yang solid dan dapat diandalkan.",
            "tertiary": "Ne (Extraverted Intuition): Keterbukaan terhadap ide-ide baru yang dapat meningkatkan kenyamanan dan kolaborasi bersama.",
            "inferior": "Ti (Introverted Thinking): Evaluasi sistematis yang independen dari pertimbangan emosional. Rentan merasa tertekan saat harus menyampaikan kritik murni yang berpotensi melukai hubungan."
        },
        "strengths_blindspots": {
            "strengths": "Kecerdasan interpersonal yang tinggi, keandalan dalam memfasilitasi kebutuhan bersama, dan kemampuan menggalang solidaritas tim secara berkelanjutan.",
            "blindspots": "Sensitivitas tinggi terhadap kritik kinerja atau penolakan sosial, kecenderungan menghindari konflik krusial demi keharmonisan semu, dan ketergantungan pada validasi eksternal."
        },
        "work_style": "Sangat produktif dalam peran yang membutuhkan interaksi langsung, koordinasi acara, hubungan masyarakat, dan manajemen layanan. Membutuhkan atmosfer kerja yang saling menghargai.",
        "stress_dynamics": "Saat terjadi perpecahan interpersonal di lingkungan kerja, dapat mengalami kecemasan akut dan rasa bersalah yang tidak proporsional. Pemulihan memerlukan penegasan batas peran pribadi dan penerimaan bahwa tidak semua friksi sosial merupakan tanggung jawab pribadinya.",
        "color": "#0EA5E9",
        "temperament": "Pengawal (Sentinel / SJ)",
        "bg_tint": "#F0F9FF",
        "border_color": "#BAE6FD"
    },
    "ISTP": {
        "code": "ISTP",
        "archetype": "Sang Virtuoso Teknis",
        "title": "ISTP · Sang Virtuoso Teknis",
        "tagline": "Menjinakkan kekacauan teknis dengan ketenangan pikiran, ketangkasan instrumen, dan penguasaan metode di lapangan.",
        "summary": "Tenang, observatif, dan sangat pragmatis. ISTP memahami cara kerja benda dan sistem lewat eksperimen langsung. Saat krisis teknis melanda, mereka adalah figur pertama yang turun tangan dengan kepala dingin, membongkar masalah hingga ke akar fisiknya, dan memulihkan fungsi dengan presisi hemat energi.",
        "avatar": "assets/avatars/istp.svg",
        "cognitive_roles": {
            "dominant": "Ti (Introverted Thinking): Pemahaman analitis internal mengenai mekanisme kerja suatu sistem. Membedah komponen untuk menemukan efisiensi fungsional tertinggi.",
            "auxiliary": "Se (Extraverted Sensing): Pengamatan tajam terhadap dinamika fisik real-time, memungkinkan respons taktis yang presisi saat menghadapi anomali operasional.",
            "tertiary": "Ni (Introverted Intuition): Pengenalan pola laten yang membantu memprediksi jalur penyelesaian masalah teknis yang tidak konvensional.",
            "inferior": "Fe (Extraverted Feeling): Komunikasi emosional sosial. Cenderung merasa lelah oleh protokol sosial formal atau tuntutan ekspresi emosional yang intens."
        },
        "strengths_blindspots": {
            "strengths": "Ketenangan luar biasa dalam situasi darurat, kapabilitas pemecahan masalah teknis secara langsung (troubleshooting), dan efisiensi tindakan tanpa pemborosan energi.",
            "blindspots": "Keengganan terhadap komitmen jangka panjang yang kaku, kecenderungan bersikap tertutup dalam komunikasi tim, dan kurangnya perhatian terhadap dampak emosional dari respons analitisnya."
        },
        "work_style": "Membutuhkan kebebasan kerja tanpa intervensi mikromanajemen, berorientasi pada penyelesaian masalah konkret daripada perdebatan teoritis abstrak. Unggul dalam rekayasa sistem, investigasi anomali, dan operasional lapangan.",
        "stress_dynamics": "Saat dipaksa beroperasi dalam birokrasi berbelit atau lingkungan yang sarat drama sosial, dapat menarik diri total atau melontarkan kritik pedas secara impulsif. Pemulihan optimal melalui aktivitas fisik mandiri atau eksplorasi proyek teknis mandiri.",
        "color": "#B45309",
        "temperament": "Penjelajah (Explorer / SP)",
        "bg_tint": "#FFFBEB",
        "border_color": "#FDE68A"
    },
    "ISFP": {
        "code": "ISFP",
        "archetype": "Sang Seniman Autentik",
        "title": "ISFP · Sang Seniman Autentik",
        "tagline": "Menerjemahkan getaran rasa ke dalam estetika hidup yang mengalir, selaras dengan nilai nurani tanpa kepura-puraan.",
        "summary": "ISFP menghidupi keindahan secara bersahaja. Mereka memiliki kepekaan sensoris dan estetika yang lembut, memandang dunia lewat lensa orisinalitas yang damai. Tanpa dorongan untuk mendominasi, kehadiran mereka membawa ketenangan dan warna autentik ke dalam ruang mana pun mereka berada.",
        "avatar": "assets/avatars/isfp.svg",
        "cognitive_roles": {
            "dominant": "Fi (Introverted Feeling): Penilaian berbasis keaslian moral dan nilai personal yang dipegang teguh secara privat tanpa dorongan untuk memaksakannya kepada orang lain.",
            "auxiliary": "Se (Extraverted Sensing): Keterlibatan mendalam dengan detail sensoris, tekstur, ruang, dan momentum pengalaman saat ini.",
            "tertiary": "Ni (Introverted Intuition): Pembentukan wawasan intuitif mengenai arah perkembangan situasi secara bertahap.",
            "inferior": "Te (Extraverted Thinking): Penegakan struktur organisasi eksternal. Rentan merasa tertekan saat dituntut menyusun perencanaan birokratis jangka panjang yang kaku."
        },
        "strengths_blindspots": {
            "strengths": "Kepekaan estetika yang halus, integritas batin yang autentik, keterbukaan pikiran tanpa menghakimi, dan kemampuan adaptasi yang tenang terhadap situasi nyata.",
            "blindspots": "Kecenderungan menghindari negosiasi batas kerja yang tegas, kesulitan menyusun strategi jangka panjang yang sistematis, dan keengganan menghadapi konfrontasi argumen terbuka."
        },
        "work_style": "Bekerja paling optimal dalam ruang kerja yang fleksibel dengan atmosfer yang tidak menekan. Berkontribusi luar biasa dalam bidang desain visual, arsitektur interior, pemulihan kesehatan, dan seni terapan.",
        "stress_dynamics": "Saat berada di bawah tekanan target agresif atau atmosfer yang tidak selaras dengan nilainya, cenderung menutup diri atau meragukan seluruh hasil karyanya. Pemulihan dicapai melalui kontak langsung dengan keindahan alam, kegiatan manual tanpa tenggat, dan ruang privasi yang aman.",
        "color": "#D97706",
        "temperament": "Penjelajah (Explorer / SP)",
        "bg_tint": "#FFFBEB",
        "border_color": "#FDE68A"
    },
    "ESTP": {
        "code": "ESTP",
        "archetype": "Sang Pengusaha Responsif",
        "title": "ESTP · Sang Pengusaha Responsif",
        "tagline": "Menembus dinamika krisis dengan keberanian aksi seketika, membaca peluang lapangan, dan ketahanan fisik berenergi tinggi.",
        "summary": "ESTP adalah ahli navigasi momentum seketika. Mereka membaca lingkungan fisik dan sosial dengan kecepatan kilat, berani mengambil risiko yang telah diperhitungkan, dan mengatasi hambatan di lapangan dengan akal praktis serta semangat kompetisi yang menyala.",
        "avatar": "assets/avatars/estp.svg",
        "cognitive_roles": {
            "dominant": "Se (Extraverted Sensing): Penyerapan data empiris langsung dari lingkungan fisik secara tajam, tangkas memanfaatkan peluang nyata tanpa keraguan.",
            "auxiliary": "Ti (Introverted Thinking): Kalkulasi risiko logis yang berlangsung seketika di balik setiap tindakan pragmatis.",
            "tertiary": "Fe (Extraverted Feeling): Kemampuan negosiasi dan diplomasi situasional guna menggerakkan orang lain menuju kesepakatan praktis.",
            "inferior": "Ni (Introverted Intuition): Pemikiran konseptual spekulatif jangka panjang. Cenderung tidak sabar terhadap teori yang tidak memiliki relevansi instan di lapangan."
        },
        "strengths_blindspots": {
            "strengths": "Keberanian mengambil keputusan cepat dalam kondisi ketidakpastian tinggi, ketahanan mental menghadapi krisis langsung, dan keahlian persuasi situasional.",
            "blindspots": "Impulsivitas yang berpotensi mengabaikan konsekuensi jangka panjang, intoleransi terhadap perencanaan teoritis mendalam, dan kebosanan cepat terhadap fase pemeliharaan sistem yang stabil."
        },
        "work_style": "Membutuhkan ritme kerja yang dinamis, penuh tantangan nyata, dan memberikan keleluasaan manuver langsung. Sangat efektif dalam manajemen krisis, negosiasi komersial, operasi lapangan, dan inisiatif wirausaha.",
        "stress_dynamics": "Saat terkurung dalam tugas administratif tanpa aksi langsung, dapat menunjukkan perilaku berisiko berlebihan atau mengalami kecemasan spekulatif yang tidak proporsional. Pemulihan membutuhkan keterlibatan fisik aktif, kemenangan taktis jangka pendek, dan ruang gerak yang leluasa.",
        "color": "#92400E",
        "temperament": "Penjelajah (Explorer / SP)",
        "bg_tint": "#FFFBEB",
        "border_color": "#FDE68A"
    },
    "ESFP": {
        "code": "ESFP",
        "archetype": "Sang Penghibur Karismatik",
        "title": "ESFP · Sang Penghibur Karismatik",
        "tagline": "Menghidupkan setiap ruangan dengan spontanitas hangat, merayakan keindahan momen sekarang, dan membagikan energi positif.",
        "summary": "Bagi ESFP, kehidupan adalah panggung perayaan yang patut dinikmati bersama. Mereka menularkan kegembiraan ke mana pun mereka melangkah, peka terhadap suasana hati orang-orang di sekitar, dan terampil mengubah situasi monoton menjadi pengalaman interaktif yang penuh tawa dan kebersamaan.",
        "avatar": "assets/avatars/esfp.svg",
        "cognitive_roles": {
            "dominant": "Se (Extraverted Sensing): Keterlibatan penuh dengan momen nyata, penyerapan estetika lingkungan, dan penciptaan pengalaman sensoris yang bermakna bagi audiens.",
            "auxiliary": "Fi (Introverted Feeling): Kompas etika internal yang memastikan bahwa keterlibatan sosial tetap berpijak pada ketulusan dan kepedulian manusiawi.",
            "tertiary": "Te (Extraverted Thinking): Penerapan keteraturan praktis untuk mewujudkan ide konkret menjadi kenyataan yang terlihat.",
            "inferior": "Ni (Introverted Intuition): Analisis kemungkinan implisit jangka panjang. Rentan merasa terbebani oleh ramalan atau prediksi teoritis yang bernada pesimistis."
        },
        "strengths_blindspots": {
            "strengths": "Kapasitas menyatukan kelompok secara organik, antusiasme yang membangun moral tim, serta kepekaan tinggi dalam membaca kebutuhan langsung dari audiens atau klien.",
            "blindspots": "Penghindaran terhadap diskursus konflik yang berat, kesulitan mempertahankan fokus pada administrasi jangka panjang, dan kecenderungan mengutamakan kenyamanan saat ini dibanding keberlanjutan masa depan."
        },
        "work_style": "Berkembang dalam lingkungan kerja yang interaktif, terbuka, dan kolaboratif. Sangat efektif dalam representasi merek, fasilitasi pelatihan publik, manajemen komunitas, dan sektor layanan primer.",
        "stress_dynamics": "Saat menghadapi isolasi sosial atau tekanan birokrasi yang membatasi spontanitas, dapat menjadi cemas dan merasa tidak berdaya terhadap masa depan. Pemulihan memerlukan koneksi interpersonal yang autentik, aktivitas fisik yang menyenangkan, dan pelepasan beban tanggung jawab sementara.",
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
        "tagline": "Profil hasil evaluasi arsitektur kognitif.",
        "summary": "Kombinasi proses berpikir dan orientasi adaptasi yang memandu tindakan Anda.",
        "avatar": "assets/avatars/intj.svg",
        "cognitive_roles": {
            "dominant": "Fungsi utama dalam mengarahkan orientasi kesadaran mental.",
            "auxiliary": "Fungsi pendukung dalam menjaga keseimbangan persepsi dan evaluasi.",
            "tertiary": "Fungsi penyangga dalam konteks pemulihan dan aktivitas relaksatif.",
            "inferior": "Fungsi paling rentan yang menjadi indikator saat terjadi kelelahan mental."
        },
        "strengths_blindspots": {
            "strengths": "Kapasitas adaptif dalam menyelesaikan tantangan fungsional.",
            "blindspots": "Area kerentanan yang memerlukan pengamatan sadar secara berkala."
        },
        "work_style": "Orientasi kerja berimbang dengan kebutuhan otonomi dan kolaborasi proporsional.",
        "stress_dynamics": "Menuntut manajemen energi yang disiplin dan ruang pemulihan yang cukup.",
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
