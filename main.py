import os

#create dir if there is none with same name
def create_proj_dir(directory):
	if not os.path.exists(directory):
		print('Creating project '+directory)
		os.makedirs(directory)

#create directory
create_proj_dir('testing_file')