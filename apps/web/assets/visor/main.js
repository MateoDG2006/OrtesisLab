/** Entrada del visor: orquesta tema, STL, escena y controles. */
import * as THREE from "/vendor/three-0.169.0.module.js";
import { observarTema, colorCss } from "/visor/tema.js";
import { origenPermitido, geometria, descargarStl } from "/visor/stl.js";
import { crearCamara } from "/visor/camara.js";
import { montarChrome, cablearPuntero, cablearTeclado, cablearResize } from "/visor/controles.js";

observarTema();

const aviso = document.createElement("p");
document.body.append(aviso);

function mostrarError(texto) {
  aviso.textContent = texto;
  aviso.classList.add("error");
}

const origenParam = new URLSearchParams(location.search).get("src");
const miniatura = new URLSearchParams(location.search).get("miniatura") === "1";

if (!origenParam) {
  mostrarError("Genere una ortesis para verla aquí.");
  throw new Error("sin malla");
}
if (!origenPermitido(origenParam)) {
  mostrarError("La URL de la malla no está permitida.");
  throw new Error("origen rechazado");
}

aviso.textContent = "Cargando malla…";

let buffer;
try {
  buffer = await descargarStl(origenParam);
} catch (error) {
  if (error.message === "timeout") {
    mostrarError("La descarga tardó demasiado.");
  } else if (error.message === "red") {
    mostrarError("No se pudo contactar con el almacén de archivos.");
  } else if (error.message === "http") {
    mostrarError(
      error.status === 404 || error.status === 403
        ? "El STL ya no está en el almacén. Vuelva a generar esta variante."
        : "No se pudo leer la malla generada.",
    );
  } else if (error.message === "grande") {
    mostrarError("El archivo supera el tamaño máximo permitido para la vista previa.");
  } else if (error.message === "corto") {
    mostrarError("El archivo no parece un STL binario válido.");
  } else {
    mostrarError("No se pudo leer la malla generada.");
  }
  throw error;
}

let malla;
try {
  malla = geometria(THREE, buffer);
} catch (error) {
  mostrarError("El STL no se pudo interpretar.");
  throw error;
}

aviso.remove();
const colorEscena = colorCss("--ol-scene", "#eef1f4");
const colorMalla = colorCss("--ol-mesh-mat", "#d5dbe3");
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(innerWidth, innerHeight);
document.body.append(renderer.domElement);

const scene = new THREE.Scene();
scene.background = new THREE.Color(colorEscena);
const camera = new THREE.PerspectiveCamera(35, innerWidth / innerHeight, 0.1, 5000);
scene.add(new THREE.AmbientLight(0xffffff, 0.55));
scene.add(new THREE.HemisphereLight(0xffffff, 0x8b95a1, 0.45));
const luz = new THREE.DirectionalLight(0xffffff, 1.15);
luz.position.set(0.6, 1, 1.4);
scene.add(luz);

const material = new THREE.MeshStandardMaterial({
  color: new THREE.Color(colorMalla),
  metalness: 0.04,
  roughness: 0.62,
  side: THREE.DoubleSide,
});
scene.add(new THREE.Mesh(malla, material));

const objetivo = new THREE.Vector3();
const { orbitar, zoom, reiniciar } = crearCamara(THREE, {
  esfera: malla.boundingSphere,
  camera,
  objetivo,
});

if (miniatura) {
  renderer.render(scene, camera);
  const imagen = new Image();
  imagen.alt = "Miniatura de la ortesis";
  imagen.src = renderer.domElement.toDataURL("image/png");
  imagen.style.cssText = "display:block;width:100%;height:100%;object-fit:contain";
  renderer.domElement.replaceWith(imagen);
  renderer.dispose();
  renderer.forceContextLoss();
} else {
  montarChrome();
}

cablearPuntero(renderer.domElement, { orbitar, zoom });
cablearTeclado({ orbitar, zoom, reiniciar });
cablearResize(camera, renderer, { miniatura });

function dibujar() {
  requestAnimationFrame(dibujar);
  renderer.render(scene, camera);
}
if (!miniatura) {
  dibujar();
}
