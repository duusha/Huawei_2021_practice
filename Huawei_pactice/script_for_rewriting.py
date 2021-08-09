import string
import os
import shutil 
def get_name (start):
	name = start[:start.find(':'):]
	output_name = name[:name.find('.')] +'_output.c'
	return output_name
def script(start, end, decls, struct_name, hot):
	print(struct_name)
	start = str(start)
	end = str(end)
	name = start[:start.find(':'):]
	line_start = int(start[start.find(':') + 1: start.find(':', start.find(':') + 1, ):])
	line_end = int(end[end.find(':') + 1: end.find(':', end.find(':') + 1, ):]) + 1
	#print(name, line_start, line_end)
	output_name = name[:name.find('.')] +'_output.c'
	f_in = open(name, 'r')
	f_out = open(output_name, 'w')
	struct_1_inp = ''
	struct_2_inp = ''
	for decl in decls:
		_type = decl.type.type.names
		_type = ' '.join(_type)
		if decl.name in hot:
			struct_1_inp += '\t' + _type + ' ' + decl.name + ';\n'
		else:
			struct_2_inp += '\t' + _type + ' ' + decl.name + ';\n'

	for num, line in enumerate(f_in.readlines()):
		if num == line_start:
			f_out.write('typedef struct _' + struct_name + '1 {\n' + struct_1_inp + '}' + '_' + struct_name + '1;' + '\n' + '_' + struct_name + '1 ' + struct_name + '1;\n')
		if (num == line_end):
			f_out.write('typedef struct _' + struct_name + '2 {\n' + struct_2_inp + '}' + '_' + struct_name + '2;'+ '\n' + '_' + struct_name + '2 ' + struct_name + '2;\n')
		#if (num not in range(line_start - 1, line_end)):
		#	f_out.write(line)
	f_in.close()
	f_out.close()

	
	# for decl in decls:
	# 	if(decl.name in hot):

		

	f_in.close()
	f_out.close()
