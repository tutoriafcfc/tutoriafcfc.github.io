from pathlib import Path
import re
import shutil

carpeta = Path.home() / "Documents" / "tutoriafcfc.github.io"
index = carpeta / "index.html"
respaldo = carpeta / "index-respaldo-final.html"
servicios = carpeta / "servicios.html"

if not index.exists():
    raise SystemExit("No se encontró index.html")

if not respaldo.exists():
    shutil.copy2(index, respaldo)

html = index.read_text(encoding="utf-8")

enlaces = {
    "Tutoría académica": "tutoria",
    "Organización del tiempo": "organizacion",
    "Técnicas de estudio": "tecnicas",
    "Bienestar y orientación": "bienestar",
    "Vida universitaria": "vida",
    "Desarrollo profesional": "desarrollo",
}

for titulo, destino in enlaces.items():
    patron = re.compile(
        r'<article class="servicio">(?P<cuerpo>.*?<h3>\s*'
        + re.escape(titulo)
        + r'\s*</h3>.*?)</article>',
        re.IGNORECASE | re.DOTALL,
    )

    html, cantidad = patron.subn(
        lambda coincidencia: (
            f'<a class="servicio" href="servicios.html#{destino}">'
            f'{coincidencia.group("cuerpo")}'
            f'<span class="ver-mas">Conocer más →</span>'
            f'</a>'
        ),
        html,
        count=1,
    )

    print(
        f"{'✓' if cantidad else '⚠'} {titulo}: "
        f"{'enlazada' if cantidad else 'no encontrada'}"
    )

estilos = """
/* TARJETAS INTERACTIVAS */
.servicio {
  display: block;
  color: inherit;
  text-decoration: none;
  cursor: pointer;
  transition: transform .25s ease, box-shadow .25s ease;
}

.servicio:hover {
  transform: translateY(-6px);
  box-shadow: 0 18px 38px rgba(32, 12, 20, .16);
}

.ver-mas {
  display: inline-block;
  margin-top: 16px;
  color: var(--vino);
  font-weight: 800;
}
"""

if "TARJETAS INTERACTIVAS" not in html:
    html = html.replace("</style>", estilos + "\n</style>", 1)

index.write_text(html, encoding="utf-8")

pagina = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Servicios | FCFC Contigo</title>

<style>
:root {
  --vino:#721630;
  --vino-oscuro:#3d0917;
  --dorado:#e1aa37;
  --fondo:#f5f6f8;
  --blanco:#fff;
  --texto:#202124;
  --gris:#62666d;
}

* {
  box-sizing:border-box;
  margin:0;
  padding:0;
}

html {
  scroll-behavior:smooth;
  scroll-padding-top:90px;
}

body {
  font-family:Arial,Helvetica,sans-serif;
  color:var(--texto);
  background:var(--fondo);
  line-height:1.7;
}

a {
  text-decoration:none;
}

.contenedor {
  width:min(1100px,90%);
  margin:auto;
}

header {
  position:sticky;
  top:0;
  z-index:100;
  background:var(--blanco);
  border-bottom:1px solid #ddd;
}

.barra {
  min-height:76px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:20px;
}

.marca {
  display:flex;
  align-items:center;
  gap:12px;
  color:var(--vino);
}

.marca img {
  width:56px;
  height:56px;
  object-fit:contain;
}

.volver,
.boton {
  display:inline-flex;
  align-items:center;
  justify-content:center;
  padding:13px 19px;
  border-radius:11px;
  font-weight:800;
}

.volver,
.secundario {
  color:var(--blanco);
  background:var(--vino);
}

.principal {
  color:#251800;
  background:var(--dorado);
}

.portada {
  padding:80px 0;
  color:var(--blanco);
  background:linear-gradient(135deg,var(--vino-oscuro),var(--vino));
}

.portada h1 {
  font-size:clamp(2.5rem,7vw,5rem);
  margin-bottom:12px;
}

.portada p {
  max-width:760px;
  color:#f2e4e8;
}

.indice {
  padding:25px 0;
  background:var(--vino-oscuro);
}

.indice-grid {
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:11px;
}

