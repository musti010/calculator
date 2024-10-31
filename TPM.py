import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class MultiMachineTPMCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TPM Time Calculator for 6 Machines")
        self.geometry("500x400")

        # Input fields for each machine
        self.inputs = []
        for i in range(6):
            frame = tk.Frame(self)
            frame.pack(pady=5)
            tk.Label(frame, text=f"Machine {i + 1}").pack(side=tk.LEFT, padx=5)

            tk.Label(frame, text="Total Cycles:").pack(side=tk.LEFT, padx=5)
            total_cycles_entry = tk.Entry(frame, width=5)
            total_cycles_entry.pack(side=tk.LEFT)

            tk.Label(frame, text="Current Cycle:").pack(side=tk.LEFT, padx=5)
            current_cycle_entry = tk.Entry(frame, width=5)
            current_cycle_entry.pack(side=tk.LEFT)

            tk.Label(frame, text="Time per Cycle (s):").pack(side=tk.LEFT, padx=5)
            time_cycle_entry = tk.Entry(frame, width=5)
            time_cycle_entry.pack(side=tk.LEFT)

            self.inputs.append((total_cycles_entry, current_cycle_entry, time_cycle_entry))

        # Current time input
        tk.Label(self, text="Current Time (HH:MM):").pack(pady=5)
        self.current_time_entry = tk.Entry(self)
        self.current_time_entry.pack()

        # Calculate button
        tk.Button(self, text="Calculate", command=self.calculate_tpm_times).pack(pady=10)

        # Output text box
        self.result_text = tk.Text(self, height=10, width=60)
        self.result_text.pack()

        # Copy to clipboard button
        tk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)

    def calculate_tpm_times(self):
        self.result_text.delete("1.0", tk.END)
        try:
            current_time_str = self.current_time_entry.get()
            current_time = datetime.strptime(current_time_str, "%H:%M")
            results = []

            for index, (total_cycles_entry, current_cycle_entry, time_cycle_entry) in enumerate(self.inputs):
                total_cycles = int(total_cycles_entry.get())
                current_cycle = int(current_cycle_entry.get())
                time_per_cycle = float(time_cycle_entry.get())

                remaining_cycles = total_cycles - current_cycle
                total_time_seconds = remaining_cycles * time_per_cycle
                next_tpm_time = current_time + timedelta(seconds=total_time_seconds)
                formatted_time = next_tpm_time.strftime("%H:%M")

                result = f"Machine {index + 1}: Next TPM Time: {formatted_time}"
                results.append(result)
                self.result_text.insert(tk.END, result + "\n")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers and time.")
            return

    def copy_to_clipboard(self):
        result_text = self.result_text.get("1.0", tk.END).strip()
        self.clipboard_clear()
        self.clipboard_append(result_text)
        self.update()
        messagebox.showinfo("Copied", "Results copied to clipboard!")

if __name__ == "__main__":
    app = MultiMachineTPMCalculator()
    app.mainloop()
