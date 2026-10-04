from __future__ import annotations
import random
import textwrap
import streamlit as st
from engine import PersonalityEngine, MBTIResult
from profiles import get_profile, get_all_profiles, get_avatar_base64

st.set_page_config(
    page_title="Tes Spektrum MBTI · Kenali Diri Lebih Seru",
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
        f'style="object-fit:contain; display:block; margin:0 auto; filter:drop-shadow(0 6px 14px rgba(0,0,0,0.08));" />'
    )


APP_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700;800&display=swap');

/* ==================== GLASSMORPHISM & TACTILE DESIGN TOKENS ==================== */
:root {
    --bg-canvas: #F8FAFC;
    --surface-glass: rgba(255, 255, 255, 0.78);
    --surface-glass-strong: rgba(255, 255, 255, 0.90);
    --surface-glass-subtle: rgba(255, 255, 255, 0.58);
    
    --border-glass: 1.5px solid rgba(255, 255, 255, 0.85);
    --border-glass-subtle: 1px solid rgba(226, 232, 240, 0.8);
    --border-primary: #4F46E5;
    
    --text-title: #0F172A;
    --text-main: #1E293B;
    --text-body: #475569;
    --text-muted: #64748B;
    
    /* 4 Temperament Theme Colors */
    --nt-color: #4F46E5;
    --nt-bg: rgba(238, 242, 255, 0.85);
    --nt-border: #C7D2FE;
    
    --nf-color: #059669;
    --nf-bg: rgba(236, 253, 245, 0.85);
    --nf-border: #A7F3D0;
    
    --sj-color: #0284C7;
    --sj-bg: rgba(240, 249, 255, 0.85);
    --sj-border: #BAE6FD;
    
    --sp-color: #D97706;
    --sp-bg: rgba(255, 251, 235, 0.85);
    --sp-border: #FDE68A;

    /* Geometry */
    --radius-hero: 24px;
    --radius-card: 18px;
    --radius-md: 12px;
    --radius-pill: 9999px;
    
    /* Pure Glassmorphic Soft Shadows */
    --glass-shadow: 
        0 14px 34px -4px rgba(31, 38, 135, 0.07),
        0 2px 8px -1px rgba(15, 23, 42, 0.03),
        inset 0 1px 1.5px rgba(255, 255, 255, 0.95);
        
    --glass-shadow-hover: 
        0 20px 42px -4px rgba(79, 70, 229, 0.14),
        0 4px 12px -2px rgba(15, 23, 42, 0.04),
        inset 0 1px 1.5px rgba(255, 255, 255, 0.95);
        
    --glass-shadow-soft:
        0 8px 20px -3px rgba(31, 38, 135, 0.05),
        inset 0 1px 1px rgba(255, 255, 255, 0.9);
}

/* Atmospheric Canvas Background */
html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: var(--text-main) !important;
    background: 
        radial-gradient(ellipse 75% 45% at 15% -5%, rgba(99, 102, 241, 0.12), transparent 55%),
        radial-gradient(ellipse 65% 45% at 85% 15%, rgba(16, 185, 129, 0.09), transparent 50%),
        radial-gradient(ellipse 65% 55% at 50% 100%, rgba(2, 132, 199, 0.08), transparent 55%),
        #F8FAFC !important;
    background-attachment: fixed !important;
}

