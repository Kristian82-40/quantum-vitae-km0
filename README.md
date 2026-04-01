# Quantum Vitae KM0

> El cuaderno mundial vivo de plantas, saberes ancestrales y autocuración. Un sistema de integración holística único que no deja fuera ninguna voz de la historia medicinal humana: desde la abuela que usa ruda en la cocina hasta el grimorio medieval, pasando por la farmacéutica que extrajo morfina de la adormidera.

---

## 🎯 Visión

Quantum Vitae KM0 es el primer sistema de diagnóstico holístico global que integra milenios de sabiduría medicinal ancestral con tecnología moderna. No es solo wellness: es un rescate activo de técnicas y plantas que se están perdiendo, fusionado con evidencia científica actual y desplegado con responsabilidad legal mundial.

**Principio rector:** Quantum no deja fuera nada. Todo se integra, pero siempre con seguridad, contexto cultural y responsabilidad legal.

---

## 🌍 Qué es Quantum (definición ampliada)

Quantum Vitae KM0 es simultáneamente:

- **Un cuaderno mundial de plantas**: base de datos viva de plantas medicinales de todas las culturas, con ficha doble (cara mística + cara científica moderna)
- **Un motor de diagnóstico holístico**: cruza todas las tradiciones internamente y devuelve recomendaciones claras sin abrumar
- **Un rescatador de saberes perdidos**: documenta técnicas de curanderas, grimorios, rituales chamánicos y medicina doméstica que estaban desapareciendo
- **Un sistema de integración universal**: Ayurveda, Medicina China, Kampo, Tibetana, Unani, Siddha, Curanderismo, Mapuche, Amazónica, Africana, Bush Medicine y Medicina Oculta europea, todo en un solo diagnóstico

---

## 🚀 Características Principales

### 1. **Quantum Bio-Score**
Motor de diagnóstico que evalúa al usuario en 4 dimensiones clave:
- **Energía**: Calidad de sueño, fatiga, movimiento
- **Inflamación**: Dieta, síntomas digestivos, dolor
- **Estrés**: Carga laboral, ansiedad, desconexión
- **Coherencia KM0**: Alimentos locales, naturaleza, red social, rituales

Resultado: Score 0-100 → 3 estados:
- `0-39`: **Supervivencia** (acción inmediata)
- `40-69`: **Transición** (mejorando)
- `70-100`: **Coherencia Activa** (sostenibilidad)

### 2. **Cuaderno Mundial de Plantas**
Base de datos viva con fichas dobles para cada planta:
- **Cara mística**: historia, rituales, leyendas, usos en religiones y chamanismo, por qué se está perdiendo
- **Cara moderna**: propiedades comprobadas, toxicidad, precauciones, estado legal por país

Organizada en capas de acceso:
- **Capa 1 – Cotidiana**: fenogreco, cúrcuma, jengibre, boldo, ruda suave, especias medicinales
- **Capa 2 – Plantas Puente**: las que la farmacopea moderna se apropió (adormidera→morfina, sauce→aspirina, dedalera→digoxina, cannabis medicinal)
- **Capa 3 – Tradiciones Globales**: módulos por región (Asia, Américas, África, Oceanía, Chamanismo)
- **Capa 4 – Plantas de las Brujas**: belladona, beleño, estramonio, mandrágora, amapola, celidonia (solo info etnobotánica + advertencias, acceso de pago)

### 3. **Diagnóstico Holístico Global**
El motor consulta internamente todos los sistemas tradicionales:

**Asia**: Ayurveda · Medicina China (TCM) · Kampo (Japón) · Medicina Tibetana (Sowa Rigpa) · Unani · Siddha

**Américas**: Curanderismo · Kallawaya (Andes) · Mapuche · Aymara · Tacana/Leco (Amazonía) · Nativa Americana

**África y Oceanía**: Medicina Tradicional Africana · Bush Medicine aborigen

**Global**: Chamanismo · Medicina Oculta europea (brujas, curanderas, grimorios)

El usuario recibe solo 3-5 recomendaciones priorizadas. Puede desplegar "¿Qué diría cada tradición?" por pestaña.

### 4. **Niveles de Acceso Progresivo**
Desbloqueados por cuestionario de experiencia, país y contexto legal:
- **Nivel 1** (gratuito): plantas seguras, alimentos-medicina, prácticas simples
- **Nivel 2** (freemium): plantas puente, tradiciones completas por región
- **Nivel 3** (pago + consentimiento): Plantas de las Brujas, medicina oculta, sustancias con regulación especial

### 5. **Capa Legal Global Geo-Adaptativa**
Base de datos de restricciones actualizada por IA + equipo legal. Según país del usuario:
- Plantas legales en todo el mundo → siempre disponibles
- Plantas reguladas → información histórica + advertencia fuerte según país
- Plantas proscritas en el país del usuario → bloqueadas para uso práctico, solo ficha etnobotánica

