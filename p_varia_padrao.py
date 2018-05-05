import math
import os
import sys



num_nos = sys.argv[1]
simulacoes = int(sys.argv[2])
simulacoes_res = int(sys.argv[3])
raio = sys.argv[4]
densidade = sys.argv[5]
tipoSimulacao = sys.argv[6]
num_rounds = sys.argv[7]
multiplicadorIntensidade = sys.argv[8]
maxTimeBetweenSends = sys.argv[9] 
minTimeBetweenSends = sys.argv[10]
maxEnergyOfBattery = sys.argv[11]
minEnergyOfBattery = sys.argv[12]
maxSolarIntensity = sys.argv[13]
minSolarIntensity = sys.argv[14]
wattPico = sys.argv[15]

area = int(num_nos)/float(densidade);
lado = int(math.sqrt(area));

for j in range(simulacoes_res,simulacoes+1):
		#
	os.system("java -cp binaries/bin/ sinalgo.Run 							\
			-batch 								  							\
			-project Collect 					  							\
			-gen "+ num_nos + " Collect:GAF  Collect:Grid C=UDG        		\
			-gen 1 Collect:Sink Collect:Grid C=UDG							\
			-rounds "+ num_rounds + "										\
			-overwrite														\
			dimX="+ str(lado) + "											\
			dimY="+ str(lado) + "											\
			GeometricNodeCollection/rMax=" + raio + "						\
			UDG/rMax=" + raio + "											\
																			\
			maxTimeBetweenSends/time=" + maxTimeBetweenSends + "			\
			minTimeBetweenSends/time=" + minTimeBetweenSends + " 			\
																			\
			maxEnergyOfBattery/energy=" + maxEnergyOfBattery + "			\
	        minEnergyOfBattery/energy=" + minEnergyOfBattery + "			\
																			\
			maxSolarIntensity/intensity=" + maxSolarIntensity + "			\
		    minSolarIntensity/intensity=" + minSolarIntensity + "			\
																			\
			wattPico/power=" + wattPico +" 									\
		    radiationMultiplier/multiplier=" + multiplicadorIntensidade + " \
																			\
			nameDir/name=" + str(j) + "										\
		    simulationType/type=" + tipoSimulacao + "		    			\
		    ")
			

os.system('python3 p_processa_' + tipoSimulacao + '.py ' + str(simulacoes) + ' ' + str(num_nos))
os.system('python3 p_processa_cada_no.py ' + str(simulacoes) + ' ' + str(num_nos))
