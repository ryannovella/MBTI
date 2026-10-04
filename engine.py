from __future__ import annotations
import json
import os
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import streamlit as st


FALLBACK_QUESTIONS: List[dict] = [
    {
        "id": 1, "dim": "EI", "cog_tag": "Fe/Ti",
        "scenario": "Lagi asyik nongkrong bareng teman, tiba-tiba di tengah acara baterai sosialmu mulai habis drastis. Biasanya respon alamimu...",
        "opt_a": {"text": "Tetap lanjut nimbrung dan nyari obrolan seru, karena interaksi justru bisa naikin mood dan energimu lagi.", "dim": "E", "val": 1},
        "opt_b": {"text": "Memilih diam, menyimak obrolan saja, dan mengurangi ngomong sambil pelan-pelan istirahatin pikiran.", "dim": "I", "val": 1}
    },
    {
        "id": 7, "dim": "SN", "cog_tag": "Si/Ne",
        "scenario": "Waktu tim lagi brainstorming konsep baru, kamu paling nyaman kalau mulai dari mana...",
        "opt_a": {"text": "Dari contoh nyata dan referensi yang sudah terbukti berhasil, baru kita modifikasi sesuai kebutuhan.", "dim": "S", "val": 1},
        "opt_b": {"text": "Dari ide liar dan konsep yang belum pernah dicoba, membayangkan potensi ke depan tanpa batasan dulu.", "dim": "N", "val": 1}
    },
    {
        "id": 13, "dim": "TF", "cog_tag": "Ti/Fe",
        "scenario": "Teman dekat minta pendapat jujur soal rencana bisnis atau keputusannya yang menurutmu rapuh. Pendekatanmu...",
        "opt_a": {"text": "Kasih analisis kritis apa adanya soal titik lemah dan risikonya, karena itu yang paling dia butuhkan biar nggak rugi.", "dim": "T", "val": 1},
        "opt_b": {"text": "Jaga perasaannya dulu dan apresiasi niat baiknya, baru sampaikan masukan secara halus biar dia tetap semangat.", "dim": "F", "val": 1}
    },
    {
        "id": 19, "dim": "JP", "cog_tag": "Je/Pe",
        "scenario": "Kamu dikasih tugas atau proyek yang tenggat waktunya masih dua minggu lagi. Ritme kerjamu...",
        "opt_a": {"text": "Bikin jadwal cicilan per hari atau per minggu dari sekarang, biar di akhir waktu tinggal finishing santai.", "dim": "J", "val": 1},
        "opt_b": {"text": "Kumpulin bahan santai dulu di awal, lalu eksekusi ngebut dengan fokus penuh pas momentum dan energinya lagi dapet.", "dim": "P", "val": 1}
    }
]

COG_FUNCTION_STACKS: Dict[str, Dict[str, str]] = {
    "INTJ": {"dominant": "Ni (Introverted Intuition)", "auxiliary": "Te (Extraverted Thinking)",
             "tertiary": "Fi (Introverted Feeling)", "inferior": "Se (Extraverted Sensing)"},
    "INTP": {"dominant": "Ti (Introverted Thinking)", "auxiliary": "Ne (Extraverted Intuition)",
             "tertiary": "Si (Introverted Sensing)", "inferior": "Fe (Extraverted Feeling)"},
    "ENTJ": {"dominant": "Te (Extraverted Thinking)", "auxiliary": "Ni (Introverted Intuition)",
             "tertiary": "Se (Extraverted Sensing)", "inferior": "Fi (Introverted Feeling)"},
    "ENTP": {"dominant": "Ne (Extraverted Intuition)", "auxiliary": "Ti (Introverted Thinking)",
             "tertiary": "Fe (Extraverted Feeling)", "inferior": "Si (Introverted Sensing)"},
    "INFJ": {"dominant": "Ni (Introverted Intuition)", "auxiliary": "Fe (Extraverted Feeling)",
             "tertiary": "Ti (Introverted Thinking)", "inferior": "Se (Extraverted Sensing)"},
    "INFP": {"dominant": "Fi (Introverted Feeling)", "auxiliary": "Ne (Extraverted Intuition)",
             "tertiary": "Si (Introverted Sensing)", "inferior": "Te (Extraverted Thinking)"},
    "ENFJ": {"dominant": "Fe (Extraverted Feeling)", "auxiliary": "Ni (Introverted Intuition)",
             "tertiary": "Se (Extraverted Sensing)", "inferior": "Ti (Introverted Thinking)"},
    "ENFP": {"dominant": "Ne (Extraverted Intuition)", "auxiliary": "Fi (Introverted Feeling)",
             "tertiary": "Te (Extraverted Thinking)", "inferior": "Si (Introverted Sensing)"},
    "ISTJ": {"dominant": "Si (Introverted Sensing)", "auxiliary": "Te (Extraverted Thinking)",
             "tertiary": "Fi (Introverted Feeling)", "inferior": "Ne (Extraverted Intuition)"},
    "ISFJ": {"dominant": "Si (Introverted Sensing)", "auxiliary": "Fe (Extraverted Feeling)",
             "tertiary": "Ti (Introverted Thinking)", "inferior": "Ne (Extraverted Intuition)"},
    "ESTJ": {"dominant": "Te (Extraverted Thinking)", "auxiliary": "Si (Introverted Sensing)",
             "tertiary": "Ne (Extraverted Intuition)", "inferior": "Fi (Introverted Feeling)"},
    "ESFJ": {"dominant": "Fe (Extraverted Feeling)", "auxiliary": "Si (Introverted Sensing)",
             "tertiary": "Ne (Extraverted Intuition)", "inferior": "Ti (Introverted Thinking)"},
    "ISTP": {"dominant": "Ti (Introverted Thinking)", "auxiliary": "Se (Extraverted Sensing)",
             "tertiary": "Ni (Introverted Intuition)", "inferior": "Fe (Extraverted Feeling)"},
    "ISFP": {"dominant": "Fi (Introverted Feeling)", "auxiliary": "Se (Extraverted Sensing)",
             "tertiary": "Ni (Introverted Intuition)", "inferior": "Te (Extraverted Thinking)"},
    "ESTP": {"dominant": "Se (Extraverted Sensing)", "auxiliary": "Ti (Introverted Thinking)",
             "tertiary": "Fe (Extraverted Feeling)", "inferior": "Ni (Introverted Intuition)"},
    "ESFP": {"dominant": "Se (Extraverted Sensing)", "auxiliary": "Fi (Introverted Feeling)",
             "tertiary": "Te (Extraverted Thinking)", "inferior": "Ni (Introverted Intuition)"},
}


