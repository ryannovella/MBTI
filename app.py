from __future__ import annotations
import textwrap
import time
import streamlit as st
import streamlit.components.v1 as components
from engine import PersonalityEngine, MBTIResult
from profiles import get_profile

st.set_page_config(
    page_title="MBTI Assessment — Clinical Psychometrics",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

def render_html(html: str) -> None:
    st.html(textwrap.dedent(html).strip())


APP_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700;800&display=swap');

/* ==================== ROOT TOKENS ==================== */
:root {
    --canvas-bg: #F4F7F5;
    --card-surface: #FFFFFF;
    --card-subtle: #F7FAF8;
    
    --teal-primary: #24826B;
    --teal-hover: #1C6B58;
    --teal-light: #E8F5F1;
    --teal-border: #9ED4C7;
    
    --ocean-blue: #236B8E;
    --ocean-light: #E7F2F7;
    
    --warm-terracotta: #BA4E3E;
    --terracotta-light: #FBEFEF;
    
    --amber-gold: #B36F1C;
    --amber-light: #FDF5E8;
    
    --text-headline: #122420;
    --text-body: #283E38;
    --text-secondary: #4B6861;
    --text-muted: #66857E;
    
    --shadow-soft: 0 4px 18px rgba(18, 36, 32, 0.05), 0 1px 3px rgba(18, 36, 32, 0.04);
    --shadow-hover: 0 8px 24px rgba(36, 130, 107, 0.12), 0 2px 6px rgba(18, 36, 32, 0.04);
    --shadow-card: 0 6px 20px rgba(18, 36, 32, 0.06);
    --shadow-sunken: inset 2px 2px 5px rgba(18, 36, 32, 0.06);
    
    --radius-xl: 24px;
    --radius-lg: 18px;
    --radius-md: 14px;
    --radius-sm: 8px;
    --radius-pill: 9999px;
}

/* Base typography */
html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: var(--text-headline) !important;
}

/* Hide Streamlit default header/footer for distraction-free assessment */
header, footer, [data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu {
    display: none !important;
}

.main .block-container {
    padding: 2.2rem 1.2rem 4rem !important;
    max-width: 760px !important;
}

/* ==================== CARD COMPONENTS ==================== */
.clay-card {
    background: var(--card-surface);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-card);
    border: 1px solid rgba(226, 237, 233, 0.85);
    padding: 1.8rem 2rem;
    margin-bottom: 1.3rem;
    box-sizing: border-box;
}

.clay-hero {
    background: linear-gradient(145deg, #FFFFFF 0%, #F3F8F5 100%);
    border-radius: var(--radius-xl);
    box-shadow: var(--shadow-card);
    border: 1px solid rgba(226, 237, 233, 0.95);
    padding: 2.6rem 2rem;
    text-align: center;
    margin-bottom: 1.5rem;
}

/* ==================== BADGES & TAGS ==================== */
.badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.4rem 1.05rem;
    border-radius: var(--radius-pill);
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    background: var(--teal-light);
    color: var(--teal-primary);
    border: 1px solid var(--teal-border);
}

.badge-dim-code {
    background: var(--ocean-light);
    color: var(--ocean-blue);
    border: 1px solid rgba(35, 107, 142, 0.25);
    padding: 0.35rem 0.85rem;
    border-radius: var(--radius-pill);
    font-size: 0.76rem;
    font-weight: 800;
    letter-spacing: 0.03em;
}

/* ==================== SCENARIO CONTAINER ==================== */
.scenario-box {
    background: var(--card-subtle);
    border-radius: var(--radius-md);
    padding: 1.35rem 1.6rem;
    margin: 1rem 0 1.3rem;
    border-left: 4px solid var(--teal-primary);
    border-top: 1px solid rgba(226, 237, 233, 0.9);
    border-right: 1px solid rgba(226, 237, 233, 0.9);
    border-bottom: 1px solid rgba(226, 237, 233, 0.9);
}

.scenario-text {
    font-size: 1.08rem;
    font-weight: 600;
    color: var(--text-headline);
    line-height: 1.68;
    margin: 0;
}

