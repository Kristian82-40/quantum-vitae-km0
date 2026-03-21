# Integración con Apps de Salud y Mensajería

Este documento detalla la capa técnica de conectividad con ecosistemas externos para automatizar la captura de datos y mejorar la comunicación con el usuario.

## 1. Ecosistemas de Salud (Wearables y Sensores)

Quantum utiliza flujos oficiales de OAuth 2.0 y SDKs nativos para importar métricas biológicas sin intervención manual.

### Plataformas Soportadas
- **Apple Health (HealthKit):** Exclusivo para iOS. Permite lectura de frecuencia cardíaca, sueño, pasos y variabilidad de la frecuencia cardíaca (HRV).
- **Google Fit:** Para dispositivos Android. Enfoque en actividad física y sueño.
- **Fitbit/Otros:** Integración vía API Cloud para usuarios con otros wearables.

### Datos Solicitados (Scopes)
- **Actividad:** Pasos, distancia, calorías.
- **Descanso:** Horas de sueño, fases del sueño (si están disponibles).
- **Bio-métricas:** Frecuencia cardíaca en reposo, peso (opcional).

### Flujo de Conexión
1. **Detección:** El sistema identifica el OS del usuario.
2. **Onboarding:** Se presenta el beneficio ("Conecta tu salud para un análisis automático").
3. **Autorización:** Redirección al flujo nativo de Apple/Google.
4. **Sincronización:** Quantum realiza una petición inicial y establece un webhook o tarea programada de actualización.

## 2. Canales de Mensajería y Notificaciones

Integración con apps de comunicación para recordatorios de terapias, hábitos y citas.

### Canales
- **WhatsApp / Telegram / Signal:** Uso de APIs oficiales (ej. WhatsApp Business API).
- **Propósito:** Notificaciones push de recordatorio, entrega de resultados de Bio-Score.

### Restricciones de Privacidad
- **NO Lectura:** Quantum tiene prohibido técnicamente leer mensajes entrantes no relacionados con el bot de Quantum.
- **Tokens Temporales:** Los tokens de envío se gestionan de forma aislada.
- **Contenido:** Solo se envían mensajes iniciados por eventos del sistema o respuestas a consultas del usuario.

## 3. Redes Sociales (Publicación y Login)

### Social Login (Opcional)
- Permite el registro rápido usando cuentas de Instagram o X.
- Solo se solicita el **email** y el **perfil público básico**.

### Publicación Automatizada
- Gestión de tokens de "página oficial" para que Quantum publique contenido educativo o logros comunitarios.
- NUNCA se publicarán datos privados del usuario en perfiles sociales sin una acción de "Compartir" iniciada manualmente por el usuario.

## 4. Revocación de Acceso

El usuario puede revocar el acceso de dos formas:
1. **Desde Quantum:** En el menú "Apps Conectadas", pulsando "Desconectar". Esto borra el token en nuestra DB.
2. **Desde la App Origen:** (Ej. Ajustes de Cuenta de Google -> Seguridad -> Apps de terceros). Quantum detectará el error de token y marcará la cuenta como desconectada automáticamente.
