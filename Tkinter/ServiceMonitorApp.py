import tkinter as tk
from tkinter import ttk
import psutil

class ServiceMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Service Monitor")
        self.root.geometry("400x200")

        self.create_widgets()

        # Update resource usage every second
        self.root.after(1000, self.update_usage)

    def create_widgets(self):
        self.label_cpu = ttk.Label(self.root, text="CPU Usage:")
        self.label_cpu.grid(row=0, column=0, padx=10, pady=10)

        self.label_memory = ttk.Label(self.root, text="Memory Usage:")
        self.label_memory.grid(row=1, column=0, padx=10, pady=10)

        self.quit_button = ttk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def update_usage(self):
        # Get CPU usage and update label
        cpu_percent = psutil.cpu_percent()
        self.label_cpu.config(text=f"CPU Usage: {cpu_percent:.2f}%")

        # Get memory usage and update label
        memory_info = psutil.virtual_memory()
        self.label_memory.config(text=f"Memory Usage: {memory_info.percent:.2f}%")

        # Schedule the next update
        self.root.after(1000, self.update_usage)

if __name__ == "__main__":
    root = tk.Tk()
    app = ServiceMonitorApp(root)
    root.mainloop()