/* ==================== MINI DOTS MATRIX ==================== */
.matrix-row {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    justify-content: center;
    margin-top: 0.75rem;
}

.matrix-dot {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 0.64rem;
    font-weight: 700;
    transition: all 0.2s ease;
}

.dot-done {
    background: var(--teal-primary);
    color: #FFFFFF;
}

.dot-current {
    background: #FFFFFF;
    color: var(--teal-primary);
    border: 2px solid var(--teal-primary);
    transform: scale(1.18);
    box-shadow: 0 0 0 2px var(--teal-light);
}

.dot-empty {
    background: #E5EDE9;
    color: var(--text-muted);
}

/* ==================== RADIO SELECTION CARDS ==================== */
div[data-testid="stRadio"] > div[role="radiogroup"] {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.85rem !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"] {
    background: #FFFFFF !important;
    border-radius: var(--radius-md) !important;
    border: 2px solid #E2EDE9 !important;
    padding: 1.15rem 1.4rem !important;
    margin: 0 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 2px 8px rgba(18, 36, 32, 0.03) !important;
    display: flex !important;
    align-items: flex-start !important;
    gap: 0.75rem !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {
    border-color: var(--teal-primary) !important;
    transform: translateY(-2px) !important;
    box-shadow: var(--shadow-hover) !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {
    background: var(--teal-light) !important;
    border-color: var(--teal-primary) !important;
    box-shadow: 0 4px 14px rgba(36, 130, 107, 0.16) !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"] div[data-testid="stMarkdownContainer"] p {
    font-size: 0.96rem !important;
    line-height: 1.62 !important;
    color: var(--text-headline) !important;
    font-weight: 500 !important;
    margin: 0 !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) div[data-testid="stMarkdownContainer"] p {
    font-weight: 600 !important;
    color: #0E352B !important;
}

/* ==================== SPECTRUM VISUALIZER ==================== */
.spectrum-row {
    margin-bottom: 1.35rem;
}

.spectrum-row:last-child {
    margin-bottom: 0;
}

.spectrum-meta {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 0.88rem;
    margin-bottom: 0.45rem;
}

.pole-label {
    font-weight: 600;
    color: var(--text-muted);
}

.pole-active {
    color: var(--teal-primary);
    font-size: 0.94rem;
    font-weight: 800;
}

.spectrum-track {
    height: 16px;
    background: #E2EDE9;
    border-radius: var(--radius-pill);
    overflow: hidden;
    position: relative;
    padding: 2px;
    box-sizing: border-box;
}

.spectrum-bar-fill {
    height: 100%;
    border-radius: var(--radius-pill);
    background: linear-gradient(90deg, var(--teal-primary), var(--ocean-blue));
    box-shadow: 0 1px 5px rgba(36, 130, 107, 0.35);
    transition: width 0.6s ease;
}

.borderline-badge {
    display: inline-flex;
    align-items: center;
    padding: 0.2rem 0.65rem;
    background: var(--amber-light);
    color: #8C530A;
    border-radius: var(--radius-pill);
    font-size: 0.72rem;
    font-weight: 800;
    border: 1px solid rgba(179, 111, 28, 0.35);
    margin-left: 0.5rem;
}

/* ==================== HERO RESULT & COGNITIVE ==================== */
.hero-mbti-type {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 3.8rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1.05;
    margin: 0.3rem 0;
    background: linear-gradient(135deg, var(--teal-primary), var(--ocean-blue));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
}

.cog-item-card {
    background: var(--card-subtle);
    border-radius: var(--radius-md);
    padding: 1.2rem 1.4rem;
    margin-bottom: 0.95rem;
    border-left: 5px solid var(--teal-primary);
    border-top: 1px solid rgba(226, 237, 233, 0.9);
    border-right: 1px solid rgba(226, 237, 233, 0.9);
    border-bottom: 1px solid rgba(226, 237, 233, 0.9);
    box-shadow: 0 2px 8px rgba(18, 36, 32, 0.03);
}

.cog-role-name {
    font-size: 0.74rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--teal-primary);
}

.cog-func-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-headline);
    margin: 0.25rem 0 0.35rem;
}

