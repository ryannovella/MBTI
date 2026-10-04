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


def render_avatar_img(code: str, size: int = 80, alt: str = "") -> str:
    b64 = get_avatar_base64(code)
    if not b64:
        return ""
    return (
        f'<img src="data:image/svg+xml;base64,{b64}" alt="{alt}" '
        f'width="{size}" height="{size}" '
        f'style="object-fit:contain; display:block; margin:0 auto; filter:drop-shadow(0 4px 10px rgba(0,0,0,0.10));" />'
    )


def generate_theme_styles(theme_mode: str) -> str:
    """Generate dynamic CSS supporting Auto (device preference), Light, and Dark modes."""
    # Force class condition based on user choice
    force_dark = (theme_mode == "Gelap")
    force_light = (theme_mode == "Terang")

    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700;800&display=swap');
/* ==================== THEME TOKENS: LIGHT (DEFAULT) ==================== */
:root {{
    --bg-canvas: #F8FAFC;
    --surface-glass: rgba(255, 255, 255, 0.85);
    --surface-glass-strong: #FFFFFF;
    --surface-glass-subtle: rgba(241, 245, 249, 0.75);
    
    --border-glass: 1.5px solid rgba(226, 232, 240, 0.9);
    --border-glass-subtle: 1px solid rgba(226, 232, 240, 0.8);
    --border-primary: #4F46E5;
    
    --text-title: #0F172A;
    --text-main: #1E293B;
    --text-body: #334155;
    --text-muted: #475569;
    
    --tab-active-bg: #FFFFFF;
    --copy-bg: #F8FAFC;
    --copy-border: #E2E8F0;
    
    --canvas-gradient: 
        radial-gradient(ellipse 75% 45% at 15% -5%, rgba(99, 102, 241, 0.12), transparent 55%),
        radial-gradient(ellipse 65% 45% at 85% 15%, rgba(16, 185, 129, 0.09), transparent 50%),
        radial-gradient(ellipse 65% 55% at 50% 100%, rgba(2, 132, 199, 0.08), transparent 55%),
        #F8FAFC;
        
    --glass-shadow: 
        0 10px 28px -4px rgba(31, 38, 135, 0.06),
        0 2px 6px -1px rgba(15, 23, 42, 0.03),
        inset 0 1px 1.5px rgba(255, 255, 255, 0.95);
        
    --glass-shadow-hover: 
        0 16px 36px -4px rgba(79, 70, 229, 0.12),
        0 3px 8px -2px rgba(15, 23, 42, 0.04),
        inset 0 1px 1.5px rgba(255, 255, 255, 0.95);
        
    --glass-shadow-soft: 
        0 4px 14px -2px rgba(31, 38, 135, 0.04),
        inset 0 1px 1px rgba(255, 255, 255, 0.9);

    /* 4 Temperaments (Deep, rich hues: all > 8:1 contrast on light backgrounds) */
    --nt-color: #3730A3;
    --nt-bg: #EEF2FF;
    --nt-border: #C7D2FE;
    
    --nf-color: #065F46;
    --nf-bg: #ECFDF5;
    --nf-border: #A7F3D0;
    
    --sj-color: #075985;
    --sj-bg: #F0F9FF;
    --sj-border: #BAE6FD;
    
    --sp-color: #92400E;
    --sp-bg: #FFFBEB;
    --sp-border: #FDE68A;

    /* 4 Dimensions (Deep, readable text colors on light cards) */
    --dim-ei-pos: #3730A3;
    --dim-ei-neg: #075985;
    --dim-sn-pos: #065F46;
    --dim-sn-neg: #5B21B6;
    --dim-tf-pos: #0369A1;
    --dim-tf-neg: #9D174D;
    --dim-jp-pos: #92400E;
    --dim-jp-neg: #065F46;
    --dim-badge-bg: rgba(0, 0, 0, 0.05);

    /* Button & Interactive Widget Contrast Tokens (WCAG AAA) */
    --btn-primary-bg: linear-gradient(135deg, #4F46E5 0%, #4338CA 100%);
    --btn-primary-bg-hover: linear-gradient(135deg, #4338CA 0%, #3730A3 100%);
    --btn-primary-text: #FFFFFF;
    --btn-primary-border: rgba(255, 255, 255, 0.3);

    --btn-secondary-bg: #FFFFFF;
    --btn-secondary-bg-hover: #F8FAFC;
    --btn-secondary-text: #0F172A;
    --btn-secondary-text-hover: #4338CA;
    --btn-secondary-border: #CBD5E1;
    --btn-secondary-border-hover: #6366F1;

    --theme-ctrl-bg: rgba(241, 245, 249, 0.95);
    --theme-ctrl-border: #CBD5E1;
    --theme-ctrl-item-text: #475569;
    --theme-ctrl-item-hover: rgba(255, 255, 255, 0.85);
    --theme-ctrl-active-bg: #FFFFFF;
    --theme-ctrl-active-text: #4F46E5;
    --theme-ctrl-active-border: #CBD5E1;
    --theme-ctrl-active-shadow: 0 2px 6px rgba(15, 23, 42, 0.12);

    --quiz-opt-unsel-bg: rgba(255, 255, 255, 0.95);
    --quiz-opt-unsel-border: #CBD5E1;
    --quiz-opt-unsel-text: #0F172A;
    --quiz-opt-sel-bg: #EEF2FF;
    --quiz-opt-sel-border: #4F46E5;
    --quiz-opt-sel-text: #1E1B4B;

    /* Geometry */
    --radius-hero: 20px;
    --radius-card: 15px;
    --radius-md: 10px;
    --radius-pill: 9999px;
}}

/* ==================== AUTO DARK MODE (Device Preference) ==================== */
{'@media (prefers-color-scheme: dark) {' if not force_light else '/* Light Forced */'}
{':root {' if not force_light else ':root.never {'}
    --bg-canvas: #090D16;
    --surface-glass: rgba(17, 24, 39, 0.82);
    --surface-glass-strong: #1E293B;
    --surface-glass-subtle: rgba(30, 41, 59, 0.65);
    
    --border-glass: 1.5px solid rgba(255, 255, 255, 0.14);
    --border-glass-subtle: 1px solid rgba(255, 255, 255, 0.09);
    --border-primary: #818CF8;
    
    --text-title: #F8FAFC;
    --text-main: #F1F5F9;
    --text-body: #CBD5E1;
    --text-muted: #94A3B8;
    
    --tab-active-bg: #1E293B;
    --copy-bg: #0F172A;
    --copy-border: rgba(255, 255, 255, 0.12);
    
    --canvas-gradient: 
        radial-gradient(ellipse 75% 45% at 15% -5%, rgba(99, 102, 241, 0.22), transparent 55%),
        radial-gradient(ellipse 65% 45% at 85% 15%, rgba(16, 185, 129, 0.16), transparent 50%),
        radial-gradient(ellipse 65% 55% at 50% 100%, rgba(2, 132, 199, 0.15), transparent 55%),
        #090D16;
        
    --glass-shadow: 
        0 10px 28px -4px rgba(0, 0, 0, 0.35),
        inset 0 1px 1px rgba(255, 255, 255, 0.08);
        
    --glass-shadow-hover: 
        0 16px 36px -4px rgba(99, 102, 241, 0.25),
        inset 0 1px 1px rgba(255, 255, 255, 0.12);
        
    --glass-shadow-soft: 
        0 4px 14px -2px rgba(0, 0, 0, 0.25),
        inset 0 1px 1px rgba(255, 255, 255, 0.06);

    /* 4 Temperaments (Luminous, bright hues: all > 8:1 contrast on dark canvas) */
    --nt-color: #A5B4FC;
    --nt-bg: rgba(79, 70, 229, 0.25);
    --nt-border: rgba(199, 210, 254, 0.35);
    
    --nf-color: #6EE7B7;
    --nf-bg: rgba(5, 150, 105, 0.25);
    --nf-border: rgba(167, 243, 208, 0.35);
    
    --sj-color: #7DD3FC;
    --sj-bg: rgba(2, 132, 199, 0.25);
    --sj-border: rgba(186, 230, 253, 0.35);
    
    --sp-color: #FCD34D;
    --sp-bg: rgba(217, 119, 6, 0.25);
    --sp-border: rgba(253, 230, 138, 0.35);

    /* 4 Dimensions (Luminous text colors on dark cards) */
    --dim-ei-pos: #A5B4FC;
    --dim-ei-neg: #7DD3FC;
    --dim-sn-pos: #6EE7B7;
    --dim-sn-neg: #C4B5FD;
    --dim-tf-pos: #7DD3FC;
    --dim-tf-neg: #F472B6;
    --dim-jp-pos: #FCD34D;
    --dim-jp-neg: #6EE7B7;
    --dim-badge-bg: rgba(255, 255, 255, 0.1);

    /* Button & Interactive Widget Contrast Tokens (WCAG AAA) */
    --btn-primary-bg: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%);
    --btn-primary-bg-hover: linear-gradient(135deg, #4F46E5 0%, #4338CA 100%);
    --btn-primary-text: #FFFFFF;
    --btn-primary-border: rgba(255, 255, 255, 0.25);

    --btn-secondary-bg: #1E293B;
    --btn-secondary-bg-hover: #334155;
    --btn-secondary-text: #F8FAFC;
    --btn-secondary-text-hover: #FFFFFF;
    --btn-secondary-border: rgba(255, 255, 255, 0.22);
    --btn-secondary-border-hover: #818CF8;

    --theme-ctrl-bg: rgba(30, 41, 59, 0.95);
    --theme-ctrl-border: rgba(255, 255, 255, 0.16);
    --theme-ctrl-item-text: #94A3B8;
    --theme-ctrl-item-hover: rgba(255, 255, 255, 0.12);
    --theme-ctrl-active-bg: #4F46E5;
    --theme-ctrl-active-text: #FFFFFF;
    --theme-ctrl-active-border: #818CF8;
    --theme-ctrl-active-shadow: 0 2px 8px rgba(0, 0, 0, 0.45);

    --quiz-opt-unsel-bg: rgba(17, 24, 39, 0.85);
    --quiz-opt-unsel-border: rgba(255, 255, 255, 0.16);
    --quiz-opt-unsel-text: #F1F5F9;
    --quiz-opt-sel-bg: rgba(79, 70, 229, 0.28);
    --quiz-opt-sel-border: #818CF8;
    --quiz-opt-sel-text: #FFFFFF;
}}
{'}' if not force_light else ''}

