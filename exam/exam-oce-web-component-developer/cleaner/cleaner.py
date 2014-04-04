import re

linestring = open('servlets_questions.txt', 'r').read()
result = ''.join(linestring)

linestring = open('servlets_questions_respostas.txt', 'r').read()
result_respostas = ''.join(linestring)
rerespostas = re.compile ('<li>.*?</li>')
arrayresultado = []

resultado_respostas = rerespostas.findall(result_respostas)

for item_resposta in resultado_respostas:
     arrayresultado.append(item_resposta.replace("<li>","").replace("</li>",""))
     
requestions = re.compile ("question.+?999\n\n", re.DOTALL)
result_requestions = requestions.findall(result)
realternatives = re.compile ('111.+?999', re.DOTALL)

total = 0
resultado = []
for item in result_requestions:
	 result_alternatives = realternatives.findall(item)
	 alternative = 'a'
	 resultado.append("<question>")
	 resultado.append("<alternatives>")
	 
	 for item_alternative in result_alternatives:
	     resultado.append("<alternative>")
	     resultado.append("<name><![CDATA[")
	     resultado.append(item_alternative.replace('111','').replace('999',''))
	     resultado.append("]]></name>")
	     resultado.append("<id>"+alternative+"</id>")
	     alternative = chr(ord(alternative) + 1)
	     resultado.append("</alternative>")
	 resultado.append ("<corrects>")
	 resultado.append (arrayresultado[total].replace(" ",""))
	 resultado.append ("</corrects>")	 
	 resultado.append("</alternatives>")
	 item = re.sub('111.+?999',"",item)
	 resultado.append("<question_name><![CDATA[")
	 resultado.append(item.replace("question.",""))
	 resultado.append("]]></question_name>")
	 resultado.append("</question>")
	 total = total + 1

myFile = open('servlets_questions.xml', 'w')
myFile.write(''.join(resultado))
myFile.close()
print total


