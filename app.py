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
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap');

/* ==================== ROOT DESIGN TOKENS ==================== */
:root {
    --bg-main: #F8FAFC;
    --surface-card: #FFFFFF;
    --surface-subtle: #F1F5F9;
    
    --border-subtle: #E2E8F0;
    --border-focus: #0F172A;
    
    --text-primary: #0F172A;
    --text-secondary: #334155;
    --text-muted: #64748B;
    
    --accent-slate: #1E293B;
    --accent-teal: #0D9488;
    
    --radius-lg: 12px;
    --radius-md: 8px;
    --radius-sm: 6px;
    --radius-pill: 9999px;
    
    --shadow-clean: 0 1px 3px 0 rgba(0, 0, 0, 0.04), 0 1px 2px -1px rgba(0, 0, 0, 0.04);
    --shadow-card: 0 4px 6px -1px rgba(0, 0, 0, 0.04), 0 2px 4px -2px rgba(0, 0, 0, 0.03);
}

/* Global Typography */
html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: var(--text-primary) !important;
    background-color: var(--bg-main) !important;
}

/* Hide default clutter */
header, footer, [data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu {
    display: none !important;
}

.main .block-container {
    padding: 2.2rem 1.2rem 4.5rem !important;
    max-width: 740px !important;
}

/* ==================== CLEAN CONTAINERS ==================== */
.clean-hero {
    background: var(--surface-card);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-clean);
    padding: 2.4rem 2rem;
    text-align: center;
    margin-bottom: 1.25rem;
}

.clean-card {
    background: var(--surface-card);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-clean);
    padding: 1.5rem 1.75rem;
    margin-bottom: 1.25rem;
}

.badge-tag {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.3rem 0.85rem;
    border-radius: var(--radius-pill);
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    background: var(--surface-subtle);
    color: var(--text-secondary);
    border: 1px solid var(--border-subtle);
}

.scenario-panel {
    background: var(--surface-card);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-lg);
    padding: 1.6rem 1.75rem;
    box-shadow: var(--shadow-clean);
    margin-bottom: 1rem;
}

.scenario-quote {
    font-size: 1.05rem;
    font-weight: 600;
    line-height: 1.68;
    color: var(--text-primary);
    margin: 0.75rem 0 1.2rem;
    letter-spacing: -0.01em;
}

/* ==================== RADIO SELECTION CARDS ==================== */
div[data-testid="stRadio"] > div[role="radiogroup"] {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.75rem !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"] {
    background: var(--surface-card) !important;
    border-radius: var(--radius-md) !important;
    border: 1px solid var(--border-subtle) !important;
    padding: 1.05rem 1.25rem !important;
    margin: 0 !important;
    cursor: pointer !important;
    transition: all 0.15s ease !important;
    box-shadow: var(--shadow-clean) !important;
    display: flex !important;
    align-items: flex-start !important;
    gap: 0.85rem !important;
    min-height: 52px !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {
    border-color: #94A3B8 !important;
    background: #FAFAFA !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {
    background: #F8FAFC !important;
    border-color: var(--border-focus) !important;
    box-shadow: 0 0 0 1px var(--border-focus) !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"] div[data-testid="stMarkdownContainer"] p {
    font-size: 0.94rem !important;
    line-height: 1.58 !important;
    color: var(--text-secondary) !important;
    font-weight: 500 !important;
    margin: 0 !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) div[data-testid="stMarkdownContainer"] p {
    font-weight: 600 !important;
    color: var(--text-primary) !important;
}

/* ==================== BUTTON POLISH ==================== */
button[data-testid="baseButton-primary"], button[data-testid="baseButton-secondary"] {
    min-height: 44px !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    border-radius: var(--radius-md) !important;
    transition: all 0.15s ease !important;
}

/* ==================== SPECTRUM VISUALIZER ==================== */
.spectrum-box {
    margin-bottom: 1.25rem;
}

.spectrum-box:last-child {
    margin-bottom: 0;
}

.spectrum-labels {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.84rem;
    margin-bottom: 0.4rem;
}

.spectrum-pole {
    color: var(--text-muted);
    font-weight: 500;
}

.spectrum-pole.active-pole {
    color: var(--text-primary);
    font-weight: 700;
}

.spectrum-rail {
    height: 8px;
    background: #E2E8F0;
    border-radius: var(--radius-pill);
    overflow: hidden;
    position: relative;
}

.spectrum-fill {
    height: 100%;
    border-radius: var(--radius-pill);
    background: #0F172A;
    transition: width 0.5s ease;
}

.badge-borderline {
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    background: #FEF3C7;
    color: #92400E;
    padding: 0.15rem 0.55rem;
    border-radius: var(--radius-pill);
    border: 1px solid #FDE68A;
    margin-left: 0.4rem;
}

/* ==================== RESULT PRESENTATION ==================== */
.hero-code {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.85rem;
    font-weight: 700;
    letter-spacing: -0.04em;
    line-height: 1.1;
    color: #0F172A;
    margin: 0.4rem 0 0.2rem;
}

.cog-block {
    background: var(--surface-card);
    border: 1px solid var(--border-subtle);
    border-left: 3px solid #0F172A;
    border-radius: var(--radius-md);
    padding: 1.1rem 1.3rem;
    margin-bottom: 0.75rem;
}

.cog-label {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--text-muted);
    margin-bottom: 0.2rem;
}

