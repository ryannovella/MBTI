from __future__ import annotations
import textwrap
import time
import streamlit as st
import streamlit.components.v1 as components
from engine import PersonalityEngine, MBTIResult
from profiles import get_profile

st.set_page_config(
    page_title="MBTI Assessment · Jungian Cognitive Architecture",
    page_icon=":material/psychology:",
    layout="centered",
    initial_sidebar_state="collapsed",
)


def render_html(html: str) -> None:
    st.html(textwrap.dedent(html).strip())


APP_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700;800&display=swap');

/* ==================== DESIGN TOKENS ==================== */
:root {
    --bg-canvas: #F8FAFC;
    --surface-card: #FFFFFF;
    --surface-subtle: #F1F5F9;
    --surface-elevated: #FFFFFF;
    
    --border-light: #E2E8F0;
    --border-medium: #CBD5E1;
    --border-dark: #0F172A;
    
    --text-main: #0F172A;
    --text-body: #334155;
    --text-muted: #64748B;
    
    /* 4 Temperament Colors */
    --nt-color: #4F46E5;
    --nt-bg: #EEF2FF;
    --nt-border: #C7D2FE;
    
    --nf-color: #059669;
    --nf-bg: #ECFDF5;
    --nf-border: #A7F3D0;
    
    --sj-color: #0284C7;
    --sj-bg: #F0F9FF;
    --sj-border: #BAE6FD;
    
    --sp-color: #D97706;
    --sp-bg: #FFFBEB;
    --sp-border: #FDE68A;

    /* Radii */
    --radius-xl: 16px;
    --radius-lg: 12px;
    --radius-md: 10px;
    --radius-pill: 9999px;
    
    /* Tactile Shadows */
    --shadow-soft: 0 1px 3px 0 rgba(15, 23, 42, 0.04), 0 1px 2px -1px rgba(15, 23, 42, 0.04);
    --shadow-card: 0 4px 8px -2px rgba(15, 23, 42, 0.06), 0 2px 4px -2px rgba(15, 23, 42, 0.04);
    --shadow-lift: 0 12px 22px -4px rgba(15, 23, 42, 0.09), 0 4px 8px -2px rgba(15, 23, 42, 0.04);
    --shadow-glow: 0 0 0 3px rgba(15, 23, 42, 0.08);
}

/* Global Typography & Layout */
html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: var(--text-main) !important;
    background-color: var(--bg-canvas) !important;
}

header, footer, [data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu {
    display: none !important;
}

.main .block-container {
    padding: 2.2rem 1.2rem 4.5rem !important;
    max-width: 760px !important;
}

/* ==================== HERO & CONTAINER CARDS ==================== */
.hero-box {
    background: var(--surface-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-xl);
    box-shadow: var(--shadow-card);
    padding: 2.3rem 2rem 2.1rem;
    text-align: center;
    margin-bottom: 1.25rem;
    position: relative;
    overflow: hidden;
}

.hero-box::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #0F172A 0%, #334155 50%, #0F172A 100%);
}

.badge-tag-main {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.35rem 0.95rem;
    border-radius: var(--radius-pill);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    background: var(--surface-subtle);
    color: var(--text-body);
    border: 1px solid var(--border-light);
}

.feature-pill-cluster {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.55rem;
    margin-top: 1.1rem;
}

.feature-pill-item {
    font-size: 0.78rem;
    font-weight: 600;
    color: var(--text-body);
    background: #F8FAFC;
    padding: 0.3rem 0.85rem;
    border-radius: var(--radius-pill);
    border: 1px solid var(--border-light);
    box-shadow: var(--shadow-soft);
}

/* ==================== QUIZ SCENARIO CONTAINER ==================== */
.scenario-box {
    background: var(--surface-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-xl);
    padding: 1.6rem 1.8rem 1.4rem;
    box-shadow: var(--shadow-card);
    margin-bottom: 1.1rem;
    position: relative;
}

.scenario-header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.75rem;
    padding-bottom: 0.55rem;
    border-bottom: 1px solid #F1F5F9;
}

