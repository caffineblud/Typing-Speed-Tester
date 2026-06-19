# ⌨️ Typing Speed Tester

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-GUI-1F6AA5?style=flat-square&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-22c55e?style=flat-square)

> A typing speed test built **twice** — once as a Python desktop app, once as a vanilla web app. Same core idea, two completely different implementations. Pick your platform.

---

## 📸 Preview

<table align="center">
<tr>
<td><img src="https://raw.githubusercontent.com/caffineblud/typing-speed-tester/main/desktop%20version/screenshots/V2.3.png" width="430" alt="Desktop Edition"/></td>
<td><img src="https://raw.githubusercontent.com/caffineblud/typing-speed-tester/main/web%20version/screenshots/V3.0.png" width="430" alt="Web Edition"/></td>
</tr>
<tr>
<td align="center"><b>🖥️ Desktop Edition (V2.4)</b></td>
<td align="center"><b>🌐 Web Edition (V3.0)</b></td>
</tr>
</table>

---

## 🧭 Choose Your Version

| | 🖥️ Desktop Edition | 🌐 Web Edition |
|---|---|---|
| **Stack** | Python + CustomTkinter | HTML + CSS + JavaScript |
| **Run Requirement** | Python + pip install | Just a browser |
| **High Score Storage** | `highscore.json` (file) | `localStorage` (browser) |
| **Highlighting Method** | `CTkTextbox` text tags | One `<span>` per character |
| **Audio** | `playsound` on daemon threads | HTML5 `Audio` API |
| **Best for** | Offline practice, native desktop feel | Quick access, no install, shareable link |
| **Docs** | [Desktop Documentation →](./desktop%20version/README.md) | [Web Documentation →](./web%20version/README.md) |

---

## ✨ Shared Features (Both Versions)

- 🚀 Real-time WPM calculation
- 🎯 Live accuracy tracking
- ⏱️ 60-second countdown timer, starts on first keystroke
- 🟢🔴 Live correct/wrong character highlighting
- 📚 Difficulty modes — Easy / Medium / Hard
- 🏆 Persistent high score tracking
- 🔊 Sound feedback — keystroke, error, and finish sounds
- 🔄 Instant restart
- 🌙 Dark-themed UI

---

## 🗂️ Repository Structure

```
typing-speed-tester/
│
├── README.md                     # 📍 You are here
├── .gitignore
│
├── desktop version/               # 🖥️  Python Edition (V2.x)
│   ├── main.py
│   ├── ui.py
│   ├── logic.py
│   ├── sentences.py
│   ├── highscore.json
│   ├── requirements.txt
│   ├── sounds/
│   ├── screenshots/
│   └── README.md                  # → Full desktop documentation
│
└── web version/                   # 🌐 Web Edition (V3.x)
    ├── index.html
    ├── style.css
    ├── script.js
    ├── sentences.js
    ├── sounds/
    ├── screenshots/
    └── README.md                  # → Full web documentation
```

---

## ⚡ Quick Start

### Desktop Edition
```bash
cd "desktop version"
pip install -r requirements.txt
python main.py
```

### Web Edition
```bash
cd "web version"
# just open index.html in your browser
```

For full setup, architecture, and feature breakdowns, see each version's own README linked above.

---

## 🆕 Version Timeline

| Version | Edition | Highlights |
|---|---|---|
| **V2.0 – V2.4** | 🖥️ Desktop | Countdown timer → live highlighting → difficulty modes → high scores → sound effects |
| **V3.0** | 🌐 Web | Full rebuild as a zero-dependency browser app with the same core feature set |

---

## 🔮 Roadmap

- [ ] 📊 WPM-over-time graphs (both versions)
- [ ] 🌐 Deploy web version live (GitHub Pages / Vercel)
- [ ] 🎨 Theme switcher
- [ ] ⌨️ Custom sentence import
- [ ] 🏆 Online leaderboard (web version)

---

## 👨‍💻 Author

<div align="center">

**Yash Kumar Singh**

[![GitHub](https://img.shields.io/badge/GitHub-caffineblud-181717?style=flat-square&logo=github)](https://github.com/caffineblud)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Yash_Kumar_Singh-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/yash-kumar-singh-8a4b193b1)

⭐ If you like this project, consider giving it a star.

</div>