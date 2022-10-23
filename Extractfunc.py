from symbol import break_stmt
from turtle import bk
from functiondefextractor import core_extractor

srcPath = r'Arducopter'

output0 = core_extractor.extractor (srcPath, exclude=r'*.h, *.txt, wscript, Makefile.waf')

print(output0)
output0.to_csv('ExtractFunctions.csv')  # local folder file , adds sr no #
#output0.to_csv('ExtractFunctions1.csv', index=False )  # local folder file , adds sr no #
break_stm

#extrac delta lines above/below
output1 = core_extractor.extractor_comments(srcPath, annot="get_pilot_desired_yaw_rate", delta="5", exclude=r'*.h, *.txt, wscript, Makefile.waf')
print(output1)
# out_put.to_csv(r'c:\data\pandas.csv', header=None, index=None, sep=' ', mode='a')
# out_put.to_csv(r'c:\data\pandas1.csv', index=False)  # better format 
# out_put.to_csv('pandas2.csv')  # local folder file , adds sr no #


#out_put = core_extractor.check_condition("@SupressWarning", r"c_files", "(")
#print(out_put[0], out_put[1])
output2 = core_extractor.get_delta_lines(file_name="memmgr.c", annot="memmgr_alloc", delta="5")
print(output2)