.cog-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.98rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.35rem;
}

.cog-desc {
    font-size: 0.88rem;
    color: var(--text-secondary);
    line-height: 1.62;
    margin: 0;
}

/* Keyboard hint */
.kbd-legend {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    font-size: 0.76rem;
    color: var(--text-muted);
    background: var(--surface-subtle);
    padding: 0.3rem 0.75rem;
    border-radius: var(--radius-pill);
    border: 1px solid var(--border-subtle);
    margin-top: 0.5rem;
}

.kbd-cap {
    background: #FFFFFF;
    border: 1px solid #CBD5E1;
    box-shadow: 0 1px 1px rgba(0,0,0,0.05);
    border-radius: 4px;
    padding: 0.08rem 0.35rem;
    font-family: monospace;
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--text-primary);
}

.copy-area {
    background: var(--surface-subtle);
    border-radius: var(--radius-md);
    padding: 1.1rem 1.25rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 0.82rem;
    color: var(--text-primary);
    line-height: 1.65;
    border: 1px solid var(--border-subtle);
    user-select: all;
    margin: 0.6rem 0;
    white-space: pre-wrap;
}

@media (max-width: 640px) {
    .main .block-container {
        padding: 1.2rem 0.8rem 3.5rem !important;
    }
    .clean-hero {
        padding: 1.75rem 1.25rem !important;
    }
    .scenario-panel {
        padding: 1.25rem 1.15rem !important;
    }
    .scenario-quote {
        font-size: 0.98rem !important;
    }
    .kbd-legend {
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
    <div class="clean-hero">
        <div class="badge-tag">Instrumen Tipologi & Arsitektur Kognitif</div>
        <h1 style="font-family:'Space Grotesk',sans-serif; font-size:2.1rem; font-weight:700; color:#0F172A; margin:0.8rem 0 0.4rem; letter-spacing:-0.03em;">
            Asesmen Spektrum MBTI
        </h1>
        <p style="font-size:0.98rem; color:#334155; line-height:1.65; max-width:540px; margin:0 auto;">
            Mengevaluasi preferensi mental dan dinamika 8 fungsi kognitif Carl Jung melalui 24 skenario pertimbangan terukur tanpa bias respon sosial.
        </p>
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

    st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
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
        "EI": ("Mind", "Ekstraversi vs Introversi"),
        "SN": ("Energy", "Penginderaan vs Intuisi"),
        "TF": ("Nature", "Pemikiran vs Perasaan"),
        "JP": ("Tactics", "Penilaian vs Eksplorasi"),
    }
    dim_name, dim_detail = dim_map.get(q["dim"], (q["dim"], ""))

    # Header and Navigation Container
    with st.container(border=True):
        col_meta, col_jump, col_adv = st.columns([3, 1.8, 1.6], vertical_alignment="center")
        with col_meta:
            st.markdown(f"**Butir {current_idx + 1:02d} / {total:02d}** · <span class='badge-tag'>{dim_name} ({q['dim']})</span>", unsafe_allow_html=True)
            st.caption(dim_detail)
        with col_jump:
            with st.popover(f"Daftar Butir ({answered_count}/{total})", icon=":material/format_list_numbered:", width="stretch"):
                st.caption("Pilih butir untuk meninjau:")
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
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:0.3rem;">
            <span style="font-size:0.75rem; font-weight:700; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.06em;">
                Skenario #{current_idx + 1:02d}
            </span>
            <span style="font-size:0.75rem; color:var(--text-muted); font-weight:600;">Dinamika: {q.get('cog_tag', '')}</span>
        </div>
        <div class="scenario-quote">"{q['scenario']}"</div>
        <div style="font-size:0.8rem; font-weight:600; color:var(--text-secondary); margin-bottom:0.75rem;">
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
        <div class="kbd-legend">
            <span>Pintasan: <span class="kbd-cap">A</span> / <span class="kbd-cap">1</span> Opsi A &bull; <span class="kbd-cap">B</span> / <span class="kbd-cap">2</span> Opsi B &bull; <span class="kbd-cap">&larr;</span> <span class="kbd-cap">&rarr;</span> Navigasi</span>
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

    # Hero Result Presentation
    render_html(f"""
    <div class="clean-hero">
        <div class="badge-tag">Laporan Tipologi Kognitif</div>
        <div class="hero-code">{result.mbti_type}</div>
        <h2 style="font-family:'Space Grotesk',sans-serif; font-size:1.35rem; font-weight:700; color:#0F172A; margin:0 0 0.35rem;">
            {profile.get('title', result.mbti_type)}
        </h2>
        <p style="font-size:0.96rem; color:#334155; line-height:1.65; max-width:540px; margin:0.3rem auto 0;">
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
        with st.container(border=True):
            st.markdown("**:material/info: Zona Ekuilibrium (Borderline Trait)**")
            st.caption(
                f"Hasil evaluasi pada dimensi **{bl_text}** berada dalam rentang ekuilibrium (47%–53%). "
                "Hal ini mencerminkan fleksibilitas kontekstual di mana Anda dapat beroperasi secara seimbang pada kedua kutub sesuai tuntutan situasi."
            )

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
        bl_tag = '<span class="badge-borderline">Ekuilibrium</span>' if score_obj.is_borderline else ""

        spectrum_html += f"""
        <div class="spectrum-box">
            <div class="spectrum-labels">
                <span class="spectrum-pole {'active-pole' if pct_pos >= 50 else ''}">{pos_name} {pct_pos:.0f}%</span>
                <div>
                    <strong style="color:#0F172A; font-size:0.88rem;">{dom_side} {dom_pct:.0f}%</strong>
                    {bl_tag}
                </div>
                <span class="spectrum-pole {'active-pole' if pct_neg > 50 else ''}">{neg_name} {pct_neg:.0f}%</span>
            </div>
            <div class="spectrum-rail">
                <div class="spectrum-fill" style="width: {pct_pos}%;"></div>
            </div>
        </div>
        """

    with st.container(border=True):
        st.markdown("**Spektrum Kontinu 4 Dimensi**")
        st.caption("Distribusi persentase proses mental dan orientasi energi")
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
            "dominant": "Fungsi Dominan (Leading Function)",
            "auxiliary": "Fungsi Pembantu (Supporting Function)",
            "tertiary": "Fungsi Tersier (Tertiary Function)",
            "inferior": "Fungsi Inferior (Inferior Function)"
        }
        cog_stack = profile.get("cognitive_roles", result.cognitive_stack)
        cog_items_html = ""
        for r_key, r_label in role_meta.items():
            val = cog_stack.get(r_key, result.cognitive_stack.get(r_key, "—"))
            parts = val.split(" — ", 1) if " — " in val else (val, "")
            func_name = parts[0]
            func_detail = parts[1] if len(parts) > 1 else ""
            cog_items_html += f"""
            <div class="cog-block">
                <div class="cog-label">{r_label}</div>
                <div class="cog-name">{func_name}</div>
                <p class="cog-desc">{func_detail}</p>
            </div>
            """

        with st.container(border=True):
            st.markdown("**Hierarki 4 Lapisan Fungsi Kognitif Carl Jung**")
            st.caption("Konfigurasi instrumen mental yang membentuk cara persepsi dan evaluasi informasi:")
            render_html(cog_items_html)

    with tab_strength:
        sb = profile.get("strengths_blindspots", {})
        c_sup, c_bli = st.columns(2, gap="medium")
        with c_sup:
            with st.container(border=True):
                st.markdown("**:material/check_circle: Kompetensi Inti**")
                st.caption(sb.get("strengths", sb.get("superpower", "—")))
        with c_bli:
            with st.container(border=True):
                st.markdown("**:material/warning: Area Kerentanan**")
                st.caption(sb.get("blindspots", sb.get("blindspot", "—")))

    with tab_work:
        with st.container(border=True):
            st.markdown("**:material/hub: Modalitas Kerja & Pola Kolaborasi**")
            st.caption(profile.get("work_style", profile.get("daily_vibe", "—")))

    with tab_stress:
        with st.container(border=True):
            st.markdown("**:material/healing: Dinamika Stres & Protokol Pemulihan**")
            st.caption(profile.get("stress_dynamics", profile.get("stress_response", "—")))

    # Structured Export
    summary_text = (
        f"[LAPORAN ASESMEN TIPOLOGI MBTI]\n"
        f"Tipe: {result.mbti_type} — {profile.get('title', '')}\n\n"
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
        render_html(f'<div class="copy-area">{summary_text}</div>')
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
