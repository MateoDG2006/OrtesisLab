/** Puntero, rueda y teclado de la cámara (sin botones en pantalla). */

export function montarChrome() {
  const hint = document.createElement("p");
  hint.className = "ol-visor-hint";
  hint.textContent = "Arrastre para orbitar · rueda para zoom · flechas / + − / Inicio";
  document.body.append(hint);
}

export function cablearPuntero(lienzo, { orbitar, zoom }) {
  let arrastre = false;
  let anterior = { x: 0, y: 0 };

  lienzo.addEventListener("pointerdown", (evento) => {
    arrastre = true;
    anterior = { x: evento.clientX, y: evento.clientY };
  });
  addEventListener("pointerup", () => { arrastre = false; });
  addEventListener("pointermove", (evento) => {
    if (!arrastre) return;
    orbitar((evento.clientX - anterior.x) * 0.008, (evento.clientY - anterior.y) * 0.008);
    anterior = { x: evento.clientX, y: evento.clientY };
  });
  lienzo.addEventListener("wheel", (evento) => {
    evento.preventDefault();
    zoom(evento.deltaY > 0 ? 1.08 : 0.92);
  }, { passive: false });
}

export function cablearTeclado({ orbitar, zoom, reiniciar }) {
  addEventListener("keydown", (evento) => {
    const paso = evento.shiftKey ? 0.03 : 0.01;
    switch (evento.key) {
      case "ArrowLeft":
        orbitar(-paso, 0);
        break;
      case "ArrowRight":
        orbitar(paso, 0);
        break;
      case "ArrowUp":
        orbitar(0, -paso);
        break;
      case "ArrowDown":
        orbitar(0, paso);
        break;
      case "+":
      case "=":
        zoom(0.92);
        break;
      case "-":
      case "_":
        zoom(1.08);
        break;
      case "Home":
        reiniciar();
        break;
      default:
        return;
    }
    evento.preventDefault();
  });
}

export function cablearResize(camera, renderer, { miniatura }) {
  addEventListener("resize", () => {
    if (miniatura) return;
    camera.aspect = innerWidth / innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(innerWidth, innerHeight);
  });
}
