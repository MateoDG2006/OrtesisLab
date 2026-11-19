/** Cámara esférica alrededor del bounding sphere de la malla. */

export function crearCamara(THREE, { esfera, camera, objetivo }) {
  const esferica = { radio: 1, theta: 0.6, phi: 1.05 };
  const inicial = { theta: 0.6, phi: 1.05, radio: 1 };

  objetivo.copy(esfera.center);
  esferica.radio = Math.max(esfera.radius * 2.4, 1);
  inicial.radio = esferica.radio;
  camera.near = esfera.radius / 100;
  camera.far = esfera.radius * 30;
  camera.updateProjectionMatrix();

  function encuadrar() {
    const desplazamiento = new THREE.Vector3(
      Math.sin(esferica.phi) * Math.cos(esferica.theta),
      Math.cos(esferica.phi),
      Math.sin(esferica.phi) * Math.sin(esferica.theta),
    ).multiplyScalar(esferica.radio);
    camera.position.copy(objetivo).add(desplazamiento);
    camera.lookAt(objetivo);
  }

  function orbitar(dTheta, dPhi) {
    esferica.theta += dTheta;
    esferica.phi = Math.min(Math.max(esferica.phi + dPhi, 0.15), Math.PI - 0.15);
    encuadrar();
  }

  function zoom(factor) {
    esferica.radio = Math.min(
      Math.max(esferica.radio * factor, esfera.radius * 0.4),
      esfera.radius * 12,
    );
    encuadrar();
  }

  function reiniciar() {
    esferica.theta = inicial.theta;
    esferica.phi = inicial.phi;
    esferica.radio = inicial.radio;
    encuadrar();
  }

  encuadrar();
  return { encuadrar, orbitar, zoom, reiniciar, esferica };
}
