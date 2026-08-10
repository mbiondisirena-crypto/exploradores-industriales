# Exploradores Industriales — Guión maestro (versión 2)

Este documento **reemplaza** a `jefe-de-planta-meli-script.md` y a `exploradores-industriales-prompt.md` anteriores — llevá solo este, junto con `box-colapinto.html` (ya construido y corregido), a Claude Code.

Cambios respecto de la versión anterior:

- El juego de Mercado Libre pasa a llamarse **ClickGo** (marca ficticia, mantiene el estilo y la paleta amarillo/azul tipo marketplace, sin usar el nombre ni el logo real de Mercado Libre).
- El juego de carrera ya no menciona "Alpine" en ningún lado — el equipo se llama **ITBA Racing** (ya corregido en `box-colapinto.html`, junto con un bug del cronómetro que no corría en tiempo real).
- Se agregan **dos actividades nuevas**: "Consultores Industriales" (carga del puesto 1° a 6° de una dinámica presencial) y una **Trivia** con un Kahoot externo.
- Se agrega un **sistema de puntaje compartido** entre las cuatro actividades, acumulado y visible en el hub.

---

## 1. Sistema de puntaje compartido

Cada actividad vive en su propia página HTML. Como el sitio no tiene backend, el puntaje se comparte entre páginas usando `localStorage` del navegador, con estas claves fijas:

| Clave de localStorage | Actividad | Rango de puntos |
|---|---|---|
| `exploradores_score_racing` | ITBA Racing (Colapinto) | 10 / 20 / 30 (ya implementado en `box-colapinto.html`) |
| `exploradores_score_clickgo` | Jefe de Planta ClickGo | 0 a 17 |
| `exploradores_score_consultores` | Consultores Industriales | 5, 10, 15, 20, 25 o 30 |
| `exploradores_score_trivia` | Trivia | 0 a 30 |

**Regla general:** cada actividad, al terminar, calcula sus puntos y hace `localStorage.setItem('exploradores_score_<actividad>', puntos)`. Si un equipo repite una actividad, el valor nuevo **reemplaza** al anterior (no se suman intentos, vale el último resultado).

El **hub** (`index.html`) y la **pantalla de resultados finales** leen las cuatro claves con `localStorage.getItem(...)`, tratan como `0` cualquiera que no exista todavía (actividad no jugada), y muestran:

- El desglose por actividad (nombre + puntos, o "Todavía no jugado" si falta).
- El **puntaje total** = suma de las cuatro.

No hace falta normalizar las escalas entre actividades — cada una tiene su propio máximo según su complejidad, lo importante es que el total sea la suma transparente de las cuatro, mostrando siempre el desglose al lado del total (nunca solo el número final solo).

Agregar un botón chico **"Reiniciar puntaje del equipo"** en el hub (limpia las 4 claves de localStorage) para que cada grupo nuevo en el evento empiece de cero.

---

## 2. Landing page (`index.html`) — actualizada a 4 actividades

**Header:** título "Exploradores Industriales", bajada "Viví la ingeniería jugando", marca institucional "ITBA — Ingeniería Industrial".

**Debajo del header:** un bloque fijo con el **puntaje total acumulado del equipo** (lee de localStorage, se actualiza cada vez que se vuelve al hub), y el botón de reinicio mencionado arriba.

**Cuatro tarjetas**, mismo formato que antes (nombre, descripción corta, tag de habilidad, botón "Jugar", y ahora también el puntaje ya obtenido en esa actividad si ya se jugó):

1. **ITBA Racing: Preparen el auto de Colapinto** — "Organizá el cronograma de construcción del auto antes de la clasificación." — Tag: *Planificación de proyectos y precedencias* — Link: `juegos/box-colapinto.html`
2. **Sos el Jefe de Planta de ClickGo** — "Tu primer día al mando de un centro de distribución. 50.000 paquetes por despachar y decisiones bajo presión." — Tag: *Toma de decisiones y resolución de problemas* — Link: `juegos/clickgo.html`
3. **Consultores Industriales** — "Cargá el resultado de la dinámica de consultoría que hicieron en equipo." — Tag: *Trabajo en equipo y negociación* — Link: `juegos/consultores.html`
4. **Trivia Exploradores** — "Un Kahoot para poner a prueba lo que aprendieron." — Tag: *Repaso general* — Link: `juegos/trivia.html`

**Pantalla / sección de resultados finales:** puede ser una quinta tarjeta "Ver resultado final del equipo" o una sección aparte en el propio `index.html` que muestra el desglose de las 4 actividades + el total, con un mensaje de cierre corto (por ejemplo: "Así piensa un ingeniero industrial: planifica, decide bajo presión, negocia en equipo y no deja de aprender").

---

