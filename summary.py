import nltk
import os
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize


# Create the directory if it doesn't exist
nltk_data_path = "/opt/render/nltk_data"
os.makedirs(nltk_data_path, exist_ok=True)

# Set the path for NLTK
nltk.data.path.append(nltk_data_path)

# Download the required tokenizer
nltk.download('punkt_tab', download_dir=nltk_data_path)

print("NLTK data is ready!")



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




def summarize_text_using_words(text, num_words=5):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    # Count word frequencies
    word_freq = Counter(words)

    # Rank sentences based on word importance
    sentence_ranks = {
        sent: sum(word_freq[word] for word in word_tokenize(sent.lower()))
        for sent in sentences
    }

    # Sort sentences by importance
    sorted_sentences = sorted(sentence_ranks, key=sentence_ranks.get, reverse=True)

    # Select sentences until the word limit is reached
    selected_sentences = []
    word_count = 0

    for sentence in sorted_sentences:
        sentence_words = word_tokenize(sentence)
        if word_count + len(sentence_words) <= num_words:
            selected_sentences.append(sentence)
            word_count += len(sentence_words)
        else:
            break

    return " ".join(selected_sentences)


