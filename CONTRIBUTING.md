# Cómo trabajamos en DORSE HICK

## Ramas

Cada integrante debe trabajar en una rama propia y no realizar cambios directamente sobre `main`.

Las ramas se nombran según el tipo de trabajo:

* `feat/nombre-de-la-funcionalidad` para nuevas funcionalidades.
* `fix/nombre-del-error` para corregir errores.
* `docs/nombre-del-cambio` para documentación.
* `chore/nombre-del-cambio` para configuración y mantenimiento.

**Ejemplo:**

`feat/crear-login`

## Commits

Los commits deben escribirse en minúscula, en presente y siguiendo esta estructura:

`tipo: qué hiciste`

Tipos de commit:

* `feat`: nueva funcionalidad.
* `fix`: corrección de errores.
* `docs`: cambios en la documentación.
* `chore`: configuración y mantenimiento.

**Ejemplos:**

`feat: agregar formulario de registro`

`fix: corregir validación del usuario`

`docs: actualizar readme`

## Revisión de Pull Requests

Todo cambio debe enviarse mediante un Pull Request antes de integrarse a `main`.

Cada integrante debe revisar el trabajo de otro integrante del equipo.

Durante la revisión se debe verificar:

* Que el cambio cumpla con lo solicitado en el Issue.
* Que el código o documentación sea claro y esté organizado.
* Que no existan errores conocidos.
* Que se respeten las reglas del repositorio.
* Que no se hayan incluido contraseñas, claves, archivos `.env` u otra información sensible.

## Cuándo se aprueba un Pull Request

Un Pull Request puede ser aprobado cuando:

* Cumple con los requisitos establecidos en el Issue.
* Ha sido revisado por otro integrante del equipo.
* No presenta errores conocidos.
* Respeta la estructura del proyecto.
* Los commits siguen la convención establecida.
* No contiene información sensible.

Una vez aprobado, el Pull Request puede ser fusionado a `main`.
