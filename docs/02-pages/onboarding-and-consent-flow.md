# Flujo de Onboarding y Consentimiento de Usuario

Este documento describe la experiencia del usuario (UX) desde su primer contacto con la plataforma hasta la configuración avanzada de sus permisos de salud.

## 1. Primer Acceso: El Banner de Transparencia

Al entrar en la web por primera vez, el usuario se encuentra con un banner de diseño limpio y no obstructivo que presenta las opciones de consentimiento.

### Estructura del Banner
- **Texto Principal:** "En Quantum Vitae KM0, tu privacidad es nuestra prioridad nuclear. ¿Cómo quieres que usemos tus datos?"
- **Botón "Aceptar Todo":** Activa los 3 niveles (Técnico, Experiencia, Salud).
- **Botón "Solo Esenciales":** Activa solo el Nivel Técnico.
- **Enlace "Configurar":** Abre el modal de configuración granular.

## 2. Modal de Configuración Granular

Si el usuario elige "Configurar", se despliega un modal con interruptores (switches) para cada nivel.

| Nivel | Descripción para el Usuario | Implicación Técnica |
| :--- | :--- | :--- |
| **Técnico** | Necesario para que la web funcione. | Cookies de sesión. |
| **Experiencia** | Ayúdanos a mejorar la navegación (anónimo). | Heatmaps, Analítica UX. |
| **Salud y Apps** | Conecta tus dispositivos para automatizar datos. | OAuth HealthKit/Fit, Mensajería. |

## 3. Flujo Post-Consentimiento (Onboarding Suave)

Dependiendo de la elección, la experiencia cambia:

### Caso A: Solo Técnico
- El usuario accede a la web funcional.
- Se muestra un pequeño indicador en el perfil: "Privacidad máxima activada".
- No se solicitan permisos adicionales.

### Caso B: Experiencia Activada
- Se activan los scripts de analítica anónima.
- El sistema empieza a detectar el contexto técnico (OS, Región) para optimizar la carga de recursos.

### Caso C: Salud y Apps Activado
- Se inicia el **"Safe Onboarding de Salud"**:
  - "¿Deseas conectar Apple Health para sincronizar tus pasos y sueño automáticamente?"
  - Se muestran botones grandes con la identidad visual de Apple/Google.
  - Al pulsar, se abre el diálogo nativo de permisos del sistema operativo.

## 4. El "Centro de Privacidad y Permisos"

Dentro del área de usuario/ajustes, siempre existe una sección dedicada donde:
- Se muestra el estado actual de cada permiso.
- Se explican de nuevo los beneficios de cada nivel.
- Hay un botón de **"Revocar todo y borrar rastro"** para una salida limpia del ecosistema de datos.

## 5. Medidas de Seguridad en el Onboarding
- **Anti-Fatiga:** No pedir más de 2 permisos de salud en la primera sesión.
- **Explicación Contextual:** Si se pide acceso a WhatsApp, explicar: "Solo lo usaremos para recordarte tu toma de medicina alternativa a las 9:00 AM".
