import customtkinter as ctk

# Configuración de la apariencia
ctk.set_appearance_mode("dark")  # Modos: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue" (standard), "green", "dark-blue"

class AppHorario(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.title("Organizador de Clases - Paradigma Imperativo")
        self.geometry("450x500")

        # Datos del Horario (Diccionario para búsqueda rápida)
        self.horario = {
            "lunes": {6: "Programación", 10: "Matemáticas", 14: "Cálculo"},
            "martes": {8: "Bases de Datos", 10: "Redes", 20: "Sistemas Operativos"},
            "miércoles": {7: "Ingeniería de Software", 9: "Cálculo", 15: "Matemáticas"},
            "jueves": {8: "Sistemas Operativos", 10: "Ética Profesional", 14: "Bases de Datos"},
            "viernes": {11: "Proyecto de Laboratorio", 13: "Encriptación"}
        }

        # --- Elementos de la Interfaz ---
        self.label_titulo = ctk.CTkLabel(self, text="Mi Horario Académico", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=20)

        # Selección de Día
        self.label_dia = ctk.CTkLabel(self, text="Selecciona el día:")
        self.label_dia.pack(pady=5)
        self.combo_dia = ctk.CTkComboBox(self, values=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])
        self.combo_dia.pack(pady=10)

        # Entrada de Hora
        self.label_hora = ctk.CTkLabel(self, text="Ingresa la hora (formato 24h):")
        self.label_hora.pack(pady=5)
        self.entry_hora = ctk.CTkEntry(self, placeholder_text="Ej: 10")
        self.entry_hora.pack(pady=10)

        # Botón de Búsqueda
        self.boton_buscar = ctk.CTkButton(self, text="Consultar Clase", command=self.buscar_clase)
        self.boton_buscar.pack(pady=20)

        # Cuadro de Resultado
        self.label_resultado = ctk.CTkLabel(self, text="", text_color="#3b8ed0", font=("Roboto", 16, "italic"))
        self.label_resultado.pack(pady=20)

    def buscar_clase(self):
        """Lógica Imperativa: Captura, Procesa y Muestra"""
        dia = self.combo_dia.get().lower()
        
        try:
            hora = int(self.entry_hora.get())
            # Aplicamos la lógica de búsqueda
            clase = self.horario.get(dia, {}).get(hora)

            if clase:
                self.label_resultado.configure(text=f" Clase: {clase}", text_color="green")
            else:
                self.label_resultado.configure(text=f"☕ No tienes clase a las {hora}:00", text_color="gray")
        
        except ValueError:
            self.label_resultado.configure(text="⚠️ Por favor, ingresa una hora válida", text_color="red")

if __name__ == "__main__":
    app = AppHorario()
    app.mainloop()