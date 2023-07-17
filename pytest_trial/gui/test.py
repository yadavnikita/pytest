from tkinter import *
import tkinter as tk
import sys
from tkinter.ttk import Combobox
import subprocess

class MyWindow:
    def __init__(self):
        self.window = Tk()


    def handle_selection(self, selection):
        print("Selected option:", selection)
        if selection == "Advance":
            print("select markers ")
            op = ["wifi_bt_parallel"]
            self.drop_down(options=op, header="Advance Markers", val=[200, 95])
        if selection == "Basic":
            print("select markers ")
            op = ["wifi_uut_band_b", "wifi_uut_band_g", "wifi_uut_band_a", "wifi_uut_band_bgn", "wifi_uut_band_an", "wifi_uut_band_ac", "wifi_uut_band_ax"]
            self.drop_down(options=op, header="Basic Markers", val=[200, 95])
        if selection == "wifi_bt_parallel":
            self.marker = f'coex_functionality_test and wifi_bt_parallel'
            print(self.marker)
        if selection == "wifi_uut_band_b":
            self.marker = f'coex_functionality_test and wifi_uut_band_b'
            print(self.marker)
        if selection == "wifi_uut_band_g":
            self.marker = f'coex_functionality_test and wifi_uut_band_g'
            print(self.marker)
        if selection == "wifi_uut_band_a":
            self.marker = f'coex_functionality_test and wifi_uut_band_a'
            print(self.marker)
        if selection == "wifi_uut_band_bgn":
            self.lbl4 = Label(self.window, text='cli to uut')
            self.lbl4.place(x=400, y=95)
            self.t1 = Entry()
            self.t1.place(x=500, y=95)

            self.marker = f'coex_functionality_test and wifi_uut_band_bgn'
            print(self.marker)

        return selection

    def drop_down(self, options, header, val):
        # options = ["Advance", "Basic", "Coex", "Option 4"]
        selected_option = tk.StringVar()  # Variable to store the selected option
        selected_option.set(header)  # Set the initial selected option
        option_menu = tk.OptionMenu(self.window, selected_option, *options, command=self.handle_selection)
        print("option menu", option_menu)
        option_menu.place(x=val[0], y=val[1])
        #option_menu.pack()

    def start(self):
        # run pytest
        global process
        self.cli = str(self.t1.get())
        print("cliiii", self.cli)
        process =subprocess.Popen(['pytest', '-m', self.marker, '-s',
                                   '-vvv', '--uut', '--alluredir=result',
                                   "--cli_check_uut_band", self.cli],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, cwd='../tests/')
        self.check_process_status()

    def result_allure(self):
        # run pytest
        global process_1
        process_1 =subprocess.Popen(['allure', 'serve', 'result/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, cwd='../tests/')
        self.check_process_status_()

    def check_process_status(self):
        if process.poll() is None:
            self.window.after(100, self.check_process_status)  # Check again after 100 milliseconds
        else:  # Process has completed
            stdout, stderr = process.communicate()  # Get the subprocess output

            print("Stdout:", stdout)
            print("Stderr:", stderr)
            print("Subprocess completed.")
            # once subprocess is done run allure

    def check_process_status_(self):
        if process_1.poll() is None:
            self.window.after(100, self.check_process_status)  # Check again after 100 milliseconds
        else:  # Process has completed
            stdout, stderr = process.communicate()  # Get the subprocess output

            print("Stdout:", stdout)
            print("Stderr:", stderr)
            print("Subprocess completed.")
            # once subprocess is done run allure


    def design(self):
        self.lbl1 = Label(self.window, text='Select Test')
        self.lbl2 = Label(self.window, text='Select Markers')
        self.lbl3 = Label(self.window, text='Select Testbed')


        options = ["Advance", "Basic", "Coex"]
        self.t1 = self.drop_down(options=options, header="Select Test", val=[200, 45])
        self.lbl1.place(x=50, y=50)
        # self.t1.place(x=200, y=50)
        self.lbl2.place(x=50, y=100)
        self.b1 = Button(self.window, text='Run', command=self.start)
        self.b2 = Button(self.window, text='Result', command=self.result_allure)
        self.b1.place(x=50, y=150)
        self.b2.place(x=200, y=150)
    def run(self):

        self.window.title("Pytest Testing Tool")
        # self.window.iconbitmap("/testing_icon-icons.com_72182.ico")
        self.window.minsize(700, 250)
        self.window.configure(background="gray25")
        self.design()
        self.window.mainloop()


def main():
    obj = MyWindow()
    obj.run()

if __name__ == '__main__':
    main()

