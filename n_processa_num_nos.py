#! /usr/bin/env python3

import pandas
import numpy
import sys

simulacoes = int(sys.argv[1])
num_nos = int(sys.argv[2])

varia_min = int(sys.argv[3])
varia_max = int(sys.argv[4])
varia_tic = int(sys.argv[5])

mean_simulation = numpy.zeros((simulacoes,5))
std_simulatation = numpy.zeros((simulacoes,5))
mean_delivery_rate = numpy.zeros((simulacoes,5))
std_delivery_rate = numpy.zeros((simulacoes,5))

counter = 0
for i in range(varia_min, varia_max+1,varia_tic):
	
	for j in range(simulacoes):
		
		data = pandas.read_csv('logs/num_nos_Simulacao_' + str(i*i) + str(j+1) + '/Energia.csv')
				
		mean_simulation[j][counter] = data.mean()['Energia do no']
		
		data_delivery = pandas.read_csv('logs/num_nos_SimulacaoTX_' + str(i*i) + str(j+1) + '/TXentrega.csv')
		
		mean_delivery_rate[j][counter] = data_delivery.mean()['Porcentagem de pacotes recebidos']
		
	counter+=1

data_mean = {'225': mean_simulation.T[0][:], '361': mean_simulation.T[1][:],
			 '529': mean_simulation.T[2][:], '729': mean_simulation.T[3][:],
			 '961': mean_simulation.T[4][:]}

mean_delivery_rate = {'225': mean_delivery_rate.T[0][:], '361': mean_delivery_rate.T[1][:],
					  '529': mean_delivery_rate.T[2][:], '729': mean_delivery_rate.T[3][:],
					  '961': mean_delivery_rate.T[4][:]}
					  
data_mean = pandas.DataFrame(data_mean)
mean_delivery_rate = pandas.DataFrame(mean_delivery_rate)

result = {'media': data_mean.mean(), 'desvio padrao': data_mean.std()}
result_TX = {'media': mean_delivery_rate.mean(), 'desvio padrao': mean_delivery_rate.std()}

result = pandas.DataFrame(result)
result_TX = pandas.DataFrame(result_TX)

result.to_csv('../resultados/num_nos/result_collect.csv')
result_TX.to_csv('../resultados/num_nos/resultTX_collect.csv')