### 6. **Marketplace de Terapeutas y Productos**
Conecta con sanadores, chamanes, herbolaristas y terapeutas alternativos de todo el mundo. Productos recomendados por Bio-Score, nunca por comisión.

### 7. **Tecnología Med-Tech**
Acceso a innovaciones: láser corporal, robótica wellness, HIFU, frecuencias 432Hz, tecnologías de vanguardia integradas con la sabiduría ancestral.

---

## 📁 Estructura del Proyecto

```
/core              # Motor de diagnóstico y lógica
  scoring_logic_v1.md        # Fórmulas del Bio-Score
  quiz_variables_v1.md       # Variables del quiz
  profiles_catalog_v1.md     # Catálogo de perfiles
/data              # Bases de datos de plantas y tradiciones
/docs              # Documentación técnica y conceptual
/engine            # Bio-Score engine (Python)
  bio_score_engine.py        # Motor de puntuación con activación por dimensiones
/infrastructure    # Automatización y datos
  airtable_schema_v1.md      # Esquema de BD
  make_scenario_v1.md        # Flujo Typeform → Score → Email
/ux                # Interfaz y comunicación
  email_result_template_v1.txt  # Plantilla de resultado
index.html         # Landing page
checkout.html      # Página de pago
README.md          # Este archivo
ROADMAP.md         # Hoja de ruta 2026
PROGRESS.md        # Tracker de progreso
```

---

## ⚙️ Cómo Funciona el Diagnóstico

### Entrada
Usuario completa quiz de 18 preguntas (≈ 2 min). Cuestionario de nivel desbloquea acceso progresivo.

### Procesamiento
1. Webhook desde Typeform → Make
2. Cálculo del Bio-Score (4 sub-scores + score global)
3. Consulta interna a todos los módulos de tradiciones
4. Filtro geo-legal según país del usuario
5. Almacenamiento en Airtable

### Salida
Email personalizado con:
- Tu cluster + perfil
- 3-5 recomendaciones priorizadas (vía suave + vía experta si corresponde)
- Pestañas colapsables por tradición (si nivel lo permite)
- CTA a plan detallado, terapeuta cercano o sección de plantas

### Fórmula Global
```
Quantum Bio-Score = Energía (30%) + Inflamación (25%) + Estrés (25%) + Coherencia KM0 (20%)
```

---

## 🌿 Sección Especial: Plantas de las Brujas y Medicina Oculta

Sección de acceso de pago con estética mística (fondo oscuro, grimorios, luna). Incluye:
- Belladona · Beleño · Estramonio · Mandrágora · Amapola (faceta proscrita) · Ruda · Celidonia · Valeriana · Artemisa
- Cada ficha tiene tres planos simultáneos: **Mito y ritual** / **Uso histórico de curanderas y grimorios** / **Ficha científica moderna** (toxicidad, regulación, advertencias)
- Advertencia fija: *"Información histórica y etnobotánica solamente. Uso práctico solo bajo supervisión de profesional cualificado. Quantum no sustituye atención médica ni cubre responsabilidad legal."*

---

## 🔗 Links y Recursos

- **Web en vivo**: [quantum-vitae-km0.vercel.app](https://quantum-vitae-km0.vercel.app)
- **GitHub Pages**: [kristian82-40.github.io/quantum-vitae-km0/](https://kristian82-40.github.io/quantum-vitae-km0/)
- **Quiz Typeform**: [form.typeform.com/to/srtjLaQn](https://form.typeform.com/to/srtjLaQn)
- **Documentación técnica**: Ver `/core`, `/docs` e `/infrastructure`

---

## 🎨 Tono de Marca

- **Cercano, empoderador, honesto, humilde**
- **Sin jerga médica innecesaria**
- **Profundo respeto por el conocimiento ancestral de todos los pueblos**
- **Lo místico mantiene su misterio; lo científico aporta seguridad**
- **Enfoque KM0: local primero, luego global**

---

## ⚖️ Disclaimer Legal

Quantum Vitae KM0 **no es un diagnóstico médico**. Es una guía de hábitos, bienestar y conocimiento etnobotánico basada en cuestionarios autoreportados y documentación histórica. Las plantas de alto riesgo se presentan exclusivamente como información histórica y cultural. Siempre consulta con un profesional de salud cualificado antes de usar cualquier planta medicinal, especialmente las que aparecen en la sección de acceso avanzado.

---

## 🤝 Contribuciones

Este proyecto está en construcción activa. Buscamos colaboradores con conocimiento en etnobotánica, medicina tradicional, desarrollo web y regulación sanitaria internacional.

---

## 📝 Licencia

MIT License

---

**Última actualización**: Abril 2026  
**Estado**: Fase 2 en progreso — Arquitectura holística global definida  
**Responsable**: Kristian (GitHub: Kristian82-40)
