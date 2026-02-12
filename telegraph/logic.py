# telegraph/logic.py
MORSE_DATA = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', ' ': '/'
}

def translate_to_morse(text):
    """A clean, Pythonic translation function."""
    text = text.upper().strip()
    return " ".join(MORSE_DATA.get(char, '[?]') for char in text)