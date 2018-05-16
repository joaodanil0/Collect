#! /usr/bin/env python3

import pandas
import numpy
import sys

simulacoes = int(sys.argv[1])
num_nos = int(sys.argv[2])
num_rounds = int(sys.argv[3])
total_horas = int(num_rounds/3600)

mean_hour = numpy.zeros((total_horas,simulacoes))
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
		sum_dataPcts_hours[k][j] = dataHours.loc[k]['Pacotes enviados por hora']
		sum_configPcts_hours[k][j] = dataHours.loc[k]['Pacotes configuracao por hora']
		sum_pcts_hours[k][j] = dataHours.loc[k]['enviados+configuracao']
		dead_nodes[k][j] = dataNodes.loc[k]['Quantidade de nos mortos']
		pckt_delivered[k][j] = dataDelivered.loc[k][' porcentagem de pacotes entregues']

def frame(data_frame):
	dictionary = {}
	for i in range(simulacoes):
		dictionary["Simulacao " + str(i+1)] =  data_frame.T[i][:]		
	return dictionary

data_mean = pandas.DataFrame(frame(mean_hour))
dataPcts_hours_sum = pandas.DataFrame(frame(sum_dataPcts_hours))
configPcts_hours_sum = pandas.DataFrame(frame(sum_configPcts_hours))
pcts_hours_sum = pandas.DataFrame(frame(sum_pcts_hours))
dead_nodes = pandas.DataFrame(frame(dead_nodes))
pckt_delivered = pandas.DataFrame(frame(pckt_delivered))

result = {'media': data_mean.T.mean(), 'desvio padrao': data_mean.T.std()}
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
