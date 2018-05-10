import os
import shutil
import datetime
import math

# Variaveis da simulacao
num_nos = 529
simulacoes = 1

raio = 30
densidade = 0.03
tipoSimulacao = 'padrao'
num_rounds =  int(86400 * 4)
multiplicadorIntensidade = 0.4
maxTimeBetweenSends = 7200
minTimeBetweenSends = 120
maxEnergyOfBattery = 1000 
minEnergyOfBattery = 0
maxSolarIntensity = 1000 * multiplicadorIntensidade
minSolarIntensity = 0
wattPico = 0.15
constBattery = 1	# Divisor
constIntensity = 2  # Multiplicador


# Gera um arquivo para logs
debbugfile = open('logs_simulacoes/' + tipoSimulacao + '_sem.log', 'a+')
debbugfile.write('Iniciando a verificacao ' + tipoSimulacao + '_sem em: ')
debbugfile.write(str(datetime.datetime.now().strftime("%d/%m/%y %H:%M")) + '\n')


# inicia o processo de busca por simulacoes que ainda faltam
for simulacao in range(1, simulacoes+1):
	
	pathTX = 'logs/' + tipoSimulacao+ '_SimulacaoTX_' + str(simulacao)
	path = 'logs/' + tipoSimulacao+ '_Simulacao_' + str(simulacao)
	
	if os.path.isdir(pathTX):
		debbugfile.write('SimulacaoTX_' + str(simulacao) + ' ... ok\n' )
	else:
					
		if os.path.isdir(path):
			debbugfile.write(tipoSimulacao+ '_SimulacaoTX_' + str(simulacao) + ' ... erro\n' )
			debbugfile.write('Deletando a pasta ' + tipoSimulacao+ '_Simulacao_' + str(simulacao))
			shutil.rmtree(path)
			debbugfile.write(' ... ok\n')
			debbugfile.write('Iniciando ' + tipoSimulacao+ '_Simulacao_' + str(simulacao))
			
			# chama a simulacao faltante
			os.system('python3 p_varia_' + tipoSimulacao + '.py ' + str(num_nos) + ' ' + str(simulacoes) + ' ' + str(simulacao) + ' ' + 
																	str(raio) + ' ' + str(densidade) + ' ' + str(tipoSimulacao) + ' ' + 
																	str(num_rounds) + ' ' + str(multiplicadorIntensidade) + ' ' + str(maxTimeBetweenSends) + ' ' +
																	str(minTimeBetweenSends) + ' ' + str(maxEnergyOfBattery) + ' ' + str(minEnergyOfBattery) + ' ' +
																	str(maxSolarIntensity) + ' ' + str(minSolarIntensity) + ' ' + str(wattPico) + ' ' +
																	str(constBattery) + ' ' + str(constIntensity))
																	
			
			debbugfile.write(' ... ok\n')
			
		else:
			debbugfile.write(tipoSimulacao+ '_SimulacaoTX_' + str(simulacao) + ' ... erro\n' )
			debbugfile.write('Iniciando ' + tipoSimulacao+ '_Simulacao_' + str(simulacao))
			
			# chama a simulacao faltante
			os.system('python3 p_varia_' + tipoSimulacao + '.py ' + str(num_nos) + ' ' + str(simulacoes) + ' ' + str(simulacao) + ' ' + 
																	str(raio) + ' ' + str(densidade) + ' ' + str(tipoSimulacao) + ' ' + 
																	str(num_rounds) + ' ' + str(multiplicadorIntensidade) + ' ' + str(maxTimeBetweenSends) + ' ' +
																	str(minTimeBetweenSends) + ' ' + str(maxEnergyOfBattery) + ' ' + str(minEnergyOfBattery) + ' ' +
																	str(maxSolarIntensity) + ' ' + str(minSolarIntensity) + ' ' + str(wattPico) + ' ' +
																	str(constBattery) + ' ' + str(constIntensity))
			debbugfile.write(' ... ok\n')				
	
		break
		
debbugfile.close()



