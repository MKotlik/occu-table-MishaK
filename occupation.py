#Quinn Dibble, Misha Kotlik - Pd. 9
#9/15/16
#Hwk 2 - Occupations

import random, csv

#Global Storage Vars
g_job_names = [] #List of job names, referenced by indeces
g_job_probability = [] #List of indeces to g_job_names

# Reading function
def reader():
	#open the file, and turn it into one big string
	f = open('occupations.csv', 'r')
	rawdata = f.read()
	f.close()
	
	#split the string by the \n character, remove the heading and footing
	joblist = rawdata.split("\n")
	joblist.pop(0)
	joblist.pop(-1)
	joblist.pop(-1)

	#turn each entry into a seperate list, remove " characters, convert the numbers to floats
	jobs = []
	for x in joblist:
		if x[0] == '"':
			x = x[1:len(x)]
			x = x.split('",')
		else:
			x = x.split(',')
		x[1] = float(x[1])
		jobs += [x]

	#return the list of lists
	return jobs

# Dictionary creater function
# Creates a dictionary with job names as keys and percentages as values
def librarian(jobs_list):
	occupations_dict = {}
	for x in jobs_list:
		occupations_dict[x[0]] = x[1]
	return occupations_dict

# Storage function
# Populates global var lists used by chooser given jobs_list from reader()
def storer(jobs_list):
	#Make globals modifiable in function
	global g_job_names
	global g_job_probability
	
	#Iterate over rows of jobs_list, keeping track of ind)
	for ind in range(len(jobs_list)):
		#names of jobs get put into global name list in specific order
		g_job_names += [jobs_list[ind][0]]
		#probability list is a list of indeces corresponding to jobs in the job global
		#each index appears in frequency corresponding to popularity of job
		g_job_probability += ([ind] * int(jobs_list[ind][1] * 10))
	#no return, only modifies globals

# Choosing function
# Returns a random job name based on job popularity
def chooser():
	#Choose a random index for jobs list
	rand_job_ind = random.choice(g_job_probability)
	#Return the corresponding name from the global jobs list
	return g_job_names[rand_job_ind]

# Runtime
jobs_table = reader() #read file into table
storer(jobs_table) #populate global from table
print chooser() #return a random name

