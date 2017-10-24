import re

fname = "sample.txt"

num_lines = 0
num_words = 0
wordcounts = []
wordinsen = 0

print("Paragraph Analysis")
print("-----------------")

with open(fname, 'r') as f:
	text = f.read()
	sentences = text.split('.')

	
	for sentence in sentences:
		words = sentence.split()
		num_lines += 1
		num_words += len(words)
		wordsofsen = sentence.split(' ')
		wordcounts.append(len(wordsofsen))
		word_pat = re.compile(r"""
    	(\S+)             # Words are just groups of non-whitespace together
    	""", re.X)

		words = word_pat.findall(text)
average_word_length = sum([len(word) for word in words])/len(words)
average_wordcount = sum(wordcounts)/len(wordcounts)

print('Approximate Word Count:',num_words)
print('Approximate Sentence Count:',num_lines)
print('Average Letter Count: ',average_word_length)
print('Average Sentence Length:',average_wordcount)

# Printing the output in a text file "output -para.txt"
with open('Output-PyPara.txt', 'w') as f:
	f.write("Paragraph Analysis\n")
	f.write("-----------------\n")
	f.write('Approximate Word Count: {}\n'.format(num_words))
	f.write('Approximate Sentence Count: {}\n'.format(num_lines))
	f.write('Average Letter Count: {}\n'.format(average_word_length))
	f.write('Average Sentence Length: {}'.format(average_wordcount))

