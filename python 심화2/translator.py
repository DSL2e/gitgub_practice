from googletrans import Translator 
translator = Translator()
sentence = input("번역을 원하는 문장을 입력하시오 :")
lang = input("번역을 원하시는 나라의 언어를 입력하시오 : ")
result = translator.translate(sentence,lang)
detected= translator.detect(result.text)
#print(result)
print(result.src+":"+sentence)
print(detected.lang+":"+result.text)