/* ==================== FORCED DARK MODE (USER SELECTION) ==================== */
{':root {' if force_dark else ':root.never-dark {'}
    --bg-canvas: #090D16 !important;
    --surface-glass: rgba(17, 24, 39, 0.82) !important;
    --surface-glass-strong: #1E293B !important;
    --surface-glass-subtle: rgba(30, 41, 59, 0.65) !important;
    
    --border-glass: 1.5px solid rgba(255, 255, 255, 0.14) !important;
    --border-glass-subtle: 1px solid rgba(255, 255, 255, 0.09) !important;
    --border-primary: #818CF8 !important;
    
    --text-title: #F8FAFC !important;
    --text-main: #F1F5F9 !important;
    --text-body: #CBD5E1 !important;
    --text-muted: #94A3B8 !important;
    
    --tab-active-bg: #1E293B !important;
    --copy-bg: #0F172A !important;
    --copy-border: rgba(255, 255, 255, 0.12) !important;
    
    --canvas-gradient: 
        radial-gradient(ellipse 75% 45% at 15% -5%, rgba(99, 102, 241, 0.22), transparent 55%),
        radial-gradient(ellipse 65% 45% at 85% 15%, rgba(16, 185, 129, 0.16), transparent 50%),
        radial-gradient(ellipse 65% 55% at 50% 100%, rgba(2, 132, 199, 0.15), transparent 55%),
        #090D16 !important;
        
    --glass-shadow: 
        0 10px 28px -4px rgba(0, 0, 0, 0.35),
        inset 0 1px 1px rgba(255, 255, 255, 0.08) !important;
        
    --glass-shadow-hover: 
        0 16px 36px -4px rgba(99, 102, 241, 0.25),
        inset 0 1px 1px rgba(255, 255, 255, 0.12) !important;
        
    --glass-shadow-soft: 
        0 4px 14px -2px rgba(0, 0, 0, 0.25),
        inset 0 1px 1px rgba(255, 255, 255, 0.06) !important;

    --nt-color: #A5B4FC !important;
    --nt-bg: rgba(79, 70, 229, 0.25) !important;
    --nt-border: rgba(199, 210, 254, 0.35) !important;
    
    --nf-color: #6EE7B7 !important;
    --nf-bg: rgba(5, 150, 105, 0.25) !important;
    --nf-border: rgba(167, 243, 208, 0.35) !important;
    
    --sj-color: #7DD3FC !important;
    --sj-bg: rgba(2, 132, 199, 0.25) !important;
    --sj-border: rgba(186, 230, 253, 0.35) !important;
    
    --sp-color: #FCD34D !important;
    --sp-bg: rgba(217, 119, 6, 0.25) !important;
    --sp-border: rgba(253, 230, 138, 0.35) !important;

    --dim-ei-pos: #A5B4FC !important;
    --dim-ei-neg: #7DD3FC !important;
    --dim-sn-pos: #6EE7B7 !important;
    --dim-sn-neg: #C4B5FD !important;
    --dim-tf-pos: #7DD3FC !important;
    --dim-tf-neg: #F472B6 !important;
    --dim-jp-pos: #FCD34D !important;
    --dim-jp-neg: #6EE7B7 !important;
    --dim-badge-bg: rgba(255, 255, 255, 0.1) !important;

    /* Button & Interactive Widget Contrast Tokens (WCAG AAA) */
    --btn-primary-bg: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%) !important;
    --btn-primary-bg-hover: linear-gradient(135deg, #4F46E5 0%, #4338CA 100%) !important;
    --btn-primary-text: #FFFFFF !important;
    --btn-primary-border: rgba(255, 255, 255, 0.25) !important;

    --btn-secondary-bg: #1E293B !important;
    --btn-secondary-bg-hover: #334155 !important;
    --btn-secondary-text: #F8FAFC !important;
    --btn-secondary-text-hover: #FFFFFF !important;
    --btn-secondary-border: rgba(255, 255, 255, 0.22) !important;
    --btn-secondary-border-hover: #818CF8 !important;

    --theme-ctrl-bg: rgba(30, 41, 59, 0.95) !important;
    --theme-ctrl-border: rgba(255, 255, 255, 0.16) !important;
    --theme-ctrl-item-text: #94A3B8 !important;
    --theme-ctrl-item-hover: rgba(255, 255, 255, 0.12) !important;
    --theme-ctrl-active-bg: #4F46E5 !important;
    --theme-ctrl-active-text: #FFFFFF !important;
    --theme-ctrl-active-border: #818CF8 !important;
    --theme-ctrl-active-shadow: 0 2px 8px rgba(0, 0, 0, 0.45) !important;

    --quiz-opt-unsel-bg: rgba(17, 24, 39, 0.85) !important;
    --quiz-opt-unsel-border: rgba(255, 255, 255, 0.16) !important;
    --quiz-opt-unsel-text: #F1F5F9 !important;
    --quiz-opt-sel-bg: rgba(79, 70, 229, 0.28) !important;
    --quiz-opt-sel-border: #818CF8 !important;
    --quiz-opt-sel-text: #FFFFFF !important;
}}

/* Atmospheric Canvas Background */
html, body, [class*="css"], .stApp {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: var(--text-main) !important;
    background: var(--canvas-gradient) !important;
    background-attachment: fixed !important;
}}

/* Universal Typography & Strict Contrast Overrides */
p, label,
div[data-testid="stMarkdownContainer"] p,
div[data-testid="stMarkdownContainer"] div,
div[data-testid="stMarkdownContainer"] li {{
    color: var(--text-main);
}}

strong, b,
div[data-testid="stMarkdownContainer"] strong,
div[data-testid="stMarkdownContainer"] b {{
    color: var(--text-title);
}}

div[data-testid="stCaptionContainer"],
div[data-testid="stCaptionContainer"] p,
div[data-testid="stCaptionContainer"] span {{
    color: var(--text-muted) !important;
}}

h1, h2, h3, h4, h5, h6 {{
    color: var(--text-title) !important;
}}

header, footer, [data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu {{
    display: none !important;
}}

/* Compact Layout Spacing */
.main .block-container {{
    padding: 1.1rem 1.1rem 2.8rem !important;
    max-width: 820px !important;
}}

@media (max-width: 640px) {{
    .main .block-container {{
        padding: 0.45rem 0.75rem 1.8rem !important;
    }}
}}

/* Top Brand and Theme Switcher Row */
.top-nav-brand {{
    display: flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.86rem;
    font-weight: 700;
    color: var(--text-title);
    letter-spacing: -0.01em;
}}

.brand-pulse-dot {{
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #4F46E5;
    box-shadow: 0 0 8px #6366F1;
}}

/* ==================== THEME SELECTOR: BULLETPROOF WCAG CONTRAST ==================== */
.st-key-theme_mode_selector,
.st-key-theme_mode_selector div[data-testid="stButtonGroup"],
.st-key-theme_mode_selector div.stButtonGroup,
.st-key-theme_mode_selector div[data-baseweb="button-group"],
.st-key-theme_mode_selector div[role="radiogroup"],
.st-key-theme_mode_selector div[data-testid="stButtonGroup"] > div {{
    background: var(--theme-ctrl-bg) !important;
    border: 1px solid var(--theme-ctrl-border) !important;
    border-radius: var(--radius-pill) !important;
    padding: 0.18rem !important;
    display: inline-flex !important;
    align-items: center !important;
    box-shadow: var(--glass-shadow-soft) !important;
    box-sizing: border-box !important;
}}

/* Inactive / Default Option Pills */
.st-key-theme_mode_selector button,
.st-key-theme_mode_selector [data-testid*="segmented_control"],
.st-key-theme_mode_selector [data-variant="segmented_control"] {{
    background: transparent !important;
    border: 1px solid transparent !important;
    border-radius: var(--radius-pill) !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    padding: 0.28rem 0.72rem !important;
    transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1) !important;
    color: var(--theme-ctrl-item-text) !important;
    box-shadow: none !important;
    cursor: pointer !important;
}}

.st-key-theme_mode_selector button *,
.st-key-theme_mode_selector button p,
.st-key-theme_mode_selector button span,
.st-key-theme_mode_selector button div,
.st-key-theme_mode_selector [data-variant="segmented_control"] * {{
    color: var(--theme-ctrl-item-text) !important;
    font-weight: 600 !important;
}}

.st-key-theme_mode_selector button:hover,
.st-key-theme_mode_selector [data-variant="segmented_control"]:hover {{
    background: var(--theme-ctrl-item-hover) !important;
}}

.st-key-theme_mode_selector button:hover *,
.st-key-theme_mode_selector [data-variant="segmented_control"]:hover * {{
    color: var(--text-title) !important;
}}

