from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():

    
    return render_template("home.html")


@app.route("/ml", methods = ["POST"])
def ml():
	message = ""
	msg11 = request.form.get("name1")
	msg1 = int(msg11)
    msg22 = request.form.get("name2")
    msg2 = int(msg22)

	from PIL import Image
	simg = Image.open(msg2)
	text = pytessaract.image_to_string(img)
	print(text)
	import nltk 
	from nltk.corpus import stopwords 
	from nltk.tokenize import word_tokenize, sent_tokenize 

	# Input text - to summarize 

	# Tokenizing the text 
	stopWords = set(stopwords.words("english")) 
	words = word_tokenize(text) 

	# Creating a frequency table to keep the 
	# score of each word 

	#freqTable = dict() 
	for word in words: 
		word = word.lower() 
		if word in stopWords: 
			continue


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



#	sumValues = 0
#	for sentence in sentenceValue: 
#		sumValues += sentenceValue[sentence] 

	# Average value of a sentence from the original text 

#	average = int(sumValues / len(sentenceValue)) 

	# Storing sentences into our summary. 
#	summary = '' 
#	for sentence in sentences: 
#		if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
#			summary += " " + sentence 
	#print(summary) 
	summary = ''

	return render_template("startbootstrap-freelancer-gh-pages/index.html", summary=summary)




if __name__ == "__main__":
    app.run(port=5000, debug=True)




#@app.route("/")
#def ml():



#	return render_template('byte.html',summary = summary)






if __name__ == "__main__":
    app.run(port=5000, debug=True)

