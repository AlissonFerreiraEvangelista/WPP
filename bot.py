from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import requests


driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(10)

def bot():
	try:
		#Notificação
		bolinha = driver.find_element_by_class_name('_23LrM')
		bolinha = driver.find_elements_by_class_name('_23LrM')
		clica_bolinha = bolinha[-1]
		acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
		acao_bolinha.move_to_element_with_offset(clica_bolinha,0,-20)
		i = 0

		while i<2:
			acao_bolinha.click()
			acao_bolinha.perform()
			i+=1

		#Pega o Telefone
		telefone_cliente = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[1]/div/span')
		telefone_final = telefone_cliente.text
		print(telefone_final)
		#Pega a Mensagem
		todas_mgs = driver.find_elements_by_class_name('_1Gy50')
		todas_mgs = [e.text for e in todas_mgs]
		msg = todas_mgs[-1]
		print(msg)

		#Responder a Mensagem
		campo_texto = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
		campo_texto.click()
		resposta = requests.get('http://localhost/bot/index.php')
		bot_resposta = resposta.text

		time.sleep(3)
		campo_texto.send_keys(bot_resposta, Keys.ENTER)

		#Voltar p/ Contato
		#_1pJ9J
		contato_padrao = driver.find_element_by_class_name('_1pJ9J')
		acao_contato = webdriver.common.action_chains.ActionChains(driver)
		acao_contato.move_to_element_with_offset(contato_padrao,0,-20)

		j = 0
		while j<2:
			acao_contato.click()
			acao_contato.perform()
			j+=1

		 

	except:
		print('Não possui novas mensagens')
		time.sleep(5)

while True:
	bot()

