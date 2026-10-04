from __future__ import annotations
from typing import Dict

PROFILES: Dict[str, Dict] = {
    "INTJ": {
        "title": "INTJ — Sang Arsitek Strategi",
        "emoji": "🏛️",
        "tagline": "Visi jauh ke depan, eksekusi presisi, toleransi rendah terhadap inefisiensi.",
        "cognitive_roles": {
            "dominant": "Ni (Driver Utama) — Mesin proyeksi internal yang terus-menerus mensintesis pola dan membangun model masa depan. INTJ tidak hanya melihat apa yang ada, tapi apa yang pasti akan terjadi jika variabel tertentu bergerak.",
            "auxiliary": "Te (Co-Pilot) — Eksekutor logis yang mengubah visi Ni menjadi sistem, struktur, dan output yang terukur. Kalau Ni adalah peta, Te adalah kendaraan.",
            "tertiary": "Fi (Mode Rekreasi) — Kompas nilai personal yang sering underused. Di waktu santai, INTJ bisa sangat opinionated soal hal-hal yang benar-benar mereka pedulikan.",
            "inferior": "Se (Titik Buta) — Saat stres ekstrem, INTJ bisa lepas kendali ke sensasi fisik berlebihan atau justru freeze total karena overwhelmed oleh realitas present."
        },
        "strengths_blindspots": {
            "superpower": "Kemampuan melihat pola sistemik jangka panjang yang orang lain lewatkan. Mandiri, efisien, dan tidak mudah terbawa arus opini populer.",
            "blindspot": "Bisa tampak arogan atau dismissive karena standar intelektual yang tinggi. Sering underestimasi pentingnya buy-in emosional dari orang lain dalam eksekusi rencana."
        },
        "daily_vibe": "Deep work in blocks panjang adalah habitat asli INTJ. Lebih suka async communication, dokumentasi yang rapi, dan meeting yang ada agenda-nya. Tidak butuh validasi eksternal tapi sangat butuh otonomi.",
        "stress_response": "Saat burnout: menarik diri total, jadi hypercritical terhadap diri sendiri dan orang lain, atau justru tiba-tiba binge hal-hal yang sangat sensory (makan, scroll, olahraga ekstrim). Reset: solitude yang terstruktur, problem-solving kecil yang bisa langsung di-close, dan journaling untuk eksternalisasi loop pikiran.",
        "color": "#6C63FF"
    },
    "INTP": {
        "title": "INTP — Sang Arsitek Logika",
        "emoji": "🔬",
        "tagline": "Kalau ada celah logis di argumenmu, INTP sudah menemukannya bahkan sebelum kamu selesai bicara.",
        "cognitive_roles": {
            "dominant": "Ti (Driver Utama) — Framework internal yang terus-menerus membangun, merevisi, dan memverifikasi sistem logika secara mandiri. Kebenaran buat INTP harus konsisten secara internal, bukan hanya karena otoritas atau konsensus.",
            "auxiliary": "Ne (Co-Pilot) — Generator kemungkinan dan koneksi lintas domain. Ne adalah yang bikin INTP bisa loncat dari topik ke topik dan menemukan link yang tak terduga.",
            "tertiary": "Si (Mode Rekreasi) — Suka kembali ke hal-hal familiar dan nyaman — buku lama, genre musik yang sama, ritual kerja yang sudah terbukti.",
            "inferior": "Fe (Titik Buta) — Saat tertekan, INTP bisa tiba-tiba sangat sensitif soal apakah orang menyukai mereka atau tidak, atau justru jadi blunt tanpa filter sosial."
        },
        "strengths_blindspots": {
            "superpower": "Kemampuan dekonstruksi masalah kompleks ke elemen fundamentalnya. Objektif, tidak bias authority, dan sangat jujur dalam evaluasi intelektual.",
            "blindspot": "Prokrastinasi kronis karena selalu ada angle yang belum dianalisa. Kesulitan finalisasi dan deliver karena perfectionism yang berakar di Ti."
        },
        "daily_vibe": "Non-linear thinker. Bisa kelihatan distracted tapi otak terus jalan di background. Lebih produktif di lingkungan tanpa struktur kaku, suka rabbit hole riset dan problem-solving yang tidak ada deadline-nya.",
        "stress_response": "Saat burnout: isolasi diri dan loop di dalam kepala sendiri (ruminasi), atau ekstrem — tiba-tiba sangat perlu validasi sosial yang tidak biasanya. Reset: waktu sendiri yang gak terstruktur, biarkan diri explore hal-hal yang murni karena interest tanpa output.",
        "color": "#4ECDC4"
    },
    "ENTJ": {
        "title": "ENTJ — Sang Komandan",
        "emoji": "⚡",
        "tagline": "Sistem yang tidak efisien adalah personal insult. Visi besar, eksekusi agresif.",
        "cognitive_roles": {
            "dominant": "Te (Driver Utama) — Mengorganisir dunia eksternal menjadi sistem yang efisien dan terukur. ENTJ secara alami melihat inefisiensi dan langsung terpikir cara memperbaikinya.",
            "auxiliary": "Ni (Co-Pilot) — Visi strategis jangka panjang. Bukan hanya tau mau ke mana, tapi sudah punya roadmap 5 langkah ke depannya.",
            "tertiary": "Se (Mode Rekreasi) — Menikmati pengalaman fisik yang intens dan berkualitas: fine dining, olahraga kompetitif, travel yang well-curated.",
            "inferior": "Fi (Titik Buta) — Saat stres, ENTJ bisa menjadi sangat kaku soal nilai personal dan tidak fleksibel, atau tiba-tiba crumble kalau nilai inti mereka dilanggar."
        },
        "strengths_blindspots": {
            "superpower": "Natural leader yang bisa mobilisasi orang dan resource dengan cepat menuju tujuan. Decisive, confident, dan tidak takut konflik produktif.",
            "blindspot": "Bisa crushing orang-orang yang lebih lambat atau lebih emosional dalam prosesnya. Susah slow down dan appreciate progress kecil."
        },
        "daily_vibe": "Agenda padat, high-stakes decisions, dan environment yang challenghing adalah comfort zone ENTJ. Perlu kontrol dan authority untuk perform optimal. Tidak suka micromanagement tapi juga tidak suka ambiguitas.",
        "stress_response": "Saat burnout: jadi hypercritical dan controlling, atau tiba-tiba overwhelmed oleh perasaan yang selama ini ditekan (inferior Fi). Reset: exercise fisik intens, problem-solving dengan dampak cepat terlihat, dan space untuk reflect tanpa agenda.",
        "color": "#FF6B6B"
    },
    "ENTP": {
        "title": "ENTP — Sang Debater",
        "emoji": "💡",
        "tagline": "Devil's advocate bukan hobi — itu cara ENTP berpikir paling tajam.",
        "cognitive_roles": {
            "dominant": "Ne (Driver Utama) — Mesin eksplorasi kemungkinan yang tidak ada habisnya. ENTP melihat setiap situasi sebagai web of possibilities yang bisa dieksplor.",
            "auxiliary": "Ti (Co-Pilot) — Filter logis yang mengevaluasi dan merangkum semua kemungkinan yang Ne hasilkan. Tidak semua ide diteruskan — hanya yang lolos uji konsistensi internal.",
            "tertiary": "Fe (Mode Rekreasi) — Di waktu santai, ENTP sangat charming dan bisa sangat connect secara emosional dengan orang-orang yang mereka pedulikan.",
            "inferior": "Si (Titik Buta) — Saat tertekan, ENTP bisa jadi sangat pesimis soal masa lalu atau terjebak di nostalgia dan kebiasaan lama yang tidak produktif."
        },
        "strengths_blindspots": {
            "superpower": "Kemampuan melihat angle yang nobody else sees dan menghubungkan dots dari bidang yang sangat berbeda. Energi dan antusiasme yang genuinely contagious.",
            "blindspot": "Banyak ide, sedikit follow-through. Bored setelah problem-solving selesai — execution phase terasa membosankan. Bisa tidak sengaja mempermalukan orang saat debat."
        },
        "daily_vibe": "Butuh stimulasi intelektual konstan. Bisa hyperfocus kalau problem-nya genuinely menarik, tapi switch dengan cepat kalau sudah tidak ada novelty. Lingkungan kerja terbaik: fleksibel, banyak kolaborasi, dan toleran terhadap chaos kreatif.",
        "stress_response": "Saat burnout: jadi sarcastic dan dismissive, atau tiba-tiba rigid dan pesimis. Reset: social interaction yang stimulating, ubah problem frame dari 'harus selesai' ke 'mau eksplorasi ke mana lagi'.",
        "color": "#FFD93D"
    },
    "INFJ": {
        "title": "INFJ — Sang Advokat",
        "emoji": "🌊",
        "tagline": "Melihat manusia lebih dalam dari yang mereka lihat sendiri, dan ingin membantu mereka jadi versi terbaik.",
        "cognitive_roles": {
            "dominant": "Ni (Driver Utama) — Intuisi konvergen yang mengintegrasikan informasi dari berbagai sumber menjadi satu insight yang dalam. INFJ sering 'tahu' sesuatu tanpa bisa explain kenapa.",
            "auxiliary": "Fe (Co-Pilot) — Sangat peka terhadap dinamika emosional kelompok. INFJ secara natural calibrate komunikasi dan approach mereka untuk sesuai dengan kebutuhan orang di sekitar.",
            "tertiary": "Ti (Mode Rekreasi) — Suka menganalisa sistem dan konsep secara mendalam di waktu sendiri. Bisa sangat perfectionistic soal konsistensi internal argumen.",
            "inferior": "Se (Titik Buta) — Saat stres, bisa jadi sangat kaku dan perfectionistic soal hal-hal fisik dan detail, atau justru lepas kontrol ke sensasi berlebihan."
        },
        "strengths_blindspots": {
            "superpower": "Empati yang dalam dikombinasi dengan visi sistemik — langka dan powerful. Kemampuan membaca orang dan situasi yang sering terasa 'supernatural' bagi orang lain.",
            "blindspot": "Burnout dari absorbing too much dari orang lain. Susah set boundaries karena genuinely peduli dan takut mengecewakan. Bisa jadi perfectionistic sampai paralysis."
        },
        "daily_vibe": "Butuh makna di balik pekerjaan — tidak bisa sustain long-term di lingkungan yang terasa shallow atau tidak aligned dengan values. Deep work solo diselingi meaningful 1-on-1 adalah ritme idealnya.",
        "stress_response": "Saat burnout: isolasi total, overwhelmed oleh sensory input, dan jadi sangat self-critical. Reset: nature, creative expression (menulis/melukis), dan percakapan mendalam dengan orang yang genuinely dipercaya.",
        "color": "#A29BFE"
    },
    "INFP": {
        "title": "INFP — Sang Mediator",
        "emoji": "🌸",
        "tagline": "Dunia terlihat berbeda kalau dilihat dari sudut pandang INFP — lebih dalam, lebih bermakna, lebih penuh kemungkinan.",
        "cognitive_roles": {
            "dominant": "Fi (Driver Utama) — Kompas nilai internal yang sangat kuat dan personal. INFP tahu apa yang penting buat mereka, dan integritas terhadap nilai itu adalah non-negotiable.",
            "auxiliary": "Ne (Co-Pilot) — Eksplorasi kemungkinan yang kaya dan imajinatif. Bisa melihat multiple layers of meaning di balik satu kejadian.",
            "tertiary": "Si (Mode Rekreasi) — Nostalgia, ritual familiar, dan kenangan bermakna adalah sumber comfort yang genuine.",
            "inferior": "Te (Titik Buta) — Saat stres, bisa jadi hypercritical terhadap inefficiency atau tiba-tiba sangat demanding soal output dan hasil — tidak biasanya."
        },
        "strengths_blindspots": {
            "superpower": "Kreativitas dan kedalaman emosional yang genuine. Kemampuan berempati dan memahami pengalaman subjektif orang lain. Sangat authentic.",
            "blindspot": "Idealism yang bisa clash dengan realitas pragmatis. Prokrastinasi karena menunggu 'mood yang pas' atau takut hasil tidak sesuai standar internal yang tinggi."
        },
        "daily_vibe": "Butuh autonomy dan alignment antara pekerjaan dengan nilai. Creative projects, writing, dan helping professions adalah natural fit. Tidak suka struktur kaku atau lingkungan yang terlalu kompetitif.",
        "stress_response": "Saat burnout: menarik diri, merasa disalahpahami, dan jadi sangat sensitif terhadap kritik. Reset: creative outlet, alam, dan waktu sendiri yang tidak ada agenda apapun.",
        "color": "#FD79A8"
    },
    "ENFJ": {
        "title": "ENFJ — Sang Protagonis",
        "emoji": "🌟",
        "tagline": "Natural catalyst untuk pertumbuhan orang lain — ENFJ membuat orang-orang di sekitarnya jadi lebih baik tanpa terasa.",
        "cognitive_roles": {
            "dominant": "Fe (Driver Utama) — Sangat aware terhadap dinamika emosional kelompok dan secara aktif menciptakan harmony. Bisa read the room dengan akurasi yang mengagumkan.",
            "auxiliary": "Ni (Co-Pilot) — Visi jangka panjang tentang potensi orang dan situasi. ENFJ sering melihat siapa kamu bisa jadi sebelum kamu sendiri melihatnya.",
            "tertiary": "Se (Mode Rekreasi) — Menikmati pengalaman sensorik yang kaya — event, food, travel, dan aesthetic yang indah.",
            "inferior": "Ti (Titik Buta) — Saat stres, bisa jadi hypercritical secara logis terhadap diri sendiri atau orang lain, atau struggle dengan keputusan yang murni berbasis logika."
        },
        "strengths_blindspots": {
            "superpower": "Kemampuan inspire dan mobilisasi orang. Sangat charismatic dan empathetic — orang merasa genuinely diperhatikan dan dipahami.",
            "blindspot": "Sangat sensitif terhadap konflik dan criticism. Bisa neglect kebutuhan sendiri karena terlalu fokus pada kebutuhan orang lain. People pleasing yang tidak disadari."
        },
        "daily_vibe": "Thrives di lingkungan kolaboratif dengan dampak manusia yang nyata. Leadership, teaching, counseling, dan community building adalah comfort zone. Butuh appreciation dan feedback positif untuk sustain energy.",
        "stress_response": "Saat burnout: anxious, overthinking dampak setiap tindakan terhadap orang lain, atau justru jadi cold dan withdrawn. Reset: waktu sendiri yang gak ada orang yang perlu di-take care of, dan self-compassion yang intentional.",
        "color": "#00CEC9"
    },
    "ENFP": {
        "title": "ENFP — Sang Katalisator",
        "emoji": "🎨",
        "tagline": "Antusiasme yang genuinely contagious — ENFP bisa membuat hal paling biasa terasa seperti petualangan.",
        "cognitive_roles": {
            "dominant": "Ne (Driver Utama) — Explosion of possibilities dan connections. ENFP melihat potential di mana-mana — dalam ide, orang, dan situasi.",
            "auxiliary": "Fi (Co-Pilot) — Filter nilai yang deep. Meski terlihat spontan, ENFP sangat selektif soal apa yang benar-benar penting dan worth their energy.",
            "tertiary": "Te (Mode Rekreasi) — Di proyek yang benar-benar mereka passionate, bisa sangat focused dan driven untuk deliver hasil nyata.",
            "inferior": "Si (Titik Buta) — Saat tertekan, bisa terjebak di rutinitas unhealthy atau overthinking masa lalu yang tidak bisa diubah."
        },
        "strengths_blindspots": {
            "superpower": "Kreativitas yang explosive dan kemampuan connect dengan orang dari berbagai latar belakang secara genuinely. Highly adaptable dan open-minded.",
            "blindspot": "Start banyak, finish sedikit. Mudah excited tapi susah sustain energy saat fase 'boring' dari eksekusi. Bisa overpromise."
        },
        "daily_vibe": "Butuh variety, human connection, dan freedom untuk eksplorasi. Paling produktif kalau ada tujuan besar yang meaningful, tapi dengan fleksibilitas besar dalam cara mencapainya.",
        "stress_response": "Saat burnout: insecure, overthinking, dan jadi unusually self-critical. Reset: creative freedom tanpa ekspektasi output, quality time dengan inner circle, dan nature.",
        "color": "#FDCB6E"
    },
    "ISTJ": {
        "title": "ISTJ — Sang Logistik",
        "emoji": "🗂️",
        "tagline": "Reliable bukan hanya kata — itu identitas. Kalau ISTJ bilang akan deliver, itu sudah as good as done.",
        "cognitive_roles": {
            "dominant": "Si (Driver Utama) — Library internal pengalaman dan data historis yang sangat detail. ISTJ belajar dari apa yang sudah terbukti berhasil dan menerapkannya secara konsisten.",
            "auxiliary": "Te (Co-Pilot) — Sistem dan struktur untuk mengeksekusi standar Si secara efisien. ISTJ adalah orang yang membuat SOP dan memastikan semua mengikutinya.",
            "tertiary": "Fi (Mode Rekreasi) — Nilai personal yang kuat tapi jarang diekspresikan. Di dalam, ISTJ sangat peduli terhadap orang-orang yang mereka anggap dalam 'circle'.",
            "inferior": "Ne (Titik Buta) — Saat stres, bisa tiba-tiba catastrophizing semua kemungkinan buruk yang mungkin terjadi, atau sebaliknya menolak perubahan apapun."
        },
        "strengths_blindspots": {
            "superpower": "Reliabilitas, konsistensi, dan kemampuan execute dengan sangat detail-oriented. Orang tahu bisa depend on ISTJ.",
            "blindspot": "Resistansi terhadap perubahan dan cara baru yang belum terbukti. Bisa kelihatan kaku atau kurang imajinatif dalam situasi yang butuh inovasi."
        },
        "daily_vibe": "Struktur yang jelas, ekspektasi yang definite, dan lingkungan yang predictable adalah tempat ISTJ bersinar. Tidak suka surprises atau ambiguitas dalam pekerjaan.",
        "stress_response": "Saat burnout: hiperfokus pada detail yang tidak relevan, atau tiba-tiba catastrophize tentang semua yang bisa salah. Reset: routine yang familiar, task yang jelas dan segera bisa diselesaikan.",
        "color": "#636E72"
    },
    "ISFJ": {
        "title": "ISFJ — Sang Pelindung",
        "emoji": "🛡️",
        "tagline": "Tanpa banyak suara, ISFJ adalah yang paling konsisten ada saat kamu butuh.",
        "cognitive_roles": {
            "dominant": "Si (Driver Utama) — Memory detail tentang orang-orang dan pengalaman bermakna. ISFJ ingat preferensi, kebutuhan, dan momen penting orang yang mereka pedulikan.",
            "auxiliary": "Fe (Co-Pilot) — Sangat aware terhadap kebutuhan emosional orang lain. Secara natural ingin memastikan semua orang comfortable dan needs-nya terpenuhi.",
            "tertiary": "Ti (Mode Rekreasi) — Suka memahami sistem dan cara kerja hal-hal secara logis, terutama yang relevan dengan bidang yang mereka kuasai.",
            "inferior": "Ne (Titik Buta) — Saat stres, bisa jadi sangat pesimis soal masa depan dan catastrophize semua skenario buruk yang mungkin terjadi."
        },
        "strengths_blindspots": {
            "superpower": "Dedikasi, perhatian terhadap detail kebutuhan orang lain, dan konsistensi dalam merawat hubungan. Sangat trustworthy.",
            "blindspot": "Kesulitan berkata 'tidak' dan asserting own needs. Sering overwork karena tidak enak menolak permintaan bantuan."
        },
        "daily_vibe": "Bekerja paling baik dalam lingkungan yang terstruktur dan supportive. Lebih suka roles yang ada dampak langsung ke individu. Tidak suka spotlight tapi sangat reliable di balik layar.",
        "stress_response": "Saat burnout: jadi withdrawn dan passive-aggressive karena accumulated resentment. Reset: express needs secara eksplisit ke orang yang dipercaya, boundaries yang jelas, dan self-care tanpa guilt.",
        "color": "#55EFC4"
    },
    "ESTJ": {
        "title": "ESTJ — Sang Eksekutif",
        "emoji": "📋",
        "tagline": "Chaos adalah musuh. Order adalah bukan sekedar preferensi — itu standar hidup.",
        "cognitive_roles": {
            "dominant": "Te (Driver Utama) — Mengorganisir dunia eksternal secara efisien dan logis. ESTJ adalah natural administrator yang memastikan sistem berjalan sesuai aturan.",
            "auxiliary": "Si (Co-Pilot) — Bergantung pada precedent, tradisi, dan cara-cara yang sudah terbukti. 'Ini sudah berhasil sebelumnya' adalah argumen yang sangat kuat bagi ESTJ.",
            "tertiary": "Ne (Mode Rekreasi) — Di waktu santai, bisa lebih playful dan imaginative dari yang orang kira.",
            "inferior": "Fi (Titik Buta) — Saat stres, bisa jadi sangat touchy soal nilai personal atau tiba-tiba bereaksi emosional yang tidak biasanya."
        },
        "strengths_blindspots": {
            "superpower": "Kemampuan organisasi dan eksekusi yang luar biasa. Decisive, clear communicator, dan tidak takut membuat keputusan sulit.",
            "blindspot": "Bisa intimidating dan tidak fleksibel. Sulit mempertimbangkan cara yang tidak conventional meskipun konteksnya berubah."
        },
        "daily_vibe": "Sangat efektif dalam struktur hierarkis yang jelas. Thrives sebagai manager, administrator, atau leader dalam organisasi yang established. Butuh authority yang proporsional dengan tanggung jawabnya.",
        "stress_response": "Saat burnout: jadi sangat controlling dan hypercritical, atau tiba-tiba sangat emosional soal nilai personal. Reset: clear wins yang bisa segera diklaim, structure yang diperlonggar sedikit.",
        "color": "#0984E3"
    },
    "ESFJ": {
        "title": "ESFJ — Sang Konsul",
        "emoji": "🤝",
        "tagline": "Lingkungan yang harmonis bukan kebetulan — ada ESFJ yang aktif memastikannya terjaga.",
        "cognitive_roles": {
            "dominant": "Fe (Driver Utama) — Sangat oriented terhadap kebutuhan dan feelings orang lain. ESFJ secara aktif menciptakan dan menjaga harmony dalam kelompok.",
            "auxiliary": "Si (Co-Pilot) — Tradisi, kebiasaan, dan cara-cara yang sudah terbukti menjaga harmony adalah rujukan utama.",
            "tertiary": "Ne (Mode Rekreasi) — Bisa cukup creative dan open to new ideas, terutama dalam konteks yang sudah feel safe.",
            "inferior": "Ti (Titik Buta) — Saat tertekan, bisa jadi sangat kritis secara logis terhadap diri sendiri atau membuat keputusan yang tidak konsisten."
        },
        "strengths_blindspots": {
            "superpower": "Kemampuan membangun dan menjaga relasi yang hangat dan genuine. Sangat reliable dan considerate.",
            "blindspot": "Sangat bergantung pada approval eksternal. Kesulitan berhadapan dengan konflik langsung dan cenderung menghindarinya sampai jadi besar."
        },
        "daily_vibe": "Paling happy di lingkungan yang collaborative, dengan clear roles dan expressive appreciation. Teaching, healthcare, customer-facing, dan community roles adalah sweet spot.",
        "stress_response": "Saat burnout: jadi sangat khawatir soal apa yang orang pikirkan atau tiba-tiba sangat needy. Reset: affirmation dari orang yang dipercaya, routine yang familiar, dan space untuk vent.",
        "color": "#FDCB6E"
    },
    "ISTP": {
        "title": "ISTP — Sang Virtuoso",
        "emoji": "🔧",
        "tagline": "Tangan lebih cepat dari kata-kata. Kalau ada yang perlu di-fix, ISTP sudah setengah jalan menyelesaikannya.",
        "cognitive_roles": {
            "dominant": "Ti (Driver Utama) — Analisis logis internal yang terus-menerus mengevaluasi bagaimana sesuatu bekerja secara mekanis dan sistematis.",
            "auxiliary": "Se (Co-Pilot) — Sangat aware terhadap dunia fisik dan present moment. ISTP sangat skilled dalam merespons dengan tepat terhadap situasi yang berkembang real-time.",
            "tertiary": "Ni (Mode Rekreasi) — Bisa sangat focused dan strategic saat ada tujuan yang jelas dan menarik.",
            "inferior": "Fe (Titik Buta) — Saat stres, bisa tiba-tiba sangat sensitif terhadap dinamika sosial atau justru jadi sangat blunt tanpa mempertimbangkan dampaknya."
        },
        "strengths_blindspots": {
            "superpower": "Problem solver yang efektif dan calm under pressure. Kemampuan teknis dan hands-on yang sangat tinggi. Sangat adaptable.",
            "blindspot": "Sulit express perasaan atau kebutuhan. Komitmen jangka panjang terasa mengekang. Bisa kelihatan detached atau tidak peduli."
        },
        "daily_vibe": "Butuh autonomy dan variety dalam pekerjaan. Tidak suka paperwork atau meetings yang tidak perlu. Best dengan hands-on work, problem-solving teknis, dan lingkungan yang memberi freedom untuk explore.",
        "stress_response": "Saat burnout: isolasi, dismissive, atau tiba-tiba emotional outburst yang tidak biasanya. Reset: physical activity, proyek teknis yang bisa dikerjakan sendiri, dan minimum social obligation.",
        "color": "#B2BEC3"
    },
    "ISFP": {
        "title": "ISFP — Sang Petualang",
        "emoji": "🎵",
        "tagline": "Authentic sampai ke tulang. ISFP tidak bisa pura-pura peduli pada hal yang tidak bermakna baginya.",
        "cognitive_roles": {
            "dominant": "Fi (Driver Utama) — Nilai internal yang sangat kuat dan personal. ISFP tahu secara intuitif apa yang authentic bagi mereka dan tidak bisa bertoleransi dengan hal yang terasa fake.",
            "auxiliary": "Se (Co-Pilot) — Sangat present dan aware terhadap detail sensorik — beauty, texture, sound, dan atmosphere. ISFP sering sangat skilled secara artistik.",
            "tertiary": "Ni (Mode Rekreasi) — Kadang mendapat insight mendalam yang mengejutkan, terutama soal orang dan situasi.",
            "inferior": "Te (Titik Buta) — Saat stres, bisa jadi sangat kritis dan demanding soal efisiensi dan hasil, tidak biasanya bagi mereka."
        },
        "strengths_blindspots": {
            "superpower": "Sensitivitas estetik yang halus dan authentic presence yang genuinely menarik orang. Non-judgmental dan sangat open-minded.",
            "blindspot": "Sulit planning jangka panjang. Bisa terlalu menghindari konflik sampai masalah jadi menumpuk."
        },
        "daily_vibe": "Butuh freedom untuk express diri dan pekerjaan yang align dengan values. Art, music, craftsmanship, healing professions, dan apapun yang melibatkan keindahan dan care adalah natural habitat.",
        "stress_response": "Saat burnout: menarik diri, jadi sangat secretive, atau tiba-tiba hypercritical terhadap ketidakefisienan. Reset: creative expression tanpa ekspektasi, nature, dan waktu sendiri yang non-negotiable.",
        "color": "#A29BFE"
    },
    "ESTP": {
        "title": "ESTP — Sang Pengusaha",
        "emoji": "🚀",
        "tagline": "While others are still analyzing, ESTP sudah action dan sudah setengah jalan.",
        "cognitive_roles": {
            "dominant": "Se (Driver Utama) — Sangat present dan action-oriented. ESTP menyerap informasi dari lingkungan dan merespons dengan sangat cepat dan efektif.",
            "auxiliary": "Ti (Co-Pilot) — Analisis logis yang cepat dan pragmatis. ESTP bukan hanya action — mereka juga sangat sharp secara logika.",
            "tertiary": "Fe (Mode Rekreasi) — Bisa sangat charming dan socially intelligent, terutama saat mencoba memengaruhi atau meyakinkan seseorang.",
            "inferior": "Ni (Titik Buta) — Saat stres, bisa jadi sangat pesimis atau paranoid tentang masa depan dan what-if scenarios."
        },
        "strengths_blindspots": {
            "superpower": "Kemampuan berpikir dan bertindak cepat di situasi yang berubah-ubah. Risk-tolerant dan sangat effective di crisis situation.",
            "blindspot": "Boredom dengan hal-hal yang rutin dan long-term planning. Bisa impulsive dan tidak mempertimbangkan konsekuensi jangka panjang."
        },
        "daily_vibe": "Butuh stimulasi dan variety konstan. Environment yang dynamic, high-stakes, dan butuh quick decision-making adalah sweet spot. Sales, trading, emergency response, dan entrepreneurship cocok.",
        "stress_response": "Saat burnout: impulsive behavior yang ekstrem atau tiba-tiba sangat anxious tentang masa depan. Reset: physical activity, social interaction yang energizing, dan immediate small wins.",
        "color": "#E17055"
    },
    "ESFP": {
        "title": "ESFP — Sang Entertainer",
        "emoji": "🎭",
        "tagline": "Hidup terlalu singkat untuk tidak dinikmati sepenuhnya — dan ESFP mengajak semua orang ikut merasakannya.",
        "cognitive_roles": {
            "dominant": "Se (Driver Utama) — Fully immersed dalam present moment. ESFP menemukan joy dan excitement dalam pengalaman langsung dan sensory.",
            "auxiliary": "Fi (Co-Pilot) — Nilai personal yang kuat. Di balik energy sosialnya, ESFP sangat tahu apa yang penting bagi mereka dan tidak mudah dipengaruhi untuk melanggarnya.",
            "tertiary": "Te (Mode Rekreasi) — Bisa sangat organized dan efficient saat ada tujuan konkret yang mereka peduli.",
            "inferior": "Ni (Titik Buta) — Saat stres, bisa jadi sangat anxious tentang masa depan atau overthink meaning di balik setiap kejadian."
        },
        "strengths_blindspots": {
            "superpower": "Kemampuan menciptakan atmosphere yang joyful dan membuat orang merasa welcome dan seen. Sangat adaptable dan present.",
            "blindspot": "Penghindaran terhadap perencanaan jangka panjang dan konflik yang serius. Bisa kesulitan ketika harus deliver di situasi yang butuh sustained effort."
        },
        "daily_vibe": "Thrives di environment yang people-centered, dynamic, dan penuh interaksi. Performance arts, hospitality, teaching anak-anak, dan roles yang butuh human warmth adalah natural fit.",
        "stress_response": "Saat burnout: sangat anxious, overthinking, atau escape ke distraksi yang tidak sehat. Reset: social connection yang genuine, creative expression, dan physical movement.",
        "color": "#FAB1A0"
    }
}


def get_profile(mbti_type: str) -> Dict:
    return PROFILES.get(mbti_type.upper(), {
        "title": f"{mbti_type} — Tipe Unik",
        "emoji": "🧩",
        "tagline": "Hasil analisis sedang dalam pengembangan.",
        "cognitive_roles": {},
        "strengths_blindspots": {"superpower": "-", "blindspot": "-"},
        "daily_vibe": "-",
        "stress_response": "-",
        "color": "#6C63FF"
    })