## 3. Juego 1 — ITBA Racing (ya construido)

Usar `box-colapinto.html` tal cual está — ya no menciona a Alpine, ya tiene el cronómetro corregido (corre en tiempo real desde que arranca el juego, no desde una simulación falsa), y ya guarda sus puntos en `localStorage.exploradores_score_racing` al terminar (10/20/30 según estrellas). Solo hay que:

- Ubicarlo en `juegos/box-colapinto.html`.
- Agregarle el link "← Volver a Exploradores Industriales" arriba, apuntando a `../index.html`.

No tocar el resto del archivo.

---

## 4. Juego 2 — Jefe de Planta ClickGo

Historia, mecánica y las 9 rondas **idénticas** a la versión Mercado Libre ya diseñada, pero renombrando la empresa a **ClickGo** en todo el texto (título, historia, y cualquier mención dentro de las rondas). El estilo y la paleta de colores (amarillo vibrante + azul, estética marketplace/e-commerce) se mantienen — es una identidad visual genérica de e-commerce, no un logo ni nombre real.

### 4.1 Mecánica y puntaje

Igual que antes: 9 rondas (7 de diagnóstico + 2 de decisión sin respuesta única + 1 reto final que vale doble), sistema de rangos Operario → Supervisor → Coordinador → Gerente → Jefe de Planta.

Puntos por ronda:

- Diagnóstico (rondas 1, 2, 3, 4, 5, 7): correcta 2 pts / intermedia 1 pt / débil 0 pts.
- Decisión (rondas 6 y 8): 1 punto fijo por participar, sin "correcto/incorrecto".
- Reto final (ronda 9): correcta 3 pts / intermedia 1 pt / débil 0 pts.

Puntaje máximo: 17. Al terminar la ronda 9, además de mostrar el rango final, **guardar el puntaje total en `localStorage.setItem('exploradores_score_clickgo', puntajeTotal)`**.

### 4.2 Pantalla de inicio

**Título:** Sos el Jefe de Planta de ClickGo

**Texto:**
> Es tu primer día como Jefe/a de Planta en un centro de distribución de ClickGo. Hoy hay que despachar 50.000 paquetes. En cada ronda va a aparecer un problema real de la operación — tu equipo vota qué harían, y después vemos qué haría (y por qué) un ingeniero industrial de verdad.

Botón: **"Empezar mi primer día"**. Rango inicial visible: **Operario/a** (0 puntos).

### 4.3 Rondas de diagnóstico

**📦 Ronda 1 — Se rompe una cinta transportadora**

Situación: Se rompe una cinta transportadora en plena mañana. El flujo de paquetes hacia el sector de despacho se corta.

- A) Esperar a que mantenimiento la repare *(1 pt)*
- B) Reorganizar el flujo por otra línea *(2 pts — correcta)*
- C) Frenar toda la operación *(0 pts)*

Explicación: Un ingeniero industrial diseña procesos pensando en que algo se va a romper tarde o temprano — por eso conviene tener flexibilidad y rutas alternativas. Frenar todo paraliza la planta por un problema local; esperar sin más deja capacidad ociosa. Reorganizar el flujo mantiene la operación funcionando. *Concepto clave: redundancia y flexibilidad de procesos.*

**🚚 Ronda 2 — Llegan el doble de pedidos de lo esperado**

Situación: Un pico de ventas hace que lleguen el doble de pedidos de lo esperado para hoy.

- A) Velocidad *(1 pt)*
- B) Calidad *(1 pt)*
- C) Organización del equipo *(2 pts — correcta)*

Explicación: Sin organizar la capacidad disponible primero, apurar todo o cuidar cada detalle termina perdiendo velocidad y calidad al mismo tiempo. Reorganizar el equipo primero permite sostener ambas cosas después. *Concepto clave: gestión de la capacidad antes que la urgencia.*

**👥 Ronda 3 — Faltó el 20% del personal**

Situación: Hoy faltó el 20% del personal, y hay que seguir despachando.

- A) Pedirle horas extra al resto del equipo *(1 pt)*
- B) Redistribuir tareas priorizando las estaciones que frenan todo el proceso *(2 pts — correcta)*
- C) Mantener el mismo plan del día y aceptar que se va a atrasar *(0 pts)*

Explicación: No todas las estaciones son igual de críticas. Si falta gente en la estación que es cuello de botella, ahí hay que concentrar los recursos. Pedir horas extra a ciegas puede reforzar una estación que no lo necesitaba. *Concepto clave: teoría de las restricciones.*

**📈 Ronda 4 — Reclamos porque los paquetes llegan tarde**

Situación: Empiezan a llegar reclamos de clientes porque muchos paquetes están llegando tarde.

