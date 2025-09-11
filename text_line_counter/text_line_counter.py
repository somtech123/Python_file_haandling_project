
from collections import Counter
import string
file_path = 'text_line_counter\sample.txt'


stopwords = {'the', 'is','a', 'an','and','to,', 'in', 'of','for','on','at','with'}

#open and read the file

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

    #count lines, words, character

    lines = text.splitlines()

    num_lines = len(lines)

    num_words = len(text.split())

    num_chars = len(text)

    #remove punctuation
    translator = str.maketrans("","", string.punctuation)
    clean_text = text.translate(translator)

    words = clean_text.lower().split()

    #remove stopwords
    filtered_world = [w for w in words if w not in stopwords]

    #word count after filtering
    num_words = len(filtered_world)
    
    #count frequency
    wors_counts = Counter(filtered_world)

    top_words = wors_counts.most_common(10) #top 5 word

    #display result

    print('Lines: ', num_lines)
    print('Words (without stopwords): ', num_words)
    print('No of character: ', num_chars)
    print('Most common words: ', top_words)

    #save sumary to file

with open('text_line_counter\summary.txt', 'w', encoding='utf-8') as f:
    f.write(f'Lines: {num_lines}\n')
    f.write(f'Words (without stopwords): {num_words}\n')
    f.write(f'No of Charater: {num_chars}\n')
    f.write('Most common words:\n')

    for word, count in top_words:
        f.write(f'{word}: {count}\n')


