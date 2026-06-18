import customtkinter as ctk
import random

from sentences import (
    easy_sentences,
    medium_sentences,
    hard_sentences
)

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
        self.root.geometry("950x700")

        self.timer_started = False
        self.time_left = 60
        self.current_difficulty = "Medium"

        self.current_sentence = random.choice(
            medium_sentences
        )

        # TITLE
        self.title_label = ctk.CTkLabel(
            root,
            text="Typing Speed Tester",
            font=("Arial", 32, "bold")
        )
        self.title_label.pack(pady=20)

        # DIFFICULTY FRAME
        self.difficulty_frame = ctk.CTkFrame(root)
        self.difficulty_frame.pack(pady=10)

        self.easy_btn = ctk.CTkButton(
            self.difficulty_frame,
            text="Easy",
            command=lambda: self.set_difficulty("Easy")
        )
        self.easy_btn.grid(row=0, column=0, padx=10)

        self.medium_btn = ctk.CTkButton(
            self.difficulty_frame,
            text="Medium",
            command=lambda: self.set_difficulty("Medium")
        )
        self.medium_btn.grid(row=0, column=1, padx=10)

        self.hard_btn = ctk.CTkButton(
            self.difficulty_frame,
            text="Hard",
            command=lambda: self.set_difficulty("Hard")
        )
        self.hard_btn.grid(row=0, column=2, padx=10)

        # SENTENCE DISPLAY
        self.sentence_display = ctk.CTkTextbox(
            root,
            width=800,
            height=100,
            font=("Arial", 20)
        )

        self.sentence_display.pack(pady=20)

        self.sentence_display.insert(
            "1.0",
            self.current_sentence
        )

        self.sentence_display.tag_config(
            "correct",
            foreground="green"
        )

        self.sentence_display.tag_config(
            "wrong",
            foreground="red"
        )

        self.sentence_display.configure(
            state="disabled"
        )

        # TEXTBOX
        self.textbox = ctk.CTkTextbox(
            root,
            width=700,
            height=120,
            font=("Arial", 18)
        )

        self.textbox.pack(pady=20)

        self.textbox.bind(
            "<KeyRelease>",
            self.check_typing
        )

        # STATS FRAME
        self.stats_frame = ctk.CTkFrame(root)
        self.stats_frame.pack(pady=20)

        self.timer_label = ctk.CTkLabel(
            self.stats_frame,
            text="Time Left: 60s",
            font=("Arial", 20)
        )
        self.timer_label.grid(row=0, column=0, padx=30)

        self.wpm_label = ctk.CTkLabel(
            self.stats_frame,
            text="WPM: 0",
            font=("Arial", 20)
        )
        self.wpm_label.grid(row=0, column=1, padx=30)

        self.accuracy_label = ctk.CTkLabel(
            self.stats_frame,
            text="Accuracy: 0%",
            font=("Arial", 20)
        )
        self.accuracy_label.grid(row=0, column=2, padx=30)

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

    def set_difficulty(self, difficulty):

        self.current_difficulty = difficulty
        self.restart_test()

    def get_sentence_pool(self):

        if self.current_difficulty == "Easy":
            return easy_sentences

        elif self.current_difficulty == "Medium":
            return medium_sentences

        else:
            return hard_sentences

    def check_typing(self, event):

        typed_text = self.textbox.get("1.0", "end-1c")

        self.highlight_text(typed_text)

        if not self.timer_started and len(typed_text) > 0:
            start_timer()
            self.timer_started = True
            self.update_timer()

        wpm = calculate_wpm(typed_text)

        accuracy = calculate_accuracy(
            self.current_sentence,
            typed_text
        )

        self.wpm_label.configure(
            text=f"WPM: {wpm}"
        )

        self.accuracy_label.configure(
            text=f"Accuracy: {accuracy}%"
        )

    def highlight_text(self, typed_text):

        self.sentence_display.configure(
            state="normal"
        )

        self.sentence_display.delete(
            "1.0",
            "end"
        )

        for i, char in enumerate(self.current_sentence):

            if i < len(typed_text):

                if typed_text[i] == char:

                    self.sentence_display.insert(
                        "end",
                        char,
                        "correct"
                    )

                else:

                    self.sentence_display.insert(
                        "end",
                        char,
                        "wrong"
                    )

            else:

                self.sentence_display.insert(
                    "end",
                    char
                )

        self.sentence_display.configure(
            state="disabled"
        )

    def update_timer(self):

        if self.time_left > 0:

            self.time_left -= 1

            self.timer_label.configure(
                text=f"Time Left: {self.time_left}s"
            )

            self.root.after(
                1000,
                self.update_timer
            )

        else:

            self.textbox.configure(
                state="disabled"
            )

    def restart_test(self):

        self.timer_started = False
        self.time_left = 60

        sentence_pool = self.get_sentence_pool()

        self.current_sentence = random.choice(
            sentence_pool
        )

        self.sentence_display.configure(
            state="normal"
        )

        self.sentence_display.delete(
            "1.0",
            "end"
        )

        self.sentence_display.insert(
            "1.0",
            self.current_sentence
        )

        self.sentence_display.configure(
            state="disabled"
        )

        self.textbox.configure(
            state="normal"
        )

        self.textbox.delete(
            "1.0",
            "end"
        )

        self.timer_label.configure(
            text="Time Left: 60s"
        )

        self.wpm_label.configure(
            text="WPM: 0"
        )

        self.accuracy_label.configure(
            text="Accuracy: 0%"
        )