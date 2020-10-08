#!/usr/bin/python3
from os import system as sys
from sys import exit
from time import sleep
import glob
print('\033[31m')
sys('clear')
print('Verificando se você possui o \033[31;4mngrok\033[0m\033[31m instalado...')
sleep(2.15)
if '.ngrok2' in ''.join(glob.glob('/root/.*')):
	print('\n> Você já possui o ngrok;')
	sleep(1)
	print('\n> \033[31;7mSua chave e seus túneis:\n\033[0m\033[31m')
	sys('cat /root/.ngrok2/ngrok.yml')
else:
	inst = input('\033[31;7m\nVocê não possui o ngrok\nDeseja instalar? [Y/n]\033[0m\033[31m -> ')
	if inst in 'yYsS':
		print('\nInstalando...')
		sys('wget -q --show-progress https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip')
		sys('unzip ngrok*.zip')
		sys('rm -f ngrok*.zip')
		sys('mkdir /root/.ngrok2')
	elif inst in 'nN':
		print('\nAbortando...')
		sleep(2)
		exit()
print('\n[1] > Configuração padrão\n[2] > Configuração personalizada\n[0] > Sair')
back = 1
while back == 1:
	opt = int(input('\n[*] > Selecione a opção > '))
	if opt == 1:
		auth = input('\n> Sua Authtoken: ')
		http = int(input('> Porta HTTP: '))
		tcp = int(input('> Porta TCP: '))
		yml = open('/root/.ngrok2/ngrok.yml', 'w')
		yml.write('''authtoken: {}
		tunnels:
		  http:
		    addr: {}
		    proto: http
		  tcp:
		    addr: {}
		    proto: tcp'''.format(auth, http, tcp))
		yml.close()
		print('\n[+] <Tunnel alterado com sucesso>')
		print('\033[31;7m\nPara utilizar, digite:\n\033[0m\033[31m\n./ngrok start --all\nOU\n./ngrok.py\033[0m')
		exit()
	elif opt == 2:
		sys('nano /root/.ngrok2/ngrok.yml')
		print('\n[+] <Tunnel alterado com sucesso>')
		print('\033[31;7m\nPara utilizar, digite:\n\033[0m\033[31m\n./ngrok start --all\nOU\n./ngrok.py\033[0m')
		exit()
	elif opt == 0:
		print('\nAbortando...')
		sleep(2)
		exit()
	else:
		print('\n\033[31;7mPor favor, selecione uma opção válida\033[0m\033[31m')
