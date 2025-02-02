import nltk
import os
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize

# Tell NLTK where to find the data
nltk.data.path.append(os.path.join(os.path.dirname(__file__), "nltk_data"))

def summarize_text_using_no_of_sentences(text, num_sentences=3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    
    # Count word frequencies
    word_freq = Counter(words)
    
    # Rank sentences based on word importance
    sentence_ranks = {sent: sum(word_freq[word] for word in word_tokenize(sent.lower())) for sent in sentences}
   
    # Get top sentences
    top_sentences = sorted(sentence_ranks, key=sentence_ranks.get, reverse=True)[:num_sentences]
    
    return ' '.join(top_sentences)





def summarize_text_using_percentage(text, percentage=30):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    # Count word frequencies
    word_freq = Counter(words)

    # Rank sentences based on word importance
    sentence_ranks = {
        sent: sum(word_freq[word] for word in word_tokenize(sent.lower()))
        for sent in sentences
    }

    # Calculate the number of sentences based on percentage
    num_sentences = max(1, int(len(sentences) * (percentage / 100)))

    # Get top-ranked sentences
    top_sentences = sorted(sentence_ranks, key=sentence_ranks.get, reverse=True)[:num_sentences]

    return ' '.join(top_sentences)


