import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

description_text = "Парсер товаров корейской торговой площадки www.cream.co.kr (далее - ПАРСЕР), собирает информацию " \
                   "по введенным в конфигурционном файле (config.ini) критериям поиска в отдельный XLSX файл (при " \
                   "каждом новом запуске будет создаваться не новый файл, а новый лист документа). Возможен сбор " \
                   "информации сразу-же с ценой доставки в Российскую Федерацию, но данный процесс очень сильно " \
                   "увеличивает время работы парсера и не всегда работает корректно, так ка по ответу службы " \
                   "поддержки сайта https://brickset.com/ из РФ идет очень много ПЛОХОГО трафика и они блокируют " \
                   "работу API сервиса и приходится использовать магию PROXY. Далее собранную информацию возможно " \
                   "проанализировать запустив процесс аналитики, при данном действии будет создан новый файл куда " \
                   "будут сохраниться позиции товаров которые изменились (сравниваются ПОСЛЕДНИЙ и ПРЕДПОСЛЕДНИЙ лист "\
                   "в файле)."
author_text = "Author - @stirelshka8"
version_text = "ver 0.2a"


def set_dialog():
    app_second = Set_window()
    app_second.mainloop()


def info_dialog():
    app_second = Info_window()
    app_second.mainloop()


def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)

class Main_window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("KREAM data collection program")
        self.geometry(f"{500}x{400}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Парсер KREAM",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(70, 10))
        self.logo_label_pre = customtkinter.CTkLabel(self.sidebar_frame, text="for Andrey",
                                                     font=customtkinter.CTkFont(size=10, weight="bold"))
        self.logo_label_pre.grid(row=0, column=0, padx=20, pady=(120, 10))

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Информация",
                                                        command=info_dialog)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=30)

        self.string_input_button = customtkinter.CTkButton(self.sidebar_frame, text="Настройки",
                                                           command=set_dialog)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(80, 10))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=3, column=0, padx=10, pady=(20, 0))

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text=f"{version_text}")
        self.appearance_mode_label.grid(row=0, column=0, padx=10, pady=(0, 0))


class Info_window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Информация")
        self.geometry("400x250")
        self.textbox = customtkinter.CTkTextbox(self, width=360)
        self.textbox.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0",
                            f"Парсер данных с сайта www.cream.co.kr\n\n" +
                            f"{description_text}\n\n{author_text.upper()}\n\n")
        self.textbox.configure(state="disabled")


class Set_window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Настройки")
        self.geometry("400x300")
        self.entry_search = customtkinter.CTkEntry(self, placeholder_text="Что ищем?", width=360)
        self.entry_search.grid(row=1, column=2, columnspan=1, padx=(20, 0), pady=(5, 5), sticky="nsew")
        self.entry_save = customtkinter.CTkEntry(self, placeholder_text="Имя файла данных ", width=360)
        self.entry_save.grid(row=2, column=2, columnspan=2, padx=(20, 0), pady=(5, 5), sticky="nsew")
        self.entry_save_anal = customtkinter.CTkEntry(self, placeholder_text="Имя файла аналитики ", width=360)
        self.entry_save_anal.grid(row=3, column=2, columnspan=2, padx=(20, 0), pady=(5, 5), sticky="nsew")
        self.entry_save_login = customtkinter.CTkEntry(self, placeholder_text="Brickset логин ", width=360)
        self.entry_save_login.grid(row=4, column=2, columnspan=2, padx=(20, 0), pady=(5, 5), sticky="nsew")
        self.entry_save_pass = customtkinter.CTkEntry(self, placeholder_text="Brickset пароль ", width=360)
        self.entry_save_pass.grid(row=5, column=2, columnspan=2, padx=(20, 0), pady=(5, 5), sticky="nsew")
        self.entry_save_api = customtkinter.CTkEntry(self, placeholder_text="Brickset API токен ", width=360)
        self.entry_save_api.grid(row=6, column=2, columnspan=2, padx=(20, 0), pady=(5, 5), sticky="nsew")

        self.sidebar_button_2 = customtkinter.CTkButton(self, text="Информация",
                                                        command=info_dialog)
        self.sidebar_button_2.grid(row=8, column=2, columnspan=2, padx=20, pady=30)





if __name__ == "__main__":
    app = Main_window()
    app.mainloop()
