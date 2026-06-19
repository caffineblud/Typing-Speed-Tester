let currentSentence = "";
let startTime = null;
let timer = 60;
let timerInterval = null;
let difficulty = "easy";

const typingBox = document.getElementById("typing-box");
const sentenceBox = document.getElementById("sentence-box");

const keySound = new Audio("sounds/key.wav");
const errorSound = new Audio("sounds/error.wav");
const finishSound = new Audio("sounds/finish.wav");

function loadSentence() {
    const list = sentences[difficulty];
    currentSentence =
        list[Math.floor(Math.random() * list.length)];

    sentenceBox.innerHTML =
        currentSentence
        .split("")
        .map(char => `<span>${char}</span>`)
        .join("");

    typingBox.value = "";
}

function setDifficulty(level) {
    difficulty = level;
    restartTest();
}

function startTimer() {
    timerInterval = setInterval(() => {
        timer--;
        document.getElementById("timer").innerText =
            `Time: ${timer}s`;

        if (timer <= 0) {
            clearInterval(timerInterval);
            typingBox.disabled = true;
            finishSound.play();
            saveHighScore();
        }
    }, 1000);
}

function calculateWPM(text) {
    const minutes =
        (60 - timer) / 60;

    if (minutes === 0) return 0;

    return Math.round(
        (text.length / 5) / minutes
    );
}

function calculateAccuracy(text) {
    let correct = 0;

    for (let i = 0; i < text.length; i++) {
        if (text[i] === currentSentence[i]) {
            correct++;
        }
    }

    return text.length === 0
        ? 0
        : Math.round((correct / text.length) * 100);
}

function saveHighScore() {
    const wpm =
        parseInt(document.getElementById("wpm").innerText.split(": ")[1]);

    const accuracy =
        parseInt(document.getElementById("accuracy").innerText.split(": ")[1]);

    let bestWPM =
        localStorage.getItem("bestWPM") || 0;

    let bestAccuracy =
        localStorage.getItem("bestAccuracy") || 0;

    if (wpm > bestWPM)
        localStorage.setItem("bestWPM", wpm);

    if (accuracy > bestAccuracy)
        localStorage.setItem("bestAccuracy", accuracy);

    loadHighScores();
}

function loadHighScores() {
    document.getElementById("best-wpm").innerText =
        `Best WPM: ${localStorage.getItem("bestWPM") || 0}`;

    document.getElementById("best-accuracy").innerText =
        `Best Accuracy: ${localStorage.getItem("bestAccuracy") || 0}%`;
}

typingBox.addEventListener("input", () => {
    if (!startTime) {
        startTime = Date.now();
        startTimer();
    }

    keySound.currentTime = 0;
    keySound.play();

    const typed = typingBox.value;
    const spans = sentenceBox.querySelectorAll("span");

    spans.forEach((span, index) => {
        const char = typed[index];

        if (char == null) {
            span.className = "";
        } else if (char === span.innerText) {
            span.className = "correct";
        } else {
            span.className = "wrong";
            errorSound.currentTime = 0;
            errorSound.play();
        }
    });

    document.getElementById("wpm").innerText =
        `WPM: ${calculateWPM(typed)}`;

    document.getElementById("accuracy").innerText =
        `Accuracy: ${calculateAccuracy(typed)}%`;
});

function restartTest() {
    clearInterval(timerInterval);

    timer = 60;
    startTime = null;

    document.getElementById("timer").innerText = "Time: 60s";
    document.getElementById("wpm").innerText = "WPM: 0";
    document.getElementById("accuracy").innerText = "Accuracy: 0%";

    typingBox.disabled = false;

    loadSentence();
}

document
.getElementById("restart-btn")
.addEventListener("click", restartTest);

loadSentence();
loadHighScores();