header, footer, [data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu {
    display: none !important;
}

.main .block-container {
    padding: 2.2rem 1.4rem 4.5rem !important;
    max-width: 880px !important;
}

/* Glassmorphism for Streamlit Native Containers */
[data-testid="stVerticalBlockBorderWrapper"] > div {
    background: var(--surface-glass) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: var(--border-glass) !important;
    border-radius: var(--radius-card) !important;
    box-shadow: var(--glass-shadow-soft) !important;
}

/* Popover Glassmorphic Style */
div[data-testid="stPopoverBody"] {
    background: rgba(255, 255, 255, 0.92) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border: 1.5px solid rgba(255, 255, 255, 0.9) !important;
    border-radius: var(--radius-card) !important;
    box-shadow: 0 18px 40px -4px rgba(31, 38, 135, 0.15) !important;
}

/* ==================== GLASSMORPHIC HERO CONTAINER ==================== */
.friendly-hero {
    background: var(--surface-glass);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: var(--border-glass);
    border-radius: var(--radius-hero);
    box-shadow: var(--glass-shadow);
    padding: 2.6rem 2.2rem 2.2rem;
    text-align: center;
    margin-bottom: 1.3rem;
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
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    color: #4338CA;
    border: 1px solid rgba(199, 210, 254, 0.7);
    box-shadow: 0 2px 8px rgba(79, 70, 229, 0.08);
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
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 0.35rem 0.95rem;
    border-radius: var(--radius-pill);
    border: 1px solid rgba(226, 232, 240, 0.8);
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
}

/* ==================== 3 PILLARS GLASS GRID ==================== */
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
    background: var(--surface-glass);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-radius: var(--radius-card);
    border: var(--border-glass);
    box-shadow: var(--glass-shadow-soft);
    padding: 1.35rem 1.25rem;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    height: 100%;
    box-sizing: border-box;
    transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.22s ease;
}

.pillar-card:hover {
    transform: translateY(-3px);
    box-shadow: var(--glass-shadow-hover);
    background: var(--surface-glass-strong);
}

.pillar-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.02rem;
    font-weight: 700;
    color: var(--text-title);
    margin: 0 0 0.45rem;
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
    background: var(--surface-glass);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 20px;
    border: var(--border-glass);
    box-shadow: var(--glass-shadow-soft);
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
    background: var(--surface-glass-strong);
    box-shadow: var(--glass-shadow-hover);
}

.char-avatar-pod {
    width: 96px;
    height: 96px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 0.85rem;
    border: 2px solid rgba(255, 255, 255, 0.9);
    box-shadow: 0 6px 16px rgba(31, 38, 135, 0.08);
    transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1);
}

.char-card:hover .char-avatar-pod {
    transform: scale(1.07);
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
    -webkit-backdrop-filter: blur(8px);
    border: 1px solid rgba(226, 232, 240, 0.85);
    border-radius: var(--radius-pill);
    padding: 0.22rem 0.7rem;
    color: var(--text-muted);
}

/* ==================== REAL-TIME QUIZ PROGRESS BAR ==================== */
.quiz-progress-wrapper {
    margin: 0.9rem 0 1.25rem;
    padding: 0.75rem 1.1rem;
    background: var(--surface-glass);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: var(--border-glass);
    border-radius: var(--radius-md);
    box-shadow: var(--glass-shadow-soft);
}

.quiz-progress-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.45rem;
    font-size: 0.82rem;
    font-weight: 700;
}

.quiz-progress-text {
    color: var(--text-title);
    letter-spacing: 0.02em;
}

.quiz-progress-pct {
    color: #4F46E5;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 800;
}

.quiz-progress-track {
    height: 10px;
    background: rgba(226, 232, 240, 0.75);
    border-radius: 9999px;
    position: relative;
    overflow: hidden;
    box-shadow: inset 0 1px 2px rgba(15, 23, 42, 0.08);
}

.quiz-progress-fill {
    height: 100%;
    border-radius: 9999px;
    background: linear-gradient(90deg, #6366F1 0%, #3B82F6 50%, #10B981 100%);
    box-shadow: 0 0 10px rgba(99, 102, 241, 0.4);
    transition: width 0.38s cubic-bezier(0.16, 1, 0.3, 1);
}

/* ==================== QUIZ SCENARIO CONTAINER ==================== */
.scenario-friendly-card {
    background: var(--surface-glass);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: var(--border-glass);
    border-radius: var(--radius-hero);
    padding: 1.85rem 2rem 1.6rem;
    box-shadow: var(--glass-shadow);
    margin-bottom: 1.1rem;
    position: relative;
}

.scenario-top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.85rem;
    padding-bottom: 0.65rem;
    border-bottom: 1px solid rgba(226, 232, 240, 0.7);
}

.scenario-quote-highlight {
    font-size: 1.15rem;
    font-weight: 700;
    line-height: 1.72;
    color: var(--text-title);
    margin: 0.5rem 0 1rem;
    letter-spacing: -0.015em;
}