.scenario-quote-text {
    font-size: 1.12rem;
    font-weight: 700;
    line-height: 1.68;
    color: var(--text-main);
    margin: 0.5rem 0 1.15rem;
    letter-spacing: -0.015em;
}

/* ==================== TACTILE RADIO BUTTON CARDS ==================== */
div[data-testid="stRadio"] > div[role="radiogroup"] {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.85rem !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"] {
    background: var(--surface-card) !important;
    border-radius: var(--radius-lg) !important;
    border: 1.5px solid var(--border-light) !important;
    padding: 1.15rem 1.35rem !important;
    margin: 0 !important;
    cursor: pointer !important;
    transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1) !important;
    box-shadow: var(--shadow-soft) !important;
    display: flex !important;
    align-items: flex-start !important;
    gap: 0.95rem !important;
    min-height: 56px !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {
    border-color: var(--border-medium) !important;
    background: #FAFBFD !important;
    transform: translateY(-2px) !important;
    box-shadow: var(--shadow-lift) !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:active {
    transform: translateY(0) !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {
    background: #FFFFFF !important;
    border-color: var(--border-dark) !important;
    box-shadow: 0 0 0 2px var(--border-dark), var(--shadow-card) !important;
    transform: translateY(-1px) !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"] div[data-testid="stMarkdownContainer"] p {
    font-size: 0.98rem !important;
    line-height: 1.62 !important;
    color: var(--text-body) !important;
    font-weight: 500 !important;
    margin: 0 !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) div[data-testid="stMarkdownContainer"] p {
    font-weight: 700 !important;
    color: var(--text-main) !important;
}

/* ==================== BUTTON POLISH ==================== */
button[data-testid="baseButton-primary"], button[data-testid="baseButton-secondary"] {
    min-height: 48px !important;
    font-weight: 700 !important;
    font-size: 0.94rem !important;
    border-radius: var(--radius-md) !important;
    transition: all 0.16s ease !important;
}

button[data-testid="baseButton-primary"] {
    background: #0F172A !important;
    color: #FFFFFF !important;
    box-shadow: 0 2px 4px rgba(15, 23, 42, 0.12) !important;
}

button[data-testid="baseButton-primary"]:hover {
    transform: translateY(-1.5px) !important;
    box-shadow: 0 8px 18px rgba(15, 23, 42, 0.18) !important;
}

button[data-testid="baseButton-primary"]:active {
    transform: translateY(0.5px) !important;
}

button[data-testid="baseButton-secondary"]:hover {
    background: #F1F5F9 !important;
    border-color: var(--border-medium) !important;
    transform: translateY(-1px) !important;
}

/* ==================== RESULT HERO & ARCHETYPE CARD ==================== */
.result-hero-box {
    background: var(--surface-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-xl);
    box-shadow: var(--shadow-card);
    padding: 2.3rem 2rem 2.1rem;
    text-align: center;
    margin-bottom: 1.25rem;
    position: relative;
    overflow: hidden;
}

.hero-type-code {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 3.4rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1.05;
    margin: 0.35rem 0 0.25rem;
}

.result-tagline-quote {
    font-size: 1.02rem;
    color: var(--text-body);
    line-height: 1.68;
    max-width: 580px;
    margin: 0.75rem auto 0;
    font-style: italic;
    background: #F8FAFC;
    padding: 0.75rem 1.25rem;
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-soft);
}

/* ==================== SPECTRUM METER ROWS ==================== */
.spectrum-row {
    margin-bottom: 1.4rem;
}

.spectrum-row:last-child {
    margin-bottom: 0.3rem;
}

.spectrum-meta {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 0.86rem;
    margin-bottom: 0.5rem;
}

.pole-title {
    color: var(--text-muted);
    font-weight: 500;
}

.pole-title.active {
    color: var(--text-main);
    font-weight: 800;
}

.spectrum-track {
    position: relative;
    height: 11px;
    background: #E2E8F0;
    border-radius: var(--radius-pill);
    overflow: hidden;
    box-shadow: inset 0 1px 2px rgba(0,0,0,0.06);
}

.spectrum-mid-line {
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 2px;
    background: #FFFFFF;
    z-index: 2;
    transform: translateX(-50%);
}

.spectrum-bar {
    height: 100%;
    border-radius: var(--radius-pill);
    transition: width 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.badge-borderline-pill {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    background: #FEF3C7;
    color: #92400E;
    padding: 0.18rem 0.65rem;
    border-radius: var(--radius-pill);
    border: 1px solid #FDE68A;
    margin-left: 0.45rem;
}

/* ==================== 4-LAYER COGNITIVE STACK CARDS ==================== */
.cog-layer-card {
    background: var(--surface-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-lg);
    padding: 1.2rem 1.4rem;
    margin-bottom: 0.9rem;
    transition: all 0.16s ease;
    box-shadow: var(--shadow-soft);
}

.cog-layer-card:hover {
    border-color: var(--border-medium);
    box-shadow: var(--shadow-card);
    transform: translateY(-1px);
}

.cog-layer-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.35rem;
}

.cog-role-name {
    font-size: 0.74rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--text-muted);
}

