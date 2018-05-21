#! /usr/bin/env python3

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
constBattery = sys.argv[16]
constIntensity = sys.argv[17]
varia_min = int(sys.argv[18])
varia_max = int(sys.argv[19])
varia_tic = int(sys.argv[20])
varia_res = int(sys.argv[21])
constControl = sys.argv[22]


for i in range(varia_res, varia_max+1, varia_tic):
	
	densidade = i/100.0
	area = int(num_nos)/densidade
	lado = int(math.sqrt(area)) 
    
	for j in range(simulacoes_res,simulacoes+1):
		
		os.system("java -cp binaries/bin/ sinalgo.Run 						\
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
			nameDir/name=" + str(i) + str(j) + "							\
		    simulationType/type=" + tipoSimulacao + "		    			\
																			\
			constBattery/number=" + constBattery + " 						\
		    constIntensity/number=" + constIntensity + "					\
																			\
			constControl/number=" + constControl + "						\
		    ")									
				
os.system('./d_processa_' + tipoSimulacao + '.py ' + str(simulacoes) + ' ' + str(num_nos) + ' ' + str(varia_min) + ' ' + \
		  str(varia_max) + ' '+ str(varia_tic))