/* ==================== TACTILE QUIZ OPTION CARDS ==================== */
.st-key-quiz_options_container {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.95rem !important;
    margin: 1.1rem 0 1.25rem !important;
}

.st-key-quiz_options_container div[data-testid="stButton"] {
    width: 100% !important;
}

.st-key-quiz_options_container div[data-testid="stButton"] button {
    width: 100% !important;
    min-height: 76px !important;
    padding: 1.2rem 1.55rem !important;
    text-align: left !important;
    justify-content: flex-start !important;
    align-items: center !important;
    border-radius: var(--radius-card) !important;
    background: var(--surface-glass) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: var(--border-glass) !important;
    box-shadow: var(--glass-shadow) !important;
    transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1) !important;
    white-space: normal !important;
    word-break: break-word !important;
    color: var(--text-body) !important;
    font-size: 0.98rem !important;
    line-height: 1.64 !important;
    font-weight: 500 !important;
    cursor: pointer !important;
}

.st-key-quiz_options_container div[data-testid="stButton"] button:hover {
    transform: translateY(-2.5px) scale(1.002) !important;
    border-color: #818CF8 !important;
    background: rgba(255, 255, 255, 0.95) !important;
    box-shadow: var(--glass-shadow-hover) !important;
    color: var(--text-title) !important;
}

.st-key-quiz_options_container div[data-testid="stButton"] button:active {
    transform: translateY(1px) scale(0.995) !important;
}

.st-key-quiz_options_container div[data-testid="stButton"] button div[data-testid="stMarkdownContainer"] {
    width: 100% !important;
    text-align: left !important;
}

.st-key-quiz_options_container div[data-testid="stButton"] button div[data-testid="stMarkdownContainer"] p {
    margin: 0 !important;
    font-size: 0.98rem !important;
    line-height: 1.64 !important;
    text-align: left !important;
}

/* Selected Option Highlight State */
.st-key-quiz_options_container div[data-testid="stButton"] button[kind="primary"],
.st-key-quiz_options_container div[data-testid="stButton"] button[data-testid="baseButton-primary"] {
    background: rgba(238, 242, 255, 0.95) !important;
    border-color: #4F46E5 !important;
    color: #1E1B4B !important;
    box-shadow: 0 0 0 2px #4F46E5, 0 12px 28px -4px rgba(79, 70, 229, 0.22) !important;
    font-weight: 600 !important;
}

