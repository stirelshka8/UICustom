import configparser
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

config = configparser.ConfigParser()
config.read("config.ini")

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


def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)


def info_dialog():
    app_second = Info_window()
    app_second.mainloop()


def set_dialog():
    app_second_set = Set_window()
    app_second_set.mainloop()


class Main_window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("KREAM data collection program")
        self.geometry(f"{500}x{400}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=1)

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

        try:
            self.preset_search = config['CONFIG']['search']
            self.preset_save = config['CONFIG']['save']
            self.preset_anal = config['CONFIG']['save_analytics']
        except:
            self.preset_search = "ВВЕДИТЕ ТЕКСТ"
            self.preset_save = "ВВЕДИТЕ ТЕКСТ"
            self.preset_anal = "ВВЕДИТЕ ТЕКСТ"

        self.title("Настройки")
        self.geometry("570x200")

        self.search_label = customtkinter.CTkLabel(self, text="Что ищем?", anchor="w")
        self.search_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        self.entry_search = customtkinter.CTkEntry(self, placeholder_text=f"{self.preset_search}", width=360)
        self.entry_search.grid(row=1, column=2, columnspan=1, padx=(20, 0), pady=(5, 5), sticky="nsew")

        self.save_label = customtkinter.CTkLabel(self, text="Файл данных", anchor="w")
        self.save_label.grid(row=2, column=0, padx=20, pady=(10, 0))
        self.entry_save = customtkinter.CTkEntry(self, placeholder_text=f"{self.preset_save}", width=360)
        self.entry_save.grid(row=2, column=2, columnspan=2, padx=(20, 0), pady=(5, 5), sticky="nsew")

        self.anal_label = customtkinter.CTkLabel(self, text="Файл аналитики", anchor="w")
        self.anal_label.grid(row=3, column=0, padx=20, pady=(10, 0))
        self.entry_save_anal = customtkinter.CTkEntry(self, placeholder_text=f"{self.preset_anal}", width=360)
        self.entry_save_anal.grid(row=3, column=2, columnspan=2, padx=(20, 0), pady=(5, 5), sticky="nsew")

        self.sidebar_button_2 = customtkinter.CTkButton(self, text="СОХРАНИТЬ", command=self.save_set)
        self.sidebar_button_2.grid(row=8, column=2, columnspan=2, padx=20, pady=30)

    def save_set(self):
        search_get = self.entry_save_anal.get()
        save_get = self.entry_save_anal.get()
        save_anal = self.entry_save_anal.get()

        try:
            config.add_section("CONFIG")
        except:
            pass

        config.set("CONFIG", "search", search_get)
        config.set("CONFIG", "save", save_get)
        config.set("CONFIG", "save_analytics", save_anal)

        try:
            config.add_section("INSTALL")
            config.set("INSTALL", "set_up", "True")
        except:
            pass

        with open("config.ini", "w") as config_file:
            config.write(config_file)

        Set_window.destroy(self)


if __name__ == "__main__":
    app = Main_window()
    app.mainloop()