.indice a {
  padding:12px;
  border-radius:10px;
  color:var(--blanco);
  background:rgba(255,255,255,.09);
  text-align:center;
  font-weight:700;
}

main {
  padding:60px 0;
}

.detalle {
  margin-bottom:28px;
  padding:34px;
  border-top:6px solid var(--vino);
  border-radius:20px;
  background:var(--blanco);
  box-shadow:0 12px 32px rgba(0,0,0,.10);
}

.titulo {
  display:flex;
  align-items:center;
  gap:16px;
  margin-bottom:18px;
}

.icono {
  width:62px;
  height:62px;
  display:grid;
  place-items:center;
  border-radius:16px;
  background:#f8e9ed;
  font-size:2rem;
}

h2 {
  color:var(--vino-oscuro);
  font-size:clamp(1.7rem,4vw,2.5rem);
}

h3 {
  margin:22px 0 8px;
  color:var(--vino);
}

p,
li {
  color:var(--gris);
}

ul {
  margin:12px 0 0 23px;
}

.acciones {
  display:flex;
  flex-wrap:wrap;
  gap:12px;
  margin-top:24px;
}

footer {
  padding:38px 0;
  color:var(--blanco);
  background:#220810;
  text-align:center;
}

@media (max-width:700px) {
  .indice-grid {
    grid-template-columns:1fr;
  }

  .detalle {
    padding:24px;
  }

  .acciones {
    flex-direction:column;
  }

  .boton {
    width:100%;
  }
}
</style>
</head>

<body>

<header>
  <div class="contenedor barra">
    <a class="marca" href="index.html">
      <img src="logo-fcfc.png" alt="Logotipo de la FCFC">
      <strong>FCFC CONTIGO</strong>
    </a>

    <a class="volver" href="index.html">← Inicio</a>
  </div>
</header>

<section class="portada">
  <div class="contenedor">
    <h1>Servicios de orientación</h1>
    <p>
      Información y recomendaciones para acompañarte durante
      tu formación universitaria.
    </p>
  </div>
</section>

<nav class="indice">
  <div class="contenedor indice-grid">
    <a href="#tutoria">Tutoría académica</a>
    <a href="#organizacion">Organización del tiempo</a>
    <a href="#tecnicas">Técnicas de estudio</a>
    <a href="#bienestar">Bienestar y orientación</a>
    <a href="#vida">Vida universitaria</a>
    <a href="#desarrollo">Desarrollo profesional</a>
  </div>
</nav>

<main>
<div class="contenedor">

<section class="detalle" id="tutoria">
  <div class="titulo">
    <div class="icono">📘</div>
    <h2>Tutoría académica</h2>
  </div>

  <p>
    Acompañamiento para fortalecer el desempeño académico,
    identificar dificultades y organizar acciones de mejora.
  </p>

  <h3>Puede ayudarte ante:</h3>
  <ul>
    <li>Bajo rendimiento o desaprobación de cursos.</li>
    <li>Dificultades para planificar el semestre.</li>
    <li>Inseguridad frente a evaluaciones.</li>
    <li>Desmotivación o problemas de adaptación.</li>
  </ul>

  <div class="acciones">
    <a class="boton principal"
       href="https://chatgpt.com/g/g-6a45ad08e1348191a7600234f1895835-fcfc-contigo"
       target="_blank">
       💬 Recibir orientación
    </a>

    <a class="boton secundario"
       href="https://docs.google.com/forms/d/e/1FAIpQLScdgNAwApUS2p-DU-6qQPlByoEqDpDYwaNtJwuup33QeEvVyA/viewform"
       target="_blank">
       📅 Solicitar tutoría
    </a>
  </div>
</section>

<section class="detalle" id="organizacion">
  <div class="titulo">
    <div class="icono">⏰</div>
    <h2>Organización del tiempo</h2>
  </div>

  <p>
    Estrategias para equilibrar clases, estudio, trabajo,
    descanso y responsabilidades personales.
  </p>

  <h3>Acciones recomendadas:</h3>
  <ul>
    <li>Registrar los horarios fijos.</li>
    <li>Priorizar las actividades importantes.</li>
    <li>Dividir tareas grandes en acciones pequeñas.</li>
    <li>Planificar y revisar la semana.</li>
  </ul>

  <div class="acciones">
    <a class="boton principal"
       href="https://chatgpt.com/g/g-6a45ad08e1348191a7600234f1895835-fcfc-contigo"
       target="_blank">
       ⏰ Crear mi plan semanal
    </a>
  </div>
