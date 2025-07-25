import tkinter
root = tkinter.Tk()
root.geometry("500x500")
root.title("BMI CALCI")
root.config(bg="white")

head = tkinter.Label(root, text="BMI CALCI", font=("Arial", 20, "bold"), bg="white")
head.pack(pady=20)

frame = tkinter.Frame(root, bg="white")
frame.pack(pady=10)

ht_cm_label = tkinter.Label(frame, text="Height (in cm)", font=("Arial", 15), bg="white")
ht_cm_label.grid(row=0, column=0, padx=10, pady=5)

ht_cm_entry = tkinter.Entry(frame)
ht_cm_entry.grid(row=0, column=1, padx=10, pady=5)

ht_m_label = tkinter.Label(frame, text="Height (in m)", font=("Arial", 15), bg="white")
ht_m_label.grid(row=1, column=0, padx=10, pady=5)

ht_m_entry = tkinter.Entry(frame)
ht_m_entry.grid(row=1, column=1, padx=10, pady=5)

root.mainloop()
