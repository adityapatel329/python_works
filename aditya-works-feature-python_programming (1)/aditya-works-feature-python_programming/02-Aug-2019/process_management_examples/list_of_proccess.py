import psutil

psutil.process_iter(attrs=None, ad_value=None)

for proc in psutil.process_iter():
    try:
        processName = proc.name()
        processID = proc.pid
        print(processName , "--",processID)
    except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombiePRocess):
        pass
