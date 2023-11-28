import os,sys,math,csv,numpy as npy
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

#======================================================
#Critical Point and Molecular Weight
#======================================================

Pc0 = 0.001
Tc0 = 265.0
Rc0 = 0.0001

Data1=False
Data2=True
Data3=False
Data4=False

#======================================================
#Loading Isotherm Data 1
#======================================================

if Data1==True:
	with open('Data/Data 1 M1/394K_PMMA_75E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_394K = range(0,numpts)
				T0_394K = range(0,numpts)
				R0_394K = range(0,numpts)
				M0_394K = range(0,numpts)
				I0_394K = range(0,numpts)
			if index1 >= 6:
				P0_394K[index2] = float(row[0])
				T0_394K[index2] = float(row[1])
				R0_394K[index2] = float(row[2])
				M0_394K[index2] = float(row[3])
				I0_394K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1
			
	P0 = P0_394K
	T0 = T0_394K
	R0 = R0_394K
	M0 = M0_394K
	I0 = I0_394K

	with open('Data/Data 1 M1/404K_PMMA_75E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_404K = range(0,numpts)
				T0_404K = range(0,numpts)
				R0_404K = range(0,numpts)
				M0_404K = range(0,numpts)
				I0_404K = range(0,numpts)
			if index1 >= 6:
				P0_404K[index2] = float(row[0])
				T0_404K[index2] = float(row[1])
				R0_404K[index2] = float(row[2])
				M0_404K[index2] = float(row[3])
				I0_404K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_404K),axis=0)
	T0 = npy.concatenate((T0,T0_404K),axis=0)
	R0 = npy.concatenate((R0,R0_404K),axis=0)
	M0 = npy.concatenate((M0,M0_404K),axis=0)
	I0 = npy.concatenate((I0,I0_404K),axis=0)

	with open('Data/Data 1 M1/414K_PMMA_75E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_414K = range(0,numpts)
				T0_414K = range(0,numpts)
				R0_414K = range(0,numpts)
				M0_414K = range(0,numpts)
				I0_414K = range(0,numpts)
			if index1 >= 6:
				P0_414K[index2] = float(row[0])
				T0_414K[index2] = float(row[1])
				R0_414K[index2] = float(row[2])
				M0_414K[index2] = float(row[3])
				I0_414K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_414K),axis=0)
	T0 = npy.concatenate((T0,T0_414K),axis=0)
	R0 = npy.concatenate((R0,R0_414K),axis=0)
	M0 = npy.concatenate((M0,M0_414K),axis=0)
	I0 = npy.concatenate((I0,I0_414K),axis=0)

	with open('Data/Data 1 M1/424K_PMMA_75E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_424K = range(0,numpts)
				T0_424K = range(0,numpts)
				R0_424K = range(0,numpts)
				M0_424K = range(0,numpts)
				I0_424K = range(0,numpts)
			if index1 >= 6:
				P0_424K[index2] = float(row[0])
				T0_424K[index2] = float(row[1])
				R0_424K[index2] = float(row[2])
				M0_424K[index2] = float(row[3])
				I0_424K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_424K),axis=0)
	T0 = npy.concatenate((T0,T0_424K),axis=0)
	R0 = npy.concatenate((R0,R0_424K),axis=0)
	M0 = npy.concatenate((M0,M0_424K),axis=0)
	I0 = npy.concatenate((I0,I0_424K),axis=0)

	with open('Data/Data 1 M1/434K_PMMA_75E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_434K = range(0,numpts)
				T0_434K = range(0,numpts)
				R0_434K = range(0,numpts)
				M0_434K = range(0,numpts)
				I0_434K = range(0,numpts)
			if index1 >= 6:
				P0_434K[index2] = float(row[0])
				T0_434K[index2] = float(row[1])
				R0_434K[index2] = float(row[2])
				M0_434K[index2] = float(row[3])
				I0_434K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_434K),axis=0)
	T0 = npy.concatenate((T0,T0_434K),axis=0)
	R0 = npy.concatenate((R0,R0_434K),axis=0)
	M0 = npy.concatenate((M0,M0_434K),axis=0)
	I0 = npy.concatenate((I0,I0_434K),axis=0)

	with open('Data/Data 1 M1/444K_PMMA_75E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_444K = range(0,numpts)
				T0_444K = range(0,numpts)
				R0_444K = range(0,numpts)
				M0_444K = range(0,numpts)
				I0_444K = range(0,numpts)
			if index1 >= 6:
				P0_444K[index2] = float(row[0])
				T0_444K[index2] = float(row[1])
				R0_444K[index2] = float(row[2])
				M0_444K[index2] = float(row[3])
				I0_444K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_444K),axis=0)
	T0 = npy.concatenate((T0,T0_444K),axis=0)
	R0 = npy.concatenate((R0,R0_444K),axis=0)
	M0 = npy.concatenate((M0,M0_444K),axis=0)
	I0 = npy.concatenate((I0,I0_444K),axis=0)

	with open('Data/Data 1 M1/454K_PMMA_75E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_454K = range(0,numpts)
				T0_454K = range(0,numpts)
				R0_454K = range(0,numpts)
				M0_454K = range(0,numpts)
				I0_454K = range(0,numpts)
			if index1 >= 6:
				P0_454K[index2] = float(row[0])
				T0_454K[index2] = float(row[1])
				R0_454K[index2] = float(row[2])
				M0_454K[index2] = float(row[3])
				I0_454K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_454K),axis=0)
	T0 = npy.concatenate((T0,T0_454K),axis=0)
	R0 = npy.concatenate((R0,R0_454K),axis=0)
	M0 = npy.concatenate((M0,M0_454K),axis=0)
	I0 = npy.concatenate((I0,I0_454K),axis=0)

	with open('Data/Data 1 M1/464K_PMMA_75E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_464K = range(0,numpts)
				T0_464K = range(0,numpts)
				R0_464K = range(0,numpts)
				M0_464K = range(0,numpts)
				I0_464K = range(0,numpts)
			if index1 >= 6:
				P0_464K[index2] = float(row[0])
				T0_464K[index2] = float(row[1])
				R0_464K[index2] = float(row[2])
				M0_464K[index2] = float(row[3])
				I0_464K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_464K),axis=0)
	T0 = npy.concatenate((T0,T0_464K),axis=0)
	R0 = npy.concatenate((R0,R0_464K),axis=0)
	M0 = npy.concatenate((M0,M0_464K),axis=0)
	I0 = npy.concatenate((I0,I0_464K),axis=0)

