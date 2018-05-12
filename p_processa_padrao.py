#! /usr/bin/env python3

import pandas
import numpy
import sys

simulacoes = int(sys.argv[1])
num_nos = int(sys.argv[2])
num_rounds = int(sys.argv[3])
total_horas = int(num_rounds/3600)

mean_hour = numpy.zeros((total_horas,simulacoes))
std_hour = numpy.zeros((total_horas,simulacoes))
sum_dataPcts_hours = numpy.zeros((total_horas,simulacoes))
sum_configPcts_hours = numpy.zeros((total_horas,simulacoes))
sum_pcts_hours = numpy.zeros((total_horas,simulacoes))
dead_nodes = numpy.zeros((total_horas,simulacoes))
pckt_delivered = numpy.zeros((total_horas,simulacoes))

for j in range(simulacoes):
		
	data = pandas.read_csv('logs/padrao_Simulacao_' + str(j+1) + '/Energia.csv')
	dataHours = pandas.read_csv('logs/padrao_Simulacao_' + str(j+1) + '/PctsHora.csv')
	dataNodes = pandas.read_csv('logs/padrao_Simulacao_' + str(j+1) + '/NosMortos.csv')
	dataDelivered = pandas.read_csv('logs/padrao_Simulacao_' + str(j+1) + '/EntregasPorHora.csv')
	
	for k in range(total_horas):
		mean_hour[k][j] = data.loc[60*num_nos*k:60*num_nos*(k+1)-1]['Energia do no'].mean()
		std_hour[k][j]  = data.loc[60*num_nos*k:60*num_nos*(k+1)-1]['Energia do no'].std()
		
		sum_dataPcts_hours[k][j] = dataHours.loc[k]['Pacotes enviados por hora']
		sum_configPcts_hours[k][j] = dataHours.loc[k]['Pacotes configuracao por hora']
		sum_pcts_hours[k][j] = dataHours.loc[k]['enviados+configuracao']
		dead_nodes[k][j] = dataNodes.loc[k]['Quantidade de nos mortos']
		pckt_delivered[k][j] = dataDelivered.loc[k][' porcentagem de pacotes entregues']


data_mean = {'Simulacao 1': mean_hour.T[0][:], 'Simulacao 2': mean_hour.T[1][:], 'Simulacao 3': mean_hour.T[2][:],
			 'Simulacao 4': mean_hour.T[3][:], 'Simulacao 5': mean_hour.T[4][:], 'Simulacao 6': mean_hour.T[5][:],
			 'Simulacao 7': mean_hour.T[6][:], 'Simulacao 8': mean_hour.T[7][:], 'Simulacao 9': mean_hour.T[8][:],
			 'Simulacao 10': mean_hour.T[9][:], 'Simulacao 11': mean_hour.T[10][:], 'Simulacao 12': mean_hour.T[11][:],
			 'Simulacao 13': mean_hour.T[12][:], 'Simulacao 14': mean_hour.T[13][:], 'Simulacao 15': mean_hour.T[14][:],
			 'Simulacao 16': mean_hour.T[15][:], 'Simulacao 17': mean_hour.T[16][:], 'Simulacao 18': mean_hour.T[17][:],
			 'Simulacao 19': mean_hour.T[18][:], 'Simulacao 20': mean_hour.T[19][:], 'Simulacao 21': mean_hour.T[20][:],
			 'Simulacao 22': mean_hour.T[21][:], 'Simulacao 23': mean_hour.T[22][:], 'Simulacao 24': mean_hour.T[23][:],
			 'Simulacao 25': mean_hour.T[24][:], 'Simulacao 26': mean_hour.T[25][:], 'Simulacao 27': mean_hour.T[26][:],
			 'Simulacao 28': mean_hour.T[27][:], 'Simulacao 29': mean_hour.T[28][:], 'Simulacao 30': mean_hour.T[29][:],
			 'Simulacao 31': mean_hour.T[30][:], 'Simulacao 32': mean_hour.T[31][:], 'Simulacao 33': mean_hour.T[32][:]}

