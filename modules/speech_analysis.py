import re

def analyze_speech(text):

    words = text.split()

    word_count = len(words)

    filler_words = [
        "um", "uh", "like", "you know",
        "actually", "basically", "okay"
    ]

    fillers = 0

    for word in words:
        if word.lower() in filler_words:
            fillers += 1

    if word_count == 0:
        wpm = 0
    else:
        # Assume 30 sec audio
        wpm = word_count * 2

    return {
        "word_count": word_count,
        "fillers": fillers,
        "wpm": wpm
    }