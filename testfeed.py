from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def ml():
	import time
	for i in range(1):
		recognizer = speech_recognition.Recognizer()
		with speech_recognition.Microphone() as source:
			print("Say Something")
			audio = recognizer.listen(source)

		print("Google Speech Recognition thinks you said:")
		time.sleep(0.1)

		print(recognizer.recognize_google(audio))


# importing libraries 
# importing libraries 
	import nltk 
	from nltk.corpus import stopwords 
	from nltk.tokenize import word_tokenize, sent_tokenize 

	# Input text - to summarize 
	text = recognizer.recognize_google(audio)

	# Tokenizing the text 
	stopWords = set(stopwords.words("english")) 
	words = word_tokenize(text) 


	freqTable = dict() 
	for word in words: 
		word = word.lower() 
		if word in stopWords: 
			continue
		if word in freqTable: 
			freqTable[word] += 1
		else: 
			freqTable[word] = 1

	# Creating a dictionary to keep the score 
	# of each sentence 
	sentences = sent_tokenize(text) 
	sentenceValue = dict() 

	for sentence in sentences: 
		for word, freq in freqTable.items(): 
			if word in sentence.lower(): 
				if sentence in sentenceValue: 
					sentenceValue[sentence] += freq 
				else: 
					sentenceValue[sentence] = freq 



	sumValues = 0
	for sentence in sentenceValue: 
		sumValues += sentenceValue[sentence] 

	# Average value of a sentence from the original text 

	average = int(sumValues / len(sentenceValue)) 

	# Storing sentences into our summary. 
	summary = '' 
	for sentence in sentences: 
		if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
			summary += " " + sentence 
	#print(summary) 


	return render_template('byte.html',summary = summary)






if __name__ == "__main__":
    app.run(port=5000, debug=True)