data_std = {'Simulacao 1': std_hour.T[0][:], 'Simulacao 2': std_hour.T[1][:], 'Simulacao 3': std_hour.T[2][:],
			 'Simulacao 4': std_hour.T[3][:], 'Simulacao 5': std_hour.T[4][:], 'Simulacao 6': std_hour.T[5][:],
			 'Simulacao 7': std_hour.T[6][:], 'Simulacao 8': std_hour.T[7][:], 'Simulacao 9': std_hour.T[8][:],
			 'Simulacao 10': std_hour.T[9][:], 'Simulacao 11': std_hour.T[10][:], 'Simulacao 12': std_hour.T[11][:],
			 'Simulacao 13': std_hour.T[12][:], 'Simulacao 14': std_hour.T[13][:], 'Simulacao 15': std_hour.T[14][:],
			 'Simulacao 16': std_hour.T[15][:], 'Simulacao 17': std_hour.T[16][:], 'Simulacao 18': std_hour.T[17][:],
			 'Simulacao 19': std_hour.T[18][:], 'Simulacao 20': std_hour.T[19][:], 'Simulacao 21': std_hour.T[20][:],
			 'Simulacao 22': std_hour.T[21][:], 'Simulacao 23': std_hour.T[22][:], 'Simulacao 24': std_hour.T[23][:],
			 'Simulacao 25': std_hour.T[24][:], 'Simulacao 26': std_hour.T[25][:], 'Simulacao 27': std_hour.T[26][:],
			 'Simulacao 28': std_hour.T[27][:], 'Simulacao 29': std_hour.T[28][:], 'Simulacao 30': std_hour.T[29][:],
			 'Simulacao 31': std_hour.T[30][:], 'Simulacao 32': std_hour.T[31][:], 'Simulacao 33': std_hour.T[32][:]}

dataPcts_hours_sum = {'Simulacao 1': sum_dataPcts_hours.T[0][:], 'Simulacao 2': sum_dataPcts_hours.T[1][:], 'Simulacao 3': sum_dataPcts_hours.T[2][:],
			 'Simulacao 4': sum_dataPcts_hours.T[3][:], 'Simulacao 5': sum_dataPcts_hours.T[4][:], 'Simulacao 6': sum_dataPcts_hours.T[5][:],
			 'Simulacao 7': sum_dataPcts_hours.T[6][:], 'Simulacao 8': sum_dataPcts_hours.T[7][:], 'Simulacao 9': sum_dataPcts_hours.T[8][:],
			 'Simulacao 10': sum_dataPcts_hours.T[9][:], 'Simulacao 11': sum_dataPcts_hours.T[10][:], 'Simulacao 12': sum_dataPcts_hours.T[11][:],
			 'Simulacao 13': sum_dataPcts_hours.T[12][:], 'Simulacao 14': sum_dataPcts_hours.T[13][:], 'Simulacao 15': sum_dataPcts_hours.T[14][:],
			 'Simulacao 16': sum_dataPcts_hours.T[15][:], 'Simulacao 17': sum_dataPcts_hours.T[16][:], 'Simulacao 18': sum_dataPcts_hours.T[17][:],
			 'Simulacao 19': sum_dataPcts_hours.T[18][:], 'Simulacao 20': sum_dataPcts_hours.T[19][:], 'Simulacao 21': sum_dataPcts_hours.T[20][:],
			 'Simulacao 22': sum_dataPcts_hours.T[21][:], 'Simulacao 23': sum_dataPcts_hours.T[22][:], 'Simulacao 24': sum_dataPcts_hours.T[23][:],
			 'Simulacao 25': sum_dataPcts_hours.T[24][:], 'Simulacao 26': sum_dataPcts_hours.T[25][:], 'Simulacao 27': sum_dataPcts_hours.T[26][:],
			 'Simulacao 28': sum_dataPcts_hours.T[27][:], 'Simulacao 29': sum_dataPcts_hours.T[28][:], 'Simulacao 30': sum_dataPcts_hours.T[29][:],
			 'Simulacao 31': sum_dataPcts_hours.T[30][:], 'Simulacao 32': sum_dataPcts_hours.T[31][:], 'Simulacao 33': sum_dataPcts_hours.T[32][:]}
				      