- A) Tiempo de ciclo por pedido — cuánto tarda cada paquete en recorrer todo el proceso *(2 pts — correcta)*
- B) Cantidad total de paquetes despachados por día *(1 pt)*
- C) Costo operativo diario *(0 pts)*

Explicación: Si el problema es que llegan tarde, el indicador que explica eso es el tiempo de ciclo. El volumen total dice si se despacha mucho o poco, no dónde se generan las demoras. *Concepto clave: elegir el KPI correcto para cada problema.*

**♻️ Ronda 5 — Te piden reducir costos sin afectar al cliente**

Situación: La gerencia general pide bajar los costos operativos, sin que el cliente lo note.

- A) Bajar la calidad de los materiales de embalaje *(0 pts)*
- B) Optimizar rutas internas y eliminar tiempos muertos del proceso *(2 pts — correcta)*
- C) Despedir personal *(0 pts)*

Explicación: Bajar la calidad del embalaje o cortar personal de golpe sí afecta al cliente tarde o temprano. La forma de reducir costos sin que se note es sacarle tiempos muertos y recorridos innecesarios al proceso. *Concepto clave: mejora de procesos vs. recortar alcance o calidad.*

**🔍 Ronda 7 — Aumentan los errores de picking**

Situación: Empiezan a aumentar los errores al preparar los pedidos.

- A) Poner más cámaras para vigilar a los operarios *(0 pts)*
- B) Rediseñar el proceso de picking y capacitar en el nuevo método *(2 pts — correcta)*
- C) Sumar más personal de control de calidad al final de la línea *(1 pt)*

Explicación: Vigilar no arregla el proceso, y controlar al final detecta errores pero no evita que sigan ocurriendo. Rediseñar el proceso ataca la causa raíz. *Concepto clave: atacar la causa raíz, no solo controlar el síntoma.*

### 4.4 Rondas de decisión (sin respuesta única)

**💰 Ronda 6 — Solo alcanza para UNA mejora**

Situación: Tenés presupuesto para hacer una sola mejora este trimestre. ¿Cuál elegís?

- **A) Comprar más robots** — ✅ acelera el proceso y reduce errores manuales. ⚠️ inversión alta, no resuelve organización ni personal.
- **B) Capacitar a los empleados** — ✅ mejora calidad y motivación, costo relativamente bajo. ⚠️ resultados más lentos, depende de que el proceso ya esté bien diseñado.
- **C) Ampliar el depósito** — ✅ resuelve espacio y permite crecer. ⚠️ inversión muy alta, no soluciona nada operativo en lo inmediato.
- **D) Mejorar el software de gestión** — ✅ mejora visibilidad y planificación. ⚠️ requiere adaptación, no reemplaza mejoras físicas si el cuello de botella es de espacio o de gente.

Cierre: No hay respuesta correcta — depende del problema más urgente de la planta en ese momento. *(+1 pt automático)*

**🎄 Ronda 8 — Pico de fin de año**

Situación: Se viene el pico de pedidos más grande del año. ¿Cómo absorbés la demanda extra?

- **A) Horas extra al equipo actual** — ✅ rápido, sin curva de aprendizaje. ⚠️ cansancio del equipo, más errores si se extiende.
- **B) Contratar personal temporario** — ✅ suma capacidad real sin agotar al equipo estable. ⚠️ hay que capacitarlos rápido, rinden menos al principio.
- **C) Tercerizar parte de la operación** — ✅ capacidad casi inmediata. ⚠️ menos control de calidad, depende de un tercero.
- **D) Reducir temporalmente el mix de productos despachados** — ✅ simplifica el proceso, reduce errores. ⚠️ algunos clientes no encuentran ciertos productos durante el pico.

Cierre: Las empresas reales suelen combinar varias opciones a la vez — no existe una única forma correcta de absorber un pico. *(+1 pt automático)*

### 4.5 Ronda final

**🏆 Ronda 9 — El día antes de Navidad**

Situación: Último día antes de Navidad. Hay que despachar 50.000 paquetes, falta personal, se rompió una cinta y llegaron reclamos por demoras — todo junto. Solo podés tomar una acción inmediata.

- A) Identificar el cuello de botella actual y concentrar ahí todos los recursos *(3 pts — correcta)*
- B) Repartir el problema en partes iguales entre todas las estaciones *(1 pt)*
- C) Priorizar despachar rápido aunque se desordene el picking *(0 pts)*

Explicación: Repartir esfuerzos en partes iguales suena justo pero no es eficiente — hay una restricción que limita todo el sistema, y ahí hay que concentrarse primero. *Concepto clave: pensamiento sistémico — priorizar la restricción que más limita al conjunto.*

### 4.6 Pantalla final del juego

