#! /usr/bin/env python3

import os
import shutil
import datetime
import math

# Variaveis da simulacao
num_nos = 5
simulacoes = 3

raio = 30
densidade = 0.03
tipoSimulacao = 'num_nos'
num_rounds =  int(86400 * 1)
multiplicadorIntensidade = 0.4
maxTimeBetweenSends = 7200
minTimeBetweenSends = 120
maxEnergyOfBattery = 1000 
minEnergyOfBattery = 0
maxSolarIntensity = 1000 * multiplicadorIntensidade
minSolarIntensity = 0
wattPico = 0.15
constBattery = 1	# Divisor
constIntensity = 1  # Multiplicador

varia_min = 1
varia_max = 5
varia_tic = 1

pathExist = True
# Gera um arquivo para logs
debbugfile = open('logs_simulacoes/' + tipoSimulacao + '_sem.log', 'a+')
debbugfile.write('Iniciando a verificacao ' + tipoSimulacao + '_sem em: ')
debbugfile.write(str(datetime.datetime.now().strftime("%d/%m/%y %H:%M")) + '\n')

for varia_atual in range(varia_min, varia_max+1, varia_tic):
	
	varia_atual = varia_atual*varia_atual
	
	for simulacao in range(1, simulacoes+1):
		pathTX = 'logs/' + tipoSimulacao+ '_SimulacaoTX_' + str(varia_atual) + str(simulacao)
		path = 'logs/' + tipoSimulacao+ '_Simulacao_' + str(varia_atual) + str(simulacao)

		if os.path.isdir(pathTX):
			debbugfile.write(tipoSimulacao+ '_SimulacaoTX_' + str(varia_atual) + str(simulacao) + ' ... ok\n' )
		else:
			pathExist = False
			
			if os.path.isdir(path):
				debbugfile.write(tipoSimulacao+ '_SimulacaoTX_' + str(varia_atual) + str(simulacao) + ' ... erro\n' )
				debbugfile.write('Deletando a pasta ' + tipoSimulacao+ '_Simulacao_' + str(varia_atual) + str(simulacao))
				shutil.rmtree(path)
				debbugfile.write(' ... ok\n')
				debbugfile.write('Iniciando ' + tipoSimulacao+ '_Simulacao_' + str(varia_atual) + str(simulacao))
				
				# chama a simulacao faltante
				os.system('./n_varia_' + tipoSimulacao + '.py ' + str(num_nos) + ' ' + str(simulacoes) + ' ' + str(simulacao) + ' ' + 
																	str(raio) + ' ' + str(densidade) + ' ' + str(tipoSimulacao) + ' ' + 
																	str(num_rounds) + ' ' + str(multiplicadorIntensidade) + ' ' + str(maxTimeBetweenSends) + ' ' +
																	str(minTimeBetweenSends) + ' ' + str(maxEnergyOfBattery) + ' ' + str(minEnergyOfBattery) + ' ' +
																	str(maxSolarIntensity) + ' ' + str(minSolarIntensity) + ' ' + str(wattPico) + ' ' +
																	str(constBattery) + ' ' + str(constIntensity) + ' ' + str(varia_min) + ' ' + 
																	str(varia_max) + ' ' + str(varia_tic) + ' ' + str(int(math.sqrt(varia_atual))))
																	
			
				debbugfile.write(' ... ok\n')
				
			else:
				debbugfile.write(tipoSimulacao+ '_SimulacaoTX_' + str(varia_atual) + str(simulacao) + ' ... erro\n' )
				debbugfile.write('Iniciando ' + tipoSimulacao+ '_Simulacao_' + str(varia_atual) + str(simulacao))
				
				# chama a simulacao faltante
				os.system('./n_varia_' + tipoSimulacao + '.py ' + str(num_nos) + ' ' + str(simulacoes) + ' ' + str(simulacao) + ' ' + 
																	str(raio) + ' ' + str(densidade) + ' ' + str(tipoSimulacao) + ' ' + 
																	str(num_rounds) + ' ' + str(multiplicadorIntensidade) + ' ' + str(maxTimeBetweenSends) + ' ' +
																	str(minTimeBetweenSends) + ' ' + str(maxEnergyOfBattery) + ' ' + str(minEnergyOfBattery) + ' ' +
																	str(maxSolarIntensity) + ' ' + str(minSolarIntensity) + ' ' + str(wattPico) + ' ' +
																	str(constBattery) + ' ' + str(constIntensity) + ' ' + str(varia_min) + ' ' + 
																	str(varia_max) + ' ' + str(varia_tic) + ' ' + str(int(math.sqrt(varia_atual))))
																	
			
				debbugfile.write(' ... ok\n')		
			break
			
	if(pathExist == False):
		break
			
if pathExist == True:
	os.system('python3 n_processa_' + tipoSimulacao + '.py ' + str(simulacoes) + ' ' + str(num_nos) + ' ' + str(varia_min) + ' ' + str(varia_max) + ' '+ str(varia_tic))
	
debbugfile.close()