.cog-func-desc {
    font-size: 0.89rem;
    color: var(--text-body);
    line-height: 1.65;
    margin: 0;
}

/* Copy box */
.copy-box {
    background: #F4F8F6;
    border-radius: var(--radius-md);
    padding: 1.15rem;
    font-family: monospace;
    font-size: 0.84rem;
    color: var(--text-headline);
    line-height: 1.68;
    border: 1px solid var(--teal-border);
    user-select: all;
    margin: 0.8rem 0;
    white-space: pre-wrap;
}

/* Touch targets and mobile optimization */
button[data-testid="baseButton-primary"], button[data-testid="baseButton-secondary"] {
    min-height: 46px !important;
    font-weight: 700 !important;
    border-radius: var(--radius-md) !important;
}

.keyboard-hint {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    font-size: 0.78rem;
    color: var(--text-muted);
    background: #EAF2EE;
    padding: 0.35rem 0.85rem;
    border-radius: var(--radius-pill);
    margin-top: 0.5rem;
}

.kbd-key {
    background: #FFFFFF;
    border: 1px solid #CBDCD5;
    box-shadow: 0 1px 2px rgba(0,0,0,0.06);
    border-radius: 4px;
    padding: 0.1rem 0.4rem;
    font-family: monospace;
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--text-headline);
}

