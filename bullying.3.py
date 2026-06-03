import tkinter as tk

class RegistroApp:
    def __init__(self):
        self.victimas = []
        self.testigos = []

        self.ventana = tk.Tk()
        self.ventana.title("Registro")
        self.ventana.geometry("400x300")

        self.menu()
        self.ventana.mainloop()

    def limpiar(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menu(self):
        self.limpiar()
        tk.Label(self.ventana, text="Selecciona una opcion:").pack(pady=10)
        tk.Button(self.ventana, text="Victima", command=self.victima).pack(pady=5)
        tk.Button(self.ventana, text="Testigo", command=self.testigo).pack(pady=5)
        tk.Button(self.ventana, text="Archivo", command=self.archivos).pack(pady=5)
        tk.Button(self.ventana, text="Salir", command=self.ventana.destroy).pack(pady=5)

    def victima(self):
        self.limpiar()
        tk.Label(self.ventana, text="VICTIMA").pack()

        tk.Label(self.ventana, text="Nombre: (puede ser anonimo)").pack()
        entry_nombre = tk.Entry(self.ventana)
        entry_nombre.pack()
  
        tk.Label(self.ventana, text="Lugar de la escuela: ").pack()
        entry_lugar = tk.Entry(self.ventana)
        entry_lugar.pack()
  
        tk.Label(self.ventana, text="Tipo de bullying: ").pack()
        entry_tipo = tk.Entry(self.ventana)
        entry_tipo.pack()

        tk.Label(self.ventana, text="Si sabe el grupo del agresor/a ingreselo: ").pack()
        entry_grupo = tk.Entry(self.ventana)
        entry_grupo.pack()

        def guardar():
            self.victimas.append([
                entry_nombre.get(),
                entry_lugar.get(),
                entry_tipo.get(),
                entry_grupo.get()
            ])
            self.menu()

        tk.Button(self.ventana, text="Guardar", command=guardar).pack(pady=5)
        tk.Button(self.ventana, text="Menu", command=self.menu).pack()

    def testigo(self):
        self.limpiar()
        tk.Label(self.ventana, text="TESTIGO").pack()
        
        tk.Label(self.ventana, text="Lugar de la escuela: ").pack()
        entry_lugar = tk.Entry(self.ventana)
        entry_lugar.pack()
  
        tk.Label(self.ventana, text="Tipo de bullying: ").pack()
        entry_tipo = tk.Entry(self.ventana)
        entry_tipo.pack()
  
        tk.Label(self.ventana, text="Intervino? si/no: ").pack()
        entry_intervino = tk.Entry(self.ventana)
        entry_intervino.pack()

        tk.Label(self.ventana, text="Si sabe el grupo del agresor/a ingreselo: ").pack()
        entry_grupo = tk.Entry(self.ventana)
        entry_grupo.pack()

        def guardar():
            self.testigos.append([
                entry_lugar.get(),
                entry_tipo.get(),
                entry_intervino.get(),
                entry_grupo.get()
            ])
            self.menu()

        tk.Button(self.ventana, text="Guardar", command=guardar).pack(pady=5)
        tk.Button(self.ventana, text="Menu", command=self.menu).pack()

    def archivos(self): 
        self.limpiar()
        tk.Label(self.ventana, text="ARCHIVO").pack()

        texto = tk.Text(self.ventana, height=12, width=50)
        texto.pack()

        texto.insert(tk.END, "===VICTIMAS===\n")
        for v in self.victimas:
            texto.insert(tk.END, f"Nombre: {v[0]}, Lugar: {v[1]}, Tipo: {v[2]},\n Grupo: {v[3]}\n")

        texto.insert(tk.END, "===TESTIGOS===\n")
        for t in self.testigos:
            texto.insert(tk.END, f"Lugar: {t[0]}, Tipo: {t[1]}, Intervino: {t[2]},\n Grupo: {t[3]}\n")

        tk.Button(self.ventana, text="Menu", command=self.menu).pack()

RegistroApp()

        
