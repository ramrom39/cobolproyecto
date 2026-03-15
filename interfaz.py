#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interfaz Gráfica - Procesador Bancario Batch
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from pathlib import Path
from datetime import datetime

class BankProcessorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🏦 Procesador Bancario Batch")
        self.root.geometry("1200x750")
        self.root.configure(bg="#f0f0f0")
        
        self.data_dir = Path(__file__).parent / "data"
        self.maestro_file = self.data_dir / "maestro.dat"
        self.movimientos_file = self.data_dir / "movimientos.dat"
        self.reporte_file = self.data_dir / "reporte.txt"
        
        # Datos en memoria
        self.cuentas = {}
        self.movimientos = []
        
        self.setup_ui()
        self.cargar_datos()
        
    def setup_ui(self):
        """Crear interfaz de usuario"""
        # Frame superior
        frame_titulo = tk.Frame(self.root, bg="#2c3e50", height=70)
        frame_titulo.pack(fill=tk.X, padx=0, pady=0)
        frame_titulo.pack_propagate(False)
        
        titulo = tk.Label(frame_titulo, text="💳 Procesador Bancario Batch", 
                         font=("Arial", 20, "bold"), bg="#2c3e50", fg="white")
        titulo.pack(pady=15)
        
        # Notebook (pestañas)
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Pestaña 1: Cuentas
        self.frame_cuentas = ttk.Frame(notebook)
        notebook.add(self.frame_cuentas, text="📊 Cuentas Maestro")
        self.setup_tab_cuentas()
        
        # Pestaña 2: Movimientos
        self.frame_movimientos = ttk.Frame(notebook)
        notebook.add(self.frame_movimientos, text="📝 Movimientos")
        self.setup_tab_movimientos()
        
        # Pestaña 3: Procesar
        self.frame_procesar = ttk.Frame(notebook)
        notebook.add(self.frame_procesar, text="⚙️ Procesar")
        self.setup_tab_procesar()
        
        # Pestaña 4: Reporte
        self.frame_reporte = ttk.Frame(notebook)
        notebook.add(self.frame_reporte, text="📄 Reporte")
        self.setup_tab_reporte()
    
    def setup_tab_cuentas(self):
        """Pestaña de cuentas maestro"""
        # Marco de búsqueda
        frame_buscar = ttk.Frame(self.frame_cuentas)
        frame_buscar.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(frame_buscar, text="🔍 Buscar:").pack(side=tk.LEFT)
        self.var_buscar = tk.StringVar()
        self.var_buscar.trace_add("write", lambda *args: self.filtrar_cuentas())
        entry_buscar = ttk.Entry(frame_buscar, textvariable=self.var_buscar, width=40)
        entry_buscar.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Tabla de cuentas
        frame_tabla = ttk.Frame(self.frame_cuentas)
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar_y = ttk.Scrollbar(frame_tabla)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree_cuentas = ttk.Treeview(
            frame_tabla, 
            columns=("Cuenta", "Titular", "Saldo"),
            height=20,
            yscrollcommand=scrollbar_y.set,
            show="headings"
        )
        
        scrollbar_y.config(command=self.tree_cuentas.yview)
        
        # Configurar columnas
        self.tree_cuentas.column("Cuenta", width=150, anchor="center")
        self.tree_cuentas.column("Titular", width=350, anchor="w")
        self.tree_cuentas.column("Saldo", width=200, anchor="e")
        
        for col in ("Cuenta", "Titular", "Saldo"):
            self.tree_cuentas.heading(col, text=col)
        
        self.tree_cuentas.pack(fill=tk.BOTH, expand=True)
    
    def setup_tab_movimientos(self):
        """Pestaña para agregar movimientos"""
        # Frame para nuevo movimiento
        frame_nuevo = ttk.LabelFrame(self.frame_movimientos, text="Agregar Movimiento", padding=15)
        frame_nuevo.pack(fill=tk.X, padx=10, pady=10)
        
        # Fila 1
        ttk.Label(frame_nuevo, text="Número de Cuenta:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_cuenta = ttk.Entry(frame_nuevo, width=20)
        self.entry_cuenta.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_nuevo, text="Tipo:").grid(row=0, column=2, sticky="w", padx=(20, 0))
        self.var_tipo = tk.StringVar(value="D")
        combo_tipo = ttk.Combobox(frame_nuevo, textvariable=self.var_tipo, 
                                  values=["D - Depósito", "R - Retiro"], state="readonly", width=18)
        combo_tipo.grid(row=0, column=3, padx=5, pady=5)
        
        # Fila 2
        ttk.Label(frame_nuevo, text="Monto:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_monto = ttk.Entry(frame_nuevo, width=20)
        self.entry_monto.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        btn_agregar = ttk.Button(frame_nuevo, text="➕ Agregar", command=self.agregar_movimiento)
        btn_agregar.grid(row=1, column=2, columnspan=2, padx=20, pady=5, sticky="ew")
        
        # Tabla de movimientos
        frame_tabla = ttk.Frame(self.frame_movimientos)
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(frame_tabla)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree_movimientos = ttk.Treeview(
            frame_tabla,
            columns=("Cuenta", "Tipo", "Monto"),
            height=15,
            yscrollcommand=scrollbar.set,
            show="headings"
        )
        scrollbar.config(command=self.tree_movimientos.yview)
        
        self.tree_movimientos.column("Cuenta", width=200, anchor="center")
        self.tree_movimientos.column("Tipo", width=200, anchor="center")
        self.tree_movimientos.column("Monto", width=200, anchor="e")
        
        for col in ("Cuenta", "Tipo", "Monto"):
            self.tree_movimientos.heading(col, text=col)
        
        self.tree_movimientos.pack(fill=tk.BOTH, expand=True)
    
    def setup_tab_procesar(self):
        """Pestaña de procesamiento"""
        frame_info = ttk.LabelFrame(self.frame_procesar, text="Control de Procesamiento", padding=20)
        frame_info.pack(fill=tk.X, padx=20, pady=20)
        
        # Botones
        frame_botones = tk.Frame(frame_info)
        frame_botones.pack(fill=tk.X, pady=10)
        
        btn_procesar = ttk.Button(frame_botones, text="🚀 Procesar", command=self.procesar)
        btn_procesar.pack(side=tk.LEFT, padx=5)
        
        btn_limpiar = ttk.Button(frame_botones, text="🗑️ Limpiar Log", command=self.limpiar_log)
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        # Log
        ttk.Label(frame_info, text="📋 Log de Procesamiento:").pack(anchor="w", pady=(10, 5))
        self.text_log = scrolledtext.ScrolledText(frame_info, height=15, width=100, font=("Courier", 9))
        self.text_log.pack(fill=tk.BOTH, expand=True, padx=0, pady=10)
    
    def setup_tab_reporte(self):
        """Pestaña de reporte"""
        frame_botones = ttk.Frame(self.frame_reporte)
        frame_botones.pack(fill=tk.X, padx=10, pady=10)
        
        btn_reporte = ttk.Button(frame_botones, text="📄 Generar Reporte", command=self.generar_reporte)
        btn_reporte.pack(side=tk.LEFT, padx=5)
        
        btn_limpiar = ttk.Button(frame_botones, text="🗑️ Limpiar", 
                                command=lambda: self.text_reporte.delete("1.0", tk.END))
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        self.text_reporte = scrolledtext.ScrolledText(self.frame_reporte, height=25, font=("Courier", 10))
        self.text_reporte.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def cargar_datos(self):
        """Cargar datos de archivos"""
        # Cargar cuentas maestro (formato ancho fijo)
        try:
            with open(self.maestro_file, 'r', encoding='utf-8') as f:
                for linea in f:
                    if len(linea.strip()) > 0:
                        # Formato ancho fijo: posiciones 1-10=cuenta, 11-40=nombre, 41+=saldo
                        cuenta = linea[0:10].strip()
                        titular = linea[10:40].strip()
                        saldo_str = linea[40:].strip()
                        
                        try:
                            saldo = float(saldo_str)
                            self.cuentas[cuenta] = {'titular': titular, 'saldo': saldo}
                        except ValueError:
                            print(f"Advertencia: No se pudo convertir saldo: {saldo_str}")
        except FileNotFoundError:
            messagebox.showerror("Error", f"No se encontró {self.maestro_file}")
        
        # Cargar movimientos (formato: cuenta tipo monto)
        try:
            with open(self.movimientos_file, 'r', encoding='utf-8') as f:
                for linea in f:
                    partes = linea.strip().split()
                    if len(partes) >= 3:
                        try:
                            self.movimientos.append({
                                'cuenta': partes[0],
                                'tipo': partes[1],
                                'monto': float(partes[2])
                            })
                        except ValueError:
                            print(f"Advertencia: Error parseando movimiento: {linea.strip()}")
        except FileNotFoundError:
            pass
        
        self.mostrar_cuentas()
        self.mostrar_movimientos()
    
    def mostrar_cuentas(self):
        """Mostrar cuentas en tabla"""
        for item in self.tree_cuentas.get_children():
            self.tree_cuentas.delete(item)
        
        for cuenta, datos in sorted(self.cuentas.items()):
            self.tree_cuentas.insert("", tk.END, values=(
                cuenta,
                datos['titular'],
                f"${datos['saldo']:,.2f}"
            ))
    
    def filtrar_cuentas(self):
        """Filtrar cuentas por búsqueda"""
        filtro = self.var_buscar.get().lower()
        for item in self.tree_cuentas.get_children():
            self.tree_cuentas.delete(item)
        
        for cuenta, datos in sorted(self.cuentas.items()):
            if filtro in cuenta.lower() or filtro in datos['titular'].lower():
                self.tree_cuentas.insert("", tk.END, values=(
                    cuenta,
                    datos['titular'],
                    f"${datos['saldo']:,.2f}"
                ))
    
    def mostrar_movimientos(self):
        """Mostrar movimientos en tabla"""
        for item in self.tree_movimientos.get_children():
            self.tree_movimientos.delete(item)
        
        for mov in self.movimientos:
            tipo_texto = "✅ Depósito" if mov['tipo'] == 'D' else "❌ Retiro"
            self.tree_movimientos.insert("", tk.END, values=(
                mov['cuenta'],
                tipo_texto,
                f"${mov['monto']:,.2f}"
            ))
    
    def agregar_movimiento(self):
        """Agregar movimiento"""
        cuenta = self.entry_cuenta.get().strip()
        tipo = self.var_tipo.get()[0]
        monto_str = self.entry_monto.get().strip()
        
        # Validación
        if not cuenta or not monto_str:
            messagebox.showwarning("Validación", "Completa todos los campos")
            return
        
        if cuenta not in self.cuentas:
            messagebox.showerror("Error", f"Cuenta {cuenta} no existe en maestro")
            return
        
        try:
            monto = float(monto_str)
            if monto <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Error", "Monto inválido (debe ser > 0)")
            return
        
        # Agregar movimiento
        self.movimientos.append({'cuenta': cuenta, 'tipo': tipo, 'monto': monto})
        
        # Guardar en archivo
        with open(self.movimientos_file, 'a', encoding='utf-8') as f:
            f.write(f"{cuenta} {tipo} {monto:.2f}\n")
        
        # Limpiar campos
        self.entry_cuenta.delete(0, tk.END)
        self.entry_monto.delete(0, tk.END)
        
        self.mostrar_movimientos()
        messagebox.showinfo("Éxito", "Movimiento agregado ✅")
    
    def procesar(self):
        """Procesar movimientos"""
        self.text_log.delete("1.0", tk.END)
        self.text_log.insert(tk.END, "🔄 Iniciando procesamiento...\n\n")
        self.root.update()
        
        # Copiar saldos originales
        saldos = {c: d['saldo'] for c, d in self.cuentas.items()}
        
        # Procesar movimientos
        self.text_log.insert(tk.END, f"📊 Procesando {len(self.movimientos)} movimientos...\n\n")
        self.root.update()
        
        for mov in self.movimientos:
            cuenta = mov['cuenta']
            if cuenta in saldos:
                if mov['tipo'] == 'D':
                    saldos[cuenta] += mov['monto']
                    self.text_log.insert(tk.END, 
                        f"✅ Depósito:  {cuenta} +${mov['monto']:,.2f}\n")
                else:
                    saldos[cuenta] -= mov['monto']
                    self.text_log.insert(tk.END, 
                        f"✅ Retiro:    {cuenta} -${mov['monto']:,.2f}\n")
                self.root.update()
        
        # Actualizar cuentas
        for cuenta in self.cuentas:
            self.cuentas[cuenta]['saldo'] = saldos[cuenta]
        
        self.mostrar_cuentas()
        self.text_log.insert(tk.END, "\n✅ Procesamiento completado\n")
        messagebox.showinfo("Éxito", "Procesamiento finalizado ✅")
    
    def limpiar_log(self):
        """Limpiar log"""
        self.text_log.delete("1.0", tk.END)
    
    def generar_reporte(self):
        """Generar reporte"""
        reporte = []
        reporte.append("REPORTE DE ACTUALIZACIÓN DE SALDOS")
        reporte.append("=" * 75)
        reporte.append(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        reporte.append(f"Total de Movimientos Procesados: {len(self.movimientos)}")
        reporte.append("=" * 75)
        reporte.append("")
        
        reporte.append(f"{'Cuenta':<15} {'Titular':<30} {'Saldo':>20}")
        reporte.append("-" * 75)
        
        total = 0
        for cuenta, datos in sorted(self.cuentas.items()):
            reporte.append(
                f"{cuenta:<15} {datos['titular']:<30} ${datos['saldo']:>18,.2f}"
            )
            total += datos['saldo']
        
        reporte.append("-" * 75)
        reporte.append(f"{'TOTAL':<15} {'':<30} ${total:>18,.2f}")
        reporte.append("=" * 75)
        
        contenido = "\n".join(reporte)
        self.text_reporte.delete("1.0", tk.END)
        self.text_reporte.insert(tk.END, contenido)
        
        # Guardar en archivo
        with open(self.reporte_file, 'w', encoding='utf-8') as f:
            f.write(contenido)
        
        messagebox.showinfo("Éxito", f"Reporte guardado en:\n{self.reporte_file}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BankProcessorUI(root)
    root.mainloop()
