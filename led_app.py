import RPi.GPIO as GPIO
import tkinter as tk


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Led App")
        self.geometry("+450+300")

        self.green_led_status = tk.StringVar()
        self.red_led_status = tk.StringVar()

        self.button_green_on = tk.Button(self, text="green led on")
        self.button_green_on['command'] = lambda: self.green_led_on()
        self.button_green_on.grid(row=0, column=0, padx=5, sticky=tk.EW)

        self.button_green_off = tk.Button(self, text="green led off")
        self.button_green_off['command'] = lambda: self.green_led_off()
        self.button_green_off.grid(row=1, column=0, padx=5, sticky=tk.EW)

        self.button_red_on = tk.Button(self, text="red led on")
        self.button_red_on['command'] = lambda: self.red_led_on()
        self.button_red_on.grid(row=0, column=1, padx=5, sticky=tk.EW)

        self.button_red_off = tk.Button(self, text="red led off")
        self.button_red_off['command'] = lambda: self.red_led_off()
        self.button_red_off.grid(row=1, column=1, padx=5, sticky=tk.EW)

        self.text_red_led = tk.Entry(self, textvariable=self.red_led_status, justify="center", bd=5)
        self.text_red_led.grid(row=3, column=1, padx=5)

        self.text_green_led = tk.Entry(self, textvariable=self.green_led_status, justify="center", bd=5)
        self.text_green_led.grid(row=3, column=0, padx=5)

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(29, GPIO.OUT)
        GPIO.setup(31, GPIO.OUT)

    def green_led_on(self):
        GPIO.output(29, 1)
        self.green_led_status.set("Green led is on")

    def green_led_off(self):
        GPIO.output(29, 0)
        self.green_led_status.set("Green led is off")

    def red_led_on(self):
        GPIO.output(31, 1)
        self.red_led_status.set("Red led is on")

    def red_led_off(self):
        GPIO.output(31, 0)
        self.red_led_status.set("Red led is off")

    def main(self):
        self.mainloop()

    def clean_ports(self):
        GPIO.cleanup()


if __name__ == '__main__':
    app = App()
    app.main()
    app.clean_ports()
