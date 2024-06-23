import re
from collections import Counter

class TextAnalysisTool:
    def __init__(self, text):
        self.text = text
        self.words = self.get_words()
        self.sentences = self.get_sentences()
    
    def get_words(self):
        return re.findall(r'\b\w+\b', self.text.lower())
    
    def get_sentences(self):
        return re.split(r'[.!?]', self.text)
    
    def character_analysis(self):
        total_chars = len(self.text)
        alphabetic_chars = sum(c.isalpha() for c in self.text)
        digits = sum(c.isdigit() for c in self.text)
        whitespace = sum(c.isspace() for c in self.text)
        special_chars = total_chars - (alphabetic_chars + digits + whitespace)
        
        return {
            "Total Characters": total_chars,
            "Alphabetic Characters": alphabetic_chars,
            "Digits": digits,
            "Whitespace Characters": whitespace,
            "Special Characters": special_chars
        }
    
    def word_analysis(self):
        word_count = len(self.words)
        word_frequency = Counter(self.words)
        most_common_word = word_frequency.most_common(1)[0][0] if word_count > 0 else None
        longest_word = max(self.words, key=len) if word_count > 0 else None
        shortest_word = min(self.words, key=len) if word_count > 0 else None
        
        return {
            "Total Words": word_count,
            "Word Frequency": word_frequency,
            "Most Common Word": most_common_word,
            "Longest Word": longest_word,
            "Shortest Word": shortest_word
        }
    
    def sentence_analysis(self):
        total_sentences = len(self.sentences)
        words_per_sentence = [len(re.findall(r'\b\w+\b', sentence)) for sentence in self.sentences if sentence]
        avg_words_per_sentence = sum(words_per_sentence) / len(words_per_sentence) if words_per_sentence else 0
        
        return {
            "Total Sentences": total_sentences,
            "Average Words per Sentence": avg_words_per_sentence
        }
    
    def analyze_text(self):
        return {
            "Character Analysis": self.character_analysis(),
            "Word Analysis": self.word_analysis(),
            "Sentence Analysis": self.sentence_analysis()
        }

# Example usage
text = "Hello world! This is a test. Testing, one, two, three."
tool = TextAnalysisTool(text)
analysis = tool.analyze_text()
print(analysis)