/* Active / Selected Option Pill (Strict WCAG AAA Highlight) */
.st-key-theme_mode_selector button[data-selected],
.st-key-theme_mode_selector button[data-selected="true"],
.st-key-theme_mode_selector button[aria-selected="true"],
.st-key-theme_mode_selector button[aria-checked="true"],
.st-key-theme_mode_selector button[kind="segmented_controlActive"],
.st-key-theme_mode_selector button[data-testid*="Active"],
.st-key-theme_mode_selector [data-variant="segmented_control"][data-selected] {{
    background: var(--theme-ctrl-active-bg) !important;
    border: 1px solid var(--theme-ctrl-active-border) !important;
    box-shadow: var(--theme-ctrl-active-shadow) !important;
    color: var(--theme-ctrl-active-text) !important;
    font-weight: 800 !important;
}}

.st-key-theme_mode_selector button[data-selected] *,
.st-key-theme_mode_selector button[data-selected="true"] *,
.st-key-theme_mode_selector button[aria-selected="true"] *,
.st-key-theme_mode_selector button[aria-checked="true"] *,
.st-key-theme_mode_selector button[kind="segmented_controlActive"] *,
.st-key-theme_mode_selector button[data-testid*="Active"] *,
.st-key-theme_mode_selector [data-variant="segmented_control"][data-selected] * {{
    color: var(--theme-ctrl-active-text) !important;
    font-weight: 800 !important;
}}

/* Temperament Badge & Text Helper Classes */
.temp-badge-nt {{
    background: var(--nt-bg) !important;
    color: var(--nt-color) !important;
    border: 1.5px solid var(--nt-border) !important;
}}
.temp-badge-nf {{
    background: var(--nf-bg) !important;
    color: var(--nf-color) !important;
    border: 1.5px solid var(--nf-border) !important;
}}
.temp-badge-sj {{
    background: var(--sj-bg) !important;
    color: var(--sj-color) !important;
    border: 1.5px solid var(--sj-border) !important;
}}
.temp-badge-sp {{
    background: var(--sp-bg) !important;
    color: var(--sp-color) !important;
    border: 1.5px solid var(--sp-border) !important;
}}

.temp-text-nt {{ color: var(--nt-color) !important; }}
.temp-text-nf {{ color: var(--nf-color) !important; }}
.temp-text-sj {{ color: var(--sj-color) !important; }}
.temp-text-sp {{ color: var(--sp-color) !important; }}

.temp-quote-nt {{ border-left: 3.5px solid var(--nt-color) !important; }}
.temp-quote-nf {{ border-left: 3.5px solid var(--nf-color) !important; }}
.temp-quote-sj {{ border-left: 3.5px solid var(--sj-color) !important; }}
.temp-quote-sp {{ border-left: 3.5px solid var(--sp-color) !important; }}

.analysis-body-text {{
    color: var(--text-body) !important;
    font-size: 0.88rem !important;
    line-height: 1.6 !important;
    margin-top: 0.35rem !important;
}}

/* Glassmorphism for Streamlit Native Containers */
[data-testid="stVerticalBlockBorderWrapper"] > div {{
    background: var(--surface-glass) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: var(--border-glass) !important;
    border-radius: var(--radius-card) !important;
    box-shadow: var(--glass-shadow-soft) !important;
}}

/* Popover Glassmorphic Style */
div[data-testid="stPopoverBody"] {{
    background: var(--surface-glass-strong) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border: var(--border-glass) !important;
    border-radius: var(--radius-card) !important;
    box-shadow: var(--glass-shadow-hover) !important;
    padding: 0.75rem !important;
}}

/* ==================== GLASSMORPHIC HERO CONTAINER ==================== */
.friendly-hero {{
    background: var(--surface-glass);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: var(--border-glass);
    border-radius: var(--radius-hero);
    box-shadow: var(--glass-shadow);
    padding: 1.7rem 1.5rem 1.35rem;
    text-align: center;
    margin-bottom: 0.85rem;
    position: relative;
    overflow: hidden;
}}

.friendly-hero::before {{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #6366F1 0%, #3B82F6 40%, #10B981 70%, #F59E0B 100%);
}}

.badge-friendly-tag {{
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.25rem 0.85rem;
    border-radius: var(--radius-pill);
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    background: var(--surface-glass-strong);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    color: var(--border-primary);
    border: 1px solid var(--border-primary);
    box-shadow: 0 2px 6px rgba(79, 70, 229, 0.08);
}}

.pill-row-cluster {{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.4rem;
    margin-top: 0.8rem;
}}

.pill-feature-chip {{
    font-size: 0.76rem;
    font-weight: 600;
    color: var(--text-body);
    background: var(--surface-glass-strong);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 0.25rem 0.75rem;
    border-radius: var(--radius-pill);
    border: var(--border-glass-subtle);
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.02);
}}

/* ==================== 3 PILLARS GLASS GRID ==================== */
.pillar-grid-row {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.75rem;
    margin-bottom: 0.85rem;
}}

@media (max-width: 768px) {{
    .pillar-grid-row {{
        grid-template-columns: 1fr;
        gap: 0.55rem;
    }}
}}

.pillar-card {{
    background: var(--surface-glass);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-radius: var(--radius-card);
    border: var(--border-glass);
    box-shadow: var(--glass-shadow-soft);
    padding: 0.9rem 1rem;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    height: 100%;
    box-sizing: border-box;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}}

.pillar-card:hover {{
    transform: translateY(-2px);
    box-shadow: var(--glass-shadow-hover);
    background: var(--surface-glass-strong);
}}

.pillar-title {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--text-title);
    margin: 0 0 0.25rem;
}}

.pillar-desc {{
    font-size: 0.82rem;
    color: var(--text-body);
    line-height: 1.5;
    margin: 0;
}}

/* ==================== 16PERSONALITIES CHARACTER SHOWCASE ==================== */
.showcase-header-box {{
    text-align: center;
    margin: 1.3rem 0 0.75rem;
}}

.showcase-heading {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.25rem;
    font-weight: 800;
    color: var(--text-title);
    margin: 0 0 0.25rem;
    letter-spacing: -0.02em;
}}

.showcase-subheading {{
    font-size: 0.85rem;
    color: var(--text-muted);
    margin: 0 auto;
    max-width: 560px;
    line-height: 1.5;
}}

.char-grid-row {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.75rem;
    margin: 0.75rem 0;
}}

@media (max-width: 860px) {{
    .char-grid-row {{
        grid-template-columns: repeat(2, 1fr);
    }}
}}

@media (max-width: 520px) {{
    .char-grid-row {{
        grid-template-columns: repeat(2, 1fr);
        gap: 0.55rem;
    }}
}}

.char-card {{
    background: var(--surface-glass);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: var(--radius-card);
    border: var(--border-glass);
    box-shadow: var(--glass-shadow-soft);
    padding: 0.95rem 0.8rem 0.85rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    text-align: center;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    box-sizing: border-box;
    height: 100%;
}}

.char-card:hover {{
    transform: translateY(-3px);
    background: var(--surface-glass-strong);
    box-shadow: var(--glass-shadow-hover);
}}

.char-avatar-pod {{
    width: 74px;
    height: 74px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 0.65rem;
    background: var(--surface-glass-subtle);
    border: 1.5px solid var(--border-glass);
    box-shadow: var(--glass-shadow-soft);
    transition: transform 0.2s ease;
}}

.char-card:hover .char-avatar-pod {{
    transform: scale(1.06);
}}

.char-code-badge {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.76rem;
    font-weight: 800;
    letter-spacing: 0.04em;
    padding: 0.16rem 0.65rem;
    border-radius: var(--radius-pill);
    margin-bottom: 0.3rem;
    display: inline-block;
}}

.char-name {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.92rem;
    font-weight: 700;
    color: var(--text-title);
    margin: 0 0 0.25rem;
    line-height: 1.3;
}}

.char-desc {{
    font-size: 0.77rem;
    color: var(--text-body);
    line-height: 1.45;
    margin: 0 0 0.65rem;
    flex-grow: 1;
}}

.char-cog-chip {{
    font-size: 0.71rem;
    font-weight: 700;
    background: var(--surface-glass-strong);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border: var(--border-glass-subtle);
    border-radius: var(--radius-pill);
    padding: 0.16rem 0.55rem;
    color: var(--text-muted);
}}

/* ==================== SLIM REAL-TIME PROGRESS TRACK ==================== */
.quiz-compact-progress-track {{
    height: 6px;
    background: var(--surface-glass-subtle);
    border: 1px solid var(--border-glass-subtle);
    border-radius: 9999px;
    position: relative;
    overflow: hidden;
    margin: 0.35rem 0 0.55rem;
    box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.12);
}}

.quiz-compact-progress-fill {{
    height: 100%;
    border-radius: 9999px;
    background: linear-gradient(90deg, #6366F1 0%, #3B82F6 50%, #10B981 100%);
    box-shadow: 0 0 8px rgba(99, 102, 241, 0.4);
    transition: width 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}}

/* ==================== QUIZ SCENARIO CONTAINER ==================== */
.scenario-compact-card {{
    background: var(--surface-glass);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: var(--border-glass);
    border-radius: var(--radius-card);
    padding: 0.85rem 1.15rem;
    box-shadow: var(--glass-shadow-soft);
    margin: 0.35rem 0 0.65rem;
    position: relative;
}}

.scenario-compact-dim-detail {{
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-muted);
    margin-bottom: 0.3rem;
    letter-spacing: 0.01em;
}}

.scenario-compact-text {{
    font-size: 1.02rem;
    font-weight: 700;
    line-height: 1.55;
    color: var(--text-title);
    letter-spacing: -0.01em;
    margin: 0;
}}

