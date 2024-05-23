import tkinter as tk
from tkinter import ttk
import psutil


class ServiceMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Service Monitor")
        self.root.geometry("400x200")

        self.label = ttk.Label(self.root, text="Service with Highest CPU Usage:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.highest_cpu_label = ttk.Label(self.root, text="")
        self.highest_cpu_label.grid(row=1, column=0, padx=10, pady=10)

        self.quit_button = ttk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.grid(row=2, column=0, pady=10)

        # Update highest CPU service every second
        self.root.after(1000, self.update_highest_cpu)

    def update_highest_cpu(self):
        # Get a list of running processes
        processes = psutil.process_iter(['pid', 'name', 'cpu_percent'])

        # Find the process with the highest CPU usage
        highest_cpu_process = max(processes, key=lambda x: x.info['cpu_percent'], default=None)

        # Update the label with the process name and CPU usage
        if highest_cpu_process:
            process_name = highest_cpu_process.info['name']
            cpu_percent = highest_cpu_process.info['cpu_percent']
            self.highest_cpu_label.config(text=f"{process_name} - {cpu_percent:.2f}%")
        else:
            self.highest_cpu_label.config(text="No running processes.")

        # Schedule the next update
        self.root.after(1000, self.update_highest_cpu)


if __name__ == "__main__":
    root = tk.Tk()
    app = ServiceMonitorApp(root)
    root.mainloop()