/* ==================== BUTTONS CLEAN & TACTILE ==================== */
button[data-testid="baseButton-primary"] {
    background: linear-gradient(135deg, #4F46E5 0%, #4338CA 100%) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(255, 255, 255, 0.25) !important;
    border-radius: var(--radius-md) !important;
    box-shadow: 0 6px 18px rgba(79, 70, 229, 0.32), inset 0 1px 1px rgba(255, 255, 255, 0.3) !important;
    min-height: 48px !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    letter-spacing: -0.01em !important;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

button[data-testid="baseButton-primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 26px rgba(79, 70, 229, 0.42), inset 0 1px 1px rgba(255, 255, 255, 0.3) !important;
    background: linear-gradient(135deg, #4338CA 0%, #3730A3 100%) !important;
}

button[data-testid="baseButton-primary"]:active {
    transform: translateY(1px) scale(0.995) !important;
}

button[data-testid="baseButton-secondary"] {
    background: var(--surface-glass) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    color: var(--text-main) !important;
    border: var(--border-glass) !important;
    border-radius: var(--radius-md) !important;
    box-shadow: var(--glass-shadow-soft) !important;
    min-height: 48px !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

button[data-testid="baseButton-secondary"]:hover {
    border-color: #CBD5E1 !important;
    background: rgba(255, 255, 255, 0.92) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 22px rgba(31, 38, 135, 0.08) !important;
}

button[data-testid="baseButton-secondary"]:active {
    transform: translateY(1px) scale(0.995) !important;
}

/* ==================== SEGMENTED GLASS TABS (NO HORIZONTAL SCROLL) ==================== */
div[data-baseweb="tab-list"] {
    display: flex !important;
    width: 100% !important;
    gap: 0.35rem !important;
    background: rgba(241, 245, 249, 0.75) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    padding: 0.35rem !important;
    border-radius: var(--radius-md) !important;
    border: 1px solid rgba(226, 232, 240, 0.85) !important;
    overflow-x: hidden !important;
    margin-bottom: 1.1rem !important;
}

div[data-baseweb="tab-list"] button[data-baseweb="tab"] {
    flex: 1 1 0 !important;
    min-width: 0 !important;
    padding: 0.55rem 0.35rem !important;
    font-size: 0.86rem !important;
    font-weight: 600 !important;
    text-align: center !important;
    justify-content: center !important;
    border-radius: 9px !important;
    color: var(--text-body) !important;
    white-space: nowrap !important;
    border: none !important;
    background: transparent !important;
    transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

div[data-baseweb="tab-list"] button[data-baseweb="tab"]:hover {
    color: var(--text-title) !important;
    background: rgba(255, 255, 255, 0.5) !important;
}

div[data-baseweb="tab-list"] button[data-baseweb="tab"][aria-selected="true"] {
    background: #FFFFFF !important;
    color: var(--text-title) !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08), 0 1px 2px rgba(15, 23, 42, 0.04) !important;
}

div[data-baseweb="tab-highlight"], div[data-baseweb="tab-border"] {
    display: none !important;
}

/* ==================== RESULT HERO & SEAMLESS CHARACTER ==================== */
.friendly-result-hero {
    background: var(--surface-glass);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: var(--border-glass);
    border-radius: var(--radius-hero);
    box-shadow: var(--glass-shadow);
    padding: 2.2rem 2.2rem 2rem;
    margin-bottom: 1.4rem;
    position: relative;
    overflow: hidden;
}

.hero-result-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.8rem;
    margin-bottom: 1.25rem;
}

.hero-result-identity {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.hero-badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.35rem 0.95rem;
    border-radius: var(--radius-pill);
    font-size: 0.78rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    width: fit-content;
    margin-bottom: 0.45rem;
}

.hero-type-code {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1.05;
    margin: 0 0 0.25rem;
}

.hero-archetype-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: var(--text-title);
    margin: 0;
    letter-spacing: -0.025em;
    line-height: 1.25;
}

/* Seamless Avatar: Tanpa Card Pod, Karakter Menyatu Alami */
.hero-avatar-seamless {
    flex-shrink: 0;
    width: 140px;
    height: 140px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0;
}

.hero-avatar-seamless img {
    width: 130px !important;
    height: 130px !important;
    object-fit: contain;
    filter: drop-shadow(0 10px 18px rgba(0, 0, 0, 0.12));
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), filter 0.3s ease;
}

.hero-avatar-seamless:hover img {
    transform: scale(1.06) translateY(-2px);
    filter: drop-shadow(0 14px 24px rgba(0, 0, 0, 0.16));
}

.hero-tagline-quote {
    font-size: 0.98rem;
    line-height: 1.68;
    color: var(--text-body);
    background: rgba(255, 255, 255, 0.65);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: var(--radius-md);
    padding: 1rem 1.35rem;
    margin: 0 0 1.2rem;
    border: 1px solid rgba(226, 232, 240, 0.7);
    font-weight: 500;
    box-sizing: border-box;
}

.hero-narrative-text {
    font-size: 0.96rem;
    color: #334155;
    line-height: 1.76;
    margin: 0;
    padding-top: 1.15rem;
    border-top: 1px solid rgba(226, 232, 240, 0.7);
}

@media (max-width: 680px) {
    .hero-result-header {
        flex-direction: column-reverse;
        align-items: center;
        text-align: center;
        gap: 1.2rem;
    }
    
    .hero-result-identity {
        align-items: center;
    }
    
    .hero-avatar-seamless {
        width: 120px;
        height: 120px;
    }
    
    .hero-avatar-seamless img {
        width: 110px !important;
        height: 110px !important;
    }
    
    .hero-tagline-quote {
        text-align: center;
    }
}

/* ==================== SPECTRUM TRACK ==================== */
.spectrum-row-box {
    margin-bottom: 1.3rem;
}

.spectrum-info-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.55rem;
    font-size: 0.88rem;
}

