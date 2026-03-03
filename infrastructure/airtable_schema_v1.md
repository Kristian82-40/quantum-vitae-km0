# Airtable Schema v1

**Base Name**: Quantum Vitae KM0
**Primary Table**: QuantumBioScore_Responses

## Field Configuration

### Identificación
- `id` | Single line text | Response ID from Typeform
- `created_at` | Date | Auto-filled timestamp
- `source` | Single line text | Default: "typeform_main_quiz"

### Datos Personales
- `nombre` | Single line text | User first name
- `email` | Email | User email address
- `ciudad` | Single line text | City of residence
- `pais` | Single line text | Country code (ISO 2-letter)
- `idioma` | Single line text | Language locale (e.g., es-ES, en-US)

### Bloque ENERGÍA (Inputs)
- `q_sueno_horas` | Number | 0-12 hours
- `q_sueno_calidad` | Number | 1-5 scale
- `q_fatiga_diaria` | Number | 1-5 scale
- `q_movimiento_min` | Number | 0-300 minutes

### Bloque INFLAMACIÓN (Inputs)
- `q_dieta_ultraprocesados` | Number | 1-5 scale
- `q_azucar_freq` | Number | 1-5 scale
- `q_alcohol_freq` | Number | 1-5 scale
- `q_sintomas_digestivos` | Number | 1-5 scale
- `q_dolor_articular_cabeza` | Number | 1-5 scale

### Bloque ESTRÉS (Inputs)
- `q_carga_laboral` | Number | 1-5 scale
- `q_presion_urgencia` | Number | 1-5 scale
- `q_desconexion_capacidad` | Number | 1-5 scale
- `q_pantallas_noche` | Number | 1-5 scale
- `q_sintomas_ansiedad` | Number | 1-5 scale

### Bloque COHERENCIA KM0 (Inputs)
- `q_porcentaje_km0` | Number | 0-100 percentage
- `q_naturaleza_freq` | Number | 1-5 scale
- `q_red_social_local` | Number | 1-5 scale
- `q_rituales_coherencia` | Number | 1-5 scale

### Scores Calculados (via Make)
- `energia_score` | Number | 0-100 (calculated)
- `inflamacion_score` | Number | 0-100 (calculated)
- `estres_score` | Number | 0-100 (calculated)
- `coherencia_km0_score` | Number | 0-100 (calculated)
- `quantum_bio_score` | Number | 0-100 (calculated)

### Segmentación
- `cluster_global` | Single line text | "supervivencia", "transicion", "coherencia_activa"
- `perfil_sintetico_id` | Single line text | e.g., "hiperproductivo_inflamado"
- `perfil_sintetico_label` | Single line text | User-friendly profile name

### Comunicación y Seguimiento
- `mensaje_clave` | Long text | Personalized message for user
- `oferta_recomendada` | Single line text | "informe_premium", "suscripcion", "free_only"
- `email_resultado_enviado` | Checkbox | Email sent flag
- `whatsapp_resultado_enviado` | Checkbox | WhatsApp sent flag
- `canal_principal` | Single line text | "email" or "whatsapp"

### Re-Test
- `re_test_fecha_programada` | Date | Scheduled re-test date (30 days out)
- `re_test_estado` | Single line text | "pendiente", "enviado", "completado"

### Tracking
- `km0_clicks_total` | Number | Cumulative clicks to KM0 resources
- `km0_ultimo_click_at` | Date | Last click timestamp
- `url_resultado_unico` | URL | Link to personalized result page (optional)

### Notas
- `notas_internas` | Long text | Internal notes for manual review

## Setup Instructions

1. Create base "Quantum Vitae KM0"
2. Create table "QuantumBioScore_Responses"
3. Add all fields in order above
4. Configure field types exactly as specified
5. Set `created_at` field to auto-fill with timestamp
6. Enable Airtable API for this base (Account > Developer)
7. Copy base ID and table ID for Make integration
