import sys
#from myselector1
import os
_pathadd = os.getcwd()
pathadd=_pathadd.split('\\')

path1 = '\\'.join(pathadd[:-1])
path2 = '\\'.join(pathadd[:-2])
path3 = '\\'.join(pathadd[:-3])
sys.path.extend((path1,path2,path3,_pathadd,'./','../','spiders'))