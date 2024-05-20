
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.entry = tk.Entry(master, width=20, font=('Arial', 30))
        self.entry.grid(row=0, column=0, columnspan=10, padx=10, pady=30)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, width=10, height=4,
                               font=('Arial', 14),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, value):
        if value == '=':
            result = self.calculate()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        elif value == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, value)

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            return result
        except Exception as e:
            return "Error"

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()




