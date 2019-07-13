import os

#create dir if there is none with same name
def create_proj_dir(directory):
	if not os.path.exists(directory):
		print('Creating project '+directory)
		os.makedirs(directory)

#create directory
create_proj_dir('testing_file')


#create queue and crawled files
def create_data_file(proj_name,base_url):
	queue=proj_name+'/queue.txt'
	crawled=proj_name+'/crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue,base_url)
	if not os.path.isfile(crawled):
		write_file(crawled,'')

def append_file(path,data):
	with open(path,'a') as file:
		file.write_file(data+'\n')




#create new file
def write_file(path,data):
	f=open(path,'w')
	f.write(data)
	f.close()

create_data_file(hui,https://363687847.github.io/)