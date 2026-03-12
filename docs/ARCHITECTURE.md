# Quantum Vitae KM0 – System Architecture

## Overview

Quantum Vitae KM0 operates as an intelligent wellness ecosystem that combines:
- **Zero-Party Data Collection** (user-provided quiz responses)
- **AI-Driven Personalization** (conscious, transparent, context-aware)
- **Granular Consent Management** (opt-in by purpose)
- **KM0 Philosophy** (local-first, then global)

This document defines the core architecture pillars: Therapy Taxonomy, Consent Framework, and AI Context Engine.

---

## 1. Therapy Taxonomy (8 Families)

### Purpose
The taxonomy enables:
- Consistent tagging of therapists and treatments
- Bio-Score to therapy mapping
- Multi-modal wellness recommendations
- Respect for ancestral and modern knowledge

### The 8 Families

#### 1.1 Plantas Medicinales (Medicinal Plants)
**Sub-categories:**
- **Adaptógenas**: Ashwagandha, Rhodiola, Ginseng (stress resilience, energy regulation)
- **Calmantes**: Valeriana, Pasiflora, Lavanda (nervous system support, sleep)
- **Energizantes**: Matcha, Guaraná, Maca (vitality, focus)
- **Antiinflamatorias**: Cúrcuma, Jengibre, Boswellia (chronic inflammation)
- **Inmunomoduladoras**: Equinácea, Reishi, Sauco (immune support)

**Mapped to Bio-Score:**
- **Supervivencia** → Calmantes + Antiinflamatorias
- **Coherencia** → Adaptógenas + Inmunomoduladoras
- **Expansión** → Energizantes + Adaptógenas de alta potencia

**Sources:**
- Latinoamérica: Medicina andina (Bolivia, Perú), medicina amazónica
- Asia: Medicina tradicional china, Ayurveda
- Europa: Fitoterapia moderna validada

---

#### 1.2 Masajes y Quiromasaje Terapéutico
**Sub-categories:**ción, mejora circulatoria
- **Reflexología**: Puntos en pies/manos conectados a órganos

**Mapped to Bio-Score:**
- **Supervivencia** → Masaje terapéutico + Drenaje
- **Coherencia/Expansión** → Quiromasaje + Reflexología

---

#### 1.3 Respiración y Meditación Guiada
**Sub-categories:**
- **Respiración consciente**: Wim Hof, Pranayama, Box Breathing
- **Meditación guiada**: Mindfulness, Body Scan, Visualizaciones
- **Prácticas contemplativas**: Zen, Vipassana

**Mapped to Bio-Score:**
- **Supervivencia** → Respiración calmante, meditación guiada corta
- **Coherencia** → Pranayama, mindfulness estructurado
- **Expansión** → Prácticas contemplativas avanzadas

---

#### 1.4 Movimiento (Yoga, Tai-Chi, Danza)
**Sub-categories:**
- **Yoga terapéutico**: Yin, Restorative
- **Yoga dinámico**: Vinyasa, Ashtanga
- **Tai-Chi / Qi-Gong**: Flujo energético, equilibrio
- **Danza consciente**: Danza libre, biodanza

**Mapped to Bio-Score:**
- **Supervivencia** → Yoga terapéutico, Tai-Chi suave
- **Coherencia** → Yoga dinámico, Qi-Gong
- **Expansión** → Danza consciente, prácticas avanzadas

---

#### 1.5 Terapia Animal (Equinoterapia, Canoterapia)
**Sub-categories:**
- **Equinoterapia**: Conexión caballo-humano, desarrollo emocional
- **Canoterapia**: Perros de asistencia emocional
- **Otras**: Delfinoterapia, terapia con gatos

**Mapped to Bio-Score:**
- **Supervivencia** → Canoterapia (soporte emocional inmediato)
- **Coherencia/Expansión** → Equinoterapia (conexión profunda)

---

#### 1.6 Meditaciones y Mindfulness
**Sub-categories:**
- **Mindfulness**: Atención plena en lo cotidiano
- **Meditaciones de sonido**: Cuencos tibetanos, mantras
- **Meditación caminando**: Naturaleza, bosque

**Mapped to Bio-Score:**
- **Todas las fases**: Adaptable según intensidad

---

#### 1.7 Medicina Tradicional (Andina, Himalaya, Amazónica)
**Sub-categories:**
- **Andina**: Kallawaya (Bolivia), curanderos peruanos
- **Himalaya**: Medicina tibetana, Ayurveda
- **Amazónica**: Uso de plantas enteogénicas en contexto ritual (ceremonias)
- **México**: Curanderismo, uso de copal, limpias energéticas

**Mapped to Bio-Score:**
- **Supervivencia/Coherencia** → Medicina herbal, rituales de limpieza
- **Expansión** → Ceremonia ritual supervisada (contexto legal y ético)

**Important**: Quantum respeta las tradiciones y opera dentro de marcos legales locales.

---

#### 1.8 Medicina Moderna Integrativa
**Sub-categories:**
- **Funcional**: Análisis biométrico, suplementación basada en datos
- **Naturopatía**: Combinación de fitoterapia + nutrición
- **Tecnología wellness**: Láser corporal, HIFU, crioterapia, robótica

**Mapped to Bio-Score:**
- **Coherencia/Expansión** → Optimización con tecnología

---

## 2. Consent Framework (Consentimiento Granular)