/* ==================== TACTILE QUIZ OPTION CARDS ==================== */
.st-key-quiz_options_container,
div[data-testid="stVerticalBlock"]:has(div[class*="st-key-opt_btn_"]) {{
    display: flex !important;
    flex-direction: column !important;
    gap: 0.55rem !important;
    margin: 0.35rem 0 0.65rem !important;
    width: 100% !important;
}}

.st-key-quiz_options_container div[data-testid="stButton"],
div[class*="st-key-opt_btn_"],
div[class*="st-key-opt_btn_"] div[data-testid="stButton"] {{
    width: 100% !important;
}}

div.stElementContainer[class*="st-key-opt_btn_"] div[data-testid="stButton"] button,
.st-key-quiz_options_container button,
div[class*="st-key-opt_btn_"] button,
div[data-testid="stVerticalBlock"]:has(div[class*="st-key-opt_btn_"]) div[data-testid="stButton"] button {{
    display: flex !important;
    flex-direction: row !important;
    justify-content: flex-start !important;
    align-items: flex-start !important;
    text-align: left !important;
    width: 100% !important;
    min-height: 52px !important;
    padding: 0.85rem 1.15rem !important;
    border-radius: var(--radius-md) !important;
    background: var(--quiz-opt-unsel-bg) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 1.5px solid var(--quiz-opt-unsel-border) !important;
    box-shadow: var(--glass-shadow-soft) !important;
    transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1) !important;
    white-space: normal !important;
    overflow-wrap: break-word !important;
    word-break: normal !important;
    cursor: pointer !important;
}}

/* Force markdown container inside option buttons to take full width and left align */
div.stElementContainer[class*="st-key-opt_btn_"] button div[data-testid="stMarkdownContainer"],
.st-key-quiz_options_container button div[data-testid="stMarkdownContainer"],
div[class*="st-key-opt_btn_"] button div[data-testid="stMarkdownContainer"],
div[data-testid="stVerticalBlock"]:has(div[class*="st-key-opt_btn_"]) button div[data-testid="stMarkdownContainer"] {{
    width: 100% !important;
    max-width: 100% !important;
    flex: 1 1 100% !important;
    text-align: left !important;
    display: block !important;
    margin: 0 !important;
    padding: 0 !important;
}}

/* Force p and text elements inside option buttons to take full width and align left */
div.stElementContainer[class*="st-key-opt_btn_"] button div[data-testid="stMarkdownContainer"] p,
.st-key-quiz_options_container button div[data-testid="stMarkdownContainer"] p,
div[class*="st-key-opt_btn_"] button div[data-testid="stMarkdownContainer"] p,
div[data-testid="stVerticalBlock"]:has(div[class*="st-key-opt_btn_"]) button div[data-testid="stMarkdownContainer"] p,
div[class*="st-key-opt_btn_"] button p,
.st-key-quiz_options_container button p {{
    color: var(--quiz-opt-unsel-text) !important;
    font-size: 0.94rem !important;
    line-height: 1.52 !important;
    text-align: left !important;
    margin: 0 !important;
    width: 100% !important;
    display: block !important;
}}

/* Consistent spacing and bold weight for A. / B. prefix */
div[class*="st-key-opt_btn_"] button strong,
.st-key-quiz_options_container button strong {{
    font-weight: 800 !important;
    margin-right: 0.35rem !important;
    color: var(--text-title) !important;
    display: inline-block !important;
}}

div.stElementContainer[class*="st-key-opt_btn_"] button:hover,
.st-key-quiz_options_container button:hover,
div[class*="st-key-opt_btn_"] button:hover {{
    transform: translateY(-1.5px) !important;
    border-color: var(--border-primary) !important;
    background: var(--btn-secondary-bg-hover) !important;
    box-shadow: var(--glass-shadow-hover) !important;
}}

div.stElementContainer[class*="st-key-opt_btn_"] button:hover p,
.st-key-quiz_options_container button:hover p,
div[class*="st-key-opt_btn_"] button:hover p,
div.stElementContainer[class*="st-key-opt_btn_"] button:hover span,
.st-key-quiz_options_container button:hover span,
div[class*="st-key-opt_btn_"] button:hover span {{
    color: var(--text-title) !important;
}}

div.stElementContainer[class*="st-key-opt_btn_"] button:active,
.st-key-quiz_options_container button:active,
div[class*="st-key-opt_btn_"] button:active {{
    transform: translateY(1px) scale(0.995) !important;
}}

/* Selected option card */
div.stElementContainer[class*="st-key-opt_btn_"] button[kind="primary"],
div.stElementContainer[class*="st-key-opt_btn_"] button[data-testid*="primary"],
.st-key-quiz_options_container button[kind="primary"],
.st-key-quiz_options_container button[data-testid*="primary"],
div[class*="st-key-opt_btn_"] button[kind="primary"],
div[class*="st-key-opt_btn_"] button[data-testid*="primary"] {{
    background: var(--quiz-opt-sel-bg) !important;
    border: 2px solid var(--quiz-opt-sel-border) !important;
    box-shadow: 0 0 0 1px var(--quiz-opt-sel-border), 0 8px 20px -3px rgba(79, 70, 229, 0.22) !important;
}}

div.stElementContainer[class*="st-key-opt_btn_"] button[kind="primary"] p,
div.stElementContainer[class*="st-key-opt_btn_"] button[data-testid*="primary"] p,
.st-key-quiz_options_container button[kind="primary"] p,
.st-key-quiz_options_container button[data-testid*="primary"] p,
div[class*="st-key-opt_btn_"] button[kind="primary"] p,
div[class*="st-key-opt_btn_"] button[data-testid*="primary"] p {{
    color: var(--quiz-opt-sel-text) !important;
    font-weight: 700 !important;
}}

/* ==================== BUTTONS CLEAN, TACTILE & HIGH CONTRAST (WCAG AAA) ==================== */
/* Primary Action Buttons (Mulai Asesmen, Ulangi Asesmen, Lihat Hasil) */
button[data-testid="stBaseButton-primary"],
button[data-testid="baseButton-primary"],
div[data-testid="stButton"] button[kind="primary"],
div[data-testid="stButton"] button[data-testid*="primary"] {{
    background: var(--btn-primary-bg) !important;
    border: 1px solid var(--btn-primary-border) !important;
    border-radius: var(--radius-md) !important;
    box-shadow: 0 4px 14px rgba(79, 70, 229, 0.28), inset 0 1px 1px rgba(255, 255, 255, 0.3) !important;
    min-height: 42px !important;
    font-weight: 700 !important;
    font-size: 0.92rem !important;
    letter-spacing: -0.01em !important;
    color: var(--btn-primary-text) !important;
    transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1) !important;
}}

button[data-testid="stBaseButton-primary"] *,
button[data-testid="stBaseButton-primary"] p,
button[data-testid="stBaseButton-primary"] span,
button[data-testid="baseButton-primary"] *,
button[data-testid="baseButton-primary"] p,
button[data-testid="baseButton-primary"] span,
div[data-testid="stButton"] button[kind="primary"] *,
div[data-testid="stButton"] button[kind="primary"] p,
div[data-testid="stButton"] button[kind="primary"] span {{
    color: var(--btn-primary-text) !important;
    font-weight: 700 !important;
}}

button[data-testid="stBaseButton-primary"]:hover,
button[data-testid="baseButton-primary"]:hover,
div[data-testid="stButton"] button[kind="primary"]:hover {{
    transform: translateY(-1.5px) !important;
    box-shadow: 0 8px 22px rgba(79, 70, 229, 0.38), inset 0 1px 1px rgba(255, 255, 255, 0.3) !important;
    background: var(--btn-primary-bg-hover) !important;
    color: var(--btn-primary-text) !important;
}}

button[data-testid="stBaseButton-primary"]:active,
button[data-testid="baseButton-primary"]:active {{
    transform: translateY(1px) scale(0.995) !important;
}}

/* Secondary Buttons, Download Button & Return Home Button (Strict Contrast WCAG AAA) */
button[data-testid="stBaseButton-secondary"],
button[data-testid="baseButton-secondary"],
div[data-testid="stButton"] button[kind="secondary"],
div[data-testid="stButton"] button[data-testid*="secondary"],
div[data-testid="stDownloadButton"] button,
div.stDownloadButton button,
div[data-testid="stPopover"] button {{
    background: var(--btn-secondary-bg) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1.5px solid var(--btn-secondary-border) !important;
    border-radius: var(--radius-md) !important;
    box-shadow: var(--glass-shadow-soft) !important;
    min-height: 42px !important;
    font-weight: 700 !important;
    font-size: 0.92rem !important;
    color: var(--btn-secondary-text) !important;
    transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1) !important;
}}

button[data-testid="stBaseButton-secondary"] *,
button[data-testid="stBaseButton-secondary"] p,
button[data-testid="stBaseButton-secondary"] span,
button[data-testid="baseButton-secondary"] *,
button[data-testid="baseButton-secondary"] p,
button[data-testid="baseButton-secondary"] span,
div[data-testid="stButton"] button[kind="secondary"] *,
div[data-testid="stButton"] button[kind="secondary"] p,
div[data-testid="stButton"] button[kind="secondary"] span,
div[data-testid="stDownloadButton"] button *,
div[data-testid="stDownloadButton"] button p,
div[data-testid="stDownloadButton"] button span,
div.stDownloadButton button *,
div.stDownloadButton button p,
div.stDownloadButton button span,
div[data-testid="stPopover"] button *,
div[data-testid="stPopover"] button p,
div[data-testid="stPopover"] button span {{
    color: var(--btn-secondary-text) !important;
    font-weight: 700 !important;
}}

