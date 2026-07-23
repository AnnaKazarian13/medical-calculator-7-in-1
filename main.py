import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class PremiumMedicalApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🩺 MED-TECH QUANTUM // Медицинские Экспертные Системы")
        self.geometry("900x620")
        self.resizable(False, False)

        self.COLOR_ACCENT = "#0ea5e9"
        self.COLOR_SUCCESS = "#10b981"
        self.COLOR_WARNING = "#f59e0b"
        self.COLOR_DANGER = "#ef4444"

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, corner_radius=0, width=240, fg_color=("#1e293b", "#0f172a"))
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        self.lbl_logo = ctk.CTkLabel(self.sidebar, text="🏥 MED-TECH", font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"), text_color="#ffffff")
        self.lbl_logo.pack(pady=(30, 5), padx=20, anchor="w")
        self.lbl_subtitle = ctk.CTkLabel(self.sidebar, text="Скрининговый комплекс", font=ctk.CTkFont(family="Segoe UI", size=11), text_color="#94a3b8")
        self.lbl_subtitle.pack(pady=(0, 25), padx=22, anchor="w")

        self.menu_buttons = {}
        menu_items = [
            ("bmi", "📊  Индекс массы тела"),
            ("smoke", "🚬  Индекс курения"),
            ("water", "💧  Потребность в воде"),
            ("calories", "🔥  Калории (BMR)"),
            ("waist", "📏  Окружность талии"),
            ("homa", "🧪  Индекс HOMA-IR"),
            ("gcs", "🧠  Шкала комы Глазго")
        ]

        for key, text in menu_items:
            btn = ctk.CTkButton(
                self.sidebar, text=text, font=ctk.CTkFont(family="Segoe UI", size=13),
                anchor="w", height=42, corner_radius=8, fg_color="transparent", text_color="#cbd5e1",
                hover_color=("#334155", "#1e293b"), cursor="hand2",
                command=lambda k=key: self.switch_screen(k)
            )
            btn.pack(fill="x", padx=12, pady=2)
            self.menu_buttons[key] = btn

        self.theme_switch = ctk.CTkSwitch(
            self.sidebar, text="Темная тема", font=ctk.CTkFont(size=11), text_color="#94a3b8",
            command=self.toggle_theme, progress_color=self.COLOR_ACCENT
        )
        self.theme_switch.pack(side="bottom", pady=20, padx=20, anchor="w")
        if ctk.get_appearance_mode() == "Dark":
            self.theme_switch.select()

        self.main_content = ctk.CTkFrame(self, corner_radius=0, fg_color=("#f8fafc", "#0b0f19"))
        self.main_content.grid(row=0, column=1, sticky="nsew")

        self.current_frame = None
        self.switch_screen("bmi")

    def toggle_theme(self):
        if self.theme_switch.get() == 1:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def switch_screen(self, screen_key):
        for key, btn in self.menu_buttons.items():
            btn.configure(fg_color="transparent", text_color="#cbd5e1", font=ctk.CTkFont(weight="normal"))

        self.menu_buttons[screen_key].configure(fg_color=self.COLOR_ACCENT, text_color="#ffffff", font=ctk.CTkFont(weight="bold"))

        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = ctk.CTkFrame(self.main_content, corner_radius=16, fg_color=("#ffffff", "#111827"), border_width=1, border_color=("#e2e8f0", "#1f2937"))
        self.current_frame.pack(expand=True, fill="both", padx=30, pady=30)

        getattr(self, f"create_screen_{screen_key}")()

    def create_result_box(self, parent):
        frame = ctk.CTkFrame(parent, corner_radius=12, fg_color=("#f1f5f9", "#1f2937"), border_width=1, border_color=("#cbd5e1", "#374151"))
        frame.pack(fill="both", expand=True, pady=(20, 0))

        lbl_title = ctk.CTkLabel(frame, text="КЛИНИЧЕСКИЙ АНАЛИЗ И РИСКИ", font=ctk.CTkFont(size=10, weight="bold"), text_color=self.COLOR_ACCENT)
        lbl_title.pack(anchor="w", padx=15, pady=(12, 0))

        lbl = ctk.CTkLabel(frame, text="Ожидание ввода параметров пациента...", font=ctk.CTkFont(family="Segoe UI", size=13), text_color=("#334155", "#9ca3af"), justify="left", anchor="nw", wraplength=560)
        lbl.pack(padx=15, pady=(5, 15), fill="both", expand=True)
        return lbl


    def create_screen_bmi(self):
        ctk.CTkLabel(self.current_frame, text="Индекс Массы Тела (ИМТ)", font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=20, pady=(20, 5))
        ctk.CTkLabel(self.current_frame, text="Стандартизированный скрининг дефицита и избытка массы тела по критериям ВОЗ.", font=ctk.CTkFont(size=12), text_color="#6b7280").pack(anchor="w", padx=20, pady=(0, 20))

        f_inputs = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        f_inputs.pack(anchor="w", padx=20, fill="x")

        ctk.CTkLabel(f_inputs, text="Масса тела (кг)", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=0, sticky="w")
        ent_w = ctk.CTkEntry(f_inputs, placeholder_text="Например: 72", width=180, height=36, corner_radius=8)
        ent_w.grid(row=1, column=0, padx=(0, 20), pady=(4, 0))

        ctk.CTkLabel(f_inputs, text="Рост (см или м)", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=1, sticky="w")
        ent_h = ctk.CTkEntry(f_inputs, placeholder_text="Например: 176", width=180, height=36, corner_radius=8)
        ent_h.grid(row=1, column=1, pady=(4, 0))

        lbl_res = self.create_result_box(self.current_frame)

        def calc():
            try:
                w = float(ent_w.get().replace(",", "."))
                h = float(ent_h.get().replace(",", "."))
                if h > 3: h /= 100
                if w <= 0 or h <= 0: raise ValueError

                bmi = w / (h ** 2)
                res = f"Показатель ИМТ: {bmi:.2f}\n\n"

                if bmi < 18.5:
                    res += "🛑 ДЕФИЦИТ МАССЫ ТЕЛА\n- Высокий риск белково-энергетической недостаточности.\n- Повышена вероятность скрытых анемий, остеопороза и дисфункции иммунной системы."
                elif bmi < 25.0:
                    res += "🟢 НОРМАЛЬНЫЙ ВЕС\n- Минимальный коморбидный, кардиоваскулярный и эндокринный риск.\n- Рекомендуется поддержание текущего двигательного и пищевого режима."
                elif bmi < 30.0:
                    res += "🟡 ИЗБЫТОЧНАЯ МАССА ТЕЛА (ПРЕДОЖИРЕНИЕ)\n- Риск формирования инсулинорезистентности и метаболического синдрома.\n- Начальная стадия перегрузки опорно-двигательного аппарата."
                elif bmi < 35.0:
                    res += "🟠 ОЖИРЕНИЕ I СТЕПЕНИ\n- Высокий детерминированный риск манифестации Сахарного Диабета 2 типа.\n- Ускоренное развитие атеросклероза артерий, жировой инфильтрации печени (МАЖБП) и ночного апноэ."
                elif bmi < 40.0:
                    res += "🔴 ОЖИРЕНИЕ II СТЕПЕНИ\n- Серьезная угроза сосудистых катастроф (острый инфаркт миокарда, ишемический инсульт).\n- Высокие риски хронической болезни почек (ХБП) и сердечной недостаточности."
                else:
                    res += "❌ МОРБИДНОЕ ОЖИРЕНИЕ (III СТЕПЕНЬ)\n- Критическое сокращение средней продолжительности жизни.\n- Ассоциировано со значительным ростом онкопатологий (колоректальный рак, рак эндометрия, почек)."
                lbl_res.configure(text=res)
            except ValueError:
                messagebox.showerror("Ошибка", "Введите корректные числовые параметры.")

        btn_calc = ctk.CTkButton(self.current_frame, text="Выполнить расчет", font=ctk.CTkFont(weight="bold"), fg_color=self.COLOR_ACCENT, hover_color=self.COLOR_ACCENT, height=38, corner_radius=8, command=calc)
        btn_calc.pack(anchor="w", padx=20, pady=(20, 0))

    def create_screen_smoke(self):
        ctk.CTkLabel(self.current_frame, text="Индекс Курильщика (Пачка/лет)", font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=20, pady=(20, 5))
        ctk.CTkLabel(self.current_frame, text="Количественная оценка кумулятивной табачной нагрузки для прогнозирования рисков ХОБЛ.", font=ctk.CTkFont(size=12), text_color="#6b7280").pack(anchor="w", padx=20, pady=(0, 20))

        f_inputs = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        f_inputs.pack(anchor="w", padx=20, fill="x")

        ctk.CTkLabel(f_inputs, text="Сигарет в сутки", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=0, sticky="w")
        ent_c = ctk.CTkEntry(f_inputs, placeholder_text="Например: 20", width=180, height=36, corner_radius=8)
        ent_c.grid(row=1, column=0, padx=(0, 20), pady=(4, 0))

        ctk.CTkLabel(f_inputs, text="Общий стаж (лет)", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=1, sticky="w")
        ent_y = ctk.CTkEntry(f_inputs, placeholder_text="Например: 15", width=180, height=36, corner_radius=8)
        ent_y.grid(row=1, column=1, pady=(4, 0))

        lbl_res = self.create_result_box(self.current_frame)

        def calc():
            try:
                c = int(ent_c.get())
                y = int(ent_y.get())
                if c < 0 or y < 0: raise ValueError
                idx = (c / 20) * y
                res = f"Индекс табачной нагрузки: {idx:.2f} пачко-лет\n\n"
                if idx < 10:
                    res += "🟢 Порог критической деструкции легких не превышен.\n- Однако безопасной экспозиции дыма не существует. Сосудистый тонус и эндотелий повреждаются даже при минимальных дозах."
                elif idx < 20:
                    res += "⚠️ ВЫСОКИЙ ПУЛЬМОНОЛОГИЧЕСКИЙ РИСК\n- Доказанный триггер формирования ХОБЛ и прогрессирующей эмфиземы легких.\n- Пациенту показано проведение спирометрии с бронхолитической пробой для оценки ОФВ1."
                else:
                    res += "🚨 КРИТИЧЕСКИЙ ОНКОЛОГИЧЕСКИЙ РИСК\n- Экспоненциальный рост риска плоскоклеточного рака легкого, гортани и рака мочевого пузыря.\n- Абсолютное медицинское показание к скринингу: низкодозовая компьютерная томография (НДКТ) легких 1 раз в год."
                lbl_res.configure(text=res)
            except ValueError:
                messagebox.showerror("Ошибка", "Введите корректные целые числа.")

        btn_calc = ctk.CTkButton(self.current_frame, text="Оценить нагрузку", font=ctk.CTkFont(weight="bold"), fg_color=self.COLOR_ACCENT, height=38, corner_radius=8, command=calc)
        btn_calc.pack(anchor="w", padx=20, pady=(20, 0))

    def create_screen_water(self):
        ctk.CTkLabel(self.current_frame, text="Гидратационный статус", font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=20, pady=(20, 5))
        ctk.CTkLabel(self.current_frame, text="Расчет базовой физиологической потребности организма в жидкости.", font=ctk.CTkFont(size=12), text_color="#6b7280").pack(anchor="w", padx=20, pady=(0, 20))

        ctk.CTkLabel(self.current_frame, text="Масса тела пациента (кг)", font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=20)
        ent_w = ctk.CTkEntry(self.current_frame, placeholder_text="Например: 68", width=180, height=36, corner_radius=8)
        ent_w.pack(anchor="w", padx=20, pady=(4, 15))

        lbl_res = self.create_result_box(self.current_frame)

        def calc():
            try:
                w = float(ent_w.get().replace(",", "."))
                if w <= 0: raise ValueError
                lbl_res.configure(text=f"Рекомендуемый суточный объем жидкости: ~{w*30:.0f} мл\n(Включает чистую воду, супы, сочные фрукты и скрытую жидкость).\n\n⚠️ КЛИНИЧЕСКИЕ ОГРАНИЧЕНИЯ:\n- Объем адаптивно масштабируется в большую сторону при гипертермии (лихорадке), диарее и усиленном потоотделении.\n- ПРОТИВОПОКАЗАНИЕ: Пациентам с декомпенсированной Хронической сердечной недостаточностью (ХСН) и терминальной почечной недостаточностью водный режим жестко лимитируется кардиологом/нефрологом во избежание анасарки и отека легких!")
            except ValueError:
                messagebox.showerror("Ошибка", "Укажите корректный вес.")

        btn_calc = ctk.CTkButton(self.current_frame, text="Посчитать объем", font=ctk.CTkFont(weight="bold"), fg_color=self.COLOR_ACCENT, height=38, corner_radius=8, command=calc)
        btn_calc.pack(anchor="w", padx=20, pady=(5, 0))

    def create_screen_calories(self):
        ctk.CTkLabel(self.current_frame, text="Базальный Обмен Веществ (BMR)", font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=20, pady=(15, 5))
        ctk.CTkLabel(self.current_frame, text="Расчет энергетических затрат в условиях физиологического покоя (Миффлин - Сан Жеор).", font=ctk.CTkFont(size=12), text_color="#6b7280").pack(anchor="w", padx=20, pady=(0, 15))

        g_var = ctk.StringVar(value="m")
        f_g = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        f_g.pack(anchor="w", padx=20, pady=(0, 10))
        ctk.CTkRadioButton(f_g, text="Мужской пол", variable=g_var, value="m", font=ctk.CTkFont(size=12)).grid(row=0, column=0, padx=(0, 20))
        ctk.CTkRadioButton(f_g, text="Женский пол", variable=g_var, value="f", font=ctk.CTkFont(size=12)).grid(row=0, column=1)

        f_inputs = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        f_inputs.pack(anchor="w", padx=20, fill="x")

        ctk.CTkLabel(f_inputs, text="Вес (кг)", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=0, sticky="w")
        ent_w = ctk.CTkEntry(f_inputs, width=150, height=32, corner_radius=6)
        ent_w.grid(row=1, column=0, padx=(0, 15), pady=2)

        ctk.CTkLabel(f_inputs, text="Рост (см)", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=1, sticky="w")
        ent_h = ctk.CTkEntry(f_inputs, width=150, height=32, corner_radius=6)
        ent_h.grid(row=1, column=1, padx=(0, 15), pady=2)

        ctk.CTkLabel(f_inputs, text="Возраст", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=2, sticky="w")
        ent_a = ctk.CTkEntry(f_inputs, width=150, height=32, corner_radius=6)
        ent_a.grid(row=1, column=2, pady=2)

        lbl_res = self.create_result_box(self.current_frame)

        def calc():
            try:
                w = float(ent_w.get().replace(",", "."))
                h = float(ent_h.get().replace(",", "."))
                a = int(ent_a.get())
                if w <= 0 or h <= 0 or a <= 0: raise ValueError

                gender = g_var.get()
                bmr = 10*w + 6.25*h - 5*a + (5 if gender == "m" else -161)
                lbl_res.configure(text=f"Уровень базального метаболизма (BMR): {bmr:.0f} ккал/сутки\n\n- Столько энергии тратит организм на клеточное дыхание, терморегуляцию и работу внутренних органов в состоянии абсолютного бездействия.\n- Чтобы составить реальное меню, умножьте полученную цифру на коэффициент активности: от 1.2 (сидячая работа) до 1.9 (тяжелый ежедневный спорт).")
            except ValueError:
                messagebox.showerror("Ошибка", "Проверьте корректность заполнения полей.")

        btn_calc = ctk.CTkButton(self.current_frame, text="Вычислить ккал", font=ctk.CTkFont(weight="bold"), fg_color=self.COLOR_ACCENT, height=36, corner_radius=8, command=calc)
        btn_calc.pack(anchor="w", padx=20, pady=(15, 0))

    def create_screen_waist(self):
        ctk.CTkLabel(self.current_frame, text="Окружность талии (Висцеральный скрининг)", font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=20, pady=(20, 5))
        ctk.CTkLabel(self.current_frame, text="Критерии IDF и РКО для оценки распределения жировой ткани и метаболического синдрома.", font=ctk.CTkFont(size=12), text_color="#6b7280").pack(anchor="w", padx=20, pady=(0, 15))

        g_var = ctk.StringVar(value="м")
        f_g = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        f_g.pack(anchor="w", padx=20, pady=(0, 10))
        ctk.CTkRadioButton(f_g, text="Мужчина", variable=g_var, value="м").grid(row=0, column=0, padx=(0, 20))
        ctk.CTkRadioButton(f_g, text="Женщина", variable=g_var, value="ж").grid(row=0, column=1)

        ctk.CTkLabel(self.current_frame, text="Окружность талии на уровне пупка (см)", font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=20)
        ent_s = ctk.CTkEntry(self.current_frame, placeholder_text="Например: 88", width=180, height=36, corner_radius=8)
        ent_s.pack(anchor="w", padx=20, pady=(4, 15))

        lbl_res = self.create_result_box(self.current_frame)

        def calc():
            try:
                s = float(ent_s.get().replace(",", "."))
                if s <= 0: raise ValueError

                gender = g_var.get()
                res = f"Зафиксированный объем: {s} см\n\n"
                if gender == "м":
                    if s < 94: res += "🟢 ПОКАЗАТЕЛИ В ПРЕДЕЛАХ НОРМЫ\n- Риск висцерального депонирования жира минимален."
                    else: res += "⚠️ ВИСЦЕРАЛЬНОЕ (АБДОМИНАЛЬНОЕ) ОЖИРЕНИЕ (Порог ≥ 94 см)\n- Патологический маркер системного воспаления.\n- Высокий риск стеатогепатита, накопления жира вокруг внутренних органов, падения фракции ЛПВП («хорошего» холестерина) и прогрессирования ИБС."
                else:
                    if s < 80: res += "🟢 ПОКАЗАТЕЛИ В ПРЕДЕЛАХ НОРМЫ\n- Низкая вероятность абдоминального метаболического синдрома."
                    else: res += "⚠️ ВИСЦЕРАЛЬНОЕ (АБДОМИНАЛЬНОЕ) ОЖИРЕНИЕ (Порог ≥ 80 см)\n- Маркер угрозы развития атеросклероза артерий.\n- У женщин ассоциировано с развитием Синдрома поликистозных яичников (СПКЯ), инсулинорезистентности и ановуляторных циклов."
                lbl_res.configure(text=res)
            except ValueError:
                messagebox.showerror("Ошибка", "Введите корректное значение.")

        btn_calc = ctk.CTkButton(self.current_frame, text="Проверить порог", font=ctk.CTkFont(weight="bold"), fg_color=self.COLOR_ACCENT, height=38, corner_radius=8, command=calc)
        btn_calc.pack(anchor="w", padx=20, pady=(5, 0))

    def create_screen_homa(self):
        ctk.CTkLabel(self.current_frame, text="Индекс Инсулинорезистентности HOMA-IR", font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=20, pady=(20, 5))
        ctk.CTkLabel(self.current_frame, text="Расчет тканевой нечувствительности к инсулину. Обязательны строго указанные единицы!", font=ctk.CTkFont(size=12), text_color="#6b7280").pack(anchor="w", padx=20, pady=(0, 20))

        f_inputs = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        f_inputs.pack(anchor="w", padx=20, fill="x")

        ctk.CTkLabel(f_inputs, text="Глюкоза натощак (ммоль/л)", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=0, sticky="w")
        ent_g = ctk.CTkEntry(f_inputs, placeholder_text="Пример: 5.4", width=190, height=36, corner_radius=8)
        ent_g.grid(row=1, column=0, padx=(0, 20), pady=(4, 0))

        ctk.CTkLabel(f_inputs, text="Инсулин натощак (мкЕд/мл)", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=1, sticky="w")
        ent_i = ctk.CTkEntry(f_inputs, placeholder_text="Пример: 11.2", width=190, height=36, corner_radius=8)
        ent_i.grid(row=1, column=1, pady=(4, 0))

        lbl_res = self.create_result_box(self.current_frame)

        def calc():
            try:
                g = float(ent_g.get().replace(",", "."))
                i = float(ent_i.get().replace(",", "."))
                if g <= 0 or i <= 0: raise ValueError

                homa_val = (g * i) / 22.5
                res = f"Индекс HOMA-IR: {homa_val:.2f}\n\nКлиническая оценка:\n"
                if homa_val < 2.5:
                    res += "🟢 ПАТОЛОГИЙ НЕ ВЫЯВЛЕНО\n- Физиологическая чувствительность периферических тканей (мышц, жирового депо) к инсулину сохранена."
                else:
                    res += "⚠️ ВЫЯВЛЕНА ИНСУЛИНОРЕЗИСТЕНТНОСТЬ\n- Клетки блокируют действие инсулина, заставляя поджелудочную железу работать на износ (гиперинсулинемия).\n- Высокий риск манифестации предиабета, метаболического повреждения сосудистой стенки. Показано дообследование: Гликированный гемоглобин (HbA1c) и консультация эндокринолога."
                lbl_res.configure(text=res)
            except ValueError:
                messagebox.showerror("Ошибка", "Проверьте корректность лабораторных показателей.")

        btn_calc = ctk.CTkButton(self.current_frame, text="Рассчитать HOMA-IR", font=ctk.CTkFont(weight="bold"), fg_color=self.COLOR_ACCENT, height=38, corner_radius=8, command=calc)
        btn_calc.pack(anchor="w", padx=20, pady=(20, 0))

    def create_screen_gcs(self):
        ctk.CTkLabel(self.current_frame, text="Шкала Комы Глазго (Glasgow Coma Scale)", font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=20, pady=(15, 5))
        ctk.CTkLabel(self.current_frame, text="Стандартизированная шкала оценки степени угнетения сознания и функций ЦНС.", font=ctk.CTkFont(size=12), text_color="#6b7280").pack(anchor="w", padx=20, pady=(0, 15))

        ctk.CTkLabel(self.current_frame, text="Открывание глаз (E)", font=ctk.CTkFont(size=11, weight="bold")).pack(anchor="w", padx=20)
        c_e = ctk.CTkOptionMenu(self.current_frame, values=["4 - Спонтанное", "3 - На вербальный стимул", "2 - На болевой стимул", "1 - Отсутствует"], width=420, height=32, corner_radius=6, dropdown_font=ctk.CTkFont(size=12))
        c_e.pack(anchor="w", padx=20, pady=(2, 10))

        ctk.CTkLabel(self.current_frame, text="Речевой ответ (V)", font=ctk.CTkFont(size=11, weight="bold")).pack(anchor="w", padx=20)
        c_v = ctk.CTkOptionMenu(self.current_frame, values=["5 - Ориентирован, связная речь", "4 - Дезориентирован, спутанная речь", "3 - Неадекватные слова (крик/бессвязность)", "2 - Нечленораздельные звуки (стон)", "1 - Отсутствует"], width=420, height=32, corner_radius=6, dropdown_font=ctk.CTkFont(size=12))
        c_v.pack(anchor="w", padx=20, pady=(2, 10))

        ctk.CTkLabel(self.current_frame, text="Двигательный ответ (M)", font=ctk.CTkFont(size=11, weight="bold")).pack(anchor="w", padx=20)
        c_m = ctk.CTkOptionMenu(self.current_frame, values=["6 - Выполнение команд", "5 - Целенаправленная локализация боли", "4 - Защитное отдергивание конечности", "3 - Патологическое сгибание (декортикация)", "2 - Патологическое разгибание (децеребрация)", "1 - Отсутствует"], width=420, height=32, corner_radius=6, dropdown_font=ctk.CTkFont(size=12))
        c_m.pack(anchor="w", padx=20, pady=(2, 15))

        lbl_res = self.create_result_box(self.current_frame)

        def calc():
            e = 4 - ["4 - Спонтанное", "3 - На вербальный стимул", "2 - На болевой стимул", "1 - Отсутствует"].index(c_e.get())
            v = 5 - ["5 - Ориентирован, связная речь", "4 - Дезориентирован, спутанная речь", "3 - Неадекватные слова (крик/бессвязность)", "2 - Нечленораздельные звуки (стон)", "1 - Отсутствует"].index(c_v.get())
            m = 6 - ["6 - Выполнение команд", "5 - Целенаправленная локализация боли", "4 - Защитное отдергивание конечности", "3 - Патологическое сгибание (декортикация)", "2 - Патологическое разгибание (децеребрация)", "1 - Отсутствует"].index(c_m.get())
            total = e + v + m

            res = f"Суммарный балл GCS: {total} из 15 возможных\n\nСтатус угнетения интегративных функций мозга:\n"
            if total == 15: res += "🟢 ЯСНОЕ СОЗНАНИЕ\n- Пациент полностью ориентирован в пространстве, времени и собственной личности."
            elif total >= 13: res += "🟡 ЛЕГКОЕ ОГЛУШЕНИЕ\n- Умеренное снижение внимания, легкая заторможенность при сохранности базовых команд."
            elif total >= 9: res += "🟠 ГЛУБОКОЕ ОГЛУШЕНИЕ / СОПОР\n- Выраженная патологическая сонливость. Реакции активируются только на сильные триггеры (боль, громкий окрик)."
            else: res += "🚨 ТЯЖЕЛАЯ СТЕПЕНЬ (КОМА, 3-8 БАЛЛОВ)\n- Критическое состояние ЦНС. Потеря сознания.\n- ⚠️ КЛИНКА: Любые показатели GCS ≤ 8 баллов являются абсолютным показанием для экстренного перевода пациента на искусственную вентиляцию легких (ИВЛ) с целью превентивной защиты дыхательных путей от аспирации."
            lbl_res.configure(text=res)

        btn_calc = ctk.CTkButton(self.current_frame, text="Оценить статус ЦНС", font=ctk.CTkFont(weight="bold"), fg_color=self.COLOR_ACCENT, height=38, corner_radius=8, command=calc)
        btn_calc.pack(anchor="w", padx=20, pady=(5, 0))


if __name__ == "__main__":
    app = PremiumMedicalApp()
    app.mainloop()
