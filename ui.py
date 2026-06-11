import customtkinter as ctk
import random

from sentences import sentences
from logic import (
    start_timer,
    calculate_wpm,
    calculate_accuracy
)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class TypingSpeedApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Typing Speed Tester")

        self.root.geometry("900x600")

        self.timer_started = False

        self.current_sentence = random.choice(sentences)

        # TITLE

        self.title_label = ctk.CTkLabel(
            root,
            text="Typing Speed Tester",
            font=("Arial", 32, "bold")
        )

        self.title_label.pack(pady=20)

        # SENTENCE DISPLAY

        self.sentence_label = ctk.CTkLabel(
            root,
            text=self.current_sentence,
            wraplength=800,
            font=("Arial", 20)
        )

        self.sentence_label.pack(pady=20)

        # TEXTBOX

        self.textbox = ctk.CTkTextbox(
            root,
            width=700,
            height=120,
            font=("Arial", 18)
        )

        self.textbox.pack(pady=20)

        self.textbox.bind("<KeyRelease>", self.check_typing)

        # STATS FRAME

        self.stats_frame = ctk.CTkFrame(root)

        self.stats_frame.pack(pady=20)

        self.wpm_label = ctk.CTkLabel(
            self.stats_frame,
            text="WPM: 0",
            font=("Arial", 20)
        )

        self.wpm_label.grid(row=0, column=0, padx=30, pady=10)

        self.accuracy_label = ctk.CTkLabel(
            self.stats_frame,
            text="Accuracy: 0%",
            font=("Arial", 20)
        )

        self.accuracy_label.grid(row=0, column=1, padx=30, pady=10)

        # RESTART BUTTON

        self.restart_button = ctk.CTkButton(
            root,
            text="Restart",
            command=self.restart_test,
            width=200,
            height=50,
            font=("Arial", 18)
        )

        self.restart_button.pack(pady=20)

    def check_typing(self, event):

        typed_text = self.textbox.get("1.0", "end-1c")

        if not self.timer_started and len(typed_text) > 0:
            start_timer()
            self.timer_started = True

        wpm = calculate_wpm(typed_text)

        accuracy = calculate_accuracy(
            self.current_sentence,
            typed_text
        )

        self.wpm_label.configure(text=f"WPM: {wpm}")

        self.accuracy_label.configure(
            text=f"Accuracy: {accuracy}%"
        )

    def restart_test(self):

        self.timer_started = False

        self.current_sentence = random.choice(sentences)

        self.sentence_label.configure(
            text=self.current_sentence
        )

        self.textbox.delete("1.0", "end")

        self.wpm_label.configure(text="WPM: 0")

        self.accuracy_label.configure(
            text="Accuracy: 0%"
        )