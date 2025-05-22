import re
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from backend.utils.stop_words import STOP_WORDS

def extract_keywords(messages, top_n=5):
    words = []
    for msg in messages:
        tokens = re.findall(r'\b\w+\b', msg.lower())
        filtered = [w for w in tokens if w not in STOP_WORDS]
        words.extend(filtered)
    counts = Counter(words)
    return [w for w, _ in counts.most_common(top_n)]