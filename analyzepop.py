import matplotlib.pyplot as plt
import csv

# Global Variables
year=[]
population=[]

with open("population_csv.csv") as f:
	reader=csv.reader(f)
	header_row=next(reader)
#	print(header_row[:2])
	for row in reader:
		if int(row[0]) < -2000:
			continue
		"""elif int(row[0]) >= 1700:
			break"""
		try:
			population.append(int(row[8]))
		except ValueError:
			print(row[0],": Missing Data")
			continue
		else:
			year.append(int(row[0]))
plt.plot(year,population)
plt.xlabel("Year")
plt.ylabel("Population (in millions)")
plt.title("History of Population Change")
plt.show()
