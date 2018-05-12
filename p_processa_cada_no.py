#! /usr/bin/env python3

import pandas
import numpy
import sys

simulacoes = int(sys.argv[1])
num_nos = int(sys.argv[2])
num_rounds = int(sys.argv[3])
total_horas = int(num_rounds/3600)

no = numpy.zeros((total_horas*60,7))

nos_mean = numpy.zeros((simulacoes,num_nos, 7))
nos_std = numpy.zeros((simulacoes,num_nos, 7))

for j in range(simulacoes):
		
	data = pandas.read_csv('logs/padrao_Simulacao_' + str(j+1) + '/Energia.csv')
	
	for k in range(num_nos):
		
		counter = 0
		for i in range(0, data.shape[0]-num_nos, num_nos):
			
			no[counter] = data.loc[k+i]	
			counter+=1
		
		node = {'Tempo decorrido': no.T[0][:], 'Energia do no': no.T[1][:],
				'Coordenada x': no.T[2][:], 'Coordenada y': no.T[3][:],
				'Pacotes enviados': no.T[4][:], 'Pacotes de configuracao': no.T[5][:],
				'Enviados + configuracao': no.T[6][:]}
		node = pandas.DataFrame(node)	
		
		node_mean = node.mean()
		
		node_mean = {'Tempo decorrido': node_mean[6],
					 'Energia do no': node_mean[2],
					 'Coordenada x': node_mean[0],
					 'Coordenada y': node_mean[1],
					 'Pacotes enviados': node_mean[5],
					 'Pacotes de configuracao': node_mean[4],
					 'Enviados + configuracao': node_mean[3]}
		
		node_mean = pandas.DataFrame(node_mean, index= [j])
		
		if j == 0:
			node_mean.to_csv('nos/' + str(k) + '.csv')
		else:
			node_mean.to_csv('nos/' + str(k) + '.csv', header=False,  mode='a')

nos = numpy.zeros((num_nos,7))

for i in range(num_nos):
	data = 	pandas.read_csv('nos/'+ str(i) + '.csv')
	nos[i] = data.mean()[:][1:8]
		
node_mean = {'Tempo decorrido': nos.T[6][:], 'Energia do no': nos.T[2][:],
			'Coordenada x': nos.T[0][:], 'Coordenada y': nos.T[1][:],
			'Pacotes enviados': nos.T[5][:], 'Pacotes de configuracao': nos.T[4][:],
			'Enviados + configuracao': nos.T[3][:]}

node_mean = pandas.DataFrame(node_mean)

node_mean.to_csv('../resultados/cada_no/result_media_collect.csv')
