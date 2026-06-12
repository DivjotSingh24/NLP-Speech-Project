from collections import defaultdict
from textblob import TextBlob

def analyze_dominance(transcript):

    speaker_data = defaultdict(lambda: {
        "words": 0,
        "turns": 0,
        "sentiment": 0
    })

    lines = transcript.split("\n")

    for line in lines:

        if ":" in line:

            speaker, text = line.split(":", 1)

            speaker = speaker.strip()
            text = text.strip()

            # Word count
            word_count = len(text.split())

            # Sentiment score
            sentiment = abs(
                TextBlob(text).sentiment.polarity
            )

            # Update stats
            speaker_data[speaker]["words"] += word_count
            speaker_data[speaker]["turns"] += 1
            speaker_data[speaker]["sentiment"] += sentiment

    # Calculate dominance score
    for speaker in speaker_data:

        words = speaker_data[speaker]["words"]
        turns = speaker_data[speaker]["turns"]
        sentiment = speaker_data[speaker]["sentiment"]

        score = (
            0.5 * words +
            0.3 * turns +
            0.2 * sentiment
        )

        speaker_data[speaker]["score"] = round(score, 2)

    return speaker_data