@dataclass
class DimensionScore:
    dim: str
    pos_letter: str
    neg_letter: str
    pos_label: str
    neg_label: str
    pos_count: int = 0
    neg_count: int = 0
    total: int = 0

    @property
    def pos_pct(self) -> float:
        if self.total == 0:
            return 50.0
        return round((self.pos_count / self.total) * 100, 1)

    @property
    def neg_pct(self) -> float:
        return round(100.0 - self.pos_pct, 1)

    @property
    def dominant_letter(self) -> str:
        return self.pos_letter if self.pos_count >= self.neg_count else self.neg_letter

    @property
    def is_borderline(self) -> bool:
        pct = self.pos_pct
        return 47.0 <= pct <= 53.0


@dataclass
class MBTIResult:
    mbti_type: str
    dimensions: Dict[str, DimensionScore]
    cognitive_stack: Dict[str, str]
    borderline_dims: List[str] = field(default_factory=list)


@st.cache_data(show_spinner=False)
def _load_questions_from_disk(path: str) -> List[dict]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("Empty or invalid questions file.")
        return data
    except Exception:
        return FALLBACK_QUESTIONS


class PersonalityEngine:
    DIMENSION_META = {
        "EI": ("E", "I", "Extraversion", "Introversion"),
        "SN": ("S", "N", "Sensing", "Intuition"),
        "TF": ("T", "F", "Thinking", "Feeling"),
        "JP": ("J", "P", "Judging", "Prospecting"),
    }

    def __init__(self, questions_path: Optional[str] = None) -> None:
        if questions_path is None:
            questions_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "questions.json"
            )
        self.questions_path = questions_path
        self.questions: List[dict] = _load_questions_from_disk(questions_path)

    def get_questions(self) -> List[dict]:
        return self.questions

    def compute_result(self, answers: Dict[int, str]) -> MBTIResult:
        scores: Dict[str, DimensionScore] = {}
        for dim_key, (pos, neg, pos_label, neg_label) in self.DIMENSION_META.items():
            scores[dim_key] = DimensionScore(
                dim=dim_key,
                pos_letter=pos,
                neg_letter=neg,
                pos_label=pos_label,
                neg_label=neg_label,
            )

        for q in self.questions:
            q_id: int = q["id"]
            dim: str = q["dim"]
            if q_id not in answers:
                continue
            chosen: str = answers[q_id]
            opt = q["opt_a"] if chosen == "A" else q["opt_b"]
            letter: str = opt["dim"]
            val: int = opt.get("val", 1)

            score = scores[dim]
            score.total += val
            if letter == score.pos_letter:
                score.pos_count += val
            else:
                score.neg_count += val

        mbti_type = "".join(scores[d].dominant_letter for d in ["EI", "SN", "TF", "JP"])
        borderline = [d for d, s in scores.items() if s.is_borderline]
        cog_stack = COG_FUNCTION_STACKS.get(mbti_type, {})

        return MBTIResult(
            mbti_type=mbti_type,
            dimensions=scores,
            cognitive_stack=cog_stack,
            borderline_dims=borderline,
        )
