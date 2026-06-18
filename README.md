# ⌨️ Typing Speed Tester V2.3

![Python](https://img.shields.io/badge/Python-3.x-blue)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Version](https://img.shields.io/badge/Version-2.3-orange)

A clean and modern **Typing Speed Tester** built with **Python** and **CustomTkinter**.  
The application measures your **Words Per Minute (WPM)** and **Typing Accuracy** in real time while practicing with randomly selected sentences.

Now upgraded with **countdown timer**, **live character highlighting**, **difficulty modes**, and **persistent high score tracking**.

---

## ✨ Features

- 🚀 Real-time WPM calculation
- 🎯 Live accuracy tracking
- ⏱️ 60-second countdown timer
- 🟢 Live correct character highlighting
- 🔴 Live wrong character highlighting
- 📚 Difficulty modes (Easy / Medium / Hard)
- 🏆 Persistent high score tracking
- 🔄 Restart test anytime
- 📝 Random practice sentences
- 🌙 Modern dark-themed UI
- 🖥️ Built using CustomTkinter

---

## 🆕 What's New in V2.3

### V2.0
- ⏱️ Added **60-second countdown timer**
- ▶️ Timer starts automatically on first key press
- 🔒 Typing box disables when timer reaches zero
- 🔄 Restart fully resets timer and stats

### V2.1
- 🟢 Added **live character highlighting**
- 🔴 Correct input turns green
- ❌ Wrong input turns red
- 🎯 Improved real-time typing feedback

### V2.2
- 📚 Added **Difficulty Modes**
- 🟢 Easy → short/simple sentences
- 🟡 Medium → balanced sentence difficulty
- 🔴 Hard → long/complex sentences

### V2.3
- 🏆 Added **High Score System**
- 💾 Best WPM stored in `highscore.json`
- 💾 Best Accuracy stored in `highscore.json`
- 🔄 Auto-loads high scores on startup
- 📈 Tracks performance progression across sessions

---

## 📸 Screenshots

### V2.3 Updated UI
![V2.3](screenshots/V2.3.png)

---

## 📂 Project Structure

```text
.
├── main.py
├── ui.py
├── logic.py
├── sentences.py
├── highscore.json
├── screenshots/
│   ├── menu.png
│   ├── speed_test.png
│   └── V2.3.png
└── README.md
```

---

## ⚙️ Installation

```bash
git clone <repository-url>
cd typing-speed-tester
pip install customtkinter
```

---

## ▶️ Run

```bash
python main.py
```

---

## 🛠️ Tech Stack

- Python
- CustomTkinter
- Tkinter
- JSON (High Score Storage)

---

## 👨‍💻 Author

**Yash Kumar Singh**

---

⭐ If you like this project, consider giving it a star.