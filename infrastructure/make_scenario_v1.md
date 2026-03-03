# Make Scenario v1: QuantumBioScore_MVP_Main

## Descripción General

Este escenario automatiza el flujo completo:
Typeform webhook → Cálculo de scores → Airtable → Email de resultado

## Prerequisitos

- **Typeform**: Quiz creado con variables mapeadas
- **Airtable**: Base "Quantum Vitae KM0" y tabla "QuantumBioScore_Responses" creada
- **Gmail**: Cuenta conectada a Make
- **Make**: Cuenta de desarrollador activa

## Pasos de Configuración

### Paso 1: Crear Trigger (Webhook Typeform)

1. En Make, crea nuevo escenario
2. Nombre: `QuantumBioScore_MVP_Main`
3. Primer módulo: `Typeform` → "Custom webhook"
4. En Typeform, Settings → Webhooks → Add Webhook
5. Pega la URL de Make en el webhook de Typeform
6. Prueba: completa quiz en Typeform, debe triggerar el escenario

**Mapeo de campos**: Make debe recibir automáticamente:
- `response_id`
- Todos los campos `q_*` (respuestas del usuario)
- `nombre`, `email`, `ciudad`, `pais`

### Paso 2: Módulo 1 - Parse/Map Answers

**App**: Tools → "Set variable"
**Nombre**: "Map answers from Typeform"
**Variables a crear**:

```
v_nombre = {{trigger.hidden.[nombre]}} O {{trigger.answers.nombre}}
v_email = {{trigger.answers.email}}
v_ciudad = {{trigger.answers.ciudad}}
v_pais = {{trigger.answers.pais}}
v_q_sueno_horas = {{trigger.answers.q_sueno_horas}}
(... continúa para todos los q_*)
```

**Nota**: Adapta según cómo Typeform envíe los datos. Prueba con 1-2 campos primero.

### Paso 3: Módulo 2 - Set Variables: energia_score

**App**: Tools → "Set variable"
**Nombre**: "Calculate energia_score"

Crea variables intermedias:

```
norm_sueno_horas = min({{v_q_sueno_horas}} / 8 * 100; 100)
norm_sueno_calidad = ({{v_q_sueno_calidad}} - 1) * 25
norm_fatiga = (5 - {{v_q_fatiga_diaria}}) * 25
norm_movimiento = min({{v_q_movimiento_min}} / 60 * 100; 100)

energia_score = round(
  norm_sueno_horas * 0.35 +
  norm_sueno_calidad * 0.25 +
  norm_fatiga * 0.20 +
  norm_movimiento * 0.20
)
```

### Paso 4: Módulo 3 - Set Variables: inflamacion_score

**App**: Tools → "Set variable"
**Nombre**: "Calculate inflamacion_score"

```
norm_ultra = (5 - {{v_q_dieta_ultraprocesados}}) * 25
norm_azucar = (5 - {{v_q_azucar_freq}}) * 25
norm_alcohol = (5 - {{v_q_alcohol_freq}}) * 25
norm_digest = (5 - {{v_q_sintomas_digestivos}}) * 25
norm_dolor = (5 - {{v_q_dolor_articular_cabeza}}) * 25

inflamacion_score = round(
  (norm_ultra + norm_azucar + norm_alcohol + norm_digest + norm_dolor) / 5
)
```

### Paso 5: Módulo 4 - Set Variables: estres_score

**App**: Tools → "Set variable"
**Nombre**: "Calculate estres_score"

```
norm_carga = (5 - {{v_q_carga_laboral}}) * 25
norm_presion = (5 - {{v_q_presion_urgencia}}) * 25
norm_desconexion = (5 - {{v_q_desconexion_capacidad}}) * 25
norm_pantallas = (5 - {{v_q_pantallas_noche}}) * 25
norm_ansiedad = (5 - {{v_q_sintomas_ansiedad}}) * 25

estres_score = round(
  norm_carga * 0.25 +
  norm_presion * 0.20 +
  norm_desconexion * 0.20 +
  norm_pantallas * 0.15 +
  norm_ansiedad * 0.20
)
```

