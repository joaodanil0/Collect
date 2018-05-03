import pandas
import numpy
import sys

simulacoes = int(sys.argv[1])
num_nos = int(sys.argv[2])

total_horas = 72

mean_hour = numpy.zeros((total_horas,simulacoes))
std_hour = numpy.zeros((total_horas,simulacoes))
mean_pcts_hours = numpy.zeros((total_horas,simulacoes))
std_pcts_hours = numpy.zeros((total_horas,simulacoes))

for j in range(simulacoes):
		
	data = pandas.read_csv('logs/padrao_Simulacao_' + str(j+1) + '/Energia.csv')
	dataHours = pandas.read_csv('logs/padrao_Simulacao_' + str(j+1) + '/PctsHora.csv')
	
	
	
	for k in range(total_horas):
		mean_hour[k][j] = data.loc[60*num_nos*k:60*num_nos*(k+1)-1]['Energia do no'].mean()
		std_hour[k][j]  = data.loc[60*num_nos*k:60*num_nos*(k+1)-1]['Energia do no'].std()
		
		mean_pcts_hours[k][j] = dataHours.loc[num_nos*k:num_nos*(k+1)-1]['enviados+configuracao'].mean()
		std_pcts_hours[k][j]  = dataHours.loc[num_nos*k:num_nos*(k+1)-1]['enviados+configuracao'].std()
	
	

data_mean = {'Simulacao 1': mean_hour.T[0][:], 'Simulacao 2': mean_hour.T[1][:],
			 'Simulacao 3': mean_hour.T[2][:]}

data_std = {'Simulacao 1': std_hour.T[0][:], 'Simulacao 2': std_hour.T[1][:],
		    'Simulacao 3': std_hour.T[2][:]}

pcts_hours_mean = {'Simulacao 1': mean_pcts_hours.T[0][:], 'Simulacao 2': mean_pcts_hours.T[1][:],
				   'Simulacao 3': mean_pcts_hours.T[2][:]}
				   
pcts_hours_std = {'Simulacao 1': std_pcts_hours.T[0][:], 'Simulacao 2': std_pcts_hours.T[1][:],
				   'Simulacao 3': std_pcts_hours.T[2][:]}

data_mean = pandas.DataFrame(data_mean)
data_std = pandas.DataFrame(data_std)
pcts_hours_mean = pandas.DataFrame(pcts_hours_mean)
pcts_hours_std = pandas.DataFrame(pcts_hours_std)



result = {'media': data_mean.T.mean(), 'desvio padrao': data_std.T.mean()}
result_hours = {'media': pcts_hours_mean.T.mean(), 'desvio padrao': pcts_hours_std.T.mean()}

result = pandas.DataFrame(result)
result_hours = pandas.DataFrame(result_hours)

result.to_csv('../resultados/padrao/result_collect.csv')
result_hours.to_csv('../resultados/pcts_hora/result_collect.csv')