@media (max-width: 640px) {
    .main .block-container {
        padding: 1.2rem 0.75rem 3.5rem !important;
    }
    .clay-hero {
        padding: 1.8rem 1.1rem !important;
    }
    .scenario-box {
        padding: 1rem 1.1rem !important;
    }
    .scenario-text {
        font-size: 1rem !important;
    }
    div[data-testid="stRadio"] label[data-baseweb="radio"] {
        padding: 1rem 1.1rem !important;
        min-height: 52px !important;
    }
    .keyboard-hint {
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
    <div class="clay-hero">
        <div class="badge-pill">
            <span>🔬</span> Asesmen Psikometri Klinis · 8 Fungsi Carl Jung
        </div>
        <h1 style="font-family:'Space Grotesk',sans-serif; font-size:2.35rem; font-weight:800; color:var(--text-headline); margin:0.9rem 0 0.5rem; letter-spacing:-0.03em;">
            Tes Kepribadian Spektrum MBTI
        </h1>
        <p style="font-size:1.04rem; color:var(--text-body); line-height:1.68; max-width:580px; margin:0 auto;">
            Mengevaluasi dinamika kepribadian melalui <strong>24 skenario realistis</strong> yang rasional. 
            Menghitung spektrum kontinu 0–100% dan membedah dinamika 8 fungsi kognitif Jungian secara akurat.
        </p>
    </div>
    """)

    # 3 Distinct Feature Highlights
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            render_html("""
            <div style="text-align:center; padding:0.4rem 0;">
                <div style="font-size:1.8rem; margin-bottom:0.2rem;">⚖️</div>
                <div style="font-size:0.92rem; font-weight:700; color:var(--text-headline);">Non-Ekstrem</div>
                <div style="font-size:0.8rem; color:var(--text-secondary); margin-top:0.25rem;">Dilema sosial realistis & berimbang</div>
            </div>
            """)
    with c2:
        with st.container(border=True):
            render_html("""
            <div style="text-align:center; padding:0.4rem 0;">
                <div style="font-size:1.8rem; margin-bottom:0.2rem;">📊</div>
                <div style="font-size:0.92rem; font-weight:700; color:var(--text-headline);">Spektrum Kontinu</div>
                <div style="font-size:0.8rem; color:var(--text-secondary); margin-top:0.25rem;">Deteksi borderline di 47–53%</div>
            </div>
            """)
    with c3:
        with st.container(border=True):
            render_html("""
            <div style="text-align:center; padding:0.4rem 0;">
                <div style="font-size:1.8rem; margin-bottom:0.2rem;">🧠</div>
                <div style="font-size:0.92rem; font-weight:700; color:var(--text-headline);">Fungsi Jungian</div>
                <div style="font-size:0.8rem; color:var(--text-secondary); margin-top:0.25rem;">Anatomi 4 lapisan kognitif</div>
            </div>
            """)

    with st.container(border=True):
        render_html("""
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:0.7rem;">
            <span class="badge-pill">Panduan Pengerjaan</span>
            <span style="font-size:0.84rem; color:var(--text-muted); font-weight:600;">Estimasi: 5–7 menit</span>
        </div>
        <p style="font-size:0.93rem; color:var(--text-body); line-height:1.75; margin:0;">
            • Jawablah secara spontan berdasarkan kecenderungan nyata dirimu sehari-hari, bukan respon yang terkesan paling ideal.<br>
            • Tidak ada pilihan yang benar atau salah; kedua opsi mencerminkan pola adaptasi manusiawi yang valid.<br>
            • Progres kamu tersimpan secara otomatis, kamu dapat kembali meninjau butir sebelumnya kapan saja.
        </p>
        """)

    st.markdown("<div style='height:0.6rem;'></div>", unsafe_allow_html=True)
    if st.button("Mulai Asesmen Sekarang", key="btn_start_quiz", type="primary", icon=":material/play_arrow:", width="stretch"):
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

    # Inject Keyboard Navigation Shortcuts Listener
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
        "EI": ("Mind", "Ekstraversi vs Introversi"),
        "SN": ("Energy", "Penginderaan vs Intuisi"),
        "TF": ("Nature", "Pemikiran vs Perasaan"),
        "JP": ("Tactics", "Penilaian vs Eksplorasi"),
    }
    dim_name, dim_detail = dim_map.get(q["dim"], (q["dim"], ""))

    # Mini Visual Dots
    dots_html = ""
    for i in range(total):
        item_id = questions[i]["id"]
        if i == current_idx:
            cls = "dot-current"
        elif item_id in st.session_state.answers:
            cls = "dot-done"
        else:
            cls = "dot-empty"
        dots_html += f'<span class="matrix-dot {cls}">{i + 1}</span>'

    # Progress & Header Container
    with st.container(border=True):
        col_meta, col_jump, col_adv = st.columns([3, 2, 1.8], vertical_alignment="center")
        with col_meta:
            st.markdown(f"**Butir {current_idx + 1} dari {total}** · <span class='badge-dim-code'>{dim_name} ({q['dim']})</span>", unsafe_allow_html=True)
            st.caption(dim_detail)
        with col_jump:
            with st.popover(f"Daftar ({answered_count}/{total})", icon=":material/format_list_numbered:", width="stretch"):
                st.markdown("**Pilih butir untuk langsung meninjau:**")
                grid_cols = st.columns(4)
                for i in range(total):
                    item_qid = questions[i]["id"]
                    is_cur = (i == current_idx)
                    is_ans = (item_qid in st.session_state.answers)
                    lbl = f"{i + 1}{'✓' if is_ans else ''}"
                    btn_kind = "primary" if is_cur else "secondary"
                    if grid_cols[i % 4].button(lbl, key=f"jump_{i}", type=btn_kind, width="stretch"):
                        st.session_state.current_q = i
                        st.rerun()
        with col_adv:
            auto_val = st.toggle(
                "Auto-Next",
                value=st.session_state.get("auto_advance", True),
                key="quiz_auto_adv_toggle",
                help="Otomatis melompat ke butir berikutnya setelah memilih opsi",
            )
            st.session_state.auto_advance = auto_val

        st.progress(answered_count / total, text=f"Progres: {pct}% Selesai ({answered_count} dari {total} butir terjawab)")
        render_html(f'<div class="matrix-row">{dots_html}</div>')

    # Scenario & Question Box
    with st.container(border=True):
        render_html(f"""
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem;">
            <span style="font-size:0.78rem; font-weight:800; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.06em;">
                Skenario Nyata #{current_idx + 1}
            </span>
            <span style="font-size:0.76rem; color:var(--text-muted); font-weight:600;">Dinamika: {q.get('cog_tag', '')}</span>
        </div>
        <div class="scenario-box">
            <p class="scenario-text">"{q['scenario']}"</p>
        </div>
        <div style="font-size:0.82rem; font-weight:700; color:var(--text-secondary); text-transform:uppercase; letter-spacing:0.04em; margin-bottom:0.6rem;">
            Pilih respon yang paling mendekati kecenderungan alamiahmu:
        </div>
        """)

        prev_answer = st.session_state.answers.get(q_id)
        default_idx = 0 if prev_answer == "A" else (1 if prev_answer == "B" else None)

        def format_choice(val: str) -> str:
            if val == "A":
                return f"🔹 Opsi A:  {q['opt_a']['text']}"
            return f"🔹 Opsi B:  {q['opt_b']['text']}"

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
        <div class="keyboard-hint">
            <span>💡 <b>Shortcut:</b> Tekan <span class="kbd-key">A</span> / <span class="kbd-key">1</span> untuk Opsi A &bull; <span class="kbd-key">B</span> / <span class="kbd-key">2</span> untuk Opsi B &bull; <span class="kbd-key">&larr;</span> <span class="kbd-key">&rarr;</span> navigasi</span>
        </div>
        """)

    # Handle Auto-Advance Transition
    if st.session_state.get("trigger_advance_for") == q_id:
        st.session_state["trigger_advance_for"] = None
        if current_idx < total - 1:
            st.toast(f"Pilihan Butir #{current_idx + 1} tersimpan! Melanjutkan...", icon="✅")
            time.sleep(0.35)
            st.session_state.current_q += 1
            st.rerun()
        else:
            st.toast("Semua butir telah dijawab! Siap melihat hasil analisis.", icon="🎉")

    st.markdown("<div style='height:0.8rem;'></div>", unsafe_allow_html=True)

    # Navigation Buttons Row
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
            next_label = "Berikutnya" if is_answered else "Pilih satu opsi dulu"
            if st.button(next_label, key=f"btn_n_{current_idx}", type="primary", icon=":material/arrow_forward:", disabled=not is_answered, width="stretch"):
                st.session_state.current_q += 1
                st.rerun()
        else:
            all_done = (len(st.session_state.answers) == total)
            btn_finish_label = "Lihat Hasil Analisis" if all_done else f"Jawab Semua Dulu ({answered_count}/{total})"
            if st.button(btn_finish_label, key="btn_finish_test", type="primary", icon=":material/insights:", disabled=not all_done, width="stretch"):
                with st.spinner("Mengkalkulasi spektrum psikometrik dan fungsi Jungian..."):
                    result = engine.compute_result(st.session_state.answers)
                    st.session_state.result = result
                    st.session_state.page = "result"
                    st.rerun()


def render_result(result: MBTIResult) -> None:
    profile = get_profile(result.mbti_type)
    accent_color = profile.get("color", "#24826B")

    # Hero Result Card
    render_html(f"""
    <div class="clay-hero" style="border-top: 5px solid {accent_color};">
        <div class="badge-pill">
            <span>{profile.get('emoji', '🧩')}</span> Hasil Diagnosis Spektrum MBTI
        </div>
        <div class="hero-mbti-type">{result.mbti_type}</div>
        <h2 style="font-size:1.45rem; font-weight:800; color:var(--text-headline); margin:0 0 0.4rem;">
            {profile.get('title', result.mbti_type)}
        </h2>
        <p style="font-size:1.02rem; color:var(--text-body); font-style:italic; line-height:1.65; max-width:560px; margin:0.3rem auto 0;">
            "{profile.get('tagline', '')}"
        </p>
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
        render_html(f"""
        <div class="clay-card" style="background:var(--amber-light); border:1px solid rgba(179, 111, 28, 0.35);">
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.4rem;">
                <span style="font-size:1.25rem;">💡</span>
                <strong style="color:#784504; font-size:0.96rem;">Catatan Spektrum Seimbang (Borderline Trait)</strong>
            </div>
            <p style="font-size:0.9rem; color:#6B3E03; line-height:1.68; margin:0;">
                Skor kamu pada dimensi <strong>{bl_text}</strong> berada pada rentang seimbang (47%–53%). 
                Ini mengindikasikan kecenderungan adaptif di mana kamu luwes beralih mode sesuai tuntutan konteks secara seimbang.
            </p>
        </div>
        """)

    # Spectrum Rows Generator
    dim_pairs = {
        "EI": ("Ekstraversi (E)", "Introversi (I)"),
        "SN": ("Penginderaan (S)", "Intuisi (N)"),
        "TF": ("Pemikiran (T)", "Perasaan (F)"),
        "JP": ("Penilaian (J)", "Eksplorasi (P)"),
    }
    spectrum_html = ""
    for dim_code, (pos_name, neg_name) in dim_pairs.items():
        score_obj = result.dimensions[dim_code]
        pct_pos = score_obj.pos_pct
        pct_neg = round(100.0 - pct_pos, 1)
        dom_side = pos_name if pct_pos >= 50 else neg_name
        dom_pct = pct_pos if pct_pos >= 50 else pct_neg
        bl_tag = '<span class="borderline-badge">Borderline</span>' if score_obj.is_borderline else ""

        spectrum_html += f"""
        <div class="spectrum-row">
            <div class="spectrum-meta">
                <span class="pole-label {'pole-active' if pct_pos >= 50 else ''}">{pos_name} {pct_pos:.0f}%</span>
                <div>
                    <strong style="color:var(--text-headline); font-size:0.92rem;">{dom_side} {dom_pct:.0f}%</strong>
                    {bl_tag}
                </div>
                <span class="pole-label {'pole-active' if pct_neg > 50 else ''}">{neg_name} {pct_neg:.0f}%</span>
            </div>
            <div class="spectrum-track">
                <div class="spectrum-bar-fill" style="width: {pct_pos}%;"></div>
            </div>
        </div>
        """

    with st.container(border=True):
        render_html(f"""
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.3rem;">
            <div>
                <h3 style="font-size:1.1rem; font-weight:800; color:var(--text-headline); margin:0;">Spektrum Kontinu 4 Dimensi</h3>
                <p style="font-size:0.82rem; color:var(--text-secondary); margin:0.2rem 0 0;">Persentase kecenderungan proses mental & preferensi energi</p>
            </div>
            <span class="badge-dim-code">Spektrum Terukur</span>
        </div>
        {spectrum_html}
        """)

    # 4 Deep-Dive Tabs with Material Symbols
    tab_cog, tab_strength, tab_vibe, tab_stress = st.tabs([
        ":material/psychology: Fungsi Kognitif (Jung)",
        ":material/bolt: Superpower & Blindspot",
        ":material/work: Gaya Kerja & Kolaborasi",
        ":material/spa: Stres & Reset Mental",
    ])

    with tab_cog:
        role_meta = {
            "dominant": ("Fungsi Utama (Driver)", "Kapten pikiran — mode alamiah yang bekerja spontan dan paling dominan."),
            "auxiliary": ("Fungsi Pendukung (Co-Pilot)", "Penyeimbang krusial agar cara berpikir tidak bias atau sepihak."),
            "tertiary": ("Sisi Relaksasi (Tertiary)", "Area bermain & rekreasi kognitif saat suasana rileks."),
            "inferior": ("Titik Buta (Inferior)", "Paling rentan — sering terpantik saat kelelahan atau di bawah tekanan.")
        }
        cog_stack = profile.get("cognitive_roles", result.cognitive_stack)
        cog_items_html = ""
        for r_key, (r_title, r_desc) in role_meta.items():
            val = cog_stack.get(r_key, result.cognitive_stack.get(r_key, "—"))
            parts = val.split(" — ", 1) if " — " in val else (val, r_desc)
            func_name = parts[0]
            func_detail = parts[1] if len(parts) > 1 else r_desc
            cog_items_html += f"""
            <div class="cog-item-card">
                <div class="cog-role-name">{r_title}</div>
                <div class="cog-func-title">{func_name}</div>
                <p class="cog-func-desc">{func_detail}</p>
            </div>
            """

        with st.container(border=True):
            render_html(f"""
            <h4 style="font-size:1.02rem; font-weight:800; color:var(--text-headline); margin:0 0 0.3rem;">
                Struktur 4 Lapisan Fungsi Kognitif Jungian
            </h4>
            <p style="font-size:0.88rem; color:var(--text-body); margin-bottom:1.1rem; line-height:1.62;">
                Model 16 tipe Jungian menjelaskan bahwa arsitektur pikiran bekerja dalam hierarki 4 instrumen mental:
            </p>
            {cog_items_html}
            """)

    with tab_strength:
        sb = profile.get("strengths_blindspots", {})
        c_sup, c_bli = st.columns(2, gap="medium")
        with c_sup:
            with st.container(border=True):
                render_html(f"""
                <div style="font-size:0.82rem; font-weight:800; text-transform:uppercase; color:var(--teal-primary); margin-bottom:0.5rem;">
                    ⚡ Superpower Alami
                </div>
                <p style="font-size:0.91rem; color:var(--text-body); line-height:1.68; margin:0;">
                    {sb.get('superpower', '—')}
                </p>
                """)
        with c_bli:
            with st.container(border=True):
                render_html(f"""
                <div style="font-size:0.82rem; font-weight:800; text-transform:uppercase; color:var(--warm-terracotta); margin-bottom:0.5rem;">
                    🫥 Blindspot Sosial & Kognitif
                </div>
                <p style="font-size:0.91rem; color:var(--text-body); line-height:1.68; margin:0;">
                    {sb.get('blindspot', '—')}
                </p>
                """)

    with tab_vibe:
        with st.container(border=True):
            render_html(f"""
            <div style="font-size:0.82rem; font-weight:800; text-transform:uppercase; color:var(--ocean-blue); margin-bottom:0.5rem;">
                💼 Dinamika Eksekusi, Deep Work & Kolaborasi
            </div>
            <p style="font-size:0.93rem; color:var(--text-body); line-height:1.75; margin:0;">
                {profile.get('daily_vibe', '—')}
            </p>
            """)

    with tab_stress:
        with st.container(border=True):
            render_html(f"""
            <div style="font-size:0.82rem; font-weight:800; text-transform:uppercase; color:var(--warm-terracotta); margin-bottom:0.5rem;">
                ⛈️ Respons Saat Burnout & Panduan Reset Mental
            </div>
            <p style="font-size:0.93rem; color:var(--text-body); line-height:1.75; margin:0;">
                {profile.get('stress_response', '—')}
            </p>
            """)

    # Exportable & Copyable Summary
    summary_text = (
        f"[HASIL ASESMEN MBTI KLINIS]\n"
        f"Tipe: {result.mbti_type} — {profile.get('title', '')}\n\n"
        f"Spektrum Kontinu:\n"
        f"• Mind:    {result.dimensions['EI'].pos_pct:.0f}% Extraversion / {result.dimensions['EI'].neg_pct:.0f}% Introversion\n"
        f"• Energy:  {result.dimensions['SN'].pos_pct:.0f}% Sensing / {result.dimensions['SN'].neg_pct:.0f}% Intuition\n"
        f"• Nature:  {result.dimensions['TF'].pos_pct:.0f}% Thinking / {result.dimensions['TF'].neg_pct:.0f}% Feeling\n"
        f"• Tactics: {result.dimensions['JP'].pos_pct:.0f}% Judging / {result.dimensions['JP'].neg_pct:.0f}% Prospecting\n\n"
        f"Fungsi Kognitif Utama: {result.cognitive_stack.get('dominant', '-')}\n"
        f"Tagline: \"{profile.get('tagline', '')}\""
    )

    with st.container(border=True):
        st.markdown("**Salin atau Unduh Laporan Diagnosis:**")
        render_html(f'<div class="copy-box">{summary_text}</div>')
        st.download_button(
            label="Unduh Laporan Diagnosis (.txt)",
            data=summary_text,
            file_name=f"Hasil_MBTI_{result.mbti_type}.txt",
            mime="text/plain",
            icon=":material/download:",
            width="stretch"
        )

    st.markdown("<div style='height:0.8rem;'></div>", unsafe_allow_html=True)

    # Action Buttons Row
    c_ret, c_hom = st.columns(2, gap="medium")
    with c_ret:
        if st.button("Ulangi Tes dari Awal", key="btn_repeat_test", type="primary", icon=":material/restart_alt:", width="stretch"):
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
