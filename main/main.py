from tkinter import *
from logic import generate_key


def change_key(key):
    """Rewrite answer Entry with new generated key."""
    answer.delete(0,END)
    answer.insert(0,key)

main_window = Tk()
main_window.title("Django secret key generator.")
main_window.geometry('550x150')

main_frame = Frame(
    main_window,
    padx=10,
    pady=10
)

main_frame.pack(expand=True)

main_label = Label(
    main_frame,
    text='Generate your django secret key:'
)
main_label.grid(row=2, column=1)

answer = Entry(
    main_frame,
    width='60',
)
answer.grid(row=3, column=1,pady=5)

main_button = Button(
    main_frame,
    text='Generate',
    command=lambda: change_key(generate_key())
)
main_button.grid(row=3, column=2,padx=5)

if __name__ == "__main__":
    main_window.mainloop()