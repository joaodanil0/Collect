import pandas
import numpy
import sys

simulacoes = int(sys.argv[1])
num_nos = int(sys.argv[2])

total_horas = 24*4

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


data_mean = {'Simulacao 1': mean_hour.T[0][:], 'Simulacao 2': mean_hour.T[1][:],
			 'Simulacao 3': mean_hour.T[2][:]}

data_std = {'Simulacao 1': std_hour.T[0][:], 'Simulacao 2': std_hour.T[1][:],
		    'Simulacao 3': std_hour.T[2][:]}

dataPcts_hours_sum = {'Simulacao 1': sum_dataPcts_hours.T[0][:], 'Simulacao 2': sum_dataPcts_hours.T[1][:],
				      'Simulacao 3': sum_dataPcts_hours.T[2][:]}
				      
configPcts_hours_sum = {'Simulacao 1': sum_configPcts_hours.T[0][:], 'Simulacao 2': sum_configPcts_hours.T[1][:],
				        'Simulacao 3': sum_configPcts_hours.T[2][:]}
				        
pcts_hours_sum = {'Simulacao 1': sum_pcts_hours.T[0][:], 'Simulacao 2': sum_pcts_hours.T[1][:],
				   'Simulacao 3': sum_pcts_hours.T[2][:]}

dead_nodes = {'Simulacao 1': dead_nodes.T[0][:], 'Simulacao 2': dead_nodes.T[1][:],
				   'Simulacao 3': dead_nodes.T[2][:]}				   

pckt_delivered = {'Simulacao 1': pckt_delivered.T[0][:], 'Simulacao 2': pckt_delivered.T[1][:],
				   'Simulacao 3': pckt_delivered.T[2][:]}	

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

