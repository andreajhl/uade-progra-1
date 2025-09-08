# 📘 Proyecto `uade-progra-1`

---

## Requisitos

- **Python 3.11+** (recomendado usar la misma versión en todo el equipo).
- **pip** actualizado:
  ```bash
  python3 -m pip install --upgrade pip
  ```

## Instalación de dependencias
  Instalar Black y pre-commit como dependencias de desarrollo:

  ```
    python3 -m pip install black pre-commit
  ```

## Primeros pasos
  Este proyecto guarda la configuración en .husky/pre-commit.yaml.

1.	Instalar el hook de Git usando esa configuración:

 ``` bash
    python3 -m pre_commit install --config .husky/pre-commit.yaml
  ```
