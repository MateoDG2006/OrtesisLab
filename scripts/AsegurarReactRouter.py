"""En Windows, react-router.exe ignora --conditions=development.

Reflex hace bun install al compilar y ese paso regenera el .exe. bin.cjs
vuelve a lanzarse con el bun de Reflex y esa condición. Si el paquete aún
no está instalado, no hace nada.
"""

from pathlib import Path

MARCA = "ORTESISLAB_RR_OK"
BIN = (
    Path(__file__).resolve().parents[1]
    / "apps"
    / "web"
    / ".web"
    / "node_modules"
    / "@react-router"
    / "dev"
    / "bin.cjs"
)
GUARDIA = """if (process.env.ORTESISLAB_RR_OK !== "1") {
  const { spawn } = require("child_process");
  const fs = require("fs");
  const path = require("path");
  const localBun = path.join(process.env.LOCALAPPDATA || "", "reflex", "bun", "bin", "bun.exe");
  const bun = fs.existsSync(localBun) ? localBun : "bun";
  const child = spawn(bun, ["--conditions=development", __filename, ...process.argv.slice(2)], {
    stdio: "inherit",
    env: { ...process.env, ORTESISLAB_RR_OK: "1" },
  });
  child.on("exit", (code, signal) => {
    if (signal) process.kill(process.pid, signal);
    else process.exit(code == null ? 1 : code);
  });
  child.on("error", (error) => {
    console.error(error);
    process.exit(1);
  });
} else {
"""


def main() -> None:
    if not BIN.is_file():
        return
    texto = BIN.read_text(encoding="utf-8")
    if MARCA in texto:
        return
    lineas = texto.splitlines(keepends=True)
    if lineas and lineas[0].startswith("#!"):
        nuevo = [lineas[0], GUARDIA, *lineas[1:], "}\n"]
    else:
        nuevo = [GUARDIA, *lineas, "}\n"]
    BIN.write_text("".join(nuevo), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
