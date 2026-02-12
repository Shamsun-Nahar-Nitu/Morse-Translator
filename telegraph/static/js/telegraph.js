const MORSE_MAP = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'};

const input = document.getElementById('inputField');
const output = document.getElementById('morseDisplay');
const hidden = document.getElementById('hiddenInput');

input.addEventListener('input', (e) => {
    const text = e.target.value.toUpperCase();
    const morse = text.split('').map(c => MORSE_MAP[c] || '').join(' ');
    output.innerText = morse;
    hidden.value = text;
});

// Beep logic (Web Audio API)
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
document.getElementById('beepBtn').addEventListener('click', () => {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    setTimeout(() => osc.stop(), 200);
});