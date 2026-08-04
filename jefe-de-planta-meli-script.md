# Sos el Jefe de Planta de Mercado Libre
### Guión completo de la actividad — para pasar a Claude Code

---

## 1. Concepto y mecánica general

**Historia marco:** Es tu primer día como Jefe/a de Planta de un centro de distribución de Mercado Libre. Hoy hay que despachar **50.000 paquetes** y, como en cualquier operación real, van a ir surgiendo problemas. Los equipos (grupos de chicos) van votando qué harían en cada situación.

La actividad combina tres mecánicas en una sola experiencia:

1. **Rondas de diagnóstico** (la mayoría): plantean un problema real de operaciones, tienen una opción claramente mejor que las otras (aunque ninguna es "absurda"), y **después de votar se explica qué haría un ingeniero industrial y por qué**, nombrando el concepto detrás (cuello de botella, KPI, causa raíz, etc.).
2. **Sistema de ascenso**: arrancás como **Operario/a** y vas sumando puntos ronda a ronda. Al final, tu puntaje total te da un rango: Operario → Supervisor/a → Coordinador/a → Gerente → **Jefe/a de Planta**.
3. **Rondas de decisión** (2 en total): no hay una única respuesta correcta. Se muestra qué ventajas y desventajas tiene cada alternativa, y el mensaje pedagógico es que **en ingeniería industrial muchas veces no existe una sola solución válida** — importa poder justificar la decisión.

Total: **9 rondas** (7 de diagnóstico + 2 de decisión), más intro y pantalla final de resultados.

---

## 2. Sistema de puntos y rangos

- Rondas de diagnóstico normales (1, 2, 3, 4, 5, 7): la opción correcta da **2 puntos**, la intermedia **1 punto**, la débil **0 puntos**.
- Rondas de decisión (6 y 8): no puntúan por "correcto/incorrecto" — dan **1 punto fijo** por participar y reflexionar (se seleccione la opción que se seleccione).
- Ronda final (9, "El día antes de Navidad"): vale el doble — **3 / 1 / 0 puntos** — porque integra todo lo aprendido.

**Puntaje máximo posible: 17 puntos.**

| Puntos totales | Rango final |
|---|---|
| 0–4 | Operario/a |
| 5–8 | Supervisor/a |
| 9–11 | Coordinador/a |
| 12–14 | Gerente |
| 15–17 | **Jefe/a de Planta** |

Sugerencia de UI: mostrar una barra de progreso con los 5 rangos, y que el ícono/insignia del rango actual se actualice después de cada ronda (no solo al final), para que el grupo sienta el ascenso en tiempo real. Un pequeño efecto (confetti, "sonido" visual, badge que aparece) cuando se sube de rango.

---

## 3. Pantalla de inicio (intro)

**Título:** Sos el Jefe de Planta de Mercado Libre
**Texto:**
> Es tu primer día como Jefe/a de Planta en un centro de distribución de Mercado Libre. Hoy hay que despachar 50.000 paquetes. En cada ronda va a aparecer un problema real de la operación — tu equipo vota qué harían, y después vemos qué haría (y por qué) un ingeniero industrial de verdad.

Botón: **"Empezar mi primer día"**

Rango inicial visible: **Operario/a** (0 puntos).

---

## 4. Rondas de diagnóstico

### 📦 Ronda 1 — Se rompe una cinta transportadora

**Situación:** Se rompe una cinta transportadora en plena mañana. El flujo de paquetes hacia el sector de despacho se corta.

**¿Qué hacés?**
- A) Esperar a que mantenimiento la repare *(1 punto)*
- B) Reorganizar el flujo por otra línea *(2 puntos — correcta)*
- C) Frenar toda la operación *(0 puntos)*

**Explicación del ingeniero industrial:**
> Un ingeniero industrial diseña los procesos pensando en que algo se va a romper tarde o temprano. Por eso conviene tener **flexibilidad y rutas alternativas** (otras líneas, otros sectores) para no depender de un solo camino. Frenar todo paraliza la planta entera por un problema local; esperar sin más deja capacidad ociosa que se podría estar usando. Reorganizar el flujo mantiene la operación funcionando mientras se resuelve el problema real.
>
> **Concepto clave:** *Redundancia y flexibilidad de procesos.*