#======================================================
#Loading Isotherm Data 2
#======================================================

if Data2==True:
	with open('Data/Data 2 M1/373K_PMMA_12E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_373K = range(0,numpts)
				T0_373K = range(0,numpts)
				R0_373K = range(0,numpts)
				M0_373K = range(0,numpts)
				I0_373K = range(0,numpts)
			if index1 >= 6:
				P0_373K[index2] = float(row[0])
				T0_373K[index2] = float(row[1])
				R0_373K[index2] = float(row[2])
				M0_373K[index2] = float(row[3])
				I0_373K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1
			
	P0 = P0_373K
	T0 = T0_373K
	R0 = R0_373K
	M0 = M0_373K
	I0 = I0_373K

	with open('Data/Data 2 M1/378K_PMMA_12E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_378K = range(0,numpts)
				T0_378K = range(0,numpts)
				R0_378K = range(0,numpts)
				M0_378K = range(0,numpts)
				I0_378K = range(0,numpts)
			if index1 >= 6:
				P0_378K[index2] = float(row[0])
				T0_378K[index2] = float(row[1])
				R0_378K[index2] = float(row[2])
				M0_378K[index2] = float(row[3])
				I0_378K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_378K),axis=0)
	T0 = npy.concatenate((T0,T0_378K),axis=0)
	R0 = npy.concatenate((R0,R0_378K),axis=0)
	M0 = npy.concatenate((M0,M0_378K),axis=0)
	I0 = npy.concatenate((I0,I0_378K),axis=0)

	with open('Data/Data 2 M1/383K_PMMA_12E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_383K = range(0,numpts)
				T0_383K = range(0,numpts)
				R0_383K = range(0,numpts)
				M0_383K = range(0,numpts)
				I0_383K = range(0,numpts)
			if index1 >= 6:
				P0_383K[index2] = float(row[0])
				T0_383K[index2] = float(row[1])
				R0_383K[index2] = float(row[2])
				M0_383K[index2] = float(row[3])
				I0_383K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_383K),axis=0)
	T0 = npy.concatenate((T0,T0_383K),axis=0)
	R0 = npy.concatenate((R0,R0_383K),axis=0)
	M0 = npy.concatenate((M0,M0_383K),axis=0)
	I0 = npy.concatenate((I0,I0_383K),axis=0)

	with open('Data/Data 2 M1/388K_PMMA_12E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_388K = range(0,numpts)
				T0_388K = range(0,numpts)
				R0_388K = range(0,numpts)
				M0_388K = range(0,numpts)
				I0_388K = range(0,numpts)
			if index1 >= 6:
				P0_388K[index2] = float(row[0])
				T0_388K[index2] = float(row[1])
				R0_388K[index2] = float(row[2])
				M0_388K[index2] = float(row[3])
				I0_388K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_388K),axis=0)
	T0 = npy.concatenate((T0,T0_388K),axis=0)
	R0 = npy.concatenate((R0,R0_388K),axis=0)
	M0 = npy.concatenate((M0,M0_388K),axis=0)
	I0 = npy.concatenate((I0,I0_388K),axis=0)

	with open('Data/Data 2 M1/393K_PMMA_12E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_393K = range(0,numpts)
				T0_393K = range(0,numpts)
				R0_393K = range(0,numpts)
				M0_393K = range(0,numpts)
				I0_393K = range(0,numpts)
			if index1 >= 6:
				P0_393K[index2] = float(row[0])
				T0_393K[index2] = float(row[1])
				R0_393K[index2] = float(row[2])
				M0_393K[index2] = float(row[3])
				I0_393K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_393K),axis=0)
	T0 = npy.concatenate((T0,T0_393K),axis=0)
	R0 = npy.concatenate((R0,R0_393K),axis=0)
	M0 = npy.concatenate((M0,M0_393K),axis=0)
	I0 = npy.concatenate((I0,I0_393K),axis=0)

	with open('Data/Data 2 M1/398K_PMMA_12E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_398K = range(0,numpts)
				T0_398K = range(0,numpts)
				R0_398K = range(0,numpts)
				M0_398K = range(0,numpts)
				I0_398K = range(0,numpts)
			if index1 >= 6:
				P0_398K[index2] = float(row[0])
				T0_398K[index2] = float(row[1])
				R0_398K[index2] = float(row[2])
				M0_398K[index2] = float(row[3])
				I0_398K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_398K),axis=0)
	T0 = npy.concatenate((T0,T0_398K),axis=0)
	R0 = npy.concatenate((R0,R0_398K),axis=0)
	M0 = npy.concatenate((M0,M0_398K),axis=0)
	I0 = npy.concatenate((I0,I0_398K),axis=0)

	with open('Data/Data 2 M1/403K_PMMA_12E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_403K = range(0,numpts)
				T0_403K = range(0,numpts)
				R0_403K = range(0,numpts)
				M0_403K = range(0,numpts)
				I0_403K = range(0,numpts)
			if index1 >= 6:
				P0_403K[index2] = float(row[0])
				T0_403K[index2] = float(row[1])
				R0_403K[index2] = float(row[2])
				M0_403K[index2] = float(row[3])
				I0_403K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_403K),axis=0)
	T0 = npy.concatenate((T0,T0_403K),axis=0)
	R0 = npy.concatenate((R0,R0_403K),axis=0)
	M0 = npy.concatenate((M0,M0_403K),axis=0)
	I0 = npy.concatenate((I0,I0_403K),axis=0)

	with open('Data/Data 2 M1/408K_PMMA_12E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_408K = range(0,numpts)
				T0_408K = range(0,numpts)
				R0_408K = range(0,numpts)
				M0_408K = range(0,numpts)
				I0_408K = range(0,numpts)
			if index1 >= 6:
				P0_408K[index2] = float(row[0])
				T0_408K[index2] = float(row[1])
				R0_408K[index2] = float(row[2])
				M0_408K[index2] = float(row[3])
				I0_408K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_408K),axis=0)
	T0 = npy.concatenate((T0,T0_408K),axis=0)
	R0 = npy.concatenate((R0,R0_408K),axis=0)
	M0 = npy.concatenate((M0,M0_408K),axis=0)
	I0 = npy.concatenate((I0,I0_408K),axis=0)

	with open('Data/Data 2 M1/413K_PMMA_12E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_413K = range(0,numpts)
				T0_413K = range(0,numpts)
				R0_413K = range(0,numpts)
				M0_413K = range(0,numpts)
				I0_413K = range(0,numpts)
			if index1 >= 6:
				P0_413K[index2] = float(row[0])
				T0_413K[index2] = float(row[1])
				R0_413K[index2] = float(row[2])
				M0_413K[index2] = float(row[3])
				I0_413K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_413K),axis=0)
	T0 = npy.concatenate((T0,T0_413K),axis=0)
	R0 = npy.concatenate((R0,R0_413K),axis=0)
	M0 = npy.concatenate((M0,M0_413K),axis=0)
	I0 = npy.concatenate((I0,I0_413K),axis=0)

	with open('Data/Data 2 M1/418K_PMMA_12E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_418K = range(0,numpts)
				T0_418K = range(0,numpts)
				R0_418K = range(0,numpts)
				M0_418K = range(0,numpts)
				I0_418K = range(0,numpts)
			if index1 >= 6:
				P0_418K[index2] = float(row[0])
				T0_418K[index2] = float(row[1])
				R0_418K[index2] = float(row[2])
				M0_418K[index2] = float(row[3])
				I0_418K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_418K),axis=0)
	T0 = npy.concatenate((T0,T0_418K),axis=0)
	R0 = npy.concatenate((R0,R0_418K),axis=0)
	M0 = npy.concatenate((M0,M0_418K),axis=0)
	I0 = npy.concatenate((I0,I0_418K),axis=0)

	with open('Data/Data 2 M1/423K_PMMA_12E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_423K = range(0,numpts)
				T0_423K = range(0,numpts)
				R0_423K = range(0,numpts)
				M0_423K = range(0,numpts)
				I0_423K = range(0,numpts)
			if index1 >= 6:
				P0_423K[index2] = float(row[0])
				T0_423K[index2] = float(row[1])
				R0_423K[index2] = float(row[2])
				M0_423K[index2] = float(row[3])
				I0_423K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_423K),axis=0)
	T0 = npy.concatenate((T0,T0_423K),axis=0)
	R0 = npy.concatenate((R0,R0_423K),axis=0)
	M0 = npy.concatenate((M0,M0_423K),axis=0)
	I0 = npy.concatenate((I0,I0_423K),axis=0)

	with open('Data/Data 2 M1/428K_PMMA_12E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_428K = range(0,numpts)
				T0_428K = range(0,numpts)
				R0_428K = range(0,numpts)
				M0_428K = range(0,numpts)
				I0_428K = range(0,numpts)
			if index1 >= 6:
				P0_428K[index2] = float(row[0])
				T0_428K[index2] = float(row[1])
				R0_428K[index2] = float(row[2])
				M0_428K[index2] = float(row[3])
				I0_428K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_428K),axis=0)
	T0 = npy.concatenate((T0,T0_428K),axis=0)
	R0 = npy.concatenate((R0,R0_428K),axis=0)
	M0 = npy.concatenate((M0,M0_428K),axis=0)
	I0 = npy.concatenate((I0,I0_428K),axis=0)

	with open('Data/Data 2 M1/433K_PMMA_12E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_433K = range(0,numpts)
				T0_433K = range(0,numpts)
				R0_433K = range(0,numpts)
				M0_433K = range(0,numpts)
				I0_433K = range(0,numpts)
			if index1 >= 6:
				P0_433K[index2] = float(row[0])
				T0_433K[index2] = float(row[1])
				R0_433K[index2] = float(row[2])
				M0_433K[index2] = float(row[3])
				I0_433K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_433K),axis=0)
	T0 = npy.concatenate((T0,T0_433K),axis=0)
	R0 = npy.concatenate((R0,R0_433K),axis=0)
	M0 = npy.concatenate((M0,M0_433K),axis=0)
	I0 = npy.concatenate((I0,I0_433K),axis=0)

	with open('Data/Data 2 M1/438K_PMMA_12E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_438K = range(0,numpts)
				T0_438K = range(0,numpts)
				R0_438K = range(0,numpts)
				M0_438K = range(0,numpts)
				I0_438K = range(0,numpts)
			if index1 >= 6:
				P0_438K[index2] = float(row[0])
				T0_438K[index2] = float(row[1])
				R0_438K[index2] = float(row[2])
				M0_438K[index2] = float(row[3])
				I0_438K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_438K),axis=0)
	T0 = npy.concatenate((T0,T0_438K),axis=0)
	R0 = npy.concatenate((R0,R0_438K),axis=0)
	M0 = npy.concatenate((M0,M0_438K),axis=0)
	I0 = npy.concatenate((I0,I0_438K),axis=0)

