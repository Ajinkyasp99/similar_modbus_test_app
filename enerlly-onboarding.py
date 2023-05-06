import customtkinter
import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Enerlly Onboarding App")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "enerlly-logo.png")), size=(30, 30))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "bg_gradient.jpg")), size=(3000, 60))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "enerlly-logo.png")), size=(20, 20))
        self.modbus_test_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "modbus.png")),
                                                        dark_image=Image.open(os.path.join(image_path, "modbus.png")), size=(30, 30))
        self.tcp_ip_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "tcp-ip.png")),
                                                   dark_image=Image.open(os.path.join(image_path, "tcp-ip.png")), size=(30, 30))
        self.json_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,
                                                                                     "json-image.png")),
                                                 dark_image=Image.open(os.path.join(image_path,
                                                                                    "json-image.png")), size=(30, 30))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame, text="  Enerlly", image=self.logo_image, width=20,
                                                             compound="left", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=15, pady=15)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Modbus Serial Test",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.modbus_test_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Modbus TCP IP Test",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.tcp_ip_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Create Device Json",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.json_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid(padx=0)
        self.home_frame.grid_columnconfigure(0, weight=1)

        #  n, e, s, w
        frame_1_sub_f = customtkinter.CTkFrame(
            master=self.home_frame, width=400, height=400, fg_color="transparent", corner_radius=0,
        )
        frame_1_sub_f.grid_columnconfigure(3, weight=1)
        frame_1_sub_f.grid(row=4, column=0, pady=20, padx=20, sticky="nsew")


        # frame_2_sub_f = customtkinter.CTkFrame(
        #     master=frame_1_sub_f, bg_color="red", height=500
        # )
        # frame_2_sub_f.place(x=15, y=7, anchor="se")


        # self.connect_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "enerlly-logo.png")),
        #                                          size=(30, 30))
        # self.connect_img.grid(row=1, column=1, pady=20, padx=20, sticky="e")
        label_1 = customtkinter.CTkLabel(
            master=frame_1_sub_f, font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="transparent",
            text="Starting Address :"
        )
        # label_1.anchor("nw")
        label_1.grid(row=2, column=0, sticky="w",  pady=8, padx=25)
        self.entry_1 = customtkinter.CTkEntry(
            frame_1_sub_f, placeholder_text="Starting Address For eg: L&T 100", width=300
        )
        self.entry_1.grid(row=2, column=1, pady=8, padx=10)

        label_2 = customtkinter.CTkLabel(
            master=frame_1_sub_f, font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="transparent",
            text="Number of Count :"
        )
        label_2.grid(row=3, column=0, sticky="w", pady=8, padx=25)
        self.entry_2 = customtkinter.CTkEntry(
            frame_1_sub_f, placeholder_text="Number of reading counts", width=300
        )
        self.entry_2.grid(row=3, column=1, pady=8, padx=10)

        label_3 = customtkinter.CTkLabel(
            master=frame_1_sub_f, font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="transparent",
            text="Slave ID of Meter :"
        )
        label_3.grid(row=4, column=0, sticky="w", pady=8, padx=25)
        self.entry_3 = customtkinter.CTkEntry(
            frame_1_sub_f, placeholder_text="Slave id of meter", width=300
        )
        self.entry_3.grid(row=4, column=1, pady=8, padx=10)

        label_4 = customtkinter.CTkLabel(
            master=frame_1_sub_f, font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="transparent",
            text="Baudrate :"
        )
        label_4.grid(row=5, column=0, sticky="w", pady=8, padx=25)
        boudrate_list = ["9600", "110", "300", "600", "1200", "2400", "4800", "14400", "19200", "38400", "57600",
                         "115200", "128000", "256000"]
        combobox_1 = customtkinter.CTkComboBox(frame_1_sub_f, values=boudrate_list, width=200)
        combobox_1.grid(row=5, column=1, sticky="w", pady=8, padx=25)



        label_5 = customtkinter.CTkLabel(
            master=frame_1_sub_f, font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="transparent",
            text="Port :"
        )
        label_5.grid(row=6, column=0, sticky="w", pady=8, padx=25)
        port_list = ["/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyUSB2", "/dev/ttyUSB3", "/dev/ttyUSB4", "/dev/ttyUSB5"]
        combobox_2 = customtkinter.CTkComboBox(frame_1_sub_f, values=port_list, width=200)
        combobox_2.grid(row=6, column=1, sticky="w", pady=8, padx=25)

        label_6 = customtkinter.CTkLabel(
            master=frame_1_sub_f, font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="transparent",
            text="Parity :"
        )
        label_6.grid(row=7, column=0, sticky="w", pady=8, padx=25)
        parity_list = ["EVEN", "ODD", "NONE"]
        combobox_3 = customtkinter.CTkComboBox(frame_1_sub_f, values=parity_list, width=200)
        combobox_3.grid(row=7, column=1, sticky="w", pady=8, padx=25)

        label_7 = customtkinter.CTkLabel(
            master=frame_1_sub_f, font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="transparent",
            text="Word Length :"
        )
        label_7.grid(row=8, column=0, sticky="w", pady=8, padx=25)
        parity_list = ["8", "7"]
        combobox_4 = customtkinter.CTkComboBox(frame_1_sub_f, values=parity_list, width=200)
        combobox_4.grid(row=8, column=1, sticky="w", pady=8, padx=25)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self.home_frame, width=250, height=200)
        self.textbox.grid(row=9, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")


        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.home_frame, text="Modbus Serial Test", image=self.large_test_image, font=customtkinter.CTkFont(size=30, weight="bold")
        )
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        # self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        # self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        # self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        # self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        # self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        # self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.columnconfigure(1, weight=1)
        self.second_frame.grid(padx=0)
        self.grid_rowconfigure(2, weight=1)

        self.f1 = customtkinter.CTkLabel(
            self.second_frame, text="Modbus TCP IP Test", image=self.large_test_image, font=customtkinter.CTkFont(size=30, weight="bold")
        )
        self.f1.grid(row=1, column=1, padx=25, pady=10)
        #
        self.f2 = customtkinter.CTkFrame(
            self.second_frame,  bg_color="red", width=550, height=350
        )
        self.f2.grid(row=2, column=0, padx=20, pady=10)
        self.f2.place(x=25, y=100)

        self.f3 = customtkinter.CTkFrame(
            self.second_frame,  bg_color="blue", width=550, height=255
        )
        # self.f3.grid(row=2, column=1, padx=20, pady=10)
        self.f3.place(x=600, y=100)

        label_1 = customtkinter.CTkLabel(
            master=self.f2, font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="transparent",
            text="TCp IP Address :"
        )
        # label_1.anchor("nw")
        label_1.grid(row=2, column=0, sticky="w", pady=18, padx=25)
        self.entry_1 = customtkinter.CTkEntry(
            self.f2, placeholder_text="192.168.0.1", width=350
        )
        self.entry_1.grid(row=2, column=1, pady=18, padx=10)

        label_2 = customtkinter.CTkLabel(
            master=self.f2, font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="transparent",
            text="Number of Count :"
        )
        label_2.grid(row=3, column=0, sticky="w", pady=15, padx=25)
        self.entry_2 = customtkinter.CTkEntry(
            self.f2, placeholder_text="Number of reading counts", width=350
        )
        self.entry_2.grid(row=3, column=1, pady=18, padx=10)

        label_3 = customtkinter.CTkLabel(
            master=self.f2, font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="transparent",
            text="Slave ID of Meter :"
        )
        label_3.grid(row=4, column=0, sticky="w", pady=18, padx=25)
        self.entry_3 = customtkinter.CTkEntry(
            self.f2, placeholder_text="Slave id of meter", width=350
        )
        self.entry_3.grid(row=4, column=1, pady=18, padx=10)

        label_4 = customtkinter.CTkLabel(
            master=self.f2, font=customtkinter.CTkFont(size=14, weight="bold"), fg_color="transparent",
            text="Baudrate :"
        )
        label_4.grid(row=5, column=0, sticky="w", pady=18, padx=25)

        self.entry_4 = customtkinter.CTkEntry(
            self.f2, placeholder_text="Starting Address", width=350
        )
        self.entry_4.grid(row=5, column=1, pady=18, padx=10)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self.second_frame, width=250, height=200)
        self.textbox.place(x=800, y=500)
        # self.textbox.grid(row=15, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("frame_2")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()

