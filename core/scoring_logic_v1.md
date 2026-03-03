# Quantum Bio-Score Scoring Logic v1

## Overview
Quantum Bio-Score es un índice 0-100 que sintetiza 4 dimensiones clave:
- **Energía**: calidad de sueño, fatiga, movimiento
- **Inflamación**: dieta, síntomas digestivos/dolor
- **Estrés**: carga laboral, presión, síntomas ansiedad
- **Coherencia KM0**: alimentos de proximidad, naturaleza, red social, rituales

Cada dimensión se normaliza a 0-100 y luego se pondera para obtener el QuantumBioScore global.

## Variables de entrada (q_*)

### Bloque ENERGÍA
- `q_sueno_horas` (0-12 horas)
- `q_sueno_calidad` (1-5)
- `q_fatiga_diaria` (1-5)
- `q_movimiento_min` (0-300 minutos)

### Bloque INFLAMACIÓN
- `q_dieta_ultraprocesados` (1-5)
- `q_azucar_freq` (1-5)
- `q_alcohol_freq` (1-5)
- `q_sintomas_digestivos` (1-5)
- `q_dolor_articular_cabeza` (1-5)

### Bloque ESTRÉS
- `q_carga_laboral` (1-5)
- `q_presion_urgencia` (1-5)
- `q_desconexion_capacidad` (1-5)
- `q_pantallas_noche` (1-5)
- `q_sintomas_ansiedad` (1-5)

### Bloque COHERENCIA KM0
- `q_porcentaje_km0` (0-100 %)
- `q_naturaleza_freq` (1-5)
- `q_red_social_local` (1-5)
- `q_rituales_coherencia` (1-5)

## Funciones de normalización

```
norm_1a5_alta(valor) = (valor - 1) * 25          // 1→0, 5→100 (más es mejor)
norm_1a5_baja(valor) = (5 - valor) * 25          // 1→100, 5→0 (menos es mejor)
clamp(x, min, max) = max(min(x, max), min)       // Limita rango
```

## Fórmulas de Sub-Scores

### energia_score
```
norm_sueno_horas = clamp(min(q_sueno_horas, 8) / 8 * 100, 0, 100)
norm_sueno_calidad = norm_1a5_alta(q_sueno_calidad)
norm_fatiga = norm_1a5_baja(q_fatiga_diaria)
norm_movimiento = clamp(min(q_movimiento_min, 60) / 60 * 100, 0, 100)

energia_score = round(
    norm_sueno_horas * 0.35
  + norm_sueno_calidad * 0.25
  + norm_fatiga * 0.20
  + norm_movimiento * 0.20
)
```

### inflamacion_score
```
norm_ultra = norm_1a5_baja(q_dieta_ultraprocesados)
norm_azucar = norm_1a5_baja(q_azucar_freq)
norm_alcohol = norm_1a5_baja(q_alcohol_freq)
norm_digest = norm_1a5_baja(q_sintomas_digestivos)
norm_dolor = norm_1a5_baja(q_dolor_articular_cabeza)

inflamacion_score = round(
    (norm_ultra + norm_azucar + norm_alcohol + norm_digest + norm_dolor) / 5
)
```

### estres_score
```
norm_carga = norm_1a5_baja(q_carga_laboral)
norm_presion = norm_1a5_baja(q_presion_urgencia)
norm_desconexion = norm_1a5_baja(q_desconexion_capacidad)
norm_pantallas = norm_1a5_baja(q_pantallas_noche)
norm_ansiedad = norm_1a5_baja(q_sintomas_ansiedad)

estres_score = round(
    norm_carga * 0.25
  + norm_presion * 0.20
  + norm_desconexion * 0.20
  + norm_pantallas * 0.15
  + norm_ansiedad * 0.20
)
```

### coherencia_km0_score
```
norm_km0_pct = clamp(q_porcentaje_km0, 0, 100)
norm_naturaleza = norm_1a5_alta(q_naturaleza_freq)
norm_red_social = norm_1a5_alta(q_red_social_local)
norm_rituales = norm_1a5_alta(q_rituales_coherencia)

coherencia_km0_score = round(
    norm_km0_pct * 0.40
  + norm_naturaleza * 0.20
  + norm_red_social * 0.20
  + norm_rituales * 0.20
)
```

## Quantum Bio-Score Global

```
quantum_bio_score = round(
    energia_score * 0.30
  + inflamacion_score * 0.25
  + estres_score * 0.25
  + coherencia_km0_score * 0.20
)
```

## Clusters y rangos

| Rango | Cluster | Significado |
|-------|---------|-------------|
| 0-39 | SUPERVIVENCIA | Sistema muy presionado, acción inmediata |
| 40-69 | TRANSICIÓN | Mejorando pero aún desalineado |
| 70-100 | COHERENCIA ACTIVA | Sistema en autorregulación y sostenibilidad |

## Actualización
Última versión: v1
Fecha: 2026-03-03
Autor: Quantum Vitae KM0
