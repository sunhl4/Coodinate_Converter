import os
from openbabel import openbabel
def multi_file_convert(file_PATH,input_format,output_format):
‘’‘
file_PATH是指文件夹所在位置，本份代码使用了相对路径
input_format是指输入文件的格式，本分代码待转换的文件格式是poscar
output_format是指输出文件的格式，本份代码想得到的文件格式是xyz

’‘’
    tqdm=os.listdir(file_PATH)#文件夹中的文件列表
    for i in range(0,len(tqdm)):#逐次遍历文件夹下的文件
        inputfile = os.path.join(file_PATH,tqdm[i])#对应文件夹下的某份文件
        conv=openbabel.OBConversion()#调用转换函数
        conv.OpenInAndOutFiles(inputfile,inputfile+'_'+'.xyz')#输入待转换的文件名及定义转换成功后的文件名
        conv.SetInAndOutFormats(input_format,output_format)
        conv.Convert()
        conv.CloseOutFile()
multi_file_convert("C-N-2-defect-1652750340",'poscar','xyz')