configPcts_hours_sum = {'Simulacao 1': sum_configPcts_hours.T[0][:], 'Simulacao 2': sum_configPcts_hours.T[1][:], 'Simulacao 3': sum_configPcts_hours.T[2][:],
			 'Simulacao 4': sum_configPcts_hours.T[3][:], 'Simulacao 5': sum_configPcts_hours.T[4][:], 'Simulacao 6': sum_configPcts_hours.T[5][:],
			 'Simulacao 7': sum_configPcts_hours.T[6][:], 'Simulacao 8': sum_configPcts_hours.T[7][:], 'Simulacao 9': sum_configPcts_hours.T[8][:],
			 'Simulacao 10': sum_configPcts_hours.T[9][:], 'Simulacao 11': sum_configPcts_hours.T[10][:], 'Simulacao 12': sum_configPcts_hours.T[11][:],
			 'Simulacao 13': sum_configPcts_hours.T[12][:], 'Simulacao 14': sum_configPcts_hours.T[13][:], 'Simulacao 15': sum_configPcts_hours.T[14][:],
			 'Simulacao 16': sum_configPcts_hours.T[15][:], 'Simulacao 17': sum_configPcts_hours.T[16][:], 'Simulacao 18': sum_configPcts_hours.T[17][:],
			 'Simulacao 19': sum_configPcts_hours.T[18][:], 'Simulacao 20': sum_configPcts_hours.T[19][:], 'Simulacao 21': sum_configPcts_hours.T[20][:],
			 'Simulacao 22': sum_configPcts_hours.T[21][:], 'Simulacao 23': sum_configPcts_hours.T[22][:], 'Simulacao 24': sum_configPcts_hours.T[23][:],
			 'Simulacao 25': sum_configPcts_hours.T[24][:], 'Simulacao 26': sum_configPcts_hours.T[25][:], 'Simulacao 27': sum_configPcts_hours.T[26][:],
			 'Simulacao 28': sum_configPcts_hours.T[27][:], 'Simulacao 29': sum_configPcts_hours.T[28][:], 'Simulacao 30': sum_configPcts_hours.T[29][:],
			 'Simulacao 31': sum_configPcts_hours.T[30][:], 'Simulacao 32': sum_configPcts_hours.T[31][:], 'Simulacao 33': sum_configPcts_hours.T[32][:]}
				        
pcts_hours_sum = {'Simulacao 1': sum_pcts_hours.T[0][:], 'Simulacao 2': sum_pcts_hours.T[1][:], 'Simulacao 3': sum_pcts_hours.T[2][:],
			 'Simulacao 4': sum_pcts_hours.T[3][:], 'Simulacao 5': sum_pcts_hours.T[4][:], 'Simulacao 6': sum_pcts_hours.T[5][:],
			 'Simulacao 7': sum_pcts_hours.T[6][:], 'Simulacao 8': sum_pcts_hours.T[7][:], 'Simulacao 9': sum_pcts_hours.T[8][:],
			 'Simulacao 10': sum_pcts_hours.T[9][:], 'Simulacao 11': sum_pcts_hours.T[10][:], 'Simulacao 12': sum_pcts_hours.T[11][:],
			 'Simulacao 13': sum_pcts_hours.T[12][:], 'Simulacao 14': sum_pcts_hours.T[13][:], 'Simulacao 15': sum_pcts_hours.T[14][:],
			 'Simulacao 16': sum_pcts_hours.T[15][:], 'Simulacao 17': sum_pcts_hours.T[16][:], 'Simulacao 18': sum_pcts_hours.T[17][:],
			 'Simulacao 19': sum_pcts_hours.T[18][:], 'Simulacao 20': sum_pcts_hours.T[19][:], 'Simulacao 21': sum_pcts_hours.T[20][:],
			 'Simulacao 22': sum_pcts_hours.T[21][:], 'Simulacao 23': sum_pcts_hours.T[22][:], 'Simulacao 24': sum_pcts_hours.T[23][:],
			 'Simulacao 25': sum_pcts_hours.T[24][:], 'Simulacao 26': sum_pcts_hours.T[25][:], 'Simulacao 27': sum_pcts_hours.T[26][:],
			 'Simulacao 28': sum_pcts_hours.T[27][:], 'Simulacao 29': sum_pcts_hours.T[28][:], 'Simulacao 30': sum_pcts_hours.T[29][:],
			 'Simulacao 31': sum_pcts_hours.T[30][:], 'Simulacao 32': sum_pcts_hours.T[31][:], 'Simulacao 33': sum_pcts_hours.T[32][:]}

dead_nodes = {'Simulacao 1': dead_nodes.T[0][:], 'Simulacao 2': dead_nodes.T[1][:], 'Simulacao 3': dead_nodes.T[2][:],
			 'Simulacao 4': dead_nodes.T[3][:], 'Simulacao 5': dead_nodes.T[4][:], 'Simulacao 6': dead_nodes.T[5][:],
			 'Simulacao 7': dead_nodes.T[6][:], 'Simulacao 8': dead_nodes.T[7][:], 'Simulacao 9': dead_nodes.T[8][:],
			 'Simulacao 10': dead_nodes.T[9][:], 'Simulacao 11': dead_nodes.T[10][:], 'Simulacao 12': dead_nodes.T[11][:],
			 'Simulacao 13': dead_nodes.T[12][:], 'Simulacao 14': dead_nodes.T[13][:], 'Simulacao 15': dead_nodes.T[14][:],
			 'Simulacao 16': dead_nodes.T[15][:], 'Simulacao 17': dead_nodes.T[16][:], 'Simulacao 18': dead_nodes.T[17][:],
			 'Simulacao 19': dead_nodes.T[18][:], 'Simulacao 20': dead_nodes.T[19][:], 'Simulacao 21': dead_nodes.T[20][:],
			 'Simulacao 22': dead_nodes.T[21][:], 'Simulacao 23': dead_nodes.T[22][:], 'Simulacao 24': dead_nodes.T[23][:],
			 'Simulacao 25': dead_nodes.T[24][:], 'Simulacao 26': dead_nodes.T[25][:], 'Simulacao 27': dead_nodes.T[26][:],
			 'Simulacao 28': dead_nodes.T[27][:], 'Simulacao 29': dead_nodes.T[28][:], 'Simulacao 30': dead_nodes.T[29][:],
			 'Simulacao 31': dead_nodes.T[30][:], 'Simulacao 32': dead_nodes.T[31][:], 'Simulacao 33': dead_nodes.T[32][:]}				   

