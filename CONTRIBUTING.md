# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir a este proyecto! Aquí te indicamos cómo hacerlo.

## 🐛 Reportar Bugs

Si encuentras un bug:

1. **Verifica** si el bug ya existe en los [Issues](https://github.com/usuario/procesador-bancario-cobol/issues)
2. **Abre un nuevo Issue** con:
   - Título descriptivo
   - Descripción del problema
   - Pasos para reproducir
   - Comportamiento esperado vs actual
   - Versión de Python/COBOL
   - Screenshots si es relevante

## ✨ Sugerencias de Mejora

Para sugerir mejoras:
1. Abre un Issue con la etiqueta `enhancement`
2. Describe claramente la mejora propuesta
3. Explica el caso de uso
4. Incluye ejemplos si es posible

## 📝 Pull Requests

### Proceso

1. **Fork** el repositorio
   ```bash
   git clone https://github.com/tu-usuario/procesador-bancario-cobol.git
   cd procesador-bancario-cobol
   ```

2. **Crea una rama** para tu feature
   ```bash
   git checkout -b feature/nombre-descriptivo
   ```

3. **Realiza los cambios** siguiendo el estilo de código del proyecto

4. **Comitea** tus cambios
   ```bash
   git commit -m "Descripción clara del cambio"
   ```

5. **Push** a tu fork
   ```bash
   git push origin feature/nombre-descriptivo
   ```

6. **Abre un Pull Request** en el repositorio original

### Requisitos para PR

- ✅ Código limpio y bien documentado
- ✅ Sigue el estilo existente del proyecto
- ✅ Incluye pruebas si es relevante
- ✅ Actualiza el README si agregaste features
- ✅ Título y descripción claros

## 🎨 Estilo de Código

### Python
```python
# Usa 4 espacios para indentación
# Sigue PEP 8
# Agrupa imports: stdlib, third-party, local
# Comenta el código complejo
```

### COBOL
```cobol
*> Usa mayúsculas para palabras reservadas
*> Indenta bloques lógicos
*> Documenta funciones principales
*> Usa nombres descriptivos
```

## 📋 Checklist para PR

Antes de enviar:
- [ ] El código funciona correctamente
- [ ] Sin errores o warnings
- [ ] Documentación actualizada
- [ ] Tests pasando (si aplica)
- [ ] No incluye cambios no relacionados
- [ ] Commit messages claros

## 📚 Área de Enfoque

Áreas donde particularmente necesitamos ayuda:
- 🌐 Interfaz web (Flask/Django)
- 💾 Integración con bases de datos
- 📊 Exportación de reportes (Excel, PDF)
- 🔐 Autenticación y seguridad
- 📱 Versión móvil
- 🧪 Testing automatizado

## 💬 Comunicación

- Usa Issues para discusiones públicas
- Sé respetuoso con otros contribuidores
- Mantén el código inclusivo y accesible

## 📖 Recursos Útiles

- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [PEP 8 Style Guide](https://pep8.org/)
- [COBOL Standards](http://www.ibm.com/systems/z/os/cobol/)

---

**¡Gracias por contribuir! 🙏**
