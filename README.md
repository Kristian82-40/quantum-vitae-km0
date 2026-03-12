# Quantum Vitae KM0

> El primer ecosistema global que centraliza medicina alternativa, terapias holísticas y tecnología wellness con enfoque KM0.

## 🎯 Visión

Democratizar el acceso a la salud holística. Imaginamos un Amazon del mundo místico: chamanes, alquimistas, terapeutas alternativos y tecnologías wellness, todo en un solo lugar, desde kilómetro cero.

## 🚀 Características Principales

### 1. **Quantum Bio-Score**
Motor de diagnóstico que evalúa tu salud en 4 dimensiones clave:
- **Energía**: Calidad de sueño, fatiga, movimiento
- **Inflamación**: Dieta, síntomas digestivos, dolor
- **Estrés**: Carga laboral, ansiedad, desconexion
- **Coherencia KM0**: Alimentos locales, naturaleza, red social, rituales

Resultado: Un score 0-100 que agrupa a usuarios en 3 clusters:
- `0-39`: **Supervivencia** (acción inmediata)
- `40-69`: **Transición** (mejorando)
- `70-100`: **Coherencia Activa** (sostenibilidad)

### 2. **Plan Holístico Personalizado**
Tu plan llega en minutos, adaptado a tus necesidades únicas: nutrición, plantas medicinales, rutinas diseñadas.

### 3. **Marketplace de Terapeutas**
Conecta con sanadores, chamanes, alquimistas y terapeutas alternativos de todo el mundo.

### 4. **Tecnología Med-Tech**
Acceso a las últimas innovaciones: láser corporal, robótica wellness, HIFU, tecnologías de vanguardia.

## 📁 Estructura del Proyecto

```
/core                       # Motor de diagnóstico
  ├─ scoring_logic_v1.md   # Fórmulas del Bio-Score
  ├─ quiz_variables_v1.md  # Variables del quiz
  └─ profiles_catalog_v1.md # Catálogo de perfiles

/infrastructure            # Automatización y datos
  ├─ airtable_schema_v1.md # Esquema de BD
  └─ make_scenario_v1.md   # Flujo Typeform → Score → Email

/ux                        # Interfaz y comunicación
  └─ email_result_template_v1.txt # Plantilla de resultado

index.html                 # Landing page
checkout.html              # Página de pago
README.md                  # Este archivo
```

## ⚙️ Cómo Funciona el Quantum Bio-Score

### Entrada
Usuario completa quiz de 18 preguntas en Typeform (≈ 2 min).

### Procesamiento
1. Webhook desde Typeform → Make
2. Cálculo del score (4 sub-scores + score global)
3. Almacenamiento en Airtable

### Salida
Email personalizado con:
- Tu cluster + perfil
- Recomendaciones específicas
- CTA a plan detallado o sesión con terapeuta

### Fórmula Global
```
Quantum Bio-Score = 
  Energía (30%) + 
  Inflamación (25%) + 
  Estrés (25%) + 
  Coherencia KM0 (20%)
```

## 🔗 Links y Recursos

- **Web en vivo**: [kristian82-40.github.io/quantum-vitae-km0/](https://kristian82-40.github.io/quantum-vitae-km0/)
- **Quiz Typeform**: [form.typeform.com/to/srtjLaQn](https://form.typeform.com/to/srtjLaQn)
- **Documentación técnica**: Ver `/core` y `/infrastructure`

## 📋 Catálogo de Perfiles

Cada rango de score tiene un perfil único con recomendaciones. Ver [/core/profiles_catalog_v1.md](./core/profiles_catalog_v1.md) para detalles completos.

## 🎨 Tono de Marca

- **Cercano, empoderador, honesto**
- **Sin jerga médica innecesaria**
- **Respeto por el conocimiento ancestral y la tecnología**
- **Enfoque KM0: local primero, luego global**

## ⚖️ Disclaimer Legal

Quantum Vitae KM0 **no es un diagnóstico médico**. Es una guía de hábitos y bienestar basada en cuestionarios autoreportados. Siempre consulta con un profesional de salud antes de hacer cambios significativos.

## 🤝 Contribuciones

Este proyecto está en fase KM0 (kilómetro cero). Estamos construyendo con el usuario.

## 📝 Licencia

MIT License - Ver archivo LICENSE (por crear)

---

**Última actualización**: Marzo 2026
**Estado**: Fase 2 - Documentación + MVP Quiz