.pole-winner {
    font-weight: 800 !important;
    color: #1E1B4B !important;
    opacity: 1 !important;
    font-size: 0.92rem !important;
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.24rem 0.75rem;
    border-radius: var(--radius-pill);
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}

.pole-muted {
    font-weight: 500 !important;
    color: #94A3B8 !important;
    opacity: 0.52 !important;
    font-size: 0.84rem !important;
    padding: 0.24rem 0.5rem;
}

.spectrum-track-bg {
    height: 16px;
    background: rgba(226, 232, 240, 0.8);
    border-radius: var(--radius-pill);
    position: relative;
    overflow: hidden;
    box-shadow: inset 1px 1px 3px rgba(0,0,0,0.08);
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
    box-shadow: 0 0 4px rgba(0,0,0,0.25);
}

/* ==================== COGNITIVE LAYERS ==================== */
.cog-layer-friendly-card {
    background: var(--surface-glass);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: var(--border-glass-subtle);
    border-radius: var(--radius-md);
    box-shadow: var(--glass-shadow-soft);
    padding: 1.15rem 1.3rem;
    margin-bottom: 0.85rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.cog-layer-friendly-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--glass-shadow);
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
    background: rgba(248, 250, 252, 0.85);
    border-radius: var(--radius-md);
    padding: 1.1rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 0.82rem;
    color: var(--text-main);
    line-height: 1.7;
    border: 1px solid rgba(226, 232, 240, 0.85);
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
        "shuffled_options": {},
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val


def start_quiz_session(engine: PersonalityEngine) -> None:
    st.session_state.page = "quiz"
    st.session_state.current_q = 0
    st.session_state.answers = {}
    st.session_state.result = None
    questions = engine.get_questions()
    st.session_state.shuffled_options = {q["id"]: (random.random() < 0.5) for q in questions}


