import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import serial.tools.list_ports

class ESPBackupRestoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ESP8266 Backup and Restore")
        
        self.label = tk.Label(root, text="ESP8266 Backup and Restore Tool")
        self.label.pack(pady=10)

        self.com_port_label = tk.Label(root, text="Select COM Port:")
        self.com_port_label.pack(pady=5)
        
        self.com_port_combobox = ttk.Combobox(root, values=self.get_com_ports())
        self.com_port_combobox.pack(pady=5)

        self.refresh_button = tk.Button(root, text="Refresh COM Ports", command=self.refresh_com_ports)
        self.refresh_button.pack(pady=5)

        self.backup_button = tk.Button(root, text="Backup", command=self.backup)
        self.backup_button.pack(pady=5)
        
        self.restore_button = tk.Button(root, text="Restore", command=self.restore)
        self.restore_button.pack(pady=5)

        self.log_text = tk.Text(root, height=20, width=80)
        self.log_text.pack(pady=10)
        
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=10)
        
    def get_com_ports(self):
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def refresh_com_ports(self):
        self.com_port_combobox['values'] = self.get_com_ports()

    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def backup(self):
        com_port = self.com_port_combobox.get()
        if not com_port:
            messagebox.showerror("Error", "Please select a COM port.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Binary files", "*.bin")])
        if file_path:
            try:
                self.status_label.config(text="Backing up...")
                command = f"python -m esptool --chip esp8266 --port {com_port} --baud 921600 read_flash 0 0x400000 {file_path}"
                self.log(f"Executing: {command}")
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                self.log(result.stdout)
                if result.returncode == 0:
                    messagebox.showinfo("Success", "Backup completed successfully!")
                else:
                    self.log(result.stderr)
                    messagebox.showerror("Error", f"Backup failed:\n{result.stderr}")
            finally:
                self.status_label.config(text="")

    def restore(self):
        com_port = self.com_port_combobox.get()
        if not com_port:
            messagebox.showerror("Error", "Please select a COM port.")
            return

        file_path = filedialog.askopenfilename(filetypes=[("Binary files", "*.bin")])
        if file_path:
            try:
                self.status_label.config(text="Restoring...")
                command = f"python -m esptool --chip esp8266 --port {com_port} --baud 921600 write_flash 0 {file_path}"
                self.log(f"Executing: {command}")
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                self.log(result.stdout)
                if result.returncode == 0:
                    messagebox.showinfo("Success", "Restore completed successfully!")
                else:
                    self.log(result.stderr)
                    messagebox.showerror("Error", f"Restore failed:\n{result.stderr}")
            finally:
                self.status_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = ESPBackupRestoreApp(root)
    root.mainloop()