---

### 🚚 Ronda 2 — Llegan el doble de pedidos de lo esperado

**Situación:** Un pico de ventas hace que lleguen el doble de pedidos de lo esperado para hoy.

**¿Qué priorizás primero?**
- A) Velocidad *(1 punto)*
- B) Calidad *(1 punto)*
- C) Organización del equipo *(2 puntos — correcta)*

**Explicación del ingeniero industrial:**
> Ante una demanda inesperada, el primer instinto suele ser "apurar todo" o "cuidar cada detalle", pero sin **organizar la capacidad disponible** (quién hace qué, en qué orden, con qué recursos) terminás perdiendo velocidad Y calidad al mismo tiempo. Reorganizar el equipo primero permite sostener ambas cosas después.
>
> **Concepto clave:** *Gestión de la capacidad antes que la urgencia.*

---

### 👥 Ronda 3 — Faltó el 20% del personal

**Situación:** Hoy faltó el 20% del personal por distintos motivos, y hay que seguir despachando.

**¿Cómo reorganizás la operación?**
- A) Pedirle horas extra al resto del equipo *(1 punto)*
- B) Redistribuir tareas priorizando las estaciones que frenan todo el proceso *(2 puntos — correcta)*
- C) Mantener el mismo plan del día y aceptar que se va a atrasar *(0 puntos)*

**Explicación del ingeniero industrial:**
> No todas las estaciones de trabajo son igual de críticas: si falta gente en una estación que no frena el resto del proceso, no pasa gran cosa. Pero si falta en la estación que es **cuello de botella** (la que marca el ritmo de todo el sistema), ahí hay que concentrar los recursos. Pedir horas extra a ciegas puede terminar reforzando una estación que no lo necesitaba.
>
> **Concepto clave:** *Teoría de las restricciones — identificar el cuello de botella.*

---

### 📈 Ronda 4 — Reclamos porque los paquetes llegan tarde

**Situación:** Empiezan a llegar reclamos de clientes porque muchos paquetes están llegando tarde.

**¿Qué indicador mirarías primero para entender el problema?**
- A) Tiempo de ciclo por pedido — cuánto tarda cada paquete en recorrer todo el proceso *(2 puntos — correcta)*
- B) Cantidad total de paquetes despachados por día *(1 punto)*
- C) Costo operativo diario *(0 puntos)*

**Explicación del ingeniero industrial:**
> Si el problema es que **llegan tarde**, el indicador que explica eso es cuánto tiempo pasa cada pedido dentro del proceso (tiempo de ciclo). El volumen total te dice si estás despachando mucho o poco, pero no dónde se generan las demoras. El costo es importante, pero no está directamente relacionado con el reclamo puntual de los clientes.
>
> **Concepto clave:** *Elegir el KPI (indicador clave) correcto para cada problema.*

---

### ♻️ Ronda 5 — Te piden reducir costos sin afectar al cliente

**Situación:** La gerencia general pide bajar los costos operativos del centro de distribución, sin que el cliente lo note.

**¿Qué hacés?**
- A) Bajar la calidad de los materiales de embalaje *(0 puntos)*
- B) Optimizar rutas internas y eliminar tiempos muertos del proceso *(2 puntos — correcta)*
- C) Despedir personal *(0 puntos)*

**Explicación del ingeniero industrial:**
> Bajar la calidad del embalaje o cortar personal de golpe **sí afecta al cliente**, tarde o temprano (paquetes dañados, demoras, peor servicio). La forma de reducir costos sin que se note es sacarle "grasa" al proceso: tiempos muertos, recorridos innecesarios, movimientos que no agregan valor. Eso es directamente el trabajo de un ingeniero industrial.
>
> **Concepto clave:** *Mejora de procesos vs. recortar alcance o calidad.*

---

### 🔍 Ronda 7 — Aumentan los errores de picking

