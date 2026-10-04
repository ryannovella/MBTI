from __future__ import annotations
import textwrap
import time
import streamlit as st
from engine import PersonalityEngine, MBTIResult
from profiles import get_profile, get_all_profiles, get_avatar_base64

st.set_page_config(
    page_title="Asesmen Spektrum MBTI · Arsitektur Kognitif",
    page_icon=":material/psychology:",
    layout="centered",
    initial_sidebar_state="collapsed",
)


def render_html(html: str) -> None:
    st.html(textwrap.dedent(html).strip())


def render_avatar_img(code: str, size: int = 90, alt: str = "") -> str:
    b64 = get_avatar_base64(code)
    if not b64:
        return ""
    return (
        f'<img src="data:image/svg+xml;base64,{b64}" alt="{alt}" '
        f'width="{size}" height="{size}" '
        f'style="object-fit:contain; display:block; margin:0 auto; filter:drop-shadow(0 4px 8px rgba(0,0,0,0.06));" />'
    )


APP_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700;800&display=swap');

/* ==================== CLAYMORPHISM & GLASSMORPHISM DESIGN TOKENS ==================== */
:root {
    --bg-canvas: #F8FAFC;
    --surface-card: #FFFFFF;
    --surface-subtle: #F1F5F9;
    
    --border-light: #E2E8F0;
    --border-medium: #CBD5E1;
    --border-primary: #4F46E5;
    
    --text-title: #1E1B4B;
    --text-main: #1E293B;
    --text-body: #475569;
    --text-muted: #64748B;
    
    /* 4 Temperament Theme Colors */
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

    /* Geometry */
    --radius-clay: 22px;
    --radius-card: 18px;
    --radius-md: 12px;
    --radius-pill: 9999px;
    
    /* Claymorphism Dual Shadows */
    --shadow-clay: 
        0 14px 28px -4px rgba(79, 70, 229, 0.08),
        0 4px 10px -2px rgba(15, 23, 42, 0.03),
        inset 4px 4px 8px rgba(255, 255, 255, 0.95),
        inset -4px -4px 8px rgba(15, 23, 42, 0.035);
        
    --shadow-clay-hover: 
        0 18px 36px -4px rgba(79, 70, 229, 0.12),
        inset 4px 4px 8px rgba(255, 255, 255, 0.95),
        inset -4px -4px 8px rgba(15, 23, 42, 0.035);
        
    --shadow-clay-soft:
        0 8px 18px -3px rgba(79, 70, 229, 0.05),
        inset 3px 3px 6px rgba(255, 255, 255, 0.95),
        inset -3px -3px 6px rgba(15, 23, 42, 0.025);
        
    /* Glassmorphism Accents */
    --glass-bg: rgba(255, 255, 255, 0.72);
    --glass-border: 1px solid rgba(255, 255, 255, 0.65);
    --glass-shadow: 0 4px 14px rgba(31, 38, 135, 0.05);
}

/* Base App Layout */
html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: var(--text-main) !important;
    background-color: var(--bg-canvas) !important;
}

header, footer, [data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu {
    display: none !important;
}

.main .block-container {
    padding: 2.4rem 1.4rem 4.8rem !important;
    max-width: 880px !important;
}

/* ==================== CLAYMORPHIC HERO CONTAINER ==================== */
.friendly-hero {
    background: var(--surface-card);
    border: 1.5px solid rgba(255, 255, 255, 0.9);
    border-radius: var(--radius-clay);
    box-shadow: var(--shadow-clay);
    padding: 2.6rem 2.2rem 2.2rem;
    text-align: center;
    margin-bottom: 1.4rem;
    position: relative;
    overflow: hidden;
}

.friendly-hero::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 5px;
    background: linear-gradient(90deg, #6366F1 0%, #3B82F6 40%, #10B981 70%, #F59E0B 100%);
}

.badge-friendly-tag {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.38rem 1.1rem;
    border-radius: var(--radius-pill);
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    background: var(--glass-bg);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    color: #4338CA;
    border: var(--glass-border);
    box-shadow: var(--glass-shadow);
}

.pill-row-cluster {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.55rem;
    margin-top: 1.3rem;
}

.pill-feature-chip {
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--text-body);
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(8px);
    padding: 0.35rem 0.95rem;
    border-radius: var(--radius-pill);
    border: 1px solid var(--border-light);
    box-shadow: 0 2px 5px rgba(0,0,0,0.03);
}

/* ==================== 3 PILLARS PROPORTIONAL GRID ==================== */
.pillar-grid-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.1rem;
    margin-bottom: 1.3rem;
}

@media (max-width: 768px) {
    .pillar-grid-row {
        grid-template-columns: 1fr;
    }
}

