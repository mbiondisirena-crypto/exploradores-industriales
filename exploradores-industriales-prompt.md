# Prompt para Claude Code — "Exploradores Industriales: Viví la ingeniería jugando"

Copiá este documento (o pegalo directo en el chat de Claude Code) junto con los dos archivos ya generados:
- `alpine-boxes.html` (juego de Alpine / Colapinto, ya funcional, no hace falta rehacerlo)
- `jefe-de-planta-meli-script.md` (guión completo del juego de Mercado Libre, todavía sin construir)

---

## Encargo

Quiero que armes un sitio web llamado **"Exploradores Industriales: Viví la ingeniería jugando"**. Es un hub para un evento de difusión de Ingeniería Industrial del ITBA dirigido a chicos de secundaria. Desde la página principal se accede a dos juegos educativos independientes:

1. **Boxes de Alpine — Preparen el auto de Colapinto** (ya está construido en `alpine-boxes.html`, hay que integrarlo tal cual, respetando su lógica y estilo).
2. **Jefe de Planta de Mercado Libre** (todavía no existe — hay que construirlo desde cero siguiendo el guión de `jefe-de-planta-meli-script.md` punto por punto: las 9 rondas, el sistema de puntos y ascenso, y las notas de diseño de la sección 8 de ese documento).

---

## Estructura del sitio

```
/
├── index.html                 → Landing "Exploradores Industriales"
├── juegos/
│   ├── alpine-boxes.html      → Juego 1 (integrar el archivo existente)
│   └── jefe-de-planta.html    → Juego 2 (construir nuevo)
├── assets/
│   └── (imágenes, íconos, fuentes compartidas si hacen falta)
└── styles/
    └── shared.css             → estilos comunes al hub (header, footer, tipografía institucional)
```

Cada juego debe tener, arriba de todo, un link chico para **"← Volver a Exploradores Industriales"** que lleve al `index.html`.

---

## Landing page (`index.html`)

**Objetivo:** que un grupo de chicos de secundaria entienda en 5 segundos qué pueden jugar y elija uno de los dos.

**Contenido:**

- **Header/Hero:**
  - Título: "Exploradores Industriales"
  - Bajada: "Viví la ingeniería jugando"
  - Texto corto (2-3 líneas) explicando que la Ingeniería Industrial se trata de resolver problemas reales de procesos, decisiones y organización — y que estos dos juegos simulan situaciones reales de una fábrica de autos de carrera y de un centro de distribución.
  - Marca institucional del ITBA visible pero sin opacar el tono lúdico (usar el nombre "ITBA — Ingeniería Industrial" en el header o footer).

- **Dos tarjetas de juego** (lado a lado en desktop, apiladas en mobile/tablet), cada una con:
  - Nombre del juego.
  - 1-2 líneas describiendo de qué se trata.
  - Un tag corto de qué habilidad de ingeniería industrial pone en juego.
  - Botón grande "Jugar".

  **Tarjeta 1 — Boxes de Alpine:**
  - Nombre: "Boxes de Alpine: Preparen el auto de Colapinto"
  - Descripción: "Sos el ingeniero del box. Organizá el cronograma de construcción del auto de Franco Colapinto antes de la clasificación."
  - Tag: "Planificación de proyectos y precedencias"
  - Link: `juegos/alpine-boxes.html`

  **Tarjeta 2 — Jefe de Planta MELI:**
  - Nombre: "Sos el Jefe de Planta de Mercado Libre"
  - Descripción: "Tu primer día al mando de un centro de distribución. 50.000 paquetes por despachar y un montón de decisiones bajo presión."
  - Tag: "Toma de decisiones y resolución de problemas"
  - Link: `juegos/jefe-de-planta.html`

- **Footer:** crédito institucional simple ("Ingeniería Industrial — ITBA") y, opcionalmente, un texto tipo "Actividad pensada para trabajar en equipo — elijan un juego y decidan en grupo".

---

## Identidad visual del hub (landing + navegación compartida)

El hub necesita su propia identidad — **no debe copiar la paleta de ninguno de los dos juegos** (Alpine usa azul/rosa de F1, MELI va a usar amarillo/azul de Mercado Libre). Usar algo distintivo, con espíritu "ITBA / exploración / ingeniería", por ejemplo tonos institucionales del ITBA combinados con acentos que se sientan lúdicos (no un sitio corporativo aburrido, pero tampoco compite visualmente con las tarjetas de cada juego). Las tarjetas de cada juego sí pueden anticipar sutilmente su paleta (un borde o ícono con el color de cada juego) para que se note que son experiencias distintas.

Tipografía clara y grande, pensada para pantallas de tablet/notebook proyectadas en un evento, no para lectura larga en escritorio.

---

## Juego 1 — Boxes de Alpine (integración)

- Tomar el archivo `alpine-boxes.html` tal cual está y ubicarlo en `juegos/alpine-boxes.html`.
- Agregarle únicamente el link de vuelta al hub ("← Volver a Exploradores Industriales") en la esquina superior, sin tocar el resto de su diseño ni su lógica de juego (ya está probado y funcionando: precedencias, cronómetro, secuencia de luces, sistema de estrellas).

---

## Juego 2 — Jefe de Planta de Mercado Libre (construir desde cero)

Seguir el archivo `jefe-de-planta-meli-script.md` como especificación completa:

- **Contenido exacto de las 9 rondas** (situación, opciones, puntos por opción, texto de explicación del ingeniero industrial) tal como está escrito en las secciones 4, 5 y 6 del guión — no resumir ni inventar contenido nuevo, usar el texto ya redactado.
- **Sistema de puntos y rangos** de la sección 2 (tabla de umbrales 0-4 / 5-8 / 9-11 / 12-14 / 15-17).
- **Pantalla de inicio** con el texto de la sección 3.
- **Pantalla final** con el resumen de rango de la sección 7.
- **Notas de diseño de la sección 8**: paleta Mercado Libre (amarillo/azul), formato de pantalla única controlada por quien facilita (no multijugador por dispositivo), estructura de pantallas, comportamiento de la UI en cada ronda (barra de progreso de rango siempre visible, contador de puntos, indicador de ronda, etiqueta de tipo de ronda, bloqueo de opciones al confirmar, feedback visual, animación de ascenso de rango).

Construirlo como un único archivo HTML autocontenido (HTML + CSS + JS embebido), del mismo estilo técnico que `alpine-boxes.html` — sin frameworks ni dependencias externas más allá de una fuente web si hace falta, para que sea liviano y funcione offline en el evento.

---

## Consideraciones técnicas generales

- Todo el sitio debe verse bien en tablet/notebook horizontal (es el formato principal del evento), pero que no se rompa en mobile.
- Sin necesidad de backend ni base de datos — todo corre en el navegador, estado en memoria (JS), sin login ni persistencia entre sesiones.
- Botones grandes y táctiles en ambos juegos, pensados para que un facilitador toque la pantalla frente al grupo.
- Cuidar que cada juego mantenga su propia identidad visual (Alpine ≠ Mercado Libre ≠ hub), y que el link de "volver" sea el único elemento visual compartido entre todos.