**Situación:** Empiezan a aumentar los errores al preparar los pedidos (mandan productos equivocados o incompletos).

**¿Qué hacés?**
- A) Poner más cámaras para vigilar a los operarios *(0 puntos)*
- B) Rediseñar el proceso de picking y capacitar en el nuevo método *(2 puntos — correcta)*
- C) Sumar más personal de control de calidad al final de la línea *(1 punto)*

**Explicación del ingeniero industrial:**
> Poner cámaras no arregla el proceso, solo vigila que falle de la misma manera. Agregar control al final **detecta** errores pero no evita que sigan ocurriendo (y cuesta más). Rediseñar el proceso ataca la **causa raíz** del problema: si el método de picking está mal diseñado, los errores van a seguir pasando hasta que se corrija.
>
> **Concepto clave:** *Atacar la causa raíz, no solo controlar el síntoma (poka-yoke).*

---

## 5. Rondas de decisión (sin respuesta única)

### 💰 Ronda 6 — Solo alcanza para UNA mejora

**Situación:** Tenés presupuesto para hacer **una sola** mejora este trimestre. ¿Cuál elegís?

- **A) Comprar más robots**
  ✅ Ventaja: acelera mucho el proceso y reduce errores manuales.
  ⚠️ Desventaja: inversión alta, no resuelve problemas de organización o de personal.
- **B) Capacitar a los empleados**
  ✅ Ventaja: mejora calidad y motivación con costo relativamente bajo.
  ⚠️ Desventaja: los resultados tardan más en verse, depende de que el proceso ya esté bien diseñado.
- **C) Ampliar el depósito**
  ✅ Ventaja: resuelve problemas de espacio y permite crecer a futuro.
  ⚠️ Desventaja: inversión muy alta y no soluciona nada operativo en lo inmediato.
- **D) Mejorar el software de gestión**
  ✅ Ventaja: mejora la visibilidad y planificación de toda la operación.
  ⚠️ Desventaja: requiere tiempo de adaptación del equipo y no reemplaza mejoras físicas si el cuello de botella es de espacio o de gente.

**Mensaje de cierre de la ronda:**
> No hay una respuesta "correcta" — depende de cuál sea el problema más urgente de la planta en ese momento. En ingeniería industrial, muchas veces la mejor decisión es "depende", y lo importante es poder justificarla con datos.

*(+1 punto automático por participar, sin importar la opción elegida)*

---

### 🎄 Ronda 8 — Pico de fin de año (Hot Sale / Navidad)

**Situación:** Se viene el pico de pedidos más grande del año. Tenés que decidir cómo absorber la demanda extra.

- **A) Horas extra al equipo actual**
  ✅ Ventaja: rápido de implementar, no hay curva de aprendizaje.
  ⚠️ Desventaja: cansancio del equipo, más errores si se extiende muchos días.
- **B) Contratar personal temporario**
  ✅ Ventaja: suma capacidad real sin agotar al equipo estable.
  ⚠️ Desventaja: hay que capacitarlos rápido, al principio rinden menos.
- **C) Tercerizar parte de la operación a un operador logístico externo**
  ✅ Ventaja: capacidad casi inmediata, sin contratar ni capacitar.
  ⚠️ Desventaja: menos control sobre la calidad del servicio, depende de un tercero.
- **D) Reducir temporalmente el mix de productos que se despachan**
  ✅ Ventaja: simplifica el proceso y reduce errores en el pico más exigente.
  ⚠️ Desventaja: algunos clientes no van a poder comprar ciertos productos durante el pico.

**Mensaje de cierre de la ronda:**
> Las empresas reales suelen combinar varias de estas opciones al mismo tiempo. No existe una única forma correcta de absorber un pico de demanda — existe la que mejor se ajusta a los recursos, el tiempo y el riesgo que la empresa está dispuesta a asumir.

*(+1 punto automático por participar)*

---

## 6. Ronda final — Reto integrador

### 🏆 Ronda 9 — El día antes de Navidad

**Situación:** Es el último día antes de Navidad. Hay que despachar 50.000 paquetes, falta personal, se rompió una cinta transportadora y llegaron reclamos por demoras — todo junto. Solo podés tomar **una** acción inmediata y prioritaria.

