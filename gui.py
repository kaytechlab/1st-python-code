import tkinter as tk
import requests

def send_message():
    user_message = entry.get()
    response = requests.post("http://127.0.0.1:5000/chatbot", json={"message": user_message})
    bot_response = response.json().get("response")
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_message + "\n")
    chat_log.insert(tk.END, "Bot: " + bot_response + "\n")
    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

app = tk.Tk()
app.title("UNIOSUN Chatbot")

frame = tk.Frame(app)
scrollbar = tk.Scrollbar(frame)
chat_log = tk.Text(frame, height=20, width=50, state=tk.DISABLED, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frame.pack(pady=10)

entry = tk.Entry(app, width=40)
entry.pack(pady=5)

send_button = tk.Button(app, text="Send", command=send_message)
send_button.pack(pady=5)

app.mainloop()