</section>

<section class="detalle" id="tecnicas">
  <div class="titulo">
    <div class="icono">📝</div>
    <h2>Técnicas de estudio</h2>
  </div>

  <p>
    Métodos para comprender, repasar y recordar mejor los contenidos.
  </p>

  <h3>Estrategias:</h3>
  <ul>
    <li>Método Pomodoro.</li>
    <li>Lectura comprensiva y resúmenes.</li>
    <li>Mapas conceptuales.</li>
    <li>Repaso espaciado.</li>
    <li>Autoevaluación con preguntas y ejercicios.</li>
  </ul>

  <div class="acciones">
    <a class="boton principal"
       href="https://chatgpt.com/g/g-6a45ad08e1348191a7600234f1895835-fcfc-contigo"
       target="_blank">
       📝 Elegir una técnica
    </a>
  </div>
</section>

<section class="detalle" id="bienestar">
  <div class="titulo">
    <div class="icono">🧠</div>
    <h2>Bienestar y orientación</h2>
  </div>

  <p>
    Orientación inicial ante estrés académico, desmotivación,
    ansiedad por evaluaciones o dificultades de adaptación.
  </p>

  <h3>Temas de orientación:</h3>
  <ul>
    <li>Estrés y preocupación académica.</li>
    <li>Desmotivación.</li>
    <li>Equilibrio entre estudio y trabajo.</li>
    <li>Organización personal.</li>
    <li>Adaptación universitaria.</li>
  </ul>

  <div class="acciones">
    <a class="boton principal"
       href="https://chatgpt.com/g/g-6a45ad08e1348191a7600234f1895835-fcfc-contigo"
       target="_blank">
       🧠 Conversar sobre mi situación
    </a>
  </div>
</section>

<section class="detalle" id="vida">
  <div class="titulo">
    <div class="icono">🏫</div>
    <h2>Vida universitaria</h2>
  </div>

  <p>
    Recomendaciones para facilitar la integración, participación
    y adaptación a la comunidad universitaria.
  </p>

  <h3>Te recomendamos:</h3>
  <ul>
    <li>Participar en actividades académicas.</li>
    <li>Conocer a docentes y compañeros.</li>
    <li>Formar grupos de estudio responsables.</li>
    <li>Utilizar los servicios de orientación.</li>
  </ul>
</section>

<section class="detalle" id="desarrollo">
  <div class="titulo">
    <div class="icono">💼</div>
    <h2>Desarrollo profesional</h2>
  </div>

  <p>
    Orientación inicial para fortalecer competencias personales
    y profesionales.
  </p>

  <h3>Áreas:</h3>
  <ul>
    <li>Currículum vitae.</li>
    <li>Preparación para entrevistas.</li>
    <li>Comunicación profesional.</li>
    <li>Liderazgo y trabajo en equipo.</li>
    <li>Ética y habilidades blandas.</li>
  </ul>

  <div class="acciones">
    <a class="boton principal"
       href="https://chatgpt.com/g/g-6a45ad08e1348191a7600234f1895835-fcfc-contigo"
       target="_blank">
       💼 Recibir orientación
    </a>
  </div>
</section>

</div>
</main>

<footer>
  <div class="contenedor">
    <strong>FCFC Contigo</strong>
    <p>Oficina de Tutoría y Psicopedagogía</p>
    <p>Facultad de Ciencias Financieras y Contables</p>
    <p>Universidad Nacional Federico Villarreal</p>
  </div>
</footer>

</body>
</html>
"""

servicios.write_text(pagina, encoding="utf-8")

print("✓ Respaldo creado")
print("✓ Seis tarjetas convertidas en enlaces")
print("✓ servicios.html creado")
print("✓ Portal interactivo terminado")