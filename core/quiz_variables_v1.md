# Quiz Variables - Quantum Bio-Score v1

## Estructura del Quiz en Typeform

Cada pregunta debe tener un **"variable name"** para que Typeform mapee automáticamente a los campos de la base de datos.

## Bloque 1: Datos Básicos

| Pregunta | Variable Name | Tipo | Rango/Opciones |
|----------|---------------|------|----------------|
| ¿Cómo te llamas? | nombre | Short text | - |
| ¿Cuál es tu email? | email | Email | - |
| ¿En qué ciudad vives? | ciudad | Short text | - |
| ¿En qué país vives? | pais | Short text | - |

## Bloque 2: ENERGÍA

| Pregunta | Variable Name | Tipo | Rango/Opciones |
|----------|---------------|------|----------------|
| De media, ¿cuántas horas duermes por noche? | q_sueno_horas | Number | 0-12 |
| ¿Cómo valorarías la calidad de tu sueño? | q_sueno_calidad | Opinion Scale | 1-5 (1=muy mala, 5=muy buena) |
| ¿Cuánta fatiga sientes a lo largo del día? | q_fatiga_diaria | Opinion Scale | 1-5 (1=nada, 5=muchísima) |
| ¿Cuántos minutos de movimiento activo haces al día? | q_movimiento_min | Number | 0-300 |

## Bloque 3: INFLAMACIÓN

| Pregunta | Variable Name | Tipo | Rango/Opciones |
|----------|---------------|------|----------------|
| ¿Con qué frecuencia consumes productos ultraprocesados? | q_dieta_ultraprocesados | Opinion Scale | 1-5 (1=casi nunca, 5=varias veces al día) |
| ¿Con qué frecuencia tomas bebidas o alimentos muy azucarados? | q_azucar_freq | Opinion Scale | 1-5 (1=casi nunca, 5=varias veces al día) |
| ¿Con qué frecuencia consumes alcohol? | q_alcohol_freq | Opinion Scale | 1-5 (1=nunca, 5=a diario) |
| ¿Con qué frecuencia tienes molestias digestivas? | q_sintomas_digestivos | Opinion Scale | 1-5 (1=casi nunca, 5=muy a menudo) |
| ¿Con qué frecuencia tienes dolor articular o de cabeza? | q_dolor_articular_cabeza | Opinion Scale | 1-5 (1=casi nunca, 5=muy a menudo) |

## Bloque 4: ESTRÉS

| Pregunta | Variable Name | Tipo | Rango/Opciones |
|----------|---------------|------|----------------|
| ¿Cómo valorarías tu carga laboral ahora mismo? | q_carga_laboral | Opinion Scale | 1-5 (1=muy baja, 5=extremadamente alta) |
| ¿Con qué frecuencia sientes prisa o urgencia constante? | q_presion_urgencia | Opinion Scale | 1-5 (1=casi nunca, 5=casi todo el día) |
| ¿Qué tan fácil te resulta desconectar del trabajo? | q_desconexion_capacidad | Opinion Scale | 1-5 (1=muy fácil, 5=casi imposible) |
| ¿Cuánto usas pantallas en la última hora antes de dormir? | q_pantallas_noche | Opinion Scale | 1-5 (1=casi nada, 5=casi siempre) |
| ¿Con qué frecuencia notas síntomas de ansiedad? | q_sintomas_ansiedad | Opinion Scale | 1-5 (1=casi nunca, 5=muy a menudo) |

## Bloque 5: COHERENCIA KM0

| Pregunta | Variable Name | Tipo | Rango/Opciones |
|----------|---------------|------|----------------|
| Aproximadamente, ¿qué % de tus comidas son KM0? | q_porcentaje_km0 | Number | 0-100 |
| ¿Con qué frecuencia pasas tiempo en naturaleza? | q_naturaleza_freq | Opinion Scale | 1-5 (1=casi nunca, 5=casi a diario) |
| ¿Cuánto sientes que cuentas con red de apoyo cercana? | q_red_social_local | Opinion Scale | 1-5 (1=nada, 5=muchísimo) |
| ¿Con qué frecuencia realizas rituales que te calman? | q_rituales_coherencia | Opinion Scale | 1-5 (1=casi nunca, 5=casi a diario) |

## Instrucciones para Typeform

1. En cada pregunta, ir a **Settings**
2. Ir a la sección **Variable name**
3. Copiar el nombre exacto del campo (ej: `q_sueno_horas`)
4. Pegar en el campo de variable name de Typeform
5. Guardar

**Importante**: Los nombres deben ser exactos para que el mapeo en Make funcione correctamente.