### Paso 6: Módulo 5 - Set Variables: coherencia_km0_score

**App**: Tools → "Set variable"
**Nombre**: "Calculate coherencia_km0_score"

```
norm_km0 = {{v_q_porcentaje_km0}}
norm_naturaleza = ({{v_q_naturaleza_freq}} - 1) * 25
norm_red = ({{v_q_red_social_local}} - 1) * 25
norm_rituales = ({{v_q_rituales_coherencia}} - 1) * 25

coherencia_km0_score = round(
  norm_km0 * 0.40 +
  norm_naturaleza * 0.20 +
  norm_red * 0.20 +
  norm_rituales * 0.20
)
```

### Paso 7: Módulo 6 - Set Variables: quantum_bio_score

**App**: Tools → "Set variable"
**Nombre**: "Calculate quantum_bio_score"

```
quantum_bio_score = round(
  {{energia_score}} * 0.30 +
  {{inflamacion_score}} * 0.25 +
  {{estres_score}} * 0.25 +
  {{coherencia_km0_score}} * 0.20
)
```

### Paso 8: Módulo 7 - Airtable: Create Record

**App**: Airtable → "Create a record"
**Configuración**:
- Base: "Quantum Vitae KM0"
- Table: "QuantumBioScore_Responses"

**Mapear campos** (ejemplo):
- `id`: {{trigger.response_id}}
- `created_at`: {{now}}
- `nombre`: {{v_nombre}}
- `email`: {{v_email}}
- `ciudad`: {{v_ciudad}}
- `pais`: {{v_pais}}
- `q_sueno_horas`: {{v_q_sueno_horas}}
- ... (todos los q_*)
- `energia_score`: {{energia_score}}
- `inflamacion_score`: {{inflamacion_score}}
- `estres_score`: {{estres_score}}
- `coherencia_km0_score`: {{coherencia_km0_score}}
- `quantum_bio_score`: {{quantum_bio_score}}

### Paso 9: Módulo 8 - Gmail: Send Email

**App**: Gmail → "Send an email"
**Configuración**:

- **To**: {{v_email}}
- **Subject**: [Quantum Bio-Score] {{v_nombre}}, este es tu nivel de coherencia hoy
- **Body** (plain text o HTML):

```
Hola {{v_nombre}},

Tu Quantum Bio-Score global: {{quantum_bio_score}} / 100

Sub-scores:
- Energía: {{energia_score}} / 100
- Inflamación: {{inflamacion_score}} / 100
- Estrés: {{estres_score}} / 100
- Coherencia KM0: {{coherencia_km0_score}} / 100

Repite el test en 30 días para ver tu evolución.

Un abrazo,
Quantum Vitae KM0
```

### Paso 10: Test end-to-end

1. **Activa** el escenario en Make
2. **Completa** el quiz en Typeform (usa test responden si aplica)
3. **Verifica**:
   - Aparece record en Airtable con scores calculados
   - Recibes email con los scores

Si algo falla, revisa **Make Logs** (historial de ejecuciones).

## Troubleshooting

**Problema**: Typeform no trigguea Make  
**Solución**: Revisa que el webhook URL esté correcto en Typeform. Tipea el URL manual si copiar-pegar no funciona.

**Problema**: Campos vacíos en Airtable  
**Solución**: Verifica que el "Field Name" en Airtable coincida exactamente con el nombre en Make (case-sensitive).

**Problema**: Errores en cálculos  
**Solución**: Abre Make Logs → haz clic en módulo fallido → "View" para ver el error exacto. Usualmente son variables sin mapear o formato incorrecto.

## Próximos pasos (para después)

- Añadir condicionales para asignar cluster y perfil
- Crear plantilla de email dinámica según perfil
- Programar re-test automático con escenario recurrente
- Integrar WhatsApp como canal alternativo