button[data-testid="stBaseButton-secondary"]:hover,
button[data-testid="baseButton-secondary"]:hover,
div[data-testid="stButton"] button[kind="secondary"]:hover,
div[data-testid="stDownloadButton"] button:hover,
div.stDownloadButton button:hover,
div[data-testid="stPopover"] button:hover {{
    border-color: var(--btn-secondary-border-hover) !important;
    background: var(--btn-secondary-bg-hover) !important;
    transform: translateY(-1.5px) !important;
    box-shadow: 0 6px 16px rgba(79, 70, 229, 0.14) !important;
    color: var(--btn-secondary-text-hover) !important;
}}

button[data-testid="stBaseButton-secondary"]:hover *,
button[data-testid="baseButton-secondary"]:hover *,
div[data-testid="stButton"] button[kind="secondary"]:hover *,
div[data-testid="stDownloadButton"] button:hover *,
div.stDownloadButton button:hover *,
div[data-testid="stPopover"] button:hover * {{
    color: var(--btn-secondary-text-hover) !important;
}}

button[data-testid="stBaseButton-secondary"]:active,
button[data-testid="baseButton-secondary"]:active,
div[data-testid="stDownloadButton"] button:active {{
    transform: translateY(1px) scale(0.995) !important;
}}

/* ==================== SYMMETRICAL & PROPORTIONAL TABS ==================== */
div[data-testid="stTabs"] {{
    width: 100% !important;
}}

div[data-baseweb="tab-list"] {{
    display: flex !important;
    width: 100% !important;
    gap: 0.28rem !important;
    background: var(--surface-glass-strong) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    padding: 0.28rem !important;
    border-radius: var(--radius-card) !important;
    border: var(--border-glass) !important;
    box-shadow: var(--glass-shadow-soft) !important;
    overflow-x: hidden !important;
    margin-bottom: 0.85rem !important;
    box-sizing: border-box !important;
}}

div[data-baseweb="tab-list"] button[data-baseweb="tab"] {{
    flex: 1 1 0% !important;
    width: 25% !important;
    max-width: 25% !important;
    min-width: 0 !important;
    padding: 0.52rem 0.2rem !important;
    font-size: 0.84rem !important;
    font-weight: 700 !important;
    text-align: center !important;
    justify-content: center !important;
    align-items: center !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-body) !important;
    white-space: nowrap !important;
    border: none !important;
    background: transparent !important;
    box-sizing: border-box !important;
    transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1) !important;
}}

div[data-baseweb="tab-list"] button[data-baseweb="tab"]:hover {{
    color: var(--text-title) !important;
    background: var(--surface-glass) !important;
}}

div[data-baseweb="tab-list"] button[data-baseweb="tab"][aria-selected="true"] {{
    background: var(--tab-active-bg) !important;
    color: var(--text-title) !important;
    font-weight: 800 !important;
    box-shadow: 0 3px 10px rgba(15, 23, 42, 0.08), 0 1px 2px rgba(15, 23, 42, 0.04) !important;
}}

@media (max-width: 640px) {{
    div[data-baseweb="tab-list"] button[data-baseweb="tab"] {{
        font-size: 0.76rem !important;
        padding: 0.44rem 0.1rem !important;
        letter-spacing: -0.01em !important;
    }}
}}

@media (max-width: 440px) {{
    div[data-baseweb="tab-list"] button[data-baseweb="tab"] {{
        font-size: 0.69rem !important;
        padding: 0.4rem 0.05rem !important;
        letter-spacing: -0.02em !important;
    }}
}}

div[data-baseweb="tab-highlight"], div[data-baseweb="tab-border"] {{
    display: none !important;
}}

div[data-baseweb="tab-panel"] {{
    width: 100% !important;
    padding: 0 !important;
}}

/* ==================== RESULT HERO & SEAMLESS CHARACTER ==================== */
.friendly-result-hero {{
    background: var(--surface-glass);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: var(--border-glass);
    border-radius: var(--radius-hero);
    box-shadow: var(--glass-shadow);
    padding: 1.5rem 1.4rem 1.3rem;
    margin-bottom: 0.95rem;
    position: relative;
    overflow: hidden;
}}

.hero-result-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.2rem;
    margin-bottom: 0.9rem;
}}

.hero-result-identity {{
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
}}

.hero-badge-pill {{
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.25rem 0.8rem;
    border-radius: var(--radius-pill);
    font-size: 0.74rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    width: fit-content;
    margin-bottom: 0.35rem;
}}

.hero-type-code {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.4rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1.05;
    margin: 0 0 0.2rem;
}}

.hero-archetype-title {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.25rem;
    font-weight: 800;
    color: var(--text-title);
    margin: 0;
    letter-spacing: -0.02em;
    line-height: 1.25;
}}

.hero-avatar-seamless {{
    flex-shrink: 0;
    width: 110px;
    height: 110px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0;
}}

.hero-avatar-seamless img {{
    width: 105px !important;
    height: 105px !important;
    object-fit: contain;
    filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.12));
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), filter 0.25s ease;
}}

.hero-avatar-seamless:hover img {{
    transform: scale(1.06) translateY(-2px);
    filter: drop-shadow(0 12px 20px rgba(0, 0, 0, 0.16));
}}

.hero-tagline-quote {{
    font-size: 0.91rem;
    line-height: 1.55;
    color: var(--text-body);
    background: var(--surface-glass-subtle);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: var(--radius-md);
    padding: 0.75rem 1.05rem;
    margin: 0 0 0.85rem;
    border: var(--border-glass-subtle);
    font-weight: 500;
    box-sizing: border-box;
}}

.hero-narrative-text {{
    font-size: 0.88rem;
    color: var(--text-body);
    line-height: 1.65;
    margin: 0;
    padding-top: 0.85rem;
    border-top: var(--border-glass-subtle);
}}

@media (max-width: 680px) {{
    .hero-result-header {{
        flex-direction: column-reverse;
        align-items: center;
        text-align: center;
        gap: 0.9rem;
    }}
    .hero-result-identity {{
        align-items: center;
    }}
    .hero-avatar-seamless {{
        width: 95px;
        height: 95px;
    }}
    .hero-avatar-seamless img {{
        width: 90px !important;
        height: 90px !important;
    }}
    .hero-tagline-quote {{
        text-align: center;
    }}
}}

/* ==================== SPECTRUM TRACK: DUAL-COLOR & SYMMETRICAL ==================== */
.spectrum-block {{
    margin-bottom: 1.1rem;
}}

.spectrum-pills-row {{
    display: flex !important;
    gap: 0.5rem !important;
    width: 100% !important;
    margin-bottom: 0.45rem !important;
}}

.spectrum-pill {{
    flex: 1 1 0% !important;
    width: 50% !important;
    max-width: 50% !important;
    box-sizing: border-box !important;
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    padding: 0.42rem 0.75rem !important;
    border-radius: var(--radius-pill) !important;
    font-size: 0.82rem !important;
    transition: all 0.2s ease !important;
    border: 1.5px solid var(--border-glass-subtle) !important;
    background: var(--surface-glass-subtle) !important;
}}

.spectrum-pill.winner {{
    font-weight: 800 !important;
    background: var(--surface-glass-strong) !important;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06) !important;
}}

.spectrum-pill.muted {{
    font-weight: 500 !important;
    opacity: 0.75 !important;
}}

@media (max-width: 640px) {{
    .spectrum-pill {{
        padding: 0.35rem 0.55rem !important;
        font-size: 0.76rem !important;
    }}
    .spectrum-pill-pct {{
        font-size: 0.76rem !important;
    }}
}}

.spectrum-pill-name {{
    color: var(--text-title);
    font-weight: inherit;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}}

.spectrum-pill-pct {{
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 800;
    margin-left: 0.35rem;
    white-space: nowrap;
}}

/* Dual-Colored Track (No Empty Bar!) */
.spectrum-dual-track {{
    display: flex !important;
    height: 14px !important;
    width: 100% !important;
    border-radius: 9999px !important;
    overflow: hidden !important;
    position: relative !important;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.15) !important;
    margin-bottom: 0.55rem !important;
}}

.spectrum-segment-left {{
    height: 100% !important;
    transition: width 0.6s cubic-bezier(0.16, 1, 0.3, 1) !important;
    box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.25) !important;
}}

.spectrum-segment-right {{
    height: 100% !important;
    transition: width 0.6s cubic-bezier(0.16, 1, 0.3, 1) !important;
    box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.2) !important;
}}

.spectrum-center-marker {{
    position: absolute !important;
    top: -2px !important;
    bottom: -2px !important;
    left: 50% !important;
    width: 2.5px !important;
    background: #FFFFFF !important;
    transform: translateX(-50%) !important;
    z-index: 3 !important;
    border-radius: 9999px !important;
    box-shadow: 0 0 4px rgba(0, 0, 0, 0.45) !important;
}}

.spectrum-center-marker.balanced {{
    width: 4px !important;
    background: #FFFFFF !important;
    box-shadow: 0 0 0 2px var(--border-primary), 0 0 10px rgba(99, 102, 241, 0.6) !important;
}}

.spectrum-pill.balanced {{
    font-weight: 700 !important;
    background: var(--surface-glass-strong) !important;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06) !important;
}}

/* Compact Explanatory Card */
.spectrum-explain-card {{
    display: flex !important;
    flex-direction: column !important;
    background: var(--surface-glass) !important;
    border: var(--border-glass-subtle) !important;
    border-radius: var(--radius-card) !important;
    padding: 0.65rem 0.85rem !important;
    gap: 0.55rem !important;
    box-shadow: var(--glass-shadow-soft) !important;
}}

.spectrum-explain-cols-wrap {{
    display: flex !important;
    gap: 0.75rem !important;
    width: 100% !important;
}}

