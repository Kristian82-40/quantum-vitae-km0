# ==============================================================
# QUANTUM BIO-SCORE - Motor de Reglas de Asignacion de Perfiles
# Version: 2.0 | Proyecto: Quantum Vitae KM0
# Principio: Activacion por dimension especifica y umbrales
# ==============================================================

import json

DIMENSION_WEIGHTS = {
    "sueno_calidad": 0.15,
    "estres_cronico": 0.15,
    "alimentacion_calidad": 0.15,
    "actividad_fisica": 0.10,
    "exposicion_toxicos": 0.10,
    "ritmo_circadiano": 0.10,
    "sintomas_digestivos": 0.10,
    "claridad_mental": 0.08,
    "equilibrio_hormonal": 0.07,
}

def calculate_quantum_bio_score(responses):
    total_score = 0.0
    total_weight = 0.0
    for dimension, weight in DIMENSION_WEIGHTS.items():
        val = responses.get(dimension, 0)
        total_score += val * weight
        total_weight += weight
    return round(total_score / total_weight, 2) if total_weight > 0 else 0

def classify_score_label(score):
    if score >= 85: return "Optimización Crítica"
    if score >= 65: return "Atención Necesaria"
    if score >= 45: return "Funcional / Estable"
    return "Homeostasis / Óptimo"

def assign_profiles(responses, catalog_path="data/profiles_catalog.json"):
    """
    Asigna perfiles basados en si la dimension_principal supera el umbral_activacion.
    """
    try:
        with open(catalog_path, 'r', encoding='utf-8') as f:
            profiles_catalog = json.load(f)
    except Exception as e:
        print(f"Error cargando catálogo: {e}")
        return {}

    score = calculate_quantum_bio_score(responses)
    active_profiles = []

    for profile in profiles_catalog:
        dim = profile.get("dimension_principal")
        threshold = profile.get("umbral_activacion", 60)
        
        # Valor de la respuesta para esa dimensión específica
        dim_value = responses.get(dim, 0)
        
        if dim_value >= threshold:
            active_profiles.append({
                "id": profile["id"],
                "nombre": profile["nombre_es"],
                "tag": profile["tag"],
                "activation_strength": dim_value,
                "recomendaciones": profile["recomendaciones"]
            })

    # Ordenar por fuerza de activación (de mayor a menor impacto)
    active_profiles.sort(key=lambda x: x["activation_strength"], reverse=True)

    return {
        "quantum_bio_score": score,
        "score_label": classify_score_label(score),
        "active_profiles_count": len(active_profiles),
        "perfil_principal": active_profiles[0]["id"] if active_profiles else None,
        "perfil_secundario": active_profiles[1]["id"] if len(active_profiles) > 1 else None,
        "active_profiles": active_profiles
    }

if __name__ == "__main__":
    test_responses = {
        "sueno_calidad": 72,
        "estres_cronico": 68,
        "alimentacion_calidad": 55,
        "actividad_fisica": 40,
        "exposicion_toxicos": 60,
        "ritmo_circadiano": 78,
        "sintomas_digestivos": 50,
        "claridad_mental": 45,
        "equilibrio_hormonal": 62,
    }
    
    result = assign_profiles(test_responses)
    print(f"Quantum Bio-Score: {result['quantum_bio_score']} ({result['score_label']})")
    print(f"Perfiles Activos ({result['active_profiles_count']}):")
    for p in result['active_profiles']:
        print(f" -> {p['nombre']} | Fuerza: {p['activation_strength']}")
