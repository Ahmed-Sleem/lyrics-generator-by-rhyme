def get_line(file,word,rhyme,state=0):
	
	#importing markovify 
	import markovify 
	
	
	#seting dataset 
	dataset = file
	
	#setting text model 
	text_model = markovify.Text(dataset)
	
		
	#result line 
	result = ""
	
	#if state = 0 make sentence with last word if = 1 make sentence with last rhyme
	if state == 0 :
		while True:
			x = text_model.make_sentence()
			y = str(x).split(" ")
			last = y[-1]
			
			
			if last == word :
				result = x
				
				
				break 
	elif state == 1:
		
		while True:
			x = text_model.make_sentence()
			y = str(x).split(" ")
			last = y[-1]
			
			try: 
				rhyme[-1]
				if rhyme[-1] == last[-1] :
					try: 
						rhyme[-2]
						if rhyme[-2] == last[-2] :
							try: 
								rhyme[-3]
								if rhyme[-3] == last[-3] :
									result = x
									break 
							except:
								result = x
								break 
					except:
						result = x
						break 
			except:
				print("please enter a rhymee")
				break 
							
			
		
	return result 


	
	
#the file with lyrics dataset 
file = open("drake_lyrics.txt","r")
#to print the output (the new lines)
print(get_line(file, "play" , "ay", 0))