### Principles
1. **Transparencia**: El usuario sabe qué datos se usan y para qué.
2. **Opt-in separado por propósito**: No hay "aceptar todo".
3. **Valor claro**: Se explica qué gana el usuario al compartir.
4. **Revocación fácil**: Puede cambiar permisos en cualquier momento.

### Consent Categories

#### 2.1 Personalización Interna
**¿Qué incluye?**
- Usar respuestas del quiz para calcular Bio-Score
- Adaptar mensajes y recomendaciones

**Texto para el usuario:**
> "Usamos tus respuestas para personalizar tu Bio-Score y recomendaciones. Sin esto, Quantum no puede ofrecerte un plan adaptado."

**Estado**: Obligatorio para usar Quantum (sin esto, no hay servicio).

---

#### 2.2 Emails y Comunicaciones
**¿Qué incluye?**
- Enviar resultados del Bio-Score
- Secuencias de email automatizadas
- Newsletters con contenido educativo

**Texto para el usuario:**
> "¿Quieres recibir tu Bio-Score por email y recursos personalizados? Puedes cancelar en cualquier momento."

**Estado**: Opt-in.

---

#### 2.3 Geolocalización (Local Finder)
**¿Qué incluye?**
- Usar tu ciudad/CP para recomendarte terapeutas cercanos (KM0)
- Mapas interactivos

**Texto para el usuario:**
> "Compartir tu ubicación nos permite mostrarte terapeutas cerca de ti. Solo guardamos ciudad/CP, no dirección exacta."

**Estado**: Opt-in.

---

#### 2.4 Datos Compartidos con Terapeutas
**¿Qué incluye?**
- Compartir tu Bio-Score + motivo principal con terapeutas seleccionados
- Facilitar la conexión antes de la primera sesión

**Texto para el usuario:**
> "Si decides contactar un terapeuta, compartiremos tu estado general (ej. 'Supervivencia, estrés alto') para que puedan prepararse. No compartimos todo el cuestionario sin tu permiso."

**Estado**: Opt-in por terapeuta (decides caso por caso).

---

#### 2.5 Analítica y Mejora
**¿Qué incluye?**
- Datos anonimizados para mejorar el sistema (A/B testing, tendencias)

**Texto para el usuario:**
> "Usamos datos anonimizados para mejorar Quantum (ej. 'qué preguntas son confusas'). Nunca te identificamos personalmente."

**Estado**: Opt-in.

---

### Implementation
- **Typeform**: Checkboxes separados al final del quiz
- **Email flows**: Link para gestionar preferencias
- **Dashboard usuario**: Panel de permisos (futuro)

---

## 3. AI Context Engine (IA Consciente)

### Purpose
La IA de Quantum personaliza mensajes, recomendaciones y flujos basada en:
1. **Estado actual** (Supervivencia / Coherencia / Expansión)
2. **Ubicación** (ciudad, si el usuario dio permiso)
3. **Trayectoria** (¿mejorando o empeorando entre mediciones?)
4. **Intereses declarados** (terapias que interesan)

### How It Works

#### 3.1 Data Inputs
```
User Profile = {
  bio_score: 0-100,
  state: "Supervivencia" | "Coherencia" | "Expansión",
  location: "Barcelona, ES" (if consented),
  trajectory: "improving" | "stable" | "declining",
  interests: ["plantas", "masajes", "yoga"],
  last_interaction: timestamp
}
```

#### 3.2 Prompt Templates

**Ejemplo: Email para Supervivencia**
```
Tono: Apoyo, sin juzgar, esperanza
Contenido:
- Reconocer dónde estás
- Herramientas sencillas e inmediatas
- CTA: Hablar con terapeuta local

Prompt:
"Escribe un email para {nombre}, que está en estado Supervivencia (Bio-Score {score}). 
Le interesan {interests}. Vive en {location}.
Tono: cálido, sin alarmismo. 
Ofrece 2 acciones simples que puede hacer hoy."
```

**Ejemplo: Email para Coherencia**
```
Tono: Reto, optimización, data-driven
Contenido:
- Celebrar progreso
- Proponer siguiente nivel
- CTA: Programa avanzado o terapia específica

Prompt:
"Escribe un email para {nombre}, en Coherencia (Bio-Score {score}).
Está mejorando. Le interesan {interests}. 
Tono: motivacional, desafiante.
Propone una práctica avanzada que le lleve al siguiente nivel."
```

#### 3.3 Transparency
- Usuario sabe que mensajes son personalizados
- Panel futuro: "Por qué recibí esta recomendación"

---

## 4. Integration Summary

```
Taxonomy (8 Families) → Tag Therapists & Products
                       → Map to Bio-Score States
                       
 Consent Framework     → Collect Zero-Party Data
                       → Enable/Disable features granularly
                       
AI Context Engine      → Personalize Messages
                       → Recommend Therapies/Products
                       → Adapt Tone by State
```

---

## Next Steps

1. **Validate Taxonomy** with 5-10 therapists (KM0 priority)
2. **Implement Consent UI** in Typeform + Email flows
3. **Test AI Prompts** with real user data (pilot Fase 1)
4. **Document edge cases** (ej. usuarios sin ubicación, sin intereses declarados)

---

**Maintained by**: Kristian (Product Lead)  
**Last Updated**: March 12, 2026  
**Version**: 1.0
- **Masaje terapéutico profundo**: Liberar tensión muscular crónica
- **Quiromasaje**: Movilidad articular, equilibrio estructural
- **Drenaje linfático**: Desinflama