#======================================================
#Loading Isotherm Data 3
#======================================================

if Data3==True:
	with open('Data/Data 3 M1(Overlap Only)/393K_PMMA_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_393K = range(0,numpts)
				T0_393K = range(0,numpts)
				R0_393K = range(0,numpts)
				M0_393K = range(0,numpts)
				I0_393K = range(0,numpts)
			if index1 >= 6:
				P0_393K[index2] = float(row[0])
				T0_393K[index2] = float(row[1])
				R0_393K[index2] = float(row[2])
				M0_393K[index2] = float(row[3])
				I0_393K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1
			
	P0 = P0_393K
	T0 = T0_393K
	R0 = R0_393K
	M0 = M0_393K
	I0 = I0_393K

	with open('Data/Data 3 M1(Overlap Only)/403K_PMMA_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_403K = range(0,numpts)
				T0_403K = range(0,numpts)
				R0_403K = range(0,numpts)
				M0_403K = range(0,numpts)
				I0_403K = range(0,numpts)
			if index1 >= 6:
				P0_403K[index2] = float(row[0])
				T0_403K[index2] = float(row[1])
				R0_403K[index2] = float(row[2])
				M0_403K[index2] = float(row[3])
				I0_403K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_403K),axis=0)
	T0 = npy.concatenate((T0,T0_403K),axis=0)
	R0 = npy.concatenate((R0,R0_403K),axis=0)
	M0 = npy.concatenate((M0,M0_403K),axis=0)
	I0 = npy.concatenate((I0,I0_403K),axis=0)

	with open('Data/Data 3 M1(Overlap Only)/413K_PMMA_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_413K = range(0,numpts)
				T0_413K = range(0,numpts)
				R0_413K = range(0,numpts)
				M0_413K = range(0,numpts)
				I0_413K = range(0,numpts)
			if index1 >= 6:
				P0_413K[index2] = float(row[0])
				T0_413K[index2] = float(row[1])
				R0_413K[index2] = float(row[2])
				M0_413K[index2] = float(row[3])
				I0_413K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_413K),axis=0)
	T0 = npy.concatenate((T0,T0_413K),axis=0)
	R0 = npy.concatenate((R0,R0_413K),axis=0)
	M0 = npy.concatenate((M0,M0_413K),axis=0)
	I0 = npy.concatenate((I0,I0_413K),axis=0)

	with open('Data/Data 3 M1(Overlap Only)/423K_PMMA_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_423K = range(0,numpts)
				T0_423K = range(0,numpts)
				R0_423K = range(0,numpts)
				M0_423K = range(0,numpts)
				I0_423K = range(0,numpts)
			if index1 >= 6:
				P0_423K[index2] = float(row[0])
				T0_423K[index2] = float(row[1])
				R0_423K[index2] = float(row[2])
				M0_423K[index2] = float(row[3])
				I0_423K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_423K),axis=0)
	T0 = npy.concatenate((T0,T0_423K),axis=0)
	R0 = npy.concatenate((R0,R0_423K),axis=0)
	M0 = npy.concatenate((M0,M0_423K),axis=0)
	I0 = npy.concatenate((I0,I0_423K),axis=0)

	with open('Data/Data 3 M1(Overlap Only)/433K_PMMA_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_433K = range(0,numpts)
				T0_433K = range(0,numpts)
				R0_433K = range(0,numpts)
				M0_433K = range(0,numpts)
				I0_433K = range(0,numpts)
			if index1 >= 6:
				P0_433K[index2] = float(row[0])
				T0_433K[index2] = float(row[1])
				R0_433K[index2] = float(row[2])
				M0_433K[index2] = float(row[3])
				I0_433K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_433K),axis=0)
	T0 = npy.concatenate((T0,T0_433K),axis=0)
	R0 = npy.concatenate((R0,R0_433K),axis=0)
	M0 = npy.concatenate((M0,M0_433K),axis=0)
	I0 = npy.concatenate((I0,I0_433K),axis=0)

	with open('Data/Data 3 M1(Overlap Only)/443K_PMMA_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_443K = range(0,numpts)
				T0_443K = range(0,numpts)
				R0_443K = range(0,numpts)
				M0_443K = range(0,numpts)
				I0_443K = range(0,numpts)
			if index1 >= 6:
				P0_443K[index2] = float(row[0])
				T0_443K[index2] = float(row[1])
				R0_443K[index2] = float(row[2])
				M0_443K[index2] = float(row[3])
				I0_443K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_443K),axis=0)
	T0 = npy.concatenate((T0,T0_443K),axis=0)
	R0 = npy.concatenate((R0,R0_443K),axis=0)
	M0 = npy.concatenate((M0,M0_443K),axis=0)
	I0 = npy.concatenate((I0,I0_443K),axis=0)

	with open('Data/Data 3 M1(Overlap Only)/453K_PMMA_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_453K = range(0,numpts)
				T0_453K = range(0,numpts)
				R0_453K = range(0,numpts)
				M0_453K = range(0,numpts)
				I0_453K = range(0,numpts)
			if index1 >= 6:
				P0_453K[index2] = float(row[0])
				T0_453K[index2] = float(row[1])
				R0_453K[index2] = float(row[2])
				M0_453K[index2] = float(row[3])
				I0_453K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_453K),axis=0)
	T0 = npy.concatenate((T0,T0_453K),axis=0)
	R0 = npy.concatenate((R0,R0_453K),axis=0)
	M0 = npy.concatenate((M0,M0_453K),axis=0)
	I0 = npy.concatenate((I0,I0_453K),axis=0)

	with open('Data/Data 3 M1(Overlap Only)/463K_PMMA_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_463K = range(0,numpts)
				T0_463K = range(0,numpts)
				R0_463K = range(0,numpts)
				M0_463K = range(0,numpts)
				I0_463K = range(0,numpts)
			if index1 >= 6:
				P0_463K[index2] = float(row[0])
				T0_463K[index2] = float(row[1])
				R0_463K[index2] = float(row[2])
				M0_463K[index2] = float(row[3])
				I0_463K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_463K),axis=0)
	T0 = npy.concatenate((T0,T0_463K),axis=0)
	R0 = npy.concatenate((R0,R0_463K),axis=0)
	M0 = npy.concatenate((M0,M0_463K),axis=0)
	I0 = npy.concatenate((I0,I0_463K),axis=0)

	with open('Data/Data 3 M1(Overlap Only)/473K_PMMA_9E4_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_473K = range(0,numpts)
				T0_473K = range(0,numpts)
				R0_473K = range(0,numpts)
				M0_473K = range(0,numpts)
				I0_473K = range(0,numpts)
			if index1 >= 6:
				P0_473K[index2] = float(row[0])
				T0_473K[index2] = float(row[1])
				R0_473K[index2] = float(row[2])
				M0_473K[index2] = float(row[3])
				I0_473K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_473K),axis=0)
	T0 = npy.concatenate((T0,T0_473K),axis=0)
	R0 = npy.concatenate((R0,R0_473K),axis=0)
	M0 = npy.concatenate((M0,M0_473K),axis=0)
	I0 = npy.concatenate((I0,I0_473K),axis=0)

