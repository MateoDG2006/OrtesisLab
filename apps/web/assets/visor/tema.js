/** Tema claro/oscuro del documento del visor (host Reflex o prefers-color-scheme). */

export function oscuroActivo() {
  try {
    if (parent?.document?.documentElement?.classList?.contains("dark")) {
      return true;
    }
  } catch (_) {
    /* cross-origin o sin parent */
  }
  const forzado = document.documentElement.getAttribute("data-theme");
  if (forzado === "dark") return true;
  if (forzado === "light") return false;
  return matchMedia("(prefers-color-scheme: dark)").matches;
}

export function aplicarTemaDocumento() {
  document.documentElement.classList.toggle("dark", oscuroActivo());
}

export function observarTema() {
  aplicarTemaDocumento();
  try {
    const obs = new MutationObserver(aplicarTemaDocumento);
    obs.observe(parent.document.documentElement, { attributes: true, attributeFilter: ["class"] });
  } catch (_) {
    matchMedia("(prefers-color-scheme: dark)").addEventListener("change", aplicarTemaDocumento);
  }
}

export function colorCss(nombre, fallback) {
  return getComputedStyle(document.documentElement).getPropertyValue(nombre).trim() || fallback;
}