.spectrum-explain-col {{
    flex: 1 1 0% !important;
    width: 50% !important;
    min-width: 0 !important;
    box-sizing: border-box !important;
    padding: 0.28rem 0.4rem !important;
    border-radius: var(--radius-md) !important;
    transition: background 0.2s ease !important;
}}

.spectrum-explain-col.winner,
.spectrum-explain-col.balanced {{
    background: var(--surface-glass-strong) !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
}}

.spectrum-balance-footer {{
    display: flex !important;
    align-items: center !important;
    gap: 0.45rem !important;
    padding-top: 0.48rem !important;
    border-top: 1px dashed var(--border-glass-subtle) !important;
    font-size: 0.76rem !important;
    color: var(--text-body) !important;
    line-height: 1.45 !important;
    flex-wrap: wrap !important;
}}

.spectrum-balance-badge {{
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.3rem !important;
    padding: 0.12rem 0.5rem !important;
    border-radius: var(--radius-pill) !important;
    background: var(--surface-glass-subtle) !important;
    border: 1px solid var(--border-primary) !important;
    font-size: 0.7rem !important;
    font-weight: 800 !important;
    color: var(--border-primary) !important;
    white-space: nowrap !important;
    flex-shrink: 0 !important;
}}

/* Hero Balance Chips Row */
.hero-balance-row {{
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 0.4rem !important;
    margin-top: 0.45rem !important;
    margin-bottom: 0.2rem !important;
}}

.hero-balance-chip {{
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.35rem !important;
    padding: 0.2rem 0.65rem !important;
    border-radius: var(--radius-pill) !important;
    background: var(--surface-glass-strong) !important;
    border: 1px solid var(--border-primary) !important;
    font-size: 0.74rem !important;
    font-weight: 700 !important;
    color: var(--text-title) !important;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04) !important;
}}

.hero-balance-chip .balance-dot {{
    width: 6px !important;
    height: 6px !important;
    border-radius: 50% !important;
    background: var(--border-primary) !important;
    box-shadow: 0 0 6px var(--border-primary) !important;
    flex-shrink: 0 !important;
}}

/* Balance Advisory Card */
.balance-advisory-card {{
    background: var(--surface-glass) !important;
    backdrop-filter: blur(14px) !important;
    -webkit-backdrop-filter: blur(14px) !important;
    border: var(--border-glass) !important;
    border-left: 3.5px solid var(--border-primary) !important;
    border-radius: var(--radius-card) !important;
    padding: 0.75rem 1rem !important;
    margin-bottom: 0.85rem !important;
    box-shadow: var(--glass-shadow-soft) !important;
}}

.balance-advisory-header {{
    display: flex !important;
    align-items: center !important;
    gap: 0.5rem !important;
    flex-wrap: wrap !important;
    margin-bottom: 0.25rem !important;
}}

.balance-advisory-pill {{
    font-size: 0.72rem !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.04em !important;
    color: var(--border-primary) !important;
    background: var(--surface-glass-strong) !important;
    padding: 0.12rem 0.55rem !important;
    border-radius: var(--radius-pill) !important;
    border: 1px solid var(--border-primary) !important;
}}

.balance-advisory-dims {{
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    color: var(--text-title) !important;
}}

.balance-advisory-desc {{
    font-size: 0.78rem !important;
    color: var(--text-body) !important;
    line-height: 1.48 !important;
    margin: 0 !important;
}}

.spectrum-explain-divider {{
    width: 1px !important;
    background: var(--border-glass-subtle) !important;
    align-self: stretch !important;
    opacity: 0.8 !important;
}}

.spectrum-explain-header {{
    display: flex !important;
    align-items: center !important;
    gap: 0.35rem !important;
    margin-bottom: 0.25rem !important;
    font-size: 0.8rem !important;
    color: var(--text-title) !important;
}}

.spectrum-explain-badge {{
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 18px !important;
    height: 18px !important;
    border-radius: 50% !important;
    font-size: 0.68rem !important;
    font-weight: 800 !important;
    border: 1px solid transparent !important;
}}

.spectrum-explain-text {{
    font-size: 0.76rem !important;
    line-height: 1.4 !important;
    color: var(--text-body) !important;
    margin: 0 !important;
}}

@media (max-width: 640px) {{
    .spectrum-explain-card {{
        flex-direction: column !important;
        gap: 0.45rem !important;
        padding: 0.55rem 0.75rem !important;
    }}
    .spectrum-explain-col {{
        width: 100% !important;
    }}
    .spectrum-explain-divider {{
        width: 100% !important;
        height: 1px !important;
    }}
}}

/* ==================== COGNITIVE LAYERS ==================== */
.cog-layer-friendly-card {{
    background: var(--surface-glass);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: var(--border-glass-subtle);
    border-radius: var(--radius-md);
    box-shadow: var(--glass-shadow-soft);
    padding: 0.85rem 1.05rem;
    margin-bottom: 0.65rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}}

.cog-layer-friendly-card:hover {{
    transform: translateY(-1.5px);
    box-shadow: var(--glass-shadow);
}}

.cog-layer-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.25rem;
}}

.cog-role-badge {{
    font-size: 0.74rem;
    font-weight: 800;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.04em;
}}

.cog-symbol-tag {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.82rem;
    font-weight: 800;
    padding: 0.15rem 0.5rem;
    border-radius: var(--radius-pill);
    border: 1px solid transparent;
}}

.cog-func-heading {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--text-title);
    margin-bottom: 0.2rem;
}}

.cog-func-paragraph {{
    font-size: 0.82rem;
    line-height: 1.52;
    color: var(--text-body);
    margin: 0;
}}

/* ==================== TEXT COPY AREA ==================== */
.copy-box-area {{
    background: var(--copy-bg);
    border-radius: var(--radius-md);
    padding: 0.85rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 0.78rem;
    color: var(--text-main);
    line-height: 1.6;
    border: 1px solid var(--copy-border);
    user-select: all;
    margin: 0.5rem 0;
    white-space: pre-wrap;
}}

/* Mobile-Specific Refinement (Ultra-Compact) */
@media (max-width: 640px) {{
    .friendly-hero, .friendly-result-hero {{
        padding: 1.1rem 0.95rem 1rem !important;
    }}
    .scenario-compact-card {{
        padding: 0.7rem 0.9rem !important;
        margin: 0.25rem 0 0.5rem !important;
    }}
    .scenario-compact-text {{
        font-size: 0.93rem !important;
        line-height: 1.46 !important;
    }}
    .st-key-quiz_options_container,
    div[data-testid="stVerticalBlock"]:has(div[class*="st-key-opt_btn_"]) {{
        gap: 0.45rem !important;
        margin: 0.25rem 0 0.5rem !important;
    }}
    .st-key-quiz_options_container button,
    div[class*="st-key-opt_btn_"] button,
    div.stElementContainer[class*="st-key-opt_btn_"] div[data-testid="stButton"] button {{
        min-height: 46px !important;
        padding: 0.65rem 0.95rem !important;
        font-size: 0.88rem !important;
        line-height: 1.45 !important;
        border-radius: 9px !important;
        text-align: left !important;
        justify-content: flex-start !important;
    }}
    .st-key-quiz_options_container button div[data-testid="stMarkdownContainer"] p,
    div[class*="st-key-opt_btn_"] button div[data-testid="stMarkdownContainer"] p,
    div[class*="st-key-opt_btn_"] button p {{
        font-size: 0.88rem !important;
        line-height: 1.45 !important;
        text-align: left !important;
    }}
    button[data-testid="baseButton-primary"], button[data-testid="baseButton-secondary"] {{
        min-height: 38px !important;
        font-size: 0.86rem !important;
        padding: 0.35rem 0.75rem !important;
    }}
}}
</style>
"""


def init_session() -> None:
    defaults = {
        "page": "home",
        "answers": {},
        "current_q": 0,
        "result": None,
        "shuffled_options": {},
        "theme_mode": "Auto",
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


def render_top_bar() -> None:
    """Render top bar with brand badge and Light/Dark/Auto theme selector."""
    col_brand, col_theme = st.columns([3.2, 1.8], vertical_alignment="center")
    with col_brand:
        st.markdown(
            '<div class="top-nav-brand">'
            '<span class="brand-pulse-dot"></span>'
            '<strong>MBTI Spectrum</strong> <span style="font-size:0.75rem; opacity:0.65;">· Carl Jung</span>'
            '</div>',
            unsafe_allow_html=True
        )
    with col_theme:
        curr = st.session_state.get("theme_mode", "Auto")
        opts = ["Auto", "Terang", "Gelap"]
        sel = st.segmented_control(
            "Tema Tampilan",
            options=opts,
            default=curr if curr in opts else "Auto",
            key="theme_mode_selector",
            label_visibility="collapsed"
        )
        if sel and sel != st.session_state.get("theme_mode"):
            st.session_state["theme_mode"] = sel
            st.rerun()


def render_home(engine: PersonalityEngine) -> None:
    render_top_bar()
    total_q = len(engine.get_questions())

    render_html(f"""
    <div class="friendly-hero">
        <div class="badge-friendly-tag">Tes Tipe Kepribadian</div>
        <h1 style="font-family:'Space Grotesk',sans-serif; font-size:clamp(1.5rem, 5vw, 2.1rem); font-weight:800; color:var(--text-title); margin:0.6rem 0 0.35rem; letter-spacing:-0.03em;">
            Tes spektrum kepribadian MBTI
        </h1>
        <p style="font-size:0.92rem; color:var(--text-body); line-height:1.6; max-width:580px; margin:0 auto;">
            Kenali tipe kepribadian dan cara unik otakmu memproses hal-hal di sekitarmu, mengambil keputusan, dan berinteraksi sehari-hari lewat {total_q} skenario yang dekat banget sama kehidupan nyata.
        </p>
        <div class="pill-row-cluster">
            <span class="pill-feature-chip">{total_q} Skenario nyata</span>
            <span class="pill-feature-chip">8 Pola pikir alami</span>
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
        grp_lower = grp_key.lower()
        with tab_map[grp_key]:
            cards_html = '<div class="char-grid-row">'
            for code in grp_codes:
                p = all_prof.get(code, {})
                arch = p.get("archetype", code)
                desc = p.get("tagline", "")
                cog_dom = p.get("cognitive_roles", {}).get("dominant", "")
                dom_code = cog_dom.split()[0] if cog_dom else ""
                avatar_tag = render_avatar_img(code, size=60, alt=arch)

                cards_html += f"""
                <div class="char-card" style="border-top: 3.5px solid var(--{grp_lower}-color);">
                    <div class="char-avatar-pod">
                        {avatar_tag}
                    </div>
                    <div>
                        <span class="char-code-badge temp-badge-{grp_lower}">{code}</span>
                        <div class="char-name">{arch}</div>
                    </div>
                    <p class="char-desc">{desc}</p>
                    <span class="char-cog-chip">{dom_code} Dominan</span>
                </div>
                """
            cards_html += "</div>"
            render_html(cards_html)

    st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("**:material/info: Panduan pengerjaan**")
        est_min = max(5, round(total_q * 0.16))
        est_max = max(7, round(total_q * 0.25))
        st.caption(
            "• Jawab santai dan spontan aja, pilih opsi yang paling menggambarkan kebiasaan nyatamu sehari-hari.\n"
            "• Nggak ada jawaban yang benar atau salah; semua pilihan itu normal dan manusiawi banget.\n"
            f"• Cuma butuh waktu sekitar {est_min} sampai {est_max} menit. Progres jawabanmu tersimpan otomatis, jadi kamu bisa santai."
        )

    st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
    if st.button("Mulai asesmen", key="btn_start_quiz", type="primary", icon=":material/arrow_forward:", width="stretch"):
        start_quiz_session(engine)
        st.rerun()


