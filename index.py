from tkinter import *
from tkinter.ttk import Combobox

#Создание основного окна

def create_main_window():

	#Название паттерна

	def get_pattern_name(skin, pattern):

		if skin == "Glock-18 Лунная ночь":
			return "Звезда"

		elif skin == "Glock-18 Дальний свет":
			if pattern == "245" or pattern == "255" or pattern == "298" or pattern == "314" or pattern == "346" or pattern == "361" or pattern == "379" or pattern == "391" or pattern == "396" or pattern == "399" or pattern == "455" or pattern == "460" or pattern == "514" or pattern == "572" or pattern == "583" or pattern == "584" or pattern == "636" or pattern == "648" or pattern == "651" or pattern == "654" or pattern == "690" or pattern == "703" or pattern == "714" or pattern == "752" or pattern == "758" or pattern == "714" or pattern == "752" or pattern == "758" or pattern == "774" or pattern == "786" or pattern == "829" or pattern == "835" or pattern == "860" or pattern == "872" or pattern == "911" or pattern == "944" or pattern == "990":
				return "Full High Beam"		
			elif pattern == "302" or pattern == "487" or pattern == "508" or pattern == "597" or pattern == "639" or pattern == "800" or pattern == "936":
				return "Max High Beam"
			elif pattern == "511" or pattern == "550" or pattern == "897":
				return "Extreme High Beam"

		elif skin == "Glock-18 Реактор":
			if pattern == "108" or pattern == "126" or pattern == "395" or pattern == "511" or pattern == "527" or pattern == "571" or pattern == "628" or pattern == "702" or pattern == "742" or pattern == "763" or pattern == "848" or pattern == "892":
				return "Ядерные знаки"
			elif pattern == "923" or pattern == "281" or pattern == "152" or pattern == "743":
				return "Зубы"
			elif pattern == "204":
				return "Зубы + Ядерные знаки"
			elif pattern == "521" or pattern == "701" or pattern == "795" or pattern == "803" or pattern == "943":
				return "Кривые зубы"

		elif skin == "Glock-18 Жернов":
			if pattern == "88" or pattern == "179" or pattern == "262" or pattern == "273" or pattern == "301" or pattern == "311" or pattern == "312" or pattern == "324" or pattern == "336" or pattern == "364" or pattern == "382" or pattern == "431" or pattern == "463" or pattern == "528" or pattern == "547" or pattern == "579" or pattern == "658" or pattern == "667" or pattern == "769" or pattern == "804" or pattern == "865" or pattern == "866" or pattern == "878" or pattern == "902" or pattern == "931" or pattern == "955" or pattern == "957" or pattern == "974" or pattern == "979":
				return "Чёрный фейк"
			elif pattern == "79" or pattern == "298" or pattern == "384" or pattern == "387" or pattern == "737" or pattern == "894" or pattern == "907" or pattern == "933":
				return "Топовый чёрный фейк"
			elif pattern == "3" or pattern == "176" or pattern == "489" or pattern == "593" or pattern =="916":
				return "Идеальный чёрный"
		elif skin == "SSG-08 Пучина":
			if pattern == "796" or pattern == "16" or pattern == "32" or pattern == "79" or pattern == "146" or pattern == "436" or pattern == "451" or pattern == "517" or pattern == "548" or pattern == "661" or pattern == "736" or pattern == "771" or pattern == "794" or pattern == "871" or pattern == "910" or pattern == "995":
				return "Синяя пучина"
			elif pattern == "66" or pattern == "88" or pattern == "96" or pattern == "98" or pattern == "99" or pattern == "167" or pattern == "272" or pattern == "299" or pattern == "338" or pattern == "342" or pattern == "368" or pattern == "540" or pattern == "552":
				return "Тёмная пучина"
			elif pattern == "446" or pattern == "860" or pattern == "921" or pattern == "894":
				return "Монстр"

	#Получение значений редких паттернов

	def get_rare(skin):
		Glock_Munrise = [31, 59, 90, 95, 102, 121, 165, 194, 237, 281, 355, 385, 448, 484, 487, 617, 630, 667, 796, 769, 837, 913, 958, 968, 986]
		Glock_HighBeam = [245, 255, 298, 314, 346, 361, 379, 391, 396, 399, 355, 360, 514, 572, 583, 584, 636, 648, 651, 653, 690, 703, 714, 752, 758, 774, 786, 829, 835, 860, 872, 911, 944, 990, 302, 487, 508, 597, 639, 800, 936, 511, 550, 897]
		Glock_Reactor = [108, 126, 395, 511, 527, 571, 628, 702, 742, 763, 848, 892, 923, 281, 152, 743, 204, 521, 701, 795, 803, 943]
		Glock_Grinder = [88, 179, 262, 273, 3301, 311, 312, 324, 336, 364, 382, 431, 463, 528, 547, 579, 658, 667, 769, 804, 865, 866, 878, 902, 931, 955, 957, 974, 979, 79, 298, 384, 387, 737, 894, 907, 933, 3, 176, 489, 593, 916]
		SSG_Abyss = [796, 16, 32, 79, 146, 436, 451, 517, 548, 661, 736, 771, 794, 871, 910, 995, 66, 88, 96, 98, 99, 167, 272, 299, 338, 342, 368, 540, 552, 446, 860, 921, 894]
		if skin == "Glock-18 Лунная ночь":
			return Glock_Munrise
		elif skin == "Glock-18 Дальний свет":
			return Glock_HighBeam
		elif skin == "Glock-18 Реактор":
			return Glock_Reactor
		elif skin == "Glock-18 Жернов":
			return Glock_Grinder
		elif skin == "SSG-08 Пучина":
			return SSG_Abyss

	#Функция кнопки поиска

	def search(event):
		txt = []
		all_patterns = []
		rare_patterns = []
		txt.clear()
		all_patterns.clear()
		rare_patterns.clear()
		txt = entry1.get().split()
		entry1.delete(0,END)
		rare_list = get_rare(selected_gun + " " + selected_skin)
		for i in range(1, len(txt) + 1):
			if txt[i-1] == "Paint" and txt[i] == "Seed:":
				all_patterns.append(txt[i+1])
		for x in range(1, len(all_patterns)):
			for j in range(1, len(rare_list) + 1):
				if all_patterns[x-1] == str(rare_list[j-1]):
					rare_patterns.append(all_patterns[x-1])
					break
				else:
					continue
		if len(rare_patterns) <= 0:
			patterns_label.config(text="")
			result.config(text="Результат: Пусто")
		else:
			result.config(text="Результат: Редкие паттерны имеются")
			patterns_label.config(text="")
			for a in range(1, len(rare_patterns) + 1):
				patterns_label.config(text=patterns_label.cget("text") +rare_patterns[a-1] + " " + get_pattern_name(combo.get(), rare_patterns[a-1]) + "\n")
	
		#Создание окна настроек

	def create_settings_window(event):

		#Проверяем оружие

		def check_gun(event):
			if combo_gun.get() == "Glock-18":
				combo_skin['values'] = ("Лунная ночь", "Дальний свет", "Реактор", "Жернов")
			elif combo_gun.get() == "SSG-08":
				combo_skin['values'] = "Пучина"
			combo_skin.current(0)
			selected_gun = combo_gun.get()
			selected_skin = combo_skin.get()

		#Проверяем скин

		def get_skin(event):
			selected_gun = combo_gun.get()
			selected_skin = combo_skin.get()

		#Параметры окна

		settings_window = Tk()
		settings_window.title("Выбор скина")
		settings_window.configure(background="#ddd")
		settings_window.resizable(0,0)
		settings_window.geometry('310x350')

		gun_label = Label(settings_window, text="Выбор оружия:", background="#ddd")

		combo_gun = Combobox(settings_window, state="readonly", width = 25)  
		combo_gun['values'] = ("Glock-18", "SSG-08")  
		combo_gun.current(0)
		combo_gun.bind("<<ComboboxSelected>>", check_gun)

		skin_label = Label(settings_window, text="Выбор cкина:", background="#ddd")

		combo_skin = Combobox(settings_window, state="readonly", width = 25)  
		combo_skin['values'] = ("Лунная ночь", "Дальний свет", "Реактор", "Жернов")  
		combo_skin.current(0) 
		combo_skin.bind("<<ComboboxSelected>>", get_skin)

		gun_label.grid(column=0, row=0, sticky="w", pady=10, padx=10)
		combo_gun.grid(column=1, row=0, columnspan=3, sticky="we", pady=10, padx=10)
		skin_label.grid(column=0, row=1, sticky="w", pady=10, padx=10)
		combo_skin.grid(column=1, row=1, columnspan=3, sticky="we", pady=10, padx=10)

		settings_window.mainloop()

	#переменные

	selected_gun = "Glock-18"
	selected_skin = "Лунная ночь"

	#Параметры окна
	main_window = Tk() 
	main_window.configure(background="#ddd")
	main_window.title("Pattern Search by V1nt") 
	main_window.resizable(0,0)
	main_window.geometry('310x350')
	
	l1 = Label(main_window, text="Выбор скина:", background="#ddd")
	l2 = Label(main_window, text="Текст страницы:", background="#ddd")
	result = Label(main_window, text="Результат: ", background="#ddd")
	patterns_label = Label(main_window, text="", background="#ddd")
	settings_btn = Button(main_window, text="Параметры", width = 25, foreground="#ccc", background="#555", bd=0)  
	search_btn = Button(main_window, text="Поиск", width = 35, foreground="#ccc", background="#555", bd=0)
	search_btn.bind("<Button-1>", search)
	settings_btn.bind("<Button-1>", create_settings_window)   	
	entry1 = Entry(main_window, width = 30, bd=0)
	
	l1.grid(column=0, row=0, sticky="w", pady=10, padx=10)
	settings_btn.grid(column=1, row=0, columnspan=3, sticky="we")
	l2.grid(column=0, row=1, pady=10, padx=10, sticky="w")
	entry1.grid(column=1, row=1, columnspan=3) 	
	search_btn.grid(column=0, row=2, pady=10, padx = 25, sticky="w", columnspan=5)	
	result.grid(column=0, row=3, pady=10, padx = 10, sticky="w", columnspan=5)
	patterns_label.grid(column=0, row=4, padx=10, pady=10, sticky="w", columnspan=5)
	
	main_window.mainloop()

create_main_window()