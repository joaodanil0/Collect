import os
import math

num_nos = 4

density = 0.03
rangeNode = 30

area = num_nos/density;
side = int(math.sqrt(area));

#	-batch
os.system('java -cp binaries/bin sinalgo.Run							\
		   																\
		   -project Collect												\
		   -gen '+ str(num_nos) + ' Collect:GAF Collect:Grid C=UDG   	\
		   -gen 1  Collect:Sink Collect:Grid C=UDG						\
		   -rounds 259200												\
		   -overwrite													\
		   dimX=' + str(side) + '										\
		   dimY=' + str(side) + '										\
		   GeometricNodeCollection/rMax=' + str(rangeNode) + '			\
		   UDG/rMax=' + str(rangeNode) + '								\
																		\
		   maxTimeBetweenSends/time=7200								\
		   minTimeBetweenSends/time=300 								\
																		\
		   maxEnergyOfBattery/energy=1000								\
		   minEnergyOfBattery/energy=0									\
																		\
		   maxSolarIntensity/intensity=1000								\
		   minSolarIntensity/intensity=0								\
																		\
		   wattPico/power=0.15											\
		   radiationMultiplier/multiplier=0.75							\
		  ')