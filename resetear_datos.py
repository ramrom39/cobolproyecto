#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para resetear archivos de datos a su estado inicial.
Útil para limpiar y empezar de nuevo.
"""

from pathlib import Path

def resetear_datos():
    """Resetear archivos de datos"""
    
    data_dir = Path(__file__).parent / "data"
    
    # Datos maestro en formato ancho fijo
    maestro_data = """1000000001Juan Pérez García       100000.50
1000000002María González López     250000.75
1000000003Carlos Rodríguez Martín  500000.00
1000000004Ana Martínez Sánchez     75000.25
1000000005Pedro López Fernández    180000.90
1000000006Rosa García Jiménez      320000.40
"""
    
    # Datos de movimientos
    movimientos_data = """1000000001 D 50000.00
1000000002 R 25000.00
1000000001 R 10000.00
1000000003 D 100000.00
1000000004 D 15000.50
1000000002 D 45000.25
1000000005 R 30000.00
1000000006 D 20000.00
"""
    
    # Escribir archivos
    maestro_file = data_dir / "maestro.dat"
    movimientos_file = data_dir / "movimientos.dat"
    
    with open(maestro_file, 'w', encoding='utf-8') as f:
        f.write(maestro_data)
    print(f"✅ Reiniciado: {maestro_file}")
    
    with open(movimientos_file, 'w', encoding='utf-8') as f:
        f.write(movimientos_data)
    print(f"✅ Reiniciado: {movimientos_file}")
    
    print("\n✨ Datos reiniciados exitosamente.")
    print("🔄 Ahora ejecuta: python interfaz.py")

if __name__ == "__main__":
    resetear_datos()
