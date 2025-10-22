# 📘 Proyecto `uade-progra-1`

<p align="center">
<img src= "./CinePlayLogo.png" alt="Cine Play Logo" width="200"/>
</p>

---

## Integrantes

- **HERNANDEZ ANDREA**
- **DO REGO GUIDO**
- **FORTEZ JUAN IGNACIO**
- **LANIERE LEONARDO**

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

1. Instalar el hook de Git usando esa configuración:

```bash
   python3 -m pre_commit install --config .husky/pre-commit.yaml
```

## Descripcion del proyecto

Este proyecto simula la gestión de un cine.  
Cuenta con dos funciones principales: una para la
**administración de la sala** (definición de filas, columnas y nombre de la sala) y otra para el **uso de clientes**, quienes pueden comprar entradas y elegir sus asientos.

---

## Funcionalidades

### 🔹 Interfaz Administrador

- Cargar una nueva sala de cine.
- Definir la cantidad de filas y columnas de la sala.
- Asignar una pelicula a la sala.
- Visualizar el estado de los asientos (disponibles/ocupados).

### 🔹 Intefaz Cliente

- Ver la sala y los asientos disponibles.
- Comprar entradas seleccionando la cantidad deseada.
- Elegir asientos específicos dentro de la sala.
- Confirmar la compra (los asientos pasan a estar ocupados).

---

### Estructura d

```
├── 📁 constants/                  # Configuración del sistema
│   └── index.py
├── 📁 core/                       # Lógica principal de aplicación
│   ├── application.py             # Clase principal de la aplicación
│   ├── error_handler.py           # Manejo centralizado de errores
│   └── execution_modes.py         # Modos de ejecución
├── 📁 interface/                  # Interfaz de usuario refactorizada
│   ├── 📁 core/                   # Lógica de negocio pura
│   │   ├── hall_operations.py     # Operaciones de salas
│   │   └── ticket_operations.py   # Operaciones de tickets
│   ├── 📁 execution/              # Flujos de ejecución
│   │   ├── admin_flow.py          # Flujo de administración
│   │   ├── user_flow.py           # Flujo de usuario
│   │   ├── hall_admin_flow.py     # Flujo de admin de salas
│   │   └── ticket_flow.py         # Flujo de compra
│   ├── 📁 ui/                     # Interfaz de usuario pura
│   │   ├── display.py             # Solo mostrar datos
│   │   └── input.py               # Solo pedir datos
│   ├── 📁 view/                   # (Existente) Utilidades de vista
│   ├── 📁 seats/                  # (Existente) Utilidades de asientos
│   ├── 📁 halls/                  # (Existente) Utilidades de salas
│   └── *.py                       # Interfaces principales refactorizadas
├── 📁 tools/                      # (Existente) Herramientas del sistema
│   ├── halls/, seats/, view/      # Utilidades existentes
│   └── *.py                       # Utilidades de archivos y validación
├── 📄 main.py                     # Punto de entrada limpio
├── 📄 custom_types.py             # Tipos de datos del sistema
```
