# Arquitectura de Consentimiento y Contexto - Quantum Vitae KM0

Este documento define cómo Quantum Vitae KM0 gestiona la detección del contexto técnico del usuario y el modelo de consentimiento ético para el tratamiento de datos de salud y conectividad.

## 1. Detección de Contexto (Privacidad por Diseño)

Quantum detecta automáticamente ciertos parámetros técnicos para optimizar la interfaz y las sugerencias de integración, sin realizar tracking invasivo.

### Datos Detectados Automáticamente
- **Plataforma/OS:** iOS (iPhone, iPad), Android, o Desktop.
- **Región y Zona Horaria:** Basado en IP y encabezados de red (aproximado).
- **Idioma:** Preferencia del navegador (`Accept-Language`).

### Uso de la Información
- **UI Adaptativa:** Mostrar botones de "Conectar Apple Health" solo en dispositivos iOS.
- **Localización:** Mostrar terapeutas o productos disponibles en la región del usuario.
- **Notificaciones:** Ajustar el envío de recordatorios al huso horario local para evitar molestias nocturnas.
- **Prohibición:** Estos datos NUNCA se usarán para fingerprinting agresivo o venta a terceros.

## 2. Modelo de Consentimiento en 3 Niveles

El consentimiento se organiza de forma granular para dar control total al usuario.

### Nivel A: Técnico (Esencial)
- **Alcance:** Cookies y almacenamiento local estrictamente necesarios para el funcionamiento de la web (sesión, preferencias de idioma básicas).
- **Obligatoriedad:** No opcional para el uso del servicio, pero documentado con transparencia.

### Nivel B: Experiencia y Mejora (Analítica)
- **Alcance:** Heatmaps (mapas de calor), análisis de scroll y clicks, A/B testing.
- **Garantía:** Datos siempre agregados y anónimos. No se identifica al individuo.
- **Opción:** El usuario puede aceptar o rechazar en el banner inicial.

### Nivel C: Salud, Hábitos y Apps Conectadas
- **Alcance:** Integración con HealthKit, Google Fit, Fitbit y apps de mensajería (WhatsApp/Telegram).
- **Uso:** Importación de métricas biológicas y envío de notificaciones de salud.
- **Transparencia:** Se requiere permiso explícito por cada tipo de dato (pasos, sueño, etc.).

## 3. Registro y Gestión de Permisos

### Almacenamiento Seguro
- Se registra la fecha del consentimiento, el nivel aceptado y los "scopes" específicos.
- Los tokens de acceso a apps de terceros se cifran con estándares de seguridad nuclear.

### Centro de Preferencias
- Siempre accesible desde la sección "Privacidad y Permisos".
- Permite revocar cualquier acceso de forma instantánea.
- Al revocar el Nivel C, los tokens de conexión se eliminan permanentemente de nuestros servidores.

## 4. Flujo de Datos y Privacidad Extra

Cuando se combinan datos de salud (Nivel C) con analítica de uso (Nivel B), Quantum aplica una capa de **desvinculación temporal**. La analítica de UX nunca debe permitir la reconstrucción del perfil clínico de un usuario específico.