#======================================================
#Loading Isotherm Data 4
#======================================================

if Data4==True:
	with open('Data/Data 4/405K_PMMA_387E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_405K = range(0,numpts)
				T0_405K = range(0,numpts)
				R0_405K = range(0,numpts)
				M0_405K = range(0,numpts)
				I0_405K = range(0,numpts)
			if index1 >= 6:
				P0_405K[index2] = float(row[0])
				T0_405K[index2] = float(row[1])
				R0_405K[index2] = float(row[2])
				M0_405K[index2] = float(row[3])
				I0_405K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1
			
	P0 = P0_405K
	T0 = T0_405K
	R0 = R0_405K
	M0 = M0_405K
	I0 = I0_405K

	with open('Data/Data 4/420K_PMMA_387E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_420K = range(0,numpts)
				T0_420K = range(0,numpts)
				R0_420K = range(0,numpts)
				M0_420K = range(0,numpts)
				I0_420K = range(0,numpts)
			if index1 >= 6:
				P0_420K[index2] = float(row[0])
				T0_420K[index2] = float(row[1])
				R0_420K[index2] = float(row[2])
				M0_420K[index2] = float(row[3])
				I0_420K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_420K),axis=0)
	T0 = npy.concatenate((T0,T0_420K),axis=0)
	R0 = npy.concatenate((R0,R0_420K),axis=0)
	M0 = npy.concatenate((M0,M0_420K),axis=0)
	I0 = npy.concatenate((I0,I0_420K),axis=0)

	with open('Data/Data 4/435K_PMMA_387E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_435K = range(0,numpts)
				T0_435K = range(0,numpts)
				R0_435K = range(0,numpts)
				M0_435K = range(0,numpts)
				I0_435K = range(0,numpts)
			if index1 >= 6:
				P0_435K[index2] = float(row[0])
				T0_435K[index2] = float(row[1])
				R0_435K[index2] = float(row[2])
				M0_435K[index2] = float(row[3])
				I0_435K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_435K),axis=0)
	T0 = npy.concatenate((T0,T0_435K),axis=0)
	R0 = npy.concatenate((R0,R0_435K),axis=0)
	M0 = npy.concatenate((M0,M0_435K),axis=0)
	I0 = npy.concatenate((I0,I0_435K),axis=0)

	with open('Data/Data 4/450K_PMMA_387E3_PVT.csv','rb') as csvfile:
		datareader = csv.reader(csvfile)
		#x0 = (float(column[1]) for column in datareader)
		index1 = 0
		index2 = 0
		for row in datareader:
			if index1 == 4:
				numpts = int(float(row[0]))
				P0_450K = range(0,numpts)
				T0_450K = range(0,numpts)
				R0_450K = range(0,numpts)
				M0_450K = range(0,numpts)
				I0_450K = range(0,numpts)
			if index1 >= 6:
				P0_450K[index2] = float(row[0])
				T0_450K[index2] = float(row[1])
				R0_450K[index2] = float(row[2])
				M0_450K[index2] = float(row[3])
				I0_450K[index2] = 'isotherm'
				index2 = index2 + 1
			index1 = index1 + 1

	P0 = npy.concatenate((P0,P0_450K),axis=0)
	T0 = npy.concatenate((T0,T0_450K),axis=0)
	R0 = npy.concatenate((R0,R0_450K),axis=0)
	M0 = npy.concatenate((M0,M0_450K),axis=0)
	I0 = npy.concatenate((I0,I0_450K),axis=0)

#======================================================
#Isotherm PVT Data
#======================================================

#Including all experimental data.
#temp = ['303K','312K','321K','332K','343K','354K','364K','373K','383K','393K','402K','412K','422K','432K','442K','452K','463K','473K','482K','492K','503K','513K','524K']
#Only data 20K above the glass transition.
#temp = ['402K','412K','422K','432K','442K','452K','463K','473K','482K','492K','503K','513K','524K']
#All data excluding all data within 20K of the glass transition.
#temp = ['303K','312K','321K','332K','343K','402K','412K','422K','432K','442K','452K','463K','473K','482K','492K','503K','513K','524K']

#for i in range(0,len(temp)):
#	exec "P0_%s,T0_%s,R0_%s,M0_%s,I0_%s = loadExperimentalData('%s_PMMA_11E4_PVT','isotherm',True)" % (temp[i],temp[i],temp[i],temp[i],temp[i],temp[i])