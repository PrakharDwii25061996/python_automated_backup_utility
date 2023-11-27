# !Python3
# backToZip.py - copies an entire folder and its contents into
# a Zip file whose fileName increments.

import zipfile, os


def backupToZip(file_name):

	folder_name = 'new_folder'

	with zipfile.ZipFile(f'{folder_name}.zip', 'w') as zfile:
		# zfile.write(file_name)
		print(zfile.printdir())


# def backup_file_information():

# 	with zipfile.ZipInfo(f'new_folder.')


if __name__ == '__main__':

	file_name = input('Enter name of the file you want to create: ')

	# file = open(f"{os.getcwd()}/new_folder/{file_name}", "x")
	# file.close()

	backupToZip(file_name)

	# backup_file_information()

