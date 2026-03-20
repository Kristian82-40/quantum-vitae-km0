# ============================================================
# QUANTUM BIO-SCORE - Motor de Reglas de Asignacion de Perfiles
# Version: 1.0 | Proyecto: Quantum Vitae KM0
# Principio: perfiles NO excluyentes, activacion por rangos
# ============================================================

PROFILES_CATALOG = [
    {"id": "circadian",           "rango_min": 75,  "rango_max": 100},
    {"id": "silent_inflammation", "rango_min": 45,  "rango_max": 74},
    {"id": "metabolic",           "rango_min": 0,   "rango_max": 44},
    {"id": "hpa_axis",            "rango_min": 50,  "rango_max": 85},
    {"id": "gut_functional",      "rango_min": 35,  "rango_max": 65},
    {"id": "neuro_immune",        "rango_min": 60,  "rango_max": 100},
    {"id": "brain_fog",           "rango_min": 20,  "rango_max": 50},
    {"id": "detox_load",          "rango_min": 30,  "rango_max": 80},
    {"id": "oxidative_aging",     "rango_min": 55,  "rango_max": 100},
    {"id": "hormonal_balance",    "rango_min": 25,  "rango_max": 75},
]

DIMENSION_WEIGHTS = {
    "sueno_calidad":         0.15,
    "estres_cronico":        0.15,
    "alimentacion_calidad":  0.15,
    "actividad_fisica":      0.10,
    "exposicion_toxicos":    0.10,
    "ritmo_circadiano":      0.10,
    "sintomas_digestivos":   0.10,
    "claridad_mental":       0.08,
    "equilibrio_hormonal":   0.07,
}

def calculate_quantum_bio_score(responses):
    total_score = 0.0
    total_weight = 0.0
    for dimension, weight in DIMENSION_WEIGHTS.items():
        if dimension in responses:
            value = max(0, min(100, responses[dimension]))
            total_score += value * weight
            total_weight += weight
    return round(total_score / total_weight) if total_weight > 0 else 0

def assign_profiles(score):
    active_profiles = []
    for profile in PROFILES_CATALOG:
        if profile["rango_min"] <= score <= profile["rango_max"]:
            active_profiles.append({
                "profile_id": profile["id"],
                "score": score,
                "activation_strength": calculate_activation_strength(
                    score, profile["rango_min"], profile["rango_max"]
                )
            })
    active_profiles.sort(key=lambda x: x["activation_strength"], reverse=True)
    return active_profiles

def calculate_activation_strength(score, r_min, r_max):
    r_center = (r_min + r_max) / 2.0
    r_half = (r_max - r_min) / 2.0
    if r_half == 0:
        return 1.0
    return round(max(0.0, min(1.0, 1.0 - (abs(score - r_center) / r_half))), 3)

def classify_score_label(score):
    if score <= 25:   return "optimo"
    elif score <= 50: return "atencion"
    elif score <= 75: return "intervencion"
    else:             return "critico"

def build_user_health_report(user_id, responses, profiles_catalog_full):
    score = calculate_quantum_bio_score(responses)
    active_profile_ids = assign_profiles(score)
    active_ids = {p["profile_id"] for p in active_profile_ids}
    enriched_profiles = []
    for profile_full in profiles_catalog_full:
        if profile_full["id"] in active_ids:
            activation_meta = next(
                p for p in active_profile_ids if p["profile_id"] == profile_full["id"]
            )
            enriched_profiles.append({
                **profile_full,
                "activation_strength": activation_meta["activation_strength"]
            })
    enriched_profiles.sort(
        key=lambda x: x.get("activation_strength", 0), reverse=True
    )
    return {
        "user_id": user_id,
        "quantum_bio_score": score,
        "score_label": classify_score_label(score),
        "active_profiles_count": len(enriched_profiles),
        "active_profiles": enriched_profiles,
    }

if __name__ == "__main__":
    test_responses = {
        "sueno_calidad":        72,
        "estres_cronico":       68,
        "alimentacion_calidad": 55,
        "actividad_fisica":     40,
        "exposicion_toxicos":   60,
        "ritmo_circadiano":     78,
        "sintomas_digestivos":  50,
        "claridad_mental":      45,
        "equilibrio_hormonal":  62,
    }
    score = calculate_quantum_bio_score(test_responses)
    active = assign_profiles(score)
    print(f"Quantum Bio-Score: {score}")
    print(f"Perfiles activos ({len(active)}):")
    for p in active:
        print(f"  -> {p['profile_id']} | fuerza: {p['activation_strength']}")
