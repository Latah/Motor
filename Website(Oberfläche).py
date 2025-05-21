import tkinter as tk 
from tkinter import font 
 
# Funktion zur Motorsteuerung 
def motor_control(motor_id, direction): 
    print(f"Motor {motor_id} {'vorwärts' if direction == 'forward' else 'rückwärts'} läuft") 
 
# Fenster einrichten 
root = tk.Tk() 
root.title("Motorsteuerung") 
root.geometry("800x600") 
root.configure(bg="#f0f0f0") 
 
# Große Schriftarten definieren 
title_font = font.Font(family="Helvetica", size=36, weight="bold") 
motor_font = font.Font(family="Helvetica", size=28) 
button_font = font.Font(family="Helvetica", size=32, weight="bold") 
 
# Titel 
title_label = tk.Label(root, text="🛠️ Study Buddy", font=title_font, bg="#f0f0f0") 
title_label.pack(pady=30) 
 
# Rahmen für Motorsteuerung 
frame = tk.Frame(root, bg="#f0f0f0") 
frame.pack() 
 
# Für jeden Motor: Textfeld + zwei Buttons mit Pfeilen (nach außen zeigend) 
for i in range(4): 
    row = tk.Frame(frame, bg="#f0f0f0") 
    row.pack(pady=15) 
 
    # Label: Motor X 
    motor_label = tk.Label(row, text=f"Motor {i+1}", font=motor_font, width=10, anchor="center", bg="#f0f0f0") 
    motor_label.pack(side=tk.LEFT, padx=20) 
 
    # Button Vorwärts (←) 
    btn_fwd = tk.Button(row, text="←", font=button_font, fg="red", width=4, 
                        command=lambda i=i: motor_control(i+1, "forward")) 
    btn_fwd.pack(side=tk.LEFT, padx=20) 
 
    # Button Rückwärts (→) 
    btn_bwd = tk.Button(row, text="→", font=button_font, fg="green", width=4, 
                        command=lambda i=i: motor_control(i+1, "backward")) 
    btn_bwd.pack(side=tk.LEFT, padx=20) 
 
# Fenster starten 
root.mainloop() 