**¿Qué hacés?**
- A) Identificar cuál es el cuello de botella en este momento y concentrar ahí todos los recursos disponibles *(3 puntos — correcta)*
- B) Repartir el problema en partes iguales entre todas las estaciones *(1 punto)*
- C) Priorizar despachar rápido aunque se desordene el picking *(0 puntos)*

**Explicación del ingeniero industrial:**
> Cuando hay varios problemas a la vez, repartir esfuerzos "en partes iguales" suena justo pero **no es eficiente**: hay una restricción que está limitando todo el sistema, y es ahí donde hay que concentrarse primero. Despachar rápido sin orden genera más errores y más reclamos después. Un buen ingeniero industrial, bajo presión, no ataca todos los frentes a la vez — **prioriza el que más impacto tiene en el sistema completo.**
>
> **Concepto clave:** *Pensamiento sistémico — priorizar la restricción que más limita al conjunto.*

---

## 7. Pantalla final de resultados

Mostrar:
- Puntaje total obtenido (sobre 17).
- Rango final alcanzado (con su insignia).
- Un resumen corto de 1–2 líneas por rango (ver abajo), que conecte con la profesión real.
- Botón "Jugar de nuevo" (reinicia puntaje y rondas).

**Textos sugeridos por rango final:**

- **Operario/a:** "Hoy sobreviviste tu primer día — y eso ya es mucho. La ingeniería industrial se aprende resolviendo problemas reales, ronda tras ronda."
- **Supervisor/a:** "Empezás a ver los procesos con otros ojos: ya no solo apagás incendios, entendés por qué se producen."
- **Coordinador/a:** "Sabés priorizar y organizar recursos bajo presión — la mitad del trabajo de un ingeniero industrial es justamente eso."
- **Gerente:** "Tomás buenas decisiones con datos y pensás en el sistema completo, no solo en el problema del momento."
- **Jefe/a de Planta:** "Pensás como un ingeniero industrial: identificás restricciones, priorizás con criterio y sabés que a veces no hay una única respuesta correcta. Bienvenido/a al rol."

---

## 8. Notas de diseño para Claude Code

**Identidad visual:** paleta Mercado Libre — amarillo (#FFE600 aprox.) como color principal, azul (#3483FA aprox.) como acento, fondo neutro claro tipo depósito/almacén. Iconografía de logística: cajas, cintas transportadoras, changos/carritos, camiones.

**Formato de juego:** pantalla única controlada por quien facilita (docente/organizador), pensada para que los equipos voten a viva voz o con manos levantadas y una persona confirme la opción ganadora tocando el botón — no hace falta multijugador por dispositivo. Botones grandes, táctiles, pensados para tablet o notebook proyectada.

**Estructura de pantallas:**
1. Intro
2. Rondas 1 a 9 (cada una: situación → opciones → selección → feedback/explicación → botón "Siguiente ronda")
3. Resultado final

**Elementos de UI por ronda:**
- Barra de progreso de rango (Operario → Jefe de Planta) siempre visible, resaltando el rango actual.
- Contador de puntos.
- Indicador de ronda actual (ej. "Ronda 3 de 9").
- Etiqueta que distinga tipo de ronda: "🔍 Diagnóstico" vs "⚖️ Decisión" vs "🏆 Reto final", para que el grupo sepa si hay o no una respuesta "correcta".
- Al confirmar una opción: se bloquean los otros botones, se resalta la opción elegida, y aparece el panel de explicación con el ícono correspondiente (✅ correcta / 🟡 intermedia / ❌ débil para rondas de diagnóstico; sin marcar correcto/incorrecto para rondas de decisión, solo ventajas/desventajas de todas las opciones).
- Animación o resaltado breve cuando el puntaje cruza el umbral de un nuevo rango (ascenso).

**Tono de los textos:** directo, cercano, sin tecnicismos innecesarios — pensado para chicos de secundaria en una actividad grupal de un evento de difusión de Ingeniería Industrial (ITBA).