.cog-symbol {
    font-family: 'Space Grotesk', monospace;
    font-size: 0.86rem;
    font-weight: 800;
    padding: 0.2rem 0.65rem;
    border-radius: 6px;
    border: 1px solid;
}

.cog-func-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 0.3rem;
}

.cog-func-desc {
    font-size: 0.91rem;
    color: var(--text-body);
    line-height: 1.65;
    margin: 0;
}

/* Keyboard hint badge */
.kbd-bar {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    font-size: 0.78rem;
    color: var(--text-muted);
    background: var(--surface-subtle);
    padding: 0.35rem 0.9rem;
    border-radius: var(--radius-pill);
    border: 1px solid var(--border-light);
    margin-top: 0.65rem;
}

.kbd-badge {
    background: #FFFFFF;
    border: 1px solid #CBD5E1;
    box-shadow: 0 1px 2px rgba(0,0,0,0.06);
    border-radius: 4px;
    padding: 0.08rem 0.45rem;
    font-family: monospace;
    font-size: 0.74rem;
    font-weight: 800;
    color: var(--text-main);
}

.copy-area-box {
    background: var(--surface-subtle);
    border-radius: var(--radius-md);
    padding: 1.15rem 1.35rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 0.84rem;
    color: var(--text-main);
    line-height: 1.68;
    border: 1px solid var(--border-light);
    user-select: all;
    margin: 0.6rem 0;
    white-space: pre-wrap;
}

