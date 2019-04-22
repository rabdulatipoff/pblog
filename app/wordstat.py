from collections import Counter
import re


def word_stats(text):
    stats = Counter(re.findall(r"[\w']+", text)).items()
    return sorted(stats, key=lambda t:t[1], reverse=True)