.pillar-card {
    background: #FFFFFF;
    border-radius: var(--radius-card);
    border: 1.5px solid rgba(255, 255, 255, 0.9);
    box-shadow: var(--shadow-clay-soft);
    padding: 1.35rem 1.25rem;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    height: 100%;
    box-sizing: border-box;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.pillar-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-clay);
}

.pillar-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.02rem;
    font-weight: 700;
    color: var(--text-title);
    margin: 0 0 0.45rem;
    display: flex;
    align-items: center;
    gap: 0.45rem;
}

.pillar-desc {
    font-size: 0.86rem;
    color: var(--text-body);
    line-height: 1.58;
    margin: 0;
}

/* ==================== 16PERSONALITIES CHARACTER SHOWCASE ==================== */
.showcase-header-box {
    text-align: center;
    margin: 2.2rem 0 1.2rem;
}

.showcase-heading {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: var(--text-title);
    margin: 0 0 0.35rem;
    letter-spacing: -0.02em;
}

.showcase-subheading {
    font-size: 0.92rem;
    color: var(--text-muted);
    margin: 0 auto;
    max-width: 600px;
    line-height: 1.6;
}

.char-grid-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.1rem;
    margin: 1.1rem 0;
}

@media (max-width: 860px) {
    .char-grid-row {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 520px) {
    .char-grid-row {
        grid-template-columns: 1fr;
    }
}

.char-card {
    background: #FFFFFF;
    border-radius: 20px;
    border: 1.5px solid rgba(255, 255, 255, 0.9);
    box-shadow: var(--shadow-clay-soft);
    padding: 1.4rem 1.1rem 1.25rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    text-align: center;
    transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
    box-sizing: border-box;
    height: 100%;
}

.char-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-clay-hover);
}

.char-avatar-pod {
    width: 96px;
    height: 96px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 0.85rem;
    box-shadow: 
        inset 3px 3px 6px rgba(15, 23, 42, 0.04),
        inset -3px -3px 6px rgba(255, 255, 255, 0.95),
        0 6px 14px rgba(79, 70, 229, 0.06);
    border: 2px solid rgba(255, 255, 255, 0.9);
    transition: transform 0.2s ease;
}

.char-card:hover .char-avatar-pod {
    transform: scale(1.06);
}

.char-code-badge {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.82rem;
    font-weight: 800;
    letter-spacing: 0.05em;
    padding: 0.22rem 0.8rem;
    border-radius: var(--radius-pill);
    margin-bottom: 0.45rem;
    display: inline-block;
}

.char-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.02rem;
    font-weight: 700;
    color: var(--text-title);
    margin: 0 0 0.45rem;
    line-height: 1.35;
}

.char-desc {
    font-size: 0.81rem;
    color: var(--text-body);
    line-height: 1.55;
    margin: 0 0 0.85rem;
    flex-grow: 1;
}

.char-cog-chip {
    font-size: 0.74rem;
    font-weight: 700;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(226, 232, 240, 0.85);
    border-radius: var(--radius-pill);
    padding: 0.22rem 0.7rem;
    color: var(--text-muted);
}

/* ==================== QUIZ SCENARIO CONTAINER ==================== */
.scenario-friendly-card {
    background: var(--surface-card);
    border: 1.5px solid rgba(255, 255, 255, 0.9);
    border-radius: var(--radius-clay);
    padding: 1.85rem 2rem 1.6rem;
    box-shadow: var(--shadow-clay);
    margin-bottom: 1.2rem;
    position: relative;
}

.scenario-top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.9rem;
    padding-bottom: 0.7rem;
    border-bottom: 1px solid #F1F5F9;
}

.scenario-quote-highlight {
    font-size: 1.15rem;
    font-weight: 700;
    line-height: 1.72;
    color: var(--text-title);
    margin: 0.6rem 0 1.25rem;
    letter-spacing: -0.015em;
}