def render_quiz(engine: PersonalityEngine) -> None:
    render_top_bar()

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
        "EI": ("Mind", "Sumber energi: Kumpul seru vs Me-time tenang", "nt"),
        "SN": ("Energy", "Cara olah info: Fakta konkret vs Ide & kemungkinan", "nf"),
        "TF": ("Nature", "Cara ambil keputusan: Logika objektif vs Rasa & empati", "sj"),
        "JP": ("Tactics", "Pola keseharian: Rencana teratur vs Fleksibel santai", "sp"),
    }
    dim_name, dim_detail, temp_class = dim_map.get(
        q["dim"], (q["dim"], "", "nt")
    )

    pct = (answered_count / total) * 100.0

    # 1. Compact Header Bar: Dimension badge, Question count, Live Progress text, Popover Jump
    col_nav, col_jump = st.columns([3.8, 1.2], vertical_alignment="center")
    with col_nav:
        badge_html = f'<span class="temp-badge-{temp_class}" style="padding:0.18rem 0.65rem; border-radius:9999px; font-size:0.75rem; font-weight:800;">{dim_name} ({q["dim"]})</span>'
        pct_html = f'<span style="font-size:0.78rem; font-weight:700; color:var(--border-primary); margin-left:0.35rem;">{answered_count}/{total} ({pct:.0f}%)</span>'
        st.markdown(f"<div style='display:flex; align-items:center; gap:0.4rem; flex-wrap:wrap;'><strong>Butir {current_idx + 1:02d}</strong> · {badge_html} {pct_html}</div>", unsafe_allow_html=True)
    with col_jump:
        with st.popover(f"#{current_idx + 1:02d}", icon=":material/format_list_numbered:", width="stretch"):
            st.caption("Lompat ke butir:")
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

    # 2. Integrated Slim Real-Time Progress Bar
    render_html(f"""
    <div class="quiz-compact-progress-track">
        <div class="quiz-compact-progress-fill" style="width: {pct}%;"></div>
    </div>
    """)

    # 3. Compact Scenario Card
    render_html(f"""
    <div class="scenario-compact-card" style="border-left: 4px solid var(--{temp_class}-color);">
        <div class="scenario-compact-dim-detail">{dim_detail}</div>
        <div class="scenario-compact-text">{q['scenario']}</div>
    </div>
    """)

    # 4. Acak letak opsi A dan B
    is_flipped = st.session_state.shuffled_options.get(q_id, False)
    opt_first = q["opt_b"] if is_flipped else q["opt_a"]
    opt_second = q["opt_a"] if is_flipped else q["opt_b"]
    code_first = "B" if is_flipped else "A"
    code_second = "A" if is_flipped else "B"

    current_ans = st.session_state.answers.get(q_id)
    is_first_sel = (current_ans == code_first)
    is_second_sel = (current_ans == code_second)

    label_1 = f"**A.** {opt_first['text']}"
    if is_first_sel:
        label_1 += " :material/check_circle: *(Terpilih)*"

    label_2 = f"**B.** {opt_second['text']}"
    if is_second_sel:
        label_2 += " :material/check_circle: *(Terpilih)*"

    # 5. Options Interactive Cards
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

    # 6. Bottom Controls Compact
    if current_idx == total - 1:
        col_prev, col_finish = st.columns([1, 1.8], gap="small", vertical_alignment="center")
        with col_prev:
            if st.button("Sebelumnya", key=f"btn_p_{current_idx}", type="secondary", icon=":material/arrow_back:", disabled=(current_idx == 0), width="stretch"):
                st.session_state.current_q -= 1
                st.rerun()
        with col_finish:
            all_done = (len(st.session_state.answers) == total)
            finish_label = "Lihat hasil analisis" if all_done else f"Jawab ({len(st.session_state.answers)}/{total})"
            if st.button(finish_label, key="btn_finish_test", type="primary", icon=":material/insights:", disabled=not all_done, width="stretch"):
                with st.spinner("Mengkalkulasi tipe kepribadian..."):
                    result = engine.compute_result(st.session_state.answers)
                    st.session_state.result = result
                    st.session_state.page = "result"
                    st.rerun()
    else:
        col_prev, col_hint = st.columns([1.2, 2.8], gap="small", vertical_alignment="center")
        with col_prev:
            if st.button("Sebelumnya", key=f"btn_p_{current_idx}", type="secondary", icon=":material/arrow_back:", disabled=(current_idx == 0), width="stretch"):
                st.session_state.current_q -= 1
                st.rerun()
        with col_hint:
            if q_id in st.session_state.answers:
                st.caption(":material/check: Tersimpan · klik opsi untuk lanjut.")
            else:
                st.caption("Klik salah satu opsi untuk lanjut.")