def render_home(engine: PersonalityEngine) -> None:
    render_html("""
    <div class="friendly-hero">
        <div class="badge-friendly-tag">Tes Tipe Kepribadian</div>
        <h1 style="font-family:'Space Grotesk',sans-serif; font-size:2.45rem; font-weight:800; color:#1E1B4B; margin:0.95rem 0 0.45rem; letter-spacing:-0.035em;">
            Tes spektrum kepribadian MBTI
        </h1>
        <p style="font-size:1.02rem; color:#475569; line-height:1.72; max-width:620px; margin:0 auto;">
            Kenali tipe kepribadian dan cara unik otakmu memproses hal-hal di sekitarmu, mengambil keputusan, dan berinteraksi sehari-hari lewat 24 skenario yang dekat banget sama kehidupan nyata.
        </p>
        <div class="pill-row-cluster">
            <span class="pill-feature-chip">24 Skenario kehidupan nyata</span>
            <span class="pill-feature-chip">8 Pola pikir & naluri alami</span>
            <span class="pill-feature-chip">Spektrum luwes 0–100%</span>
            <span class="pill-feature-chip">Bebas jawaban benar/salah</span>
        </div>
    </div>
    """)

    # 3 Methodology Pillars (Glassmorphism Grid)
    render_html("""
    <div class="pillar-grid-row">
        <div class="pillar-card">
            <div class="pillar-title">Dilema realistis</div>
            <p class="pillar-desc">Pilihan situasinya membumi dan nyata, tanpa opsi klise atau jebakan jawaban yang dibuat-buat.</p>
        </div>
        <div class="pillar-card">
            <div class="pillar-title">Spektrum fleksibel</div>
            <p class="pillar-desc">Melihat persentase kecenderunganmu secara luwes, bukan kotak kaku hitam-putih.</p>
        </div>
        <div class="pillar-card">
            <div class="pillar-title">Cara berpikir alami</div>
            <p class="pillar-desc">Melihat 4 cara berpikir unikmu, dari kebiasaan sehari-hari sampai saat kamu lagi stres.</p>
        </div>
    </div>
    """)

    # 16Personalities Character Showcase
    render_html("""
    <div class="showcase-header-box">
        <div class="showcase-heading">Eksplorasi 16 karakter kepribadian</div>
        <div class="showcase-subheading">
            Tiap karakter punya keunikan visual, cara pandang tersendiri, dan kontribusi seru dalam menjalani hidup:
        </div>
    </div>
    """)

    all_prof = get_all_profiles()
    tab_nt, tab_nf, tab_sj, tab_sp = st.tabs([
        "Analis (NT)",
        "Diplomat (NF)",
        "Pengawal (SJ)",
        "Penjelajah (SP)",
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
        start_quiz_session(engine)
        st.rerun()


def render_quiz(engine: PersonalityEngine) -> None:
    questions = engine.get_questions()
    total = len(questions)
    answered_count = len(st.session_state.answers)
    current_idx = st.session_state.current_q
    q = questions[current_idx]
    q_id = q["id"]

    # Pastikan dictionary acak opsi terisi
    if "shuffled_options" not in st.session_state or not st.session_state.shuffled_options:
        st.session_state.shuffled_options = {item["id"]: (random.random() < 0.5) for item in questions}

    dim_map = {
        "EI": ("Mind", "Sumber energi: Kumpul seru vs Me-time tenang", "#4F46E5", "rgba(238, 242, 255, 0.85)", "#C7D2FE"),
        "SN": ("Energy", "Cara olah info: Fakta konkret vs Ide & kemungkinan", "#059669", "rgba(236, 253, 245, 0.85)", "#A7F3D0"),
        "TF": ("Nature", "Cara ambil keputusan: Logika objektif vs Rasa & empati", "#0284C7", "rgba(240, 249, 255, 0.85)", "#BAE6FD"),
        "JP": ("Tactics", "Pola keseharian: Rencana teratur vs Fleksibel santai", "#D97706", "rgba(255, 251, 235, 0.85)", "#FDE68A"),
    }
    dim_name, dim_detail, dim_col, dim_bg, dim_bdr = dim_map.get(
        q["dim"], (q["dim"], "", "#4F46E5", "rgba(238, 242, 255, 0.85)", "#C7D2FE")
    )

    # Header and Navigation Container (Clean, no toggle)
    with st.container(border=True):
        col_meta, col_jump = st.columns([3.5, 1.5], vertical_alignment="center")
        with col_meta:
            badge_html = f'<span style="background:{dim_bg}; color:{dim_col}; border:1px solid {dim_bdr}; padding:0.25rem 0.85rem; border-radius:9999px; font-size:0.78rem; font-weight:800; letter-spacing:0.04em;">{dim_name} ({q["dim"]})</span>'
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

    # Real-Time Glassmorphic Progress Bar
    pct = (answered_count / total) * 100.0
    render_html(f"""
    <div class="quiz-progress-wrapper">
        <div class="quiz-progress-meta">
            <span class="quiz-progress-text">Progres Jawaban</span>
            <span class="quiz-progress-pct">{answered_count} dari {total} butir ({pct:.0f}%)</span>
        </div>
        <div class="quiz-progress-track">
            <div class="quiz-progress-fill" style="width: {pct}%;"></div>
        </div>
    </div>
    """)

    # Scenario Card (Glassmorphism)
    render_html(f"""
    <div class="scenario-friendly-card" style="border-top: 4px solid {dim_col};">
        <div class="scenario-top-bar">
            <span style="font-size:0.78rem; font-weight:800; color:{dim_col}; text-transform:uppercase; letter-spacing:0.04em;">Skenario Nyata #{current_idx + 1}</span>
            <span style="font-size:0.78rem; color:#64748B; font-weight:600;">{answered_count} dari {total} butir terjawab</span>
        </div>
        <div class="scenario-quote-highlight">"{q['scenario']}"</div>
    </div>
    """)

    # Acak letak opsi A dan B
    is_flipped = st.session_state.shuffled_options.get(q_id, False)
    opt_first = q["opt_b"] if is_flipped else q["opt_a"]
    opt_second = q["opt_a"] if is_flipped else q["opt_b"]
    code_first = "B" if is_flipped else "A"
    code_second = "A" if is_flipped else "B"

    current_ans = st.session_state.answers.get(q_id)
    is_first_sel = (current_ans == code_first)
    is_second_sel = (current_ans == code_second)

    label_1 = f"**A.** &nbsp; {opt_first['text']}"
    if is_first_sel:
        label_1 += " &nbsp; :material/check_circle: *(Terpilih)*"

    label_2 = f"**B.** &nbsp; {opt_second['text']}"
    if is_second_sel:
        label_2 += " &nbsp; :material/check_circle: *(Terpilih)*"

    # Options Interactive Cards: Sekali klik langsung tercatat & otomatis beralih butir
    with st.container(key="quiz_options_container"):
        if st.button(
            label_1,
            key=f"opt_btn_{current_idx}_0",
            type="primary" if is_first_sel else "secondary",
            width="stretch"
        ):
            st.session_state.answers[q_id] = code_first
            if current_idx < total - 1:
                st.session_state.current_q = current_idx + 1
            st.rerun()

        if st.button(
            label_2,
            key=f"opt_btn_{current_idx}_1",
            type="primary" if is_second_sel else "secondary",
            width="stretch"
        ):
            st.session_state.answers[q_id] = code_second
            if current_idx < total - 1:
                st.session_state.current_q = current_idx + 1
            st.rerun()

    st.markdown("<div style='height:0.6rem;'></div>", unsafe_allow_html=True)

    # Bottom Navigation Controls (Sebelumnya + Selesaikan di akhir, Tanpa tombol Berikutnya)
    if current_idx == total - 1:
        col_prev, col_finish = st.columns([1, 1.6], gap="medium", vertical_alignment="center")
        with col_prev:
            if st.button("Sebelumnya", key=f"btn_p_{current_idx}", type="secondary", icon=":material/arrow_back:", disabled=(current_idx == 0), width="stretch"):
                st.session_state.current_q -= 1
                st.rerun()
        with col_finish:
            all_done = (len(st.session_state.answers) == total)
            finish_label = "Lihat hasil analisis" if all_done else f"Jawab seluruh butir ({len(st.session_state.answers)}/{total})"
            if st.button(finish_label, key="btn_finish_test", type="primary", icon=":material/insights:", disabled=not all_done, width="stretch"):
                with st.spinner("Mengkalkulasi kecenderungan tipe kepribadian dan pola pikirmu..."):
                    result = engine.compute_result(st.session_state.answers)
                    st.session_state.result = result
                    st.session_state.page = "result"
                    st.rerun()
    else:
        col_prev, col_hint = st.columns([1, 1.6], gap="medium", vertical_alignment="center")
        with col_prev:
            if st.button("Sebelumnya", key=f"btn_p_{current_idx}", type="secondary", icon=":material/arrow_back:", disabled=(current_idx == 0), width="stretch"):
                st.session_state.current_q -= 1
                st.rerun()
        with col_hint:
            if q_id in st.session_state.answers:
                st.caption(":material/check: Opsi tersimpan. Klik salah satu opsi untuk lanjut ke butir berikutnya.")
            else:
                st.caption("Klik salah satu opsi di atas untuk langsung beralih ke butir selanjutnya.")


def render_result(result: MBTIResult, engine: PersonalityEngine) -> None:
    profile = get_profile(result.mbti_type)
    theme_color = profile.get("color", "#4F46E5")
    temperament = profile.get("temperament", "Tipologi kognitif")
    bg_tint = profile.get("bg_tint", "#EEF2FF")
    border_color = profile.get("border_color", "#C7D2FE")
    archetype = profile.get("archetype", result.mbti_type)
    summary_narrative = profile.get("summary", "")
    avatar_hero_tag = render_avatar_img(result.mbti_type, size=130, alt=archetype)

    # Hero Result: Karakter Menyatu Alami Tanpa Card Pod
    render_html(f"""
    <div class="friendly-result-hero" style="border-top: 5px solid {theme_color};">
        <div class="hero-result-header">
            <div class="hero-result-identity">
                <span class="hero-badge-pill" style="background:{bg_tint}; color:{theme_color}; border:1.5px solid {border_color};">
                    {temperament}
                </span>
                <div class="hero-type-code" style="color:{theme_color};">{result.mbti_type}</div>
                <h2 class="hero-archetype-title">{archetype}</h2>
            </div>
            <div class="hero-avatar-seamless">
                {avatar_hero_tag}
            </div>
        </div>
        <div class="hero-tagline-quote" style="border-left: 4px solid {theme_color}; background: {bg_tint}55;">
            "{profile.get('tagline', '')}"
        </div>
        <p class="hero-narrative-text">
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
            st.markdown("**:material/info: Sifat fleksibel (seimbang)**")
            st.caption(
                f"Skormu pada dimensi **{bl_text}** berada di rentang tengah yang seimbang (47%–53%). "
                "Ini tanda bagus kalau kamu punya fleksibilitas tinggi: bisa menyesuaikan diri dengan luwes sesuai situasi dan kebutuhan momen yang kamu hadapi!"
            )

    # Spectrum Rows Generator
    dim_pairs = {
        "EI": ("Ekstraversi (Sosial)", "Introversi (Me-Time)", "#4F46E5", "rgba(238, 242, 255, 0.85)", "#C7D2FE"),
        "SN": ("Penginderaan (Fakta Nyata)", "Intuisi (Ide & Kemungkinan)", "#059669", "rgba(236, 253, 245, 0.85)", "#A7F3D0"),
        "TF": ("Pemikiran (Logika Objektif)", "Perasaan (Rasa & Empati)", "#0284C7", "rgba(240, 249, 255, 0.85)", "#BAE6FD"),
        "JP": ("Penilaian (Rencana Teratur)", "Eksplorasi (Fleksibel Santai)", "#D97706", "rgba(255, 251, 235, 0.85)", "#FDE68A"),
    }
    spectrum_html = ""
    for dim_code, (pos_name, neg_name, bar_col, bar_bg, bar_bdr) in dim_pairs.items():
        score_obj = result.dimensions[dim_code]
        pct_pos = score_obj.pos_pct
        pct_neg = round(100.0 - pct_pos, 1)

        # Standout winner vs muted
        if pct_pos >= 50:
            left_class = "pole-winner"
            left_style = f"border:1.5px solid {bar_bdr}; background:{bar_bg}; color:{bar_col};"
            right_class = "pole-muted"
            right_style = ""
        else:
            left_class = "pole-muted"
            left_style = ""
            right_class = "pole-winner"
            right_style = f"border:1.5px solid {bar_bdr}; background:{bar_bg}; color:{bar_col};"

        spectrum_html += f"""
        <div class="spectrum-row-box">
            <div class="spectrum-info-bar">
                <span class="{left_class}" style="{left_style}">{pos_name} {pct_pos:.0f}%</span>
                <span class="{right_class}" style="{right_style}">{neg_name} {pct_neg:.0f}%</span>
            </div>
            <div class="spectrum-track-bg">
                <div class="spectrum-center-divider" title="Titik Tengah 50%"></div>
                <div class="spectrum-fill-progress" style="width: {pct_pos}%; background: {bar_col};"></div>
            </div>
        </div>
        """

    with st.container(border=True):
        st.markdown("**Spektrum kecenderungan 4 dimensi**")
        st.caption("Pola alami caramu berpikir dan mengolah energi (garis tengah menandai titik keseimbangan 50%):")
        render_html(spectrum_html)

    # 4 Deep-Dive Tabs (Judul Ringkas Tanpa Scroll Horizontal)
    tab_cog, tab_strength, tab_work, tab_stress = st.tabs([
        "Pola pikir",
        "Kelebihan",
        "Gaya kerja",
        "Sisi stres",
    ])

    with tab_cog:
        role_meta = {
            "dominant": ("Kekuatan utama (Dominant)", "Naluri terkuat yang memandu keputusan sadarmu sehari-hari"),
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
            st.markdown("**4 Lapisan cara otakmu bekerja**")
            st.caption("Memetakan cara kerja pikiranmu dari naluri yang paling aktif sampai sisi yang rentan lelah:")
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
        st.markdown("**Unduh ringkasan hasil tes**")
        st.caption("Salin ringkasan teks atau unduh dokumen evaluasi untuk arsip pribadi maupun keperluan lainnya:")
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
            start_quiz_session(engine)
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
        render_home(engine)
    elif page == "quiz":
        render_quiz(engine)
    elif page == "result":
        if st.session_state.result:
            render_result(st.session_state.result, engine)
        else:
            st.session_state.page = "home"
            st.rerun()


if __name__ == "__main__":
    main()