/* ==================== TACTILE CLAY RADIO OPTIONS ==================== */
div[data-testid="stRadio"] > div[role="radiogroup"] {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.95rem !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"] {
    background: var(--surface-card) !important;
    border-radius: var(--radius-card) !important;
    border: 1.5px solid var(--border-light) !important;
    padding: 1.25rem 1.45rem !important;
    margin: 0 !important;
    cursor: pointer !important;
    transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1) !important;
    box-shadow: var(--shadow-clay-soft) !important;
    display: flex !important;
    align-items: flex-start !important;
    gap: 1rem !important;
    min-height: 60px !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {
    border-color: #A5B4FC !important;
    background: #FAF5FF !important;
    transform: translateY(-2px) !important;
    box-shadow: var(--shadow-clay) !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:active {
    transform: translateY(0) !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {
    background: #FFFFFF !important;
    border-color: #4F46E5 !important;
    box-shadow: 0 0 0 2px #4F46E5, var(--shadow-clay) !important;
    transform: translateY(-1px) !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"] div[data-testid="stMarkdownContainer"] p {
    font-size: 0.98rem !important;
    line-height: 1.64 !important;
    color: var(--text-body) !important;
    font-weight: 500 !important;
    margin: 0 !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) div[data-testid="stMarkdownContainer"] p {
    font-weight: 700 !important;
    color: var(--text-title) !important;
}

/* ==================== BUTTONS CLEAN & TACTILE ==================== */
button[data-testid="baseButton-primary"], button[data-testid="baseButton-secondary"] {
    min-height: 48px !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    border-radius: var(--radius-md) !important;
    transition: all 0.18s ease !important;
}

button[data-testid="baseButton-primary"] {
    background: linear-gradient(135deg, #4F46E5 0%, #4338CA 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    box-shadow: 0 4px 14px rgba(79, 70, 229, 0.25) !important;
}

button[data-testid="baseButton-primary"]:hover {
    transform: translateY(-1.5px) !important;
    box-shadow: 0 8px 22px rgba(79, 70, 229, 0.35) !important;
    background: linear-gradient(135deg, #4338CA 0%, #3730A3 100%) !important;
}

button[data-testid="baseButton-primary"]:active {
    transform: translateY(0.5px) !important;
}

button[data-testid="baseButton-secondary"] {
    background: #FFFFFF !important;
    color: var(--text-main) !important;
    border: 1.5px solid var(--border-light) !important;
    box-shadow: var(--shadow-clay-soft) !important;
}

button[data-testid="baseButton-secondary"]:hover {
    border-color: var(--border-medium) !important;
    background: #F8FAFC !important;
    transform: translateY(-1.5px) !important;
}

/* ==================== RESULT HERO CLAY & GLASS ==================== */
.friendly-result-hero {
    background: var(--surface-card);
    border: 1.5px solid rgba(255, 255, 255, 0.9);
    border-radius: var(--radius-clay);
    box-shadow: var(--shadow-clay);
    padding: 2.2rem 2.2rem 2rem;
    margin-bottom: 1.4rem;
    position: relative;
    overflow: hidden;
}

.hero-result-flex {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.8rem;
}

@media (max-width: 680px) {
    .hero-result-flex {
        flex-direction: column-reverse;
        text-align: center;
    }
}

.hero-result-content {
    flex: 1;
}

.hero-result-avatar-box {
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.clay-avatar-hero {
    width: 140px;
    height: 140px;
    border-radius: 26px;
    background: #FFFFFF;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 
        0 14px 28px rgba(79, 70, 229, 0.12),
        inset 4px 4px 8px rgba(255, 255, 255, 0.95),
        inset -4px -4px 8px rgba(15, 23, 42, 0.04);
    border: 2px solid rgba(255, 255, 255, 0.95);
    padding: 0.6rem;
    transition: transform 0.25s ease;
}

.clay-avatar-hero:hover {
    transform: scale(1.04) rotate(-1deg);
}

.hero-type-code {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1.05;
    margin: 0.5rem 0 0.2rem;
}

.tagline-callout {
    font-size: 0.98rem;
    line-height: 1.68;
    color: var(--text-body);
    background: rgba(248, 250, 252, 0.7);
    backdrop-filter: blur(8px);
    border-radius: var(--radius-md);
    padding: 0.95rem 1.25rem;
    margin-top: 1rem;
    border: 1px solid var(--border-light);
}

/* ==================== SPECTRUM TRACK ==================== */
.spectrum-row-box {
    margin-bottom: 1.2rem;
}

.spectrum-info-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.45rem;
    font-size: 0.86rem;
}

.pole-tag {
    font-weight: 600;
    color: var(--text-muted);
}

.pole-tag.active {
    font-weight: 800;
    color: var(--text-title);
}

.spectrum-track-bg {
    height: 16px;
    background: #E2E8F0;
    border-radius: var(--radius-pill);
    position: relative;
    overflow: hidden;
    box-shadow: inset 1px 1px 3px rgba(0,0,0,0.1);
}

.spectrum-fill-progress {
    height: 100%;
    border-radius: var(--radius-pill);
    transition: width 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.spectrum-center-divider {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 50%;
    width: 2px;
    background: #FFFFFF;
    transform: translateX(-50%);
    z-index: 2;
    box-shadow: 0 0 4px rgba(0,0,0,0.2);
}

.badge-balance-pill {
    background: #FEF3C7;
    color: #92400E;
    border: 1px solid #FDE68A;
    font-size: 0.72rem;
    font-weight: 800;
    padding: 0.15rem 0.55rem;
    border-radius: var(--radius-pill);
    margin-left: 0.4rem;
}

/* ==================== COGNITIVE LAYERS ==================== */
.cog-layer-friendly-card {
    background: #FFFFFF;
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-clay-soft);
    padding: 1.1rem 1.3rem;
    margin-bottom: 0.85rem;
}

.cog-layer-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.35rem;
}

.cog-role-badge {
    font-size: 0.78rem;
    font-weight: 800;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.04em;
}

.cog-symbol-tag {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.88rem;
    font-weight: 800;
    padding: 0.2rem 0.6rem;
    border-radius: var(--radius-pill);
    border: 1px solid transparent;
}

.cog-func-heading {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-title);
    margin-bottom: 0.3rem;
}

.cog-func-paragraph {
    font-size: 0.88rem;
    line-height: 1.62;
    color: var(--text-body);
    margin: 0;
}

/* ==================== TEXT COPY AREA ==================== */
.copy-box-area {
    background: #F8FAFC;
    border-radius: var(--radius-md);
    padding: 1.1rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 0.82rem;
    color: var(--text-main);
    line-height: 1.7;
    border: 1px solid var(--border-light);
    user-select: all;
    margin: 0.6rem 0;
    white-space: pre-wrap;
}

@media (max-width: 640px) {
    .main .block-container {
        padding: 1.4rem 0.9rem 3.8rem !important;
    }
    .friendly-hero, .friendly-result-hero {
        padding: 1.85rem 1.3rem !important;
    }
    .scenario-friendly-card {
        padding: 1.4rem 1.25rem !important;
    }
    .scenario-quote-highlight {
        font-size: 1.06rem !important;
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
    <div class="friendly-hero">
        <div class="badge-friendly-tag">Tipologi & arsitektur kognitif</div>
        <h1 style="font-family:'Space Grotesk',sans-serif; font-size:2.45rem; font-weight:800; color:#1E1B4B; margin:0.95rem 0 0.45rem; letter-spacing:-0.035em;">
            Asesmen spektrum MBTI
        </h1>
        <p style="font-size:1.02rem; color:#475569; line-height:1.72; max-width:620px; margin:0 auto;">
            Kenali tipe kepribadian dan cara unik otakmu memproses hal-hal di sekitarmu, mengambil keputusan, dan berinteraksi sehari-hari lewat 24 skenario yang dekat banget sama kehidupan nyata.
        </p>
        <div class="pill-row-cluster">
            <span class="pill-feature-chip">24 Skenario kehidupan nyata</span>
            <span class="pill-feature-chip">8 Fungsi kognitif Carl Jung</span>
            <span class="pill-feature-chip">Spektrum kontinu 0–100%</span>
            <span class="pill-feature-chip">Bebas jawaban benar/salah</span>
        </div>
    </div>
    """)

    # 3 Methodology Pillars (Proportional Grid)
    render_html("""
    <div class="pillar-grid-row">
        <div class="pillar-card">
            <div class="pillar-title">Dilema realistis</div>
            <p class="pillar-desc">Pilihan situasinya membumi dan nyata, nggak ada opsi klise atau jebakan jawaban yang dibuat-buat.</p>
        </div>
        <div class="pillar-card">
            <div class="pillar-title">Spektrum fleksibel</div>
            <p class="pillar-desc">Kuantifikasi proporsional 0–100% yang menghargai bahwa manusia itu dinamis dan adaptif.</p>
        </div>
        <div class="pillar-card">
            <div class="pillar-title">Arsitektur kognitif</div>
            <p class="pillar-desc">Menelusuri 4 lapisan cara berpikirmu, dari yang paling naluriah sampai sisi yang rentan lelah saat stres.</p>
        </div>
    </div>
    """)

    # 16Personalities Character Showcase
    render_html("""
    <div class="showcase-header-box">
        <div class="showcase-heading">Eksplorasi 16 arketipe kepribadian</div>
        <div class="showcase-subheading">
            Tiap arketipe punya karakter visual unik, cara pandang tersendiri, dan kontribusi seru dalam menjalani hidup:
        </div>
    </div>
    """)

    all_prof = get_all_profiles()
    tab_nt, tab_nf, tab_sj, tab_sp = st.tabs([
        ":material/psychology: Analis (NT)",
        ":material/favorite: Diplomat (NF)",
        ":material/shield: Pengawal (SJ)",
        ":material/explore: Penjelajah (SP)",
    ])

    groups = {
        "NT": ["INTJ", "INTP", "ENTJ", "ENTP"],
        "NF": ["INFJ", "INFP", "ENFJ", "ENFP"],
        "SJ": ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
        "SP": ["ISTP", "ISFP", "ESTP", "ESFP"],
    }

    tab_map = {
        "NT": tab_nt,
        "NF": tab_nf,
        "SJ": tab_sj,
        "SP": tab_sp,
    }

    for grp_key, grp_codes in groups.items():
        with tab_map[grp_key]:
            cards_html = '<div class="char-grid-row">'
            for code in grp_codes:
                p = all_prof.get(code, {})
                col = p.get("color", "#4F46E5")
                bg = p.get("bg_tint", "#EEF2FF")
                bdr = p.get("border_color", "#C7D2FE")
                arch = p.get("archetype", code)
                desc = p.get("tagline", "")
                cog_dom = p.get("cognitive_roles", {}).get("dominant", "")
                dom_code = cog_dom.split()[0] if cog_dom else ""
                avatar_tag = render_avatar_img(code, size=75, alt=arch)

                cards_html += f"""
                <div class="char-card" style="border-top: 4px solid {col};">
                    <div class="char-avatar-pod" style="background:{bg};">
                        {avatar_tag}
                    </div>
                    <div>
                        <span class="char-code-badge" style="background:{bg}; color:{col}; border:1px solid {bdr};">{code}</span>
                        <div class="char-name">{arch}</div>
                    </div>
                    <p class="char-desc">{desc}</p>
                    <span class="char-cog-chip">{dom_code} Dominan</span>
                </div>
                """
            cards_html += "</div>"
            render_html(cards_html)

    st.markdown("<div style='height:0.8rem;'></div>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("**:material/info: Panduan pengerjaan**")
        st.caption(
            "• Jawab santai dan spontan aja, pilih opsi yang paling menggambarkan kebiasaan nyatamu sehari-hari.\n"
            "• Nggak ada jawaban yang benar atau salah; semua pilihan itu normal dan manusiawi banget.\n"
            "• Cuma butuh waktu sekitar 5 sampai 7 menit. Progres jawabanmu tersimpan otomatis, jadi kamu bisa santai."
        )

    st.markdown("<div style='height:0.6rem;'></div>", unsafe_allow_html=True)
    if st.button("Mulai asesmen", key="btn_start_quiz", type="primary", icon=":material/arrow_forward:", width="stretch"):
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

    # Keyboard shortcut listener using parent window safe JS
    render_html("""
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
    """)

    dim_map = {
        "EI": ("Mind", "Sumber energi: Kumpul seru vs Me-time tenang", "#4F46E5", "#EEF2FF", "#C7D2FE"),
        "SN": ("Energy", "Cara olah info: Fakta konkret vs Ide & kemungkinan", "#059669", "#ECFDF5", "#A7F3D0"),
        "TF": ("Nature", "Cara ambil keputusan: Logika objektif vs Rasa & empati", "#0284C7", "#F0F9FF", "#BAE6FD"),
        "JP": ("Tactics", "Pola keseharian: Rencana teratur vs Fleksibel santai", "#D97706", "#FFFBEB", "#FDE68A"),
    }
    dim_name, dim_detail, dim_col, dim_bg, dim_bdr = dim_map.get(
        q["dim"], (q["dim"], "", "#4F46E5", "#EEF2FF", "#C7D2FE")
    )

    # Header and Navigation Container
    with st.container(border=True):
        col_meta, col_jump, col_adv = st.columns([3, 1.8, 1.6], vertical_alignment="center")
        with col_meta:
            badge_html = f'<span style="background:{dim_bg}; color:{dim_col}; border:1px solid {dim_bdr}; padding:0.28rem 0.85rem; border-radius:9999px; font-size:0.78rem; font-weight:800; letter-spacing:0.04em;">{dim_name} ({q["dim"]})</span>'
            st.markdown(f"**Butir {current_idx + 1:02d} / {total:02d}** · {badge_html}", unsafe_allow_html=True)
            st.caption(dim_detail)
        with col_jump:
            with st.popover(f"Daftar butir ({answered_count}/{total})", icon=":material/format_list_numbered:", width="stretch"):
                st.caption("Pilih butir untuk meninjau status jawaban:")
                grid_cols = st.columns(4)
                for i in range(total):
                    c_slot = grid_cols[i % 4]
                    is_done = questions[i]["id"] in st.session_state.answers
                    is_curr = i == current_idx
                    lbl = f"#{i+1}"
                    if is_curr:
                        lbl += " ◉"
                    elif is_done:
                        lbl += " ✓"
                    if c_slot.button(lbl, key=f"jump_{i}", width="stretch"):
                        st.session_state.current_q = i
                        st.rerun()
        with col_adv:
            auto_val = st.toggle("Lanjut otomatis", value=st.session_state.auto_advance, key="toggle_auto_adv")
            st.session_state.auto_advance = auto_val

    st.progress((answered_count) / total)

    # Scenario Card
    render_html(f"""
    <div class="scenario-friendly-card" style="border-top: 4px solid {dim_col};">
        <div class="scenario-top-bar">
            <span style="font-size:0.78rem; font-weight:800; color:{dim_col}; text-transform:uppercase; letter-spacing:0.04em;">Skenario Nyata #{current_idx + 1}</span>
            <span style="font-size:0.78rem; color:#64748B; font-weight:600;">{answered_count} dari {total} butir terjawab</span>
        </div>
        <div class="scenario-quote-highlight">"{q['scenario']}"</div>
    </div>
    """)

    opt_a_text = q["opt_a"]["text"]
    opt_b_text = q["opt_b"]["text"]
    options = [opt_a_text, opt_b_text]

    current_ans = st.session_state.answers.get(q_id)
    default_idx = None
    if current_ans == "A":
        default_idx = 0
    elif current_ans == "B":
        default_idx = 1

    selected_option = st.radio(
        label=f"Pilihan Butir {current_idx + 1}",
        options=options,
        index=default_idx,
        key=f"radio_q_{current_idx}",
        label_visibility="collapsed"
    )

    if selected_option is not None:
        new_ans = "A" if selected_option == opt_a_text else "B"
        if st.session_state.answers.get(q_id) != new_ans:
            st.session_state.answers[q_id] = new_ans
            if st.session_state.auto_advance and current_idx < total - 1:
                st.session_state.trigger_advance_for = current_idx

    # Keyboard shortcut hint bar
    render_html("""
    <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.78rem; color:#64748B; margin:0.8rem 0 1.2rem; padding:0.4rem 0.75rem; background:rgba(255,255,255,0.7); backdrop-filter:blur(8px); border-radius:8px; border:1px solid #E2E8F0;">
        <span>Pintasan keyboard: <kbd style="background:#FFFFFF; border:1px solid #CBD5E1; border-radius:4px; padding:0.15rem 0.4rem; font-weight:700;">1</kbd> / <kbd style="background:#FFFFFF; border:1px solid #CBD5E1; border-radius:4px; padding:0.15rem 0.4rem; font-weight:700;">A</kbd> Opsi atas &nbsp;·&nbsp; <kbd style="background:#FFFFFF; border:1px solid #CBD5E1; border-radius:4px; padding:0.15rem 0.4rem; font-weight:700;">2</kbd> / <kbd style="background:#FFFFFF; border:1px solid #CBD5E1; border-radius:4px; padding:0.15rem 0.4rem; font-weight:700;">B</kbd> Opsi bawah</span>
        <span>Navigasi: <kbd style="background:#FFFFFF; border:1px solid #CBD5E1; border-radius:4px; padding:0.15rem 0.4rem; font-weight:700;">←</kbd> Sebelumnya &nbsp;·&nbsp; <kbd style="background:#FFFFFF; border:1px solid #CBD5E1; border-radius:4px; padding:0.15rem 0.4rem; font-weight:700;">→</kbd> Berikutnya</span>
    </div>
    """)

    # Bottom Navigation Controls
    col_prev, col_next = st.columns([1, 1], gap="medium")
    with col_prev:
        if st.button("Sebelumnya", key=f"btn_p_{current_idx}", type="secondary", icon=":material/arrow_back:", disabled=(current_idx == 0), width="stretch"):
            st.session_state.current_q -= 1
            st.rerun()

    with col_next:
        if current_idx < total - 1:
            is_answered = q_id in st.session_state.answers
            next_label = "Berikutnya" if is_answered else "Pilih satu opsi terlebih dahulu"
            if st.button(next_label, key=f"btn_n_{current_idx}", type="primary", icon=":material/arrow_forward:", disabled=not is_answered, width="stretch"):
                st.session_state.current_q += 1
                st.rerun()
        else:
            all_done = (len(st.session_state.answers) == total)
            btn_finish_label = "Lihat hasil analisis" if all_done else f"Jawab seluruh butir ({answered_count}/{total})"
            if st.button(btn_finish_label, key="btn_finish_test", type="primary", icon=":material/insights:", disabled=not all_done, width="stretch"):
                with st.spinner("Mengkalkulasi spektrum psikometrik dan arsitektur fungsi kognitif..."):
                    result = engine.compute_result(st.session_state.answers)
                    st.session_state.result = result
                    st.session_state.page = "result"
                    st.rerun()

    # Trigger auto-advance if activated
    if st.session_state.trigger_advance_for == current_idx:
        st.session_state.trigger_advance_for = None
        time.sleep(0.18)
        st.session_state.current_q += 1
        st.rerun()


def render_result(result: MBTIResult) -> None:
    profile = get_profile(result.mbti_type)
    theme_color = profile.get("color", "#4F46E5")
    temperament = profile.get("temperament", "Tipologi kognitif")
    bg_tint = profile.get("bg_tint", "#EEF2FF")
    border_color = profile.get("border_color", "#C7D2FE")
    archetype = profile.get("archetype", result.mbti_type)
    summary_narrative = profile.get("summary", "")
    avatar_hero_tag = render_avatar_img(result.mbti_type, size=115, alt=archetype)

    # Hero Result Presentation (Claymorphic + Glassmorphic Hero Split)
    render_html(f"""
    <div class="friendly-result-hero" style="border-top: 5px solid {theme_color};">
        <div class="hero-result-flex">
            <div class="hero-result-content">
                <span style="background:{bg_tint}; color:{theme_color}; border:1.5px solid {border_color}; padding:0.35rem 1rem; border-radius:9999px; font-size:0.8rem; font-weight:800; text-transform:uppercase; letter-spacing:0.05em; display:inline-block; margin-bottom:0.4rem;">
                    {temperament}
                </span>
                <div class="hero-type-code" style="color:{theme_color};">{result.mbti_type}</div>
                <h2 style="font-family:'Space Grotesk',sans-serif; font-size:1.55rem; font-weight:800; color:#1E1B4B; margin:0 0 0.35rem; letter-spacing:-0.025em;">
                    {archetype}
                </h2>
                <div class="tagline-callout" style="border-left: 4px solid {theme_color};">
                    "{profile.get('tagline', '')}"
                </div>
            </div>
            <div class="hero-result-avatar-box">
                <div class="clay-avatar-hero" style="background:{bg_tint}; border-color:{border_color};">
                    {avatar_hero_tag}
                </div>
                <span style="font-family:'Space Grotesk',sans-serif; font-size:0.82rem; font-weight:700; color:{theme_color}; margin-top:0.6rem;">{result.mbti_type}</span>
            </div>
        </div>
        <p style="font-size:0.95rem; color:#334155; line-height:1.74; margin:1.3rem 0 0; border-top:1px solid #F1F5F9; padding-top:1.1rem;">
            {summary_narrative}
        </p>
    </div>
    """)

    # Borderline Advisory
    if result.borderline_dims:
        dim_labels = {
            "EI": "Mind (Sosial vs Me-Time)",
            "SN": "Energy (Fakta Nyata vs Ide & Kemungkinan)",
            "TF": "Nature (Logika Objektif vs Rasa & Empati)",
            "JP": "Tactics (Rencana Teratur vs Fleksibel Santai)",
        }
        bl_text = ", ".join(dim_labels.get(d, d) for d in result.borderline_dims)
        with st.container(border=True):
            st.markdown("**:material/info: Zona fleksibel (keseimbangan adaptif)**")
            st.caption(
                f"Skormu pada dimensi **{bl_text}** berada di rentang tengah yang seimbang (47%–53%). "
                "Ini tanda bagus kalau kamu punya fleksibilitas tinggi: bisa menyesuaikan diri dengan luwes sesuai situasi dan kebutuhan momen yang kamu hadapi!"
            )

    # Spectrum Rows Generator
    dim_pairs = {
        "EI": ("Ekstraversi (Sosial)", "Introversi (Me-Time)", "#4F46E5"),
        "SN": ("Penginderaan (Fakta Nyata)", "Intuisi (Ide & Pola)", "#059669"),
        "TF": ("Pemikiran (Logika Objektif)", "Perasaan (Rasa & Empati)", "#0284C7"),
        "JP": ("Penilaian (Rencana Teratur)", "Eksplorasi (Fleksibel Spontan)", "#D97706"),
    }
    spectrum_html = ""
    for dim_code, (pos_name, neg_name, bar_col) in dim_pairs.items():
        score_obj = result.dimensions[dim_code]
        pct_pos = score_obj.pos_pct
        pct_neg = round(100.0 - pct_pos, 1)
        dom_side = pos_name if pct_pos >= 50 else neg_name
        dom_pct = pct_pos if pct_pos >= 50 else pct_neg
        bl_tag = '<span class="badge-balance-pill">Fleksibel</span>' if score_obj.is_borderline else ""

        spectrum_html += f"""
        <div class="spectrum-row-box">
            <div class="spectrum-info-bar">
                <span class="pole-tag {'active' if pct_pos >= 50 else ''}">{pos_name} {pct_pos:.0f}%</span>
                <div>
                    <strong style="color:#1E1B4B; font-size:0.92rem;">{dom_side} {dom_pct:.0f}%</strong>
                    {bl_tag}
                </div>
                <span class="pole-tag {'active' if pct_neg > 50 else ''}">{neg_name} {pct_neg:.0f}%</span>
            </div>
            <div class="spectrum-track-bg">
                <div class="spectrum-center-divider" title="Garis Keseimbangan 50%"></div>
                <div class="spectrum-fill-progress" style="width: {pct_pos}%; background: {bar_col};"></div>
            </div>
        </div>
        """

    with st.container(border=True):
        st.markdown("**Spektrum kecenderungan 4 dimensi**")
        st.caption("Pola alami caramu berpikir dan mengolah energi (garis tengah menandai titik keseimbangan 50%):")
        render_html(spectrum_html)

    # 4 Deep-Dive Tabs
    tab_cog, tab_strength, tab_work, tab_stress = st.tabs([
        ":material/schema: Cara berpikir",
        ":material/insights: Kelebihan & titik buta",
        ":material/work: Gaya kerja & pertemanan",
        ":material/shield: Menghadapi stres",
    ])

    with tab_cog:
        role_meta = {
            "dominant": ("Pilar utama (Dominant)", "Kekuatan naluriah terbesarmu dalam mengambil keputusan sehari-hari"),
            "auxiliary": ("Pemandu pendukung (Auxiliary)", "Teman berpikir yang bikin langkahmu tetap seimbang dan realistis"),
            "tertiary": ("Sisi santai (Tertiary)", "Sisi rileks yang muncul waktu kamu lagi santai dan nggak ada beban"),
            "inferior": ("Titik rawan lelah (Inferior)", "Sisi yang paling cepat capek saat kamu burnout atau stres berat")
        }
        cog_stack = profile.get("cognitive_roles", result.cognitive_stack)
        cog_items_html = ""
        for r_key, (r_label, r_sub) in role_meta.items():
            val = cog_stack.get(r_key, result.cognitive_stack.get(r_key, "-"))
            parts = val.split(": ", 1) if ": " in val else (val, "")
            func_name = parts[0]
            func_detail = parts[1] if len(parts) > 1 else ""
            func_code = func_name.split()[0] if func_name else ""

            cog_items_html += f"""
            <div class="cog-layer-friendly-card" style="border-left: 4px solid {theme_color};">
                <div class="cog-layer-header">
                    <span class="cog-role-badge">{r_label}</span>
                    <span class="cog-symbol-tag" style="color:{theme_color}; background:{bg_tint}; border-color:{border_color};">{func_code}</span>
                </div>
                <div class="cog-func-heading">{func_name}</div>
                <p class="cog-func-paragraph">{func_detail}</p>
            </div>
            """

        with st.container(border=True):
            st.markdown("**Hierarki 4 lapisan fungsi kognitif Carl Jung**")
            st.caption("Memetakan cara kerja otakmu dari naluri yang paling aktif sampai sisi yang rentan lelah:")
            render_html(cog_items_html)

    with tab_strength:
        sb = profile.get("strengths_blindspots", {})
        c_sup, c_bli = st.columns(2, gap="medium")
        with c_sup:
            with st.container(border=True):
                st.markdown("**:material/check_circle: Kelebihan utamamu**")
                st.caption(sb.get("strengths", "-"))
        with c_bli:
            with st.container(border=True):
                st.markdown("**:material/tips_and_updates: Hal yang perlu kamu waspadai**")
                st.caption(sb.get("blindspots", "-"))

    with tab_work:
        with st.container(border=True):
            st.markdown("**:material/hub: Gaya kerja & dinamika tim**")
            st.caption(profile.get("work_style", "-"))

    with tab_stress:
        with st.container(border=True):
            st.markdown("**:material/healing: Saat stres & cara recharge paling ampuh**")
            st.caption(profile.get("stress_dynamics", "-"))

    # Structured Export
    summary_text = (
        f"[HASIL ASESMEN TIPE MBTI]\n"
        f"Tipe: {result.mbti_type}: {archetype}\n"
        f"Kelompok: {temperament}\n\n"
        f"Kecenderungan Spektrum:\n"
        f"• Mind:    {result.dimensions['EI'].pos_pct:.0f}% Ekstraversi / {result.dimensions['EI'].neg_pct:.0f}% Introversi\n"
        f"• Energy:  {result.dimensions['SN'].pos_pct:.0f}% Penginderaan / {result.dimensions['SN'].neg_pct:.0f}% Intuisi\n"
        f"• Nature:  {result.dimensions['TF'].pos_pct:.0f}% Pemikiran / {result.dimensions['TF'].neg_pct:.0f}% Perasaan\n"
        f"• Tactics: {result.dimensions['JP'].pos_pct:.0f}% Penilaian / {result.dimensions['JP'].neg_pct:.0f}% Eksplorasi\n\n"
        f"Fungsi Dominan: {result.cognitive_stack.get('dominant', '-')}\n"
        f"Catatan: \"{profile.get('tagline', '')}\""
    )

    with st.container(border=True):
        st.markdown("**Unduh laporan asesmen**")
        st.caption("Salin ringkasan teks atau unduh dokumen evaluasi untuk arsip pribadi maupun profesional:")
        render_html(f'<div class="copy-box-area">{summary_text}</div>')
        st.download_button(
            label="Unduh dokumen laporan (.txt)",
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
        if st.button("Ulangi asesmen", key="btn_repeat_test", type="primary", icon=":material/restart_alt:", width="stretch"):
            st.session_state.page = "quiz"
            st.session_state.answers = {}
            st.session_state.current_q = 0
            st.session_state.result = None
            st.rerun()
    with c_hom:
        if st.button("Kembali ke beranda", key="btn_return_home_res", type="secondary", icon=":material/home:", width="stretch"):
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
