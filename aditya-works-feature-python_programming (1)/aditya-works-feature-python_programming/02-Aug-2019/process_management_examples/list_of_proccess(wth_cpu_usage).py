from psutil import * 

as_dict(attrs=None, ad_value=None)
pInfoDict = processObj.as_dict(attrs=['pid','name','cpu_percent'])
listOfProcessNames = list()

for proc in psutil.process_iter():

    pInfoDict = proc.as_dict(attrs=['pid','name','cpu_percent'])

    listOfProcessNames.append(pInfoDict)