pckt_delivered = {'Simulacao 1': pckt_delivered.T[0][:], 'Simulacao 2': pckt_delivered.T[1][:], 'Simulacao 3': pckt_delivered.T[2][:],
			 'Simulacao 4': pckt_delivered.T[3][:], 'Simulacao 5': pckt_delivered.T[4][:], 'Simulacao 6': pckt_delivered.T[5][:],
			 'Simulacao 7': pckt_delivered.T[6][:], 'Simulacao 8': pckt_delivered.T[7][:], 'Simulacao 9': pckt_delivered.T[8][:],
			 'Simulacao 10': pckt_delivered.T[9][:], 'Simulacao 11': pckt_delivered.T[10][:], 'Simulacao 12': pckt_delivered.T[11][:],
			 'Simulacao 13': pckt_delivered.T[12][:], 'Simulacao 14': pckt_delivered.T[13][:], 'Simulacao 15': pckt_delivered.T[14][:],
			 'Simulacao 16': pckt_delivered.T[15][:], 'Simulacao 17': pckt_delivered.T[16][:], 'Simulacao 18': pckt_delivered.T[17][:],
			 'Simulacao 19': pckt_delivered.T[18][:], 'Simulacao 20': pckt_delivered.T[19][:], 'Simulacao 21': pckt_delivered.T[20][:],
			 'Simulacao 22': pckt_delivered.T[21][:], 'Simulacao 23': pckt_delivered.T[22][:], 'Simulacao 24': pckt_delivered.T[23][:],
			 'Simulacao 25': pckt_delivered.T[24][:], 'Simulacao 26': pckt_delivered.T[25][:], 'Simulacao 27': pckt_delivered.T[26][:],
			 'Simulacao 28': pckt_delivered.T[27][:], 'Simulacao 29': pckt_delivered.T[28][:], 'Simulacao 30': pckt_delivered.T[29][:],
			 'Simulacao 31': pckt_delivered.T[30][:], 'Simulacao 32': pckt_delivered.T[31][:], 'Simulacao 33': pckt_delivered.T[32][:]}	

data_mean = pandas.DataFrame(data_mean)
data_std = pandas.DataFrame(data_std)
dataPcts_hours_sum = pandas.DataFrame(dataPcts_hours_sum)
configPcts_hours_sum = pandas.DataFrame(configPcts_hours_sum)
pcts_hours_sum = pandas.DataFrame(pcts_hours_sum)
dead_nodes = pandas.DataFrame(dead_nodes)
pckt_delivered = pandas.DataFrame(pckt_delivered)


result = {'media': data_mean.T.mean(), 'desvio padrao': data_std.T.mean()}
result_hours_data = {'Pacotes enviados por hora': dataPcts_hours_sum.T.mean(),
					 'Pacotes configuracao por hora': configPcts_hours_sum.T.mean(),
					 'enviados+configuracao': pcts_hours_sum.T.mean(),
					 'STD Pacotes enviados': dataPcts_hours_sum.T.std(),
					 'STD Pacotes conf': configPcts_hours_sum.T.std(),
					 'STD envi + conf': pcts_hours_sum.T.std()}
dead_nodes = {'media': dead_nodes.T.mean(), 'desvio padrao': dead_nodes.T.std()}
pckt_delivered = {'media': pckt_delivered.T.mean(), 'desvio padrao': pckt_delivered.T.std()}

result = pandas.DataFrame(result)
result_hours = pandas.DataFrame(result_hours_data)
dead_nodes = pandas.DataFrame(dead_nodes)
pckt_delivered = pandas.DataFrame(pckt_delivered)

result.to_csv('../resultados/padrao/result_collect.csv')
result_hours.to_csv('../resultados/pcts_hora/result_collect.csv')
dead_nodes.to_csv('../resultados/pcts_hora/nos_mortos_collect.csv')
pckt_delivered.to_csv('../resultados/pcts_hora/TxEntregaHora_collect.csv')

