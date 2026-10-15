# FUNGSI: Divisi AI Penganalisis Niat Beli
import random

class IntentEngine:
    def analyze(self, text):
        spam_words = ["pinjol", "judi", "slot", "penipuan"]
        if any(w in text.lower() for w in spam_words): 
            return 0
        return random.randint(80, 99)