def render_result(result: MBTIResult, engine: PersonalityEngine) -> None:
    render_top_bar()

    profile = get_profile(result.mbti_type)
    temperament = profile.get("temperament", "Tipologi kognitif")
    temp_code = "nt" if "NT" in temperament else ("nf" if "NF" in temperament else ("sj" if "SJ" in temperament else "sp"))
    archetype = profile.get("archetype", result.mbti_type)
    summary_narrative = profile.get("summary", "")
    avatar_hero_tag = render_avatar_img(result.mbti_type, size=105, alt=archetype)

    # Hero Balance Chips
    balance_chips_html = ""
    if result.borderline_dims:
        dim_short_labels = {
            "EI": "Ambiversi (E/I Seimbang)",
            "SN": "Sensing & Intuisi Seimbang",
            "TF": "Logika & Empati Seimbang",
            "JP": "Rencana & Spontan Seimbang",
        }
        chips_inside = "".join(
            f'<span class="hero-balance-chip"><span class="balance-dot"></span>{dim_short_labels.get(d, d)}</span>'
            for d in result.borderline_dims
        )
        balance_chips_html = f'<div class="hero-balance-row">{chips_inside}</div>'

    # Hero Result: Karakter Menyatu Alami Tanpa Card Pod
    render_html(f"""
    <div class="friendly-result-hero" style="border-top: 4px solid var(--{temp_code}-color);">
        <div class="hero-result-header">
            <div class="hero-result-identity">
                <span class="hero-badge-pill temp-badge-{temp_code}">
                    {temperament}
                </span>
                <div class="hero-type-code temp-text-{temp_code}">{result.mbti_type}</div>
                <h2 class="hero-archetype-title">{archetype}</h2>
                {balance_chips_html}
            </div>
            <div class="hero-avatar-seamless">
                {avatar_hero_tag}
            </div>
        </div>
        <div class="hero-tagline-quote temp-quote-{temp_code}">
            "{profile.get('tagline', '')}"
        </div>
        <p class="hero-narrative-text">
            {summary_narrative}
        </p>
    </div>
    """)

    # Borderline / Balanced Advisory Card (Clean, Compact, Jungian)
    if result.borderline_dims:
        dim_labels = {
            "EI": "Mind (Ekstraversi &middot; Introversi)",
            "SN": "Energy (Penginderaan &middot; Intuisi)",
            "TF": "Nature (Pemikiran &middot; Perasaan)",
            "JP": "Tactics (Penilaian &middot; Eksplorasi)",
        }
        bl_chips = " &bull; ".join(dim_labels.get(d, d) for d in result.borderline_dims)
        render_html(f"""
        <div class="balance-advisory-card">
            <div class="balance-advisory-header">
                <span class="balance-advisory-pill">Kecenderungan Seimbang</span>
                <span class="balance-advisory-dims">{bl_chips}</span>
            </div>
            <p class="balance-advisory-desc">
                Skormu pada dimensi di atas berada di titik tengah seimbang (50% : 50%). Ini mencerminkan keluwesan kognitif situasional: kamu mampu beralih strategi secara luwes sesuai tuntutan situasi nyata tanpa terkunci kaku pada satu kutub.
            </p>
        </div>
        """)

    # 4 Dimensions Spectrum Data with Explanations, Symmetrical Pills & Dual Colors
    dim_meta = {
        "EI": {
            "pos": ("Ekstraversi", "E", "var(--dim-ei-pos)", "#4F46E5", "Mendapat energi dari interaksi sosial, bertindak spontan, dan memproses ide lewat komunikasi aktif."),
            "neg": ("Introversi", "I", "var(--dim-ei-neg)", "#0284C7", "Mengisi ulang energi dari waktu tenang (me-time), refleksi mandiri mendalam, dan fokus terarah."),
        },
        "SN": {
            "pos": ("Penginderaan", "S", "var(--dim-sn-pos)", "#059669", "Memproses realitas lewat fakta konkret terverifikasi, data riil, detail cermat, dan pengalaman praktis."),
            "neg": ("Intuisi", "N", "var(--dim-sn-neg)", "#8B5CF6", "Memahami pola tersembunyi, menghubungkan konsep abstrak, menangkap gambaran besar, dan prospek masa depan."),
        },
        "TF": {
            "pos": ("Pemikiran", "T", "var(--dim-tf-pos)", "#0284C7", "Membuat keputusan berbasis analisis objektif, logika konsisten, kejelasan fakta, dan evaluasi sebab-akibat."),
            "neg": ("Perasaan", "F", "var(--dim-tf-neg)", "#EC4899", "Memutuskan berdasarkan pertimbangan empati, dampak hubungan antarmanusia, dan keharmonisan nilai pribadi."),
        },
        "JP": {
            "pos": ("Penilaian", "J", "var(--dim-jp-pos)", "#D97706", "Menyukai rencana terstruktur, kejelasan langkah, jadwal teratur, dan kepastian target yang tuntas."),
            "neg": ("Eksplorasi", "P", "var(--dim-jp-neg)", "#10B981", "Menikmati fleksibilitas, spontanitas, adaptif terhadap kejutan situasi, dan menjaga opsi tetap terbuka."),
        },
    }

    spectrum_html = ""
    for dim_code, meta in dim_meta.items():
        score_obj = result.dimensions[dim_code]
        pct_pos = score_obj.pos_pct
        pct_neg = round(100.0 - pct_pos, 1)

        pos_name, pos_let, col_pos_text, col_pos_bar, pos_desc = meta["pos"]
        neg_name, neg_let, col_neg_text, col_neg_bar, neg_desc = meta["neg"]

        is_balanced = score_obj.is_borderline or (pct_pos == 50.0) or (abs(pct_pos - 50.0) <= 3.0)

        if is_balanced:
            left_class = "balanced"
            right_class = "balanced"
            left_tag = "· Seimbang"
            right_tag = "· Seimbang"
            left_border = f"border-color:{col_pos_text} !important;"
            right_border = f"border-color:{col_neg_text} !important;"
            left_winner_class = "balanced"
            right_winner_class = "balanced"
            marker_class = "balanced"
            balance_footer_html = f"""
            <div class="spectrum-balance-footer">
                <span class="spectrum-balance-badge">Seimbang 50:50</span>
                <span>Kamu memiliki keluwesan menggunakan <strong>{pos_name}</strong> maupun <strong>{neg_name}</strong> sesuai kebutuhan situasi nyata.</span>
            </div>
            """
        else:
            is_pos_winner = pct_pos > 50
            left_class = "winner" if is_pos_winner else "muted"
            right_class = "winner" if not is_pos_winner else "muted"
            left_tag = "· Dominan" if is_pos_winner else ""
            right_tag = "· Dominan" if not is_pos_winner else ""
            left_border = f"border-color:{col_pos_text} !important;" if is_pos_winner else ""
            right_border = f"border-color:{col_neg_text} !important;" if not is_pos_winner else ""
            left_winner_class = "winner" if is_pos_winner else ""
            right_winner_class = "winner" if not is_pos_winner else ""
            marker_class = ""
            balance_footer_html = ""

        spectrum_html += f"""
        <div class="spectrum-block">
            <!-- 1. Symmetrical Pills: Lebar & Tinggi Sama Persis -->
            <div class="spectrum-pills-row">
                <div class="spectrum-pill {left_class}" style="{left_border}">
                    <span class="spectrum-pill-name">{pos_name}</span>
                    <span class="spectrum-pill-pct" style="color:{col_pos_text};">{pct_pos:.0f}% {left_tag}</span>
                </div>
                <div class="spectrum-pill {right_class}" style="{right_border}">
                    <span class="spectrum-pill-name">{neg_name}</span>
                    <span class="spectrum-pill-pct" style="color:{col_neg_text};">{pct_neg:.0f}% {right_tag}</span>
                </div>
            </div>

            <!-- 2. Dual-Colored Track: Bar Penuh Berwarna Tanpa Efek Bar Kosong -->
            <div class="spectrum-dual-track">
                <div class="spectrum-segment-left" style="width:{pct_pos}%; background:{col_pos_bar};"></div>
                <div class="spectrum-segment-right" style="width:{pct_neg}%; background:{col_neg_bar};"></div>
                <div class="spectrum-center-marker {marker_class}" title="Titik Seimbang 50%"></div>
            </div>

            <!-- 3. Compact Explanatory Card di Bawah Bar -->
            <div class="spectrum-explain-card">
                <div class="spectrum-explain-cols-wrap">
                    <div class="spectrum-explain-col {left_winner_class}">
                        <div class="spectrum-explain-header">
                            <span class="spectrum-explain-badge" style="background:var(--dim-badge-bg); color:{col_pos_text}; border-color:{col_pos_text};">{pos_let}</span>
                            <strong>{pos_name}</strong>
                        </div>
                        <p class="spectrum-explain-text">{pos_desc}</p>
                    </div>
                    <div class="spectrum-explain-divider"></div>
                    <div class="spectrum-explain-col {right_winner_class}">
                        <div class="spectrum-explain-header">
                            <span class="spectrum-explain-badge" style="background:var(--dim-badge-bg); color:{col_neg_text}; border-color:{col_neg_text};">{neg_let}</span>
                            <strong>{neg_name}</strong>
                        </div>
                        <p class="spectrum-explain-text">{neg_desc}</p>
                    </div>
                </div>
                {balance_footer_html}
            </div>
        </div>
        """

    with st.container(border=True):
        st.markdown("**Spektrum kecenderungan 4 dimensi**")
        st.caption("Keseimbangan dua kutub alami caramu berinteraksi, mengolah informasi, memutuskan, dan bertindak:")
        render_html(spectrum_html)

    # 4 Deep-Dive Tabs (Simetris & Proporsional dengan Lebar Card)
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
            <div class="cog-layer-friendly-card" style="border-left: 3.5px solid var(--{temp_code}-color);">
                <div class="cog-layer-header">
                    <span class="cog-role-badge">{r_label}</span>
                    <span class="cog-symbol-tag temp-badge-{temp_code}">{func_code}</span>
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
        c_sup, c_bli = st.columns(2, gap="small")
        with c_sup:
            with st.container(border=True):
                st.markdown("**:material/check_circle: Kelebihan utamamu**")
                st.markdown(f'<div class="analysis-body-text">{sb.get("strengths", "-")}</div>', unsafe_allow_html=True)
        with c_bli:
            with st.container(border=True):
                st.markdown("**:material/tips_and_updates: Hal yang perlu kamu waspadai**")
                st.markdown(f'<div class="analysis-body-text">{sb.get("blindspots", "-")}</div>', unsafe_allow_html=True)

    with tab_work:
        with st.container(border=True):
            st.markdown("**:material/hub: Gaya kerja & dinamika tim**")
            st.markdown(f'<div class="analysis-body-text">{profile.get("work_style", "-")}</div>', unsafe_allow_html=True)

    with tab_stress:
        with st.container(border=True):
            st.markdown("**:material/healing: Saat stres & cara recharge paling ampuh**")
            st.markdown(f'<div class="analysis-body-text">{profile.get("stress_dynamics", "-")}</div>', unsafe_allow_html=True)

    # Structured Export
    summary_spectrum_lines = []
    for dim_k, dim_lbl, p_name, n_name in [
        ("EI", "Mind", "Ekstraversi", "Introversi"),
        ("SN", "Energy", "Penginderaan", "Intuisi"),
        ("TF", "Nature", "Pemikiran", "Perasaan"),
        ("JP", "Tactics", "Penilaian", "Eksplorasi"),
    ]:
        sc = result.dimensions[dim_k]
        is_bal = sc.is_borderline or (sc.pos_pct == 50.0) or (abs(sc.pos_pct - 50.0) <= 3.0)
        b_tag = " · [Seimbang / Fleksibel]" if is_bal else ""
        summary_spectrum_lines.append(f"• {dim_lbl:7s}: {sc.pos_pct:.0f}% {p_name} / {sc.neg_pct:.0f}% {n_name}{b_tag}")
    summary_spectrum_text = "\n".join(summary_spectrum_lines)

    summary_text = (
        f"[HASIL ASESMEN TIPE MBTI]\n"
        f"Tipe: {result.mbti_type}: {archetype}\n"
        f"Kelompok: {temperament}\n\n"
        f"Kecenderungan Spektrum:\n"
        f"{summary_spectrum_text}\n\n"
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

    st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)

    # Action Buttons Row
    c_ret, c_hom = st.columns(2, gap="small")
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
    init_session()
    theme_mode = st.session_state.get("theme_mode", "Auto")
    render_html(generate_theme_styles(theme_mode))

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
