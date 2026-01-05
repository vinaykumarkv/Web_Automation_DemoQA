import tkinter as tk
from main import WebAutomation as wa
from tkinter import messagebox


class App:
    def __init__(self, root):
        self.root = root
        #self.root.geometry('350x300')
        #self.root.resizable(False, False)
        self.root.title('Web Automation DemoQA GUI')

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=50, pady=10)
        tk.Label(self.login_frame, text='Username:').grid(row=0, column=0, sticky='w')
        self.entry_username = tk.Entry(self.login_frame, textvariable=tk.StringVar())
        self.entry_username.grid(row=0, column=1, sticky='ew')
        tk.Label(self.login_frame, text='Password:').grid(row=1, column=0, sticky='w')
        self.entry_password = tk.Entry(self.login_frame, show="*", textvariable=tk.StringVar())
        self.entry_password.grid(row=1, column=1, sticky='ew')

        self.form_submission = tk.Frame(self.root)
        self.form_submission.pack(padx=10, pady=10)
        tk.Label(self.form_submission, text='Full Name:').grid(row=0, column=0, sticky='w')
        self.entry_full_name = tk.Entry(self.form_submission, textvariable=tk.StringVar())
        self.entry_full_name.grid(row=0, column=1, sticky='ew')
        tk.Label(self.form_submission, text='Email ID:').grid(row=1, column=0, sticky='w')
        self.entry_email_id = tk.Entry(self.form_submission, textvariable=tk.StringVar())
        self.entry_email_id.grid(row=1, column=1, sticky='ew')
        tk.Label(self.form_submission, text='Current Address:').grid(row=2, column=0, sticky='w')
        self.entry_current_address = tk.Entry(self.form_submission, textvariable=tk.StringVar())
        self.entry_current_address.grid(row=2, column=1, sticky='ew')
        tk.Label(self.form_submission, text='Permanent Address:').grid(row=3, column=0, sticky='w')
        self.entry_permanent_address = tk.Entry(self.form_submission, textvariable=tk.StringVar())
        self.entry_permanent_address.grid(row=3, column=1, sticky='ew')

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(padx=100, pady=10)
        tk.Button(
            self.button_frame, text='Submit', command=self.submit_data).grid(row=0, column=0,  padx=10)
        tk.Button(self.button_frame, text='Close Browser', command=self.close_window).grid(row=0, column=1,  padx=5)

    def submit_data(self):
        un = self.entry_username.get()
        ps = self.entry_password.get()
        full_name = self.entry_full_name.get()
        email = self.entry_email_id.get()
        current_address = self.entry_current_address.get()
        permanent_address = self.entry_permanent_address.get()
        self.d = wa()
        self.d.login(un, ps)
        self.d.fillform(full_name, email, current_address, permanent_address)
        messagebox.showinfo('Success', 'Submitted Successfully')


    def close_window(self):
        self.d.close()
        messagebox.showinfo('Success', 'Browser Closed')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