@media (max-width: 640px) {
    .main .block-container {
        padding: 1.2rem 0.8rem 3.5rem !important;
    }
    .hero-box, .result-hero-box {
        padding: 1.75rem 1.25rem !important;
    }
    .scenario-box {
        padding: 1.3rem 1.2rem !important;
    }
    .scenario-quote-text {
        font-size: 1.02rem !important;
    }
    .kbd-bar {
        display: none !important;
    }
}
</style>
"""


def init_session() -> None:
    defaults = {
        "page": "home",
        "answers": {},
        "current_q": 0,
        "result": None,
        "auto_advance": True,
        "trigger_advance_for": None,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val


def render_home() -> None:
    render_html("""
    <div class="hero-box">
        <div class="badge-tag-main">Instrumen Tipologi & Arsitektur Kognitif</div>
        <h1 style="font-family:'Space Grotesk',sans-serif; font-size:2.35rem; font-weight:800; color:#0F172A; margin:0.9rem 0 0.45rem; letter-spacing:-0.035em;">
            Asesmen Spektrum MBTI
        </h1>
        <p style="font-size:1rem; color:#334155; line-height:1.7; max-width:560px; margin:0 auto;">
            Mengevaluasi preferensi mental dan dinamika 8 fungsi kognitif Carl Jung melalui 24 skenario pertimbangan terukur tanpa bias respon sosial.
        </p>
        <div class="feature-pill-cluster">
            <span class="feature-pill-item">24 Skenario Riil</span>
            <span class="feature-pill-item">8 Fungsi Kognitif Carl Jung</span>
            <span class="feature-pill-item">Spektrum 0–100% Kontinu</span>
            <span class="feature-pill-item">Deteksi Zona Ekuilibrium</span>
        </div>
    </div>
    """)

    # 3 Methodology Pillars
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.markdown("**:material/balance: Dilema Rasional**")
            st.caption("Pilihan situasi realistis yang berimbang tanpa opsi klise atau jebakan ideal.")
    with c2:
        with st.container(border=True):
            st.markdown("**:material/tune: Spektrum Kontinu**")
            st.caption("Kuantifikasi proporsional 0–100% serta deteksi ekuilibrium adaptif.")
    with c3:
        with st.container(border=True):
            st.markdown("**:material/schema: Arsitektur Kognitif**")
            st.caption("Pemetaan hierarki 4 lapisan fungsi kognitif yang memandu proses pengambilan keputusan.")

    with st.container(border=True):
        st.markdown("**:material/info: Panduan Pengerjaan**")
        st.caption(
            "• Jawab secara spontan berdasarkan kecenderungan tindakan nyata Anda sehari-hari.\n"
            "• Seluruh pilihan mencerminkan pola adaptasi manusiawi yang valid tanpa nilai benar atau salah.\n"
            "• Estimasi durasi pengerjaan: 5 hingga 7 menit. Seluruh progres tersimpan secara otomatis."
        )

    st.markdown("<div style='height:0.6rem;'></div>", unsafe_allow_html=True)
    if st.button("Mulai Asesmen", key="btn_start_quiz", type="primary", icon=":material/arrow_forward:", width="stretch"):
        st.session_state.page = "quiz"
        st.session_state.current_q = 0
        st.session_state.answers = {}
        st.rerun()


def render_quiz(engine: PersonalityEngine) -> None:
    questions = engine.get_questions()
    total = len(questions)
    answered_count = len(st.session_state.answers)
    current_idx = st.session_state.current_q
    q = questions[current_idx]
    q_id = q["id"]

    # Keyboard shortcut listener
    components.html("""
    <script>
    const pDoc = window.parent.document;
    if (!window.parent._mbti_keys_bound) {
        window.parent._mbti_keys_bound = true;
        pDoc.addEventListener('keydown', function(e) {
            if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;
            const key = e.key.toLowerCase();
            if (key === 'a' || key === '1') {
                const radios = pDoc.querySelectorAll('div[data-testid="stRadio"] label[data-baseweb="radio"]');
                if (radios.length >= 1) radios[0].click();
            } else if (key === 'b' || key === '2') {
                const radios = pDoc.querySelectorAll('div[data-testid="stRadio"] label[data-baseweb="radio"]');
                if (radios.length >= 2) radios[1].click();
            } else if (e.key === 'ArrowLeft') {
                const btns = Array.from(pDoc.querySelectorAll('button'));
                const prev = btns.find(b => b.innerText.includes('Sebelumnya'));
                if (prev) prev.click();
            } else if (e.key === 'ArrowRight') {
                const btns = Array.from(pDoc.querySelectorAll('button'));
                const next = btns.find(b => b.innerText.includes('Berikutnya'));
                if (next && !next.disabled) next.click();
            }
        });
    }
    </script>
    """, height=0, width=0)

    pct = int((answered_count / total) * 100)
    dim_map = {
        "EI": ("Mind", "Ekstraversi vs Introversi", "#4F46E5", "#EEF2FF", "#C7D2FE"),
        "SN": ("Energy", "Penginderaan vs Intuisi", "#059669", "#ECFDF5", "#A7F3D0"),
        "TF": ("Nature", "Pemikiran vs Perasaan", "#0284C7", "#F0F9FF", "#BAE6FD"),
        "JP": ("Tactics", "Penilaian vs Eksplorasi", "#D97706", "#FFFBEB", "#FDE68A"),
    }
    dim_name, dim_detail, dim_col, dim_bg, dim_bdr = dim_map.get(
        q["dim"], (q["dim"], "", "#0F172A", "#F1F5F9", "#E2E8F0")
    )

    # Header and Navigation Container
    with st.container(border=True):
        col_meta, col_jump, col_adv = st.columns([3, 1.8, 1.6], vertical_alignment="center")
        with col_meta:
            badge_html = f'<span style="background:{dim_bg}; color:{dim_col}; border:1px solid {dim_bdr}; padding:0.25rem 0.75rem; border-radius:9999px; font-size:0.75rem; font-weight:800; letter-spacing:0.04em;">{dim_name} ({q["dim"]})</span>'
            st.markdown(f"**Butir {current_idx + 1:02d} / {total:02d}** · {badge_html}", unsafe_allow_html=True)
            st.caption(dim_detail)
        with col_jump:
            with st.popover(f"Daftar Butir ({answered_count}/{total})", icon=":material/format_list_numbered:", width="stretch"):
                st.caption("Pilih butir untuk meninjau status jawaban:")
                grid_cols = st.columns(4)
                for i in range(total):
                    item_qid = questions[i]["id"]
                    is_cur = (i == current_idx)
                    is_ans = (item_qid in st.session_state.answers)
                    lbl = f"{i + 1:02d}{' •' if is_ans else ''}"
                    btn_kind = "primary" if is_cur else "secondary"
                    if grid_cols[i % 4].button(lbl, key=f"jump_{i}", type=btn_kind, width="stretch"):
                        st.session_state.current_q = i
                        st.rerun()
        with col_adv:
            auto_val = st.toggle(
                "Auto-Next",
                value=st.session_state.get("auto_advance", True),
                key="quiz_auto_adv_toggle",
                help="Otomatis beralih ke butir berikutnya setelah opsi dipilih",
            )
            st.session_state.auto_advance = auto_val

        st.progress(answered_count / total, text=f"{pct}% Selesai ({answered_count} dari {total} butir terjawab)")

    # Scenario and Choice Box
    with st.container(border=True):
        render_html(f"""
        <div style="border-left: 4px solid {dim_col}; padding-left: 0.95rem; margin-bottom: 0.85rem;">
            <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:0.25rem;">
                <span style="font-size:0.75rem; font-weight:800; color:{dim_col}; text-transform:uppercase; letter-spacing:0.06em;">
                    Skenario #{current_idx + 1:02d}
                </span>
                <span style="font-size:0.75rem; color:var(--text-muted); font-weight:700;">Dinamika: {q.get('cog_tag', '')}</span>
            </div>
            <div class="scenario-quote-text">"{q['scenario']}"</div>
        </div>
        <div style="font-size:0.84rem; font-weight:700; color:var(--text-body); margin-bottom:0.85rem;">
            Pilih respon yang paling mendekati kecenderungan spontan Anda:
        </div>
        """)

        prev_answer = st.session_state.answers.get(q_id)
        default_idx = 0 if prev_answer == "A" else (1 if prev_answer == "B" else None)

        def format_choice(val: str) -> str:
            if val == "A":
                return f"A.  {q['opt_a']['text']}"
            return f"B.  {q['opt_b']['text']}"

        def on_radio_selected() -> None:
            chosen = st.session_state.get(f"radio_q_{q_id}")
            if chosen:
                st.session_state.answers[q_id] = chosen
                if st.session_state.get("auto_advance", True):
                    st.session_state["trigger_advance_for"] = q_id

        chosen_option = st.radio(
            label=f"Pilihan Butir {q_id}:",
            options=["A", "B"],
            format_func=format_choice,
            index=default_idx,
            key=f"radio_q_{q_id}",
            label_visibility="collapsed",
            on_change=on_radio_selected,
        )

        if chosen_option:
            st.session_state.answers[q_id] = chosen_option

        render_html("""
        <div class="kbd-bar">
            <span>Pintasan Keyboard: <span class="kbd-badge">A</span> / <span class="kbd-badge">1</span> Opsi A &bull; <span class="kbd-badge">B</span> / <span class="kbd-badge">2</span> Opsi B &bull; <span class="kbd-badge">&larr;</span> <span class="kbd-badge">&rarr;</span> Navigasi</span>
        </div>
        """)

    # Auto-advance handling
    if st.session_state.get("trigger_advance_for") == q_id:
        st.session_state["trigger_advance_for"] = None
        if current_idx < total - 1:
            st.toast(f"Butir {current_idx + 1:02d} tersimpan", icon=":material/check_circle:")
            time.sleep(0.35)
            st.session_state.current_q += 1
            st.rerun()
        else:
            st.toast("Seluruh butir telah terjawab", icon=":material/task_alt:")

    st.markdown("<div style='height:0.6rem;'></div>", unsafe_allow_html=True)

    # Navigation Buttons
    c_prev, c_next = st.columns(2, gap="medium")
    with c_prev:
        if current_idx > 0:
            if st.button("Sebelumnya", key=f"btn_p_{current_idx}", type="secondary", icon=":material/arrow_back:", width="stretch"):
                st.session_state.current_q -= 1
                st.rerun()
        else:
            if st.button("Kembali ke Beranda", key="btn_home_nav", type="secondary", icon=":material/home:", width="stretch"):
                st.session_state.page = "home"
                st.rerun()

    with c_next:
        if current_idx < total - 1:
            is_answered = q_id in st.session_state.answers
            next_label = "Berikutnya" if is_answered else "Pilih satu opsi terlebih dahulu"
            if st.button(next_label, key=f"btn_n_{current_idx}", type="primary", icon=":material/arrow_forward:", disabled=not is_answered, width="stretch"):
                st.session_state.current_q += 1
                st.rerun()
        else:
            all_done = (len(st.session_state.answers) == total)
            btn_finish_label = "Lihat Hasil Analisis" if all_done else f"Jawab Seluruh Butir ({answered_count}/{total})"
            if st.button(btn_finish_label, key="btn_finish_test", type="primary", icon=":material/insights:", disabled=not all_done, width="stretch"):
                with st.spinner("Mengkalkulasi spektrum psikometrik dan arsitektur fungsi kognitif..."):
                    result = engine.compute_result(st.session_state.answers)
                    st.session_state.result = result
                    st.session_state.page = "result"
                    st.rerun()


def render_result(result: MBTIResult) -> None:
    profile = get_profile(result.mbti_type)
    theme_color = profile.get("color", "#0F172A")
    temperament = profile.get("temperament", "Tipologi Kognitif")
    bg_tint = profile.get("bg_tint", "#F1F5F9")
    border_color = profile.get("border_color", "#E2E8F0")

    # Hero Result Presentation
    render_html(f"""
    <div class="result-hero-box" style="border-top: 5px solid {theme_color};">
        <span style="background:{bg_tint}; color:{theme_color}; border:1.5px solid {border_color}; padding:0.32rem 0.95rem; border-radius:9999px; font-size:0.78rem; font-weight:800; text-transform:uppercase; letter-spacing:0.05em;">
            {temperament}
        </span>
        <div class="hero-type-code" style="color:{theme_color};">{result.mbti_type}</div>
        <h2 style="font-family:'Space Grotesk',sans-serif; font-size:1.42rem; font-weight:800; color:#0F172A; margin:0 0 0.35rem; letter-spacing:-0.02em;">
            {profile.get('title', result.mbti_type)}
        </h2>
        <div class="result-tagline-quote" style="border-left: 4px solid {theme_color};">
            "{profile.get('tagline', '')}"
        </div>
    </div>
    """)

    # Borderline Advisory
    if result.borderline_dims:
        dim_labels = {
            "EI": "Mind (Ekstraversi vs Introversi)",
            "SN": "Energy (Penginderaan vs Intuisi)",
            "TF": "Nature (Pemikiran vs Perasaan)",
            "JP": "Tactics (Penilaian vs Eksplorasi)",
        }
        bl_text = ", ".join(dim_labels.get(d, d) for d in result.borderline_dims)
        with st.container(border=True):
            st.markdown("**:material/info: Zona Ekuilibrium (Borderline Trait)**")
            st.caption(
                f"Hasil evaluasi pada dimensi **{bl_text}** berada dalam rentang ekuilibrium (47%–53%). "
                "Hal ini mencerminkan fleksibilitas kontekstual di mana Anda dapat beroperasi secara seimbang pada kedua kutub sesuai tuntutan situasi."
            )

    # Spectrum Rows Generator
    dim_pairs = {
        "EI": ("Ekstraversi (E)", "Introversi (I)", "#4F46E5"),
        "SN": ("Penginderaan (S)", "Intuisi (N)", "#059669"),
        "TF": ("Pemikiran (T)", "Perasaan (F)", "#0284C7"),
        "JP": ("Penilaian (J)", "Eksplorasi (P)", "#D97706"),
    }
    spectrum_html = ""
    for dim_code, (pos_name, neg_name, bar_col) in dim_pairs.items():
        score_obj = result.dimensions[dim_code]
        pct_pos = score_obj.pos_pct
        pct_neg = round(100.0 - pct_pos, 1)
        dom_side = pos_name if pct_pos >= 50 else neg_name
        dom_pct = pct_pos if pct_pos >= 50 else pct_neg
        bl_tag = '<span class="badge-borderline-pill">Ekuilibrium</span>' if score_obj.is_borderline else ""

        spectrum_html += f"""
        <div class="spectrum-row">
            <div class="spectrum-meta">
                <span class="pole-title {'active' if pct_pos >= 50 else ''}">{pos_name} {pct_pos:.0f}%</span>
                <div>
                    <strong style="color:#0F172A; font-size:0.9rem;">{dom_side} {dom_pct:.0f}%</strong>
                    {bl_tag}
                </div>
                <span class="pole-title {'active' if pct_neg > 50 else ''}">{neg_name} {pct_neg:.0f}%</span>
            </div>
            <div class="spectrum-track">
                <div class="spectrum-mid-line" title="Garis Keseimbangan 50%"></div>
                <div class="spectrum-bar" style="width: {pct_pos}%; background: {bar_col};"></div>
            </div>
        </div>
        """

    with st.container(border=True):
        st.markdown("**Spektrum Kontinu 4 Dimensi**")
        st.caption("Distribusi proporsional proses mental dan orientasi energi (garis tengah menandai ekuilibrium 50%):")
        render_html(spectrum_html)

    # 4 Deep-Dive Tabs
    tab_cog, tab_strength, tab_work, tab_stress = st.tabs([
        ":material/schema: Arsitektur Kognitif",
        ":material/insights: Kompetensi & Kerentanan",
        ":material/work: Modalitas Kerja",
        ":material/shield: Regulasi Stres",
    ])

    with tab_cog:
        role_meta = {
            "dominant": ("Pilar Utama (Dominant)", "Fungsi utama yang memandu keputusan sadar sehari-hari"),
            "auxiliary": ("Pemandu Sekunder (Auxiliary)", "Fungsi penyeimbang yang memperkaya perspektif pilar utama"),
            "tertiary": ("Arah Relaksasi (Tertiary)", "Fungsi pemulihan energi dan eksplorasi non-tekanan"),
            "inferior": ("Titik Buta & Stres (Inferior)", "Fungsi bawah sadar yang rentan tertekan dalam kondisi stres akut")
        }
        cog_stack = profile.get("cognitive_roles", result.cognitive_stack)
        cog_items_html = ""
        for r_key, (r_label, r_sub) in role_meta.items():
            val = cog_stack.get(r_key, result.cognitive_stack.get(r_key, "-"))
            parts = val.split(": ", 1) if ": " in val else (val, "")
            func_name = parts[0]
            func_detail = parts[1] if len(parts) > 1 else ""
            
            # Extract function abbreviation (e.g. "Ni", "Te")
            func_code = func_name.split()[0] if func_name else ""

            cog_items_html += f"""
            <div class="cog-layer-card" style="border-left: 4px solid {theme_color};">
                <div class="cog-layer-head">
                    <span class="cog-role-name">{r_label}</span>
                    <span class="cog-symbol" style="color:{theme_color}; background:{bg_tint}; border-color:{border_color};">{func_code}</span>
                </div>
                <div class="cog-func-title">{func_name}</div>
                <p class="cog-func-desc">{func_detail}</p>
            </div>
            """

        with st.container(border=True):
            st.markdown("**Hierarki 4 Lapisan Fungsi Kognitif Carl Jung**")
            st.caption("Pemetaan arsitektur mental dari fungsi yang paling sadar hingga titik buta bawah sadar:")
            render_html(cog_items_html)

    with tab_strength:
        sb = profile.get("strengths_blindspots", {})
        c_sup, c_bli = st.columns(2, gap="medium")
        with c_sup:
            with st.container(border=True):
                st.markdown("**:material/check_circle: Kompetensi Inti**")
                st.caption(sb.get("strengths", sb.get("superpower", "-")))
        with c_bli:
            with st.container(border=True):
                st.markdown("**:material/warning: Area Kerentanan**")
                st.caption(sb.get("blindspots", sb.get("blindspot", "-")))

    with tab_work:
        with st.container(border=True):
            st.markdown("**:material/hub: Modalitas Kerja & Pola Kolaborasi**")
            st.caption(profile.get("work_style", profile.get("daily_vibe", "-")))

    with tab_stress:
        with st.container(border=True):
            st.markdown("**:material/healing: Dinamika Stres & Protokol Pemulihan**")
            st.caption(profile.get("stress_dynamics", profile.get("stress_response", "-")))

    # Structured Export
    summary_text = (
        f"[LAPORAN ASESMEN TIPOLOGI MBTI]\n"
        f"Tipe: {result.mbti_type}: {profile.get('title', '')}\n"
        f"Temperamen: {temperament}\n\n"
        f"Distribusi Spektrum:\n"
        f"• Mind:    {result.dimensions['EI'].pos_pct:.0f}% Extraversion / {result.dimensions['EI'].neg_pct:.0f}% Introversion\n"
        f"• Energy:  {result.dimensions['SN'].pos_pct:.0f}% Sensing / {result.dimensions['SN'].neg_pct:.0f}% Intuition\n"
        f"• Nature:  {result.dimensions['TF'].pos_pct:.0f}% Thinking / {result.dimensions['TF'].neg_pct:.0f}% Feeling\n"
        f"• Tactics: {result.dimensions['JP'].pos_pct:.0f}% Judging / {result.dimensions['JP'].neg_pct:.0f}% Prospecting\n\n"
        f"Fungsi Dominan: {result.cognitive_stack.get('dominant', '-')}\n"
        f"Ringkasan: \"{profile.get('tagline', '')}\""
    )

    with st.container(border=True):
        st.markdown("**Unduh Laporan Asesmen**")
        st.caption("Salin ringkasan teks atau unduh dokumen evaluasi untuk keperluan arsip profesional:")
        render_html(f'<div class="copy-area-box">{summary_text}</div>')
        st.download_button(
            label="Unduh Dokumen Laporan (.txt)",
            data=summary_text,
            file_name=f"Laporan_MBTI_{result.mbti_type}.txt",
            mime="text/plain",
            icon=":material/download:",
            width="stretch"
        )

    st.markdown("<div style='height:0.6rem;'></div>", unsafe_allow_html=True)

    # Action Buttons Row
    c_ret, c_hom = st.columns(2, gap="medium")
    with c_ret:
        if st.button("Ulangi Asesmen", key="btn_repeat_test", type="primary", icon=":material/restart_alt:", width="stretch"):
            st.session_state.page = "quiz"
            st.session_state.answers = {}
            st.session_state.current_q = 0
            st.session_state.result = None
            st.rerun()
    with c_hom:
        if st.button("Kembali ke Beranda", key="btn_return_home_res", type="secondary", icon=":material/home:", width="stretch"):
            st.session_state.page = "home"
            st.session_state.answers = {}
            st.session_state.current_q = 0
            st.session_state.result = None
            st.rerun()


def main() -> None:
    render_html(APP_STYLES)
    init_session()
    engine = PersonalityEngine()

    page = st.session_state.page
    if page == "home":
        render_home()
    elif page == "quiz":
        render_quiz(engine)
    elif page == "result":
        if st.session_state.result:
            render_result(st.session_state.result)
        else:
            st.session_state.page = "home"
            st.rerun()


if __name__ == "__main__":
    main()
