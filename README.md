# 🏦 Procesador Bancario Batch - COBOL

Un sistema moderno de procesamiento batch para actualización de saldos bancarios. Implementado en **COBOL** con interfaz gráfica en **Python** (Tkinter).

[![Estado](https://img.shields.io/badge/estado-activo-success.svg)](https://github.com)
[![COBOL](https://img.shields.io/badge/COBOL-GnuCOBOL%203.2-blue.svg)](https://www.gnu-cobol.org)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org)
[![Licencia](https://img.shields.io/badge/licencia-MIT-green.svg)](LICENSE)

## 📋 Descripción

Este proyecto implementa un procesador bancario batch que:
- **Lee** un archivo maestro con cuentas bancarias
- **Procesa** transacciones diarias (depósitos y retiros)
- **Actualiza** los saldos de las cuentas
- **Genera** reportes con los resultados finales

Está disponible en dos versiones:
1. **Versión COBOL puro** (compilable con GnuCOBOL)
2. **Versión con interfaz Python** (Tkinter) para facilidad de uso

## ✨ Características

✅ **Interfaz Gráfica Intuitiva**
- 4 pestañas funcionales
- Búsqueda de cuentas en tiempo real
- Visualización de datos en tablas interactivas

✅ **Gestión de Movimientos**
- Agregar depósitos y retiros
- Validación automática de datos
- Procesamiento batch de movimientos

✅ **Reportes Profesionales**
- Generación de reportes formateados
- Exportación a archivos de texto
- Información de saldos finales

✅ **Implementación Dual**
- Código COBOL puro compilable
- Interfaz Python amigable
- Procesamiento eficiente

## 🚀 Inicio Rápido

### Requisitos

- **Para la interfaz Python:**
  - Python 3.8 o superior
  - tkinter (incluido con Python)

- **Para compilar COBOL:**
  - GnuCOBOL 3.2+
  - MinGW (en Windows)

### Instalación

#### Opción 1: Interfaz Python (Recomendado)

1. **Instalar Python** (si no lo tienes)
   ```bash
   # Windows - Microsoft Store
   # Busca "Python" en la Windows Store
   
   # O descarga de python.org
   # https://www.python.org/downloads/
   ```

2. **Clonar el repositorio**
   ```bash
   git clone https://github.com/usuario/procesador-bancario-cobol.git
   cd procesador-bancario-cobol
   ```

3. **Ejecutar la interfaz**
   ```bash
   python interfaz.py
   ```

#### Opción 2: Compilar COBOL

1. **Instalar GnuCOBOL**
   ```bash
   # Windows: Descargar de https://www.gnu-cobol.org/download/
   # Linux: sudo apt-get install gnucobol
   # macOS: brew install gnu-cobol
   ```

2. **Compilar el programa**
   ```bash
   cobc -x procesador_simple.cbl -o procesador
   ```

3. **Ejecutar**
   ```bash
   procesador
   ```

## 📁 Estructura del Proyecto

```
procesador-bancario-cobol/
├── README.md                    # Este archivo
├── interfaz.py                  # Interfaz gráfica Python
├── interfaz.html                # Versión web (alternativa)
│
├── procesador.cbl               # Programa COBOL original
├── procesador_simple.cbl        # Programa COBOL mejorado
├── procesador.py                # Procesador en Python puro
│
└── data/
    ├── maestro.dat              # Archivo maestro de cuentas
    ├── movimientos.dat          # Archivo de transacciones
    └── reporte.txt              # Reporte generado
```

## 💻 Uso

### Interfaz Python

**Pestaña 📊 Cuentas Maestro:**
- Ver todas las cuentas registradas
- Buscar por número de cuenta o nombre de titular
- Visualizar saldos iniciales

**Pestaña 📝 Movimientos:**
- Agregar nuevos depósitos o retiros
- Validación automática de datos
- Vista de todos los movimientos registrados

**Pestaña ⚙️ Procesar:**
- Ejecutar procesamiento batch
- Ver log detallado de operaciones
- Verificar saldos actualizados

**Pestaña 📄 Reporte:**
- Generar reporte final
- Visualizar saldos actualizados
- Exportar a archivo

### Formato de Datos

#### maestro.dat (Ancho Fijo)
```
Posiciones:
1-10:    Número de Cuenta (10 dígitos)
11-40:   Nombre del Titular (30 caracteres)
41-60:   Saldo Inicial (20 caracteres)

Ejemplo:
1000000001Juan Pérez García       100000.50
1000000002María González López     250000.75
```

#### movimientos.dat (Delimitado por espacios)
```
Formato:
Número_Cuenta Tipo Monto

Tipo: D = Depósito, R = Retiro

Ejemplo:
1000000001 D 50000.00
1000000002 R 25000.00
1000000001 R 10000.00
```

## 📊 Ejemplo de Uso

1. **Abrir la interfaz**
   ```bash
   python interfaz.py
   ```

2. **Ir a la pestaña "Movimientos"**
   - Cuenta: `1000000001`
   - Tipo: `D - Depósito`
   - Monto: `25000`
   - Click en "Agregar"

3. **Ir a la pestaña "Procesar"**
   - Click en "🚀 Procesar"
   - Ver el log de operaciones

4. **Ir a la pestaña "Reporte"**
   - Click en "📄 Generar Reporte"
   - Ver saldos actualizados

## 🛠️ Desarrollo

### Estructura del Código Python

```python
class BankProcessorUI:
    - setup_ui()              # Crear interfaz
    - setup_tab_cuentas()     # Pestaña de cuentas
    - cargar_datos()          # Cargar archivos
    - procesar()              # Procesar movimientos
    - generar_reporte()       # Generar reporte
```

### Estructura del Código COBOL

```cobol
PROCEDURE DIVISION
    - INICIALIZAR         # Abrir archivos
    - CARGAR-MAESTRO      # Leer cuentas
    - PROCESAR-MOVIMIENTOS # Procesar transacciones
    - GENERAR-REPORTE     # Generar salida
    - FINALIZAR           # Cerrar archivos
```

## 📈 Casos de Uso

- ✅ Sistemas legacy que necesitan modernización
- ✅ Procesamiento batch nocturno
- ✅ Reconciliación de cuentas
- ✅ Educación en mantenimiento COBOL
- ✅ Migración gradual de aplicaciones

## 🐛 Control de Errores

- Validación de montos positivos
- Verificación de cuentas existentes
- Detección de archivos faltantes
- Formateo seguro de números

## 📝 Autor

**Ramón Romero Montilla**

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 💬 Preguntas y Soporte

Para reportar bugs o sugerencias:
- Abre un [Issue](https://github.com/usuario/procesador-bancario-cobol/issues)
- Incluye pasos para reproducir el problema
- Especifica tu versión de Python/COBOL

## 📚 Referencias

- [GnuCOBOL Documentation](https://www.gnu-cobol.org/docs/)
- [Python Tkinter Reference](https://docs.python.org/3/library/tkinter.html)
- [COBOL Programming Guide](https://en.wikipedia.org/wiki/COBOL)

## 🎯 Roadmap

- [ ] Interfaz web con Flask
- [ ] Base de datos integrada (SQLite)
- [ ] Soporte para múltiples monedas
- [ ] Exportación a Excel
- [ ] Autenticación de usuarios
- [ ] Auditoría de cambios
- [ ] API REST

## ⭐ Si te fue útil, ¡Dale una estrella!

```
   ⭐ ⭐ ⭐ ⭐ ⭐
```

---

**Hecho con ❤️ en COBOL y Python**
