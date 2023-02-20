import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class Main_window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("KREAM data collection program v0.2a")
        self.geometry(f"{800}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Парсер KREAM",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Информация",
                                                        command=self.info_dialog)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.string_input_button = customtkinter.CTkButton(self.sidebar_frame, text="Настройки",
                                                           command=self.ruuuuu)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(70, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Тема:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Масштаб:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    def ruuuuu(self):
        print("FACK")

    def info_dialog(self):
        app_second = Second_window()
        app_second.mainloop()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


class Second_window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Информация")
        self.geometry(f"{400}x{250}")
        self.textbox = customtkinter.CTkTextbox(self, width=360)
        self.textbox.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0", "Парсер данных с сайта www.cream.co.kr\n\n" + "Парам пам пам\n\n")
        self.textbox.configure(state="disabled")


if __name__ == "__main__":
    app = Main_window()
    app.mainloop()
