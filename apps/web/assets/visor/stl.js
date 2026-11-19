/** Carga y parseo de STL binario para el visor. */

export const LIMITE_BYTES = 64 * 1024 * 1024;

export function origenPermitido(url) {
  try {
    const parsed = new URL(url, location.origin);
    if (parsed.protocol !== "http:" && parsed.protocol !== "https:") {
      return false;
    }
    if (parsed.origin === location.origin) {
      return true;
    }
    return /\/usuarios\/[0-9a-f-]{36}\/assets\/[0-9a-f-]{36}\.stl(?:\?|$)/i.test(parsed.pathname + parsed.search);
  } catch {
    return false;
  }
}

export function geometria(THREE, buf) {
  const vista = new DataView(buf);
  const caras = vista.getUint32(80, true);
  const bytesNecesarios = 84 + caras * 50;
  if (bytesNecesarios > buf.byteLength) {
    throw new Error("cabecera STL inconsistente");
  }
  const posiciones = new Float32Array(caras * 9);
  let cursor = 84;
  let escrito = 0;
  for (let cara = 0; cara < caras; cara += 1) {
    cursor += 12;
    for (let componente = 0; componente < 9; componente += 1) {
      posiciones[escrito] = vista.getFloat32(cursor, true);
      escrito += 1;
      cursor += 4;
    }
    cursor += 2;
  }
  const malla = new THREE.BufferGeometry();
  malla.setAttribute("position", new THREE.BufferAttribute(posiciones, 3));
  malla.computeVertexNormals();
  malla.computeBoundingSphere();
  return malla;
}

export async function descargarStl(url) {
  const controlador = new AbortController();
  const temporizador = setTimeout(() => controlador.abort(), 120000);
  let respuesta;
  try {
    respuesta = await fetch(url, { signal: controlador.signal });
  } catch (error) {
    const abortado = controlador.signal.aborted;
    const err = new Error(abortado ? "timeout" : "red");
    err.cause = error;
    throw err;
  } finally {
    clearTimeout(temporizador);
  }

  if (!respuesta.ok) {
    const err = new Error("http");
    err.status = respuesta.status;
    throw err;
  }

  const longitud = Number(respuesta.headers.get("content-length") || 0);
  if (longitud > LIMITE_BYTES) {
    throw new Error("grande");
  }

  const buffer = await respuesta.arrayBuffer();
  if (buffer.byteLength > LIMITE_BYTES) {
    throw new Error("grande");
  }
  if (buffer.byteLength < 84) {
    throw new Error("corto");
  }
  return buffer;
}