Mostrar: puntaje total (sobre 17), rango final alcanzado, un texto corto de cierre según el rango (igual que en la versión anterior: Operario/a, Supervisor/a, Coordinador/a, Gerente, Jefe/a de Planta), botón "Jugar de nuevo", y link "← Volver a Exploradores Industriales".

### 4.7 Notas de diseño (UI)

Pantalla única controlada por quien facilita, equipos votan a viva voz o levantando la mano. Botones grandes y táctiles. Barra de progreso de rango siempre visible. Contador de puntos. Indicador de ronda ("Ronda 3 de 9"). Etiqueta de tipo de ronda (🔍 Diagnóstico / ⚖️ Decisión / 🏆 Reto final). Al confirmar una opción se bloquean las demás, se resalta la elegida y aparece el panel de explicación (con ✅/🟡/❌ en rondas de diagnóstico; solo ventajas/desventajas en rondas de decisión). Animación breve al cruzar un umbral de rango nuevo. Archivo único autocontenido (HTML+CSS+JS embebido), sin dependencias externas, liviano y offline.

---

## 5. Actividad 3 — Consultores Industriales (`juegos/consultores.html`)

Esta actividad complementa una **dinámica presencial** que el equipo organizador ya hace en el evento (una simulación de consultoría/negociación en grupos). La parte web es simplemente la carga del resultado para sumarlo al puntaje total.

**Pantalla única:**

- Título: "Consultores Industriales"
- Texto: "Cargá el puesto en el que salió tu equipo en la dinámica de consultoría. 1° es el mejor puesto."
- Seis botones grandes, uno por puesto: **1°, 2°, 3°, 4°, 5°, 6°** (multiple choice, se selecciona uno solo).
- Al seleccionar un puesto se resalta el botón elegido y aparece un botón **"Confirmar resultado"**.
- Al confirmar:
  - Calcular puntos según esta tabla y guardarlos en `localStorage.setItem('exploradores_score_consultores', puntos)`:

  | Puesto | Puntos |
  |---|---|
  | 1° | 30 |
  | 2° | 25 |
  | 3° | 20 |
  | 4° | 15 |
  | 5° | 10 |
  | 6° | 5 |

  - Mostrar un mensaje corto de confirmación (ej: "¡Cargado! Sumaron 25 puntos como equipo.") y el link "← Volver a Exploradores Industriales".

**Estilo visual:** mantener la identidad neutra/institucional del hub (no necesita paleta propia como los otros dos juegos, es más una pantalla de carga de resultado que un juego en sí).

---

## 6. Actividad 4 — Trivia (`juegos/trivia.html`)

**Pantalla única:**

- Título: "Trivia Exploradores"
- Texto: "Jueguen esta trivia en equipo. Cuando terminen, vuelvan acá y cuenten cuántas respondieron bien para sumar los puntos."
- Botón grande: **"Abrir la trivia"**, que abre en una pestaña nueva:
  `https://kahoot.it/challenge/06844580?challenge-id=7e31b506-7a77-4ca6-831a-03fa1e117b35_1786128191783`
- Debajo, un formulario simple con dos campos numéricos:
  - "¿Cuántas respondieron bien?" (respuestas correctas)
  - "¿Cuántas preguntas tenía en total?" (total de preguntas)
- Botón **"Calcular puntos"**: valida que correctas ≤ total y ambos sean números positivos, calcula:
  ```
  puntos = Math.round((correctas / total) * 30)
  ```
  Guarda en `localStorage.setItem('exploradores_score_trivia', puntos)`, muestra el resultado ("Sumaron X puntos") y el link "← Volver a Exploradores Industriales".

**Nota:** como el Kahoot es una plataforma externa, no hay forma de leer el puntaje automáticamente desde el sitio — por eso el equipo lo carga a mano. Si en el futuro cambian el link del Kahoot, alcanza con reemplazar la URL del botón, no hace falta tocar nada más de esta pantalla.

---

## 7. Consideraciones técnicas generales (igual que antes + lo nuevo)

- Sin backend ni base de datos — todo corre en el navegador. El único estado que persiste entre páginas es el puntaje, vía `localStorage` con las claves de la sección 1.
- Todo el sitio debe verse bien en tablet/notebook horizontal, sin romperse en mobile.
- Botones grandes y táctiles en las cuatro actividades.
- Cada juego mantiene su propia identidad visual (ITBA Racing ≠ ClickGo ≠ hub ≠ pantallas de Consultores/Trivia, que son más neutras). El único elemento visual compartido entre todas las páginas es el link "← Volver a Exploradores Industriales" y, en el hub, el bloque de puntaje total.
- Ningún texto del sitio debe mencionar "Alpine" ni "Mercado Libre" — usar siempre "ITBA Racing" y "ClickGo".
