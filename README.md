# Diseño y Prototipado de API REST para Banca

La institución financiera requiere una nueva API REST para gestionar operaciones de cuentas bancarias. La API debe permitir la creación, lectura, actualización y eliminación de cuentas, así como la realización de transferencias entre cuentas. El sistema debe manejar la autenticación de usuarios y garantizar la integridad de las operaciones. Los actores involucrados son el 'cliente', el'sistema de autenticación' y el 'core bancario'. La API debe soportar un throughput de 1 000 operaciones por segundo con una latencia máxima de 500 ms. Las cuentas tienen un identificador único, un saldo inicial, y un estado (activa/inactiva). Las transferencias deben ser idempotentes con clave de operación y canal. En caso de fallo del core bancario, la API debe encolar las solicitudes para reintentar automáticamente.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | diseño de api rest en el dominio de banca |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición de Requisitos y Especificación de la API

**Objetivo:** Establecer los requisitos funcionales y no funcionales de la API, y especificar sus endpoints.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identificar y documentar los requisitos funcionales y no funcionales de la API.
- Definir los endpoints de la API, incluyendo métodos HTTP, parámetros de entrada y salida, y códigos de estado HTTP esperados.
- Establecer las reglas de negocio para la creación, lectura, actualización y eliminación de cuentas, así como para las transferencias.

**Entregable:** Documento de especificación de la API con requisitos y endpoints definidos.

<details>
<summary>Pistas de conocimiento</summary>

- Considera las propiedades operativas como throughput y latencia en la definición de requisitos.
- Piensa en cómo garantizar la idempotencia de las transferencias.

</details>

### Fase 2: Prototipado de la API y Autenticación de Usuarios

**Objetivo:** Implementar un prototipado de la API y configurar la autenticación de usuarios.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Crear un prototipado de la API con los endpoints definidos en la fase anterior.
- Configurar la autenticación de usuarios utilizando el sistema de autenticación proporcionado.
- Implementar la lógica básica para la creación, lectura, actualización y eliminación de cuentas.

**Entregable:** Prototipado funcional de la API con autenticación de usuarios y lógica básica de cuentas.

<details>
<summary>Pistas de conocimiento</summary>

- Utiliza el sistema de autenticación para verificar la identidad de los usuarios.
- Considera cómo manejar los errores de autenticación y autorización.

</details>

### Fase 3: Implementación de Transferencias Idempotentes

**Objetivo:** Implementar la lógica para realizar transferencias idempotentes entre cuentas.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Implementar la lógica para realizar transferencias entre cuentas utilizando una clave de operación y canal.
- Garantizar que las transferencias sean idempotentes, es decir, que dos invocaciones con la misma clave produzcan el mismo resultado.
- Manejar los casos de error y fallo del core bancario encolando las solicitudes para reintentar automáticamente.

**Entregable:** API con lógica implementada para transferencias idempotentes y manejo de errores.

<details>
<summary>Pistas de conocimiento</summary>

- Utiliza una clave de operación y canal para garantizar la idempotencia de las transferencias.
- Considera cómo encolar las solicitudes para reintentar automáticamente en caso de fallo del core bancario.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una API REST y cuáles son sus componentes principales?
- **paraQueSirve**: ¿Para qué sirve la autenticación de usuarios en una API REST?
- **comoSeUsa**: ¿Cómo se utiliza una clave de operación y canal para garantizar la idempotencia de las transferencias?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar una API REST y cómo se pueden evitar?
- **queDecisionesImplica**: ¿Qué decisiones implica el diseño de una API REST para banca?

## Criterios de Evaluacion

- Especificación de la API con requisitos y endpoints definidos.
- Prototipado funcional de la API con autenticación de usuarios y lógica básica de cuentas.
- Lógica implementada para transferencias idempotentes y manejo de errores.

## Como trabajar con un asistente de IA

- **AGENTS.md** — instrucciones nativas del repo (Cursor, Codex, Copilot, Gemini, Claude Code). Abrí el proyecto y el agente las carga solo.
- **PROMPT_MEJORA.md** — el mismo prompt, para copiar y pegar en un chat (claude.ai, ChatGPT, etc.).

---

*Reto generado automaticamente por Challenge Generator - Pragma*
