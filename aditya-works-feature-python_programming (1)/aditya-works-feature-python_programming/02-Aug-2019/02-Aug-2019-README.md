## Process Management
* Passenger manages multiple processes in order to maximize stability and
performance.
* Learn how passenger manages processes and learn about Passenger's
process management tools.
* You have learned in Fundamental concepts that at its core,
Passenger is a process manager.
* Instead of running an application inside its process space,
launches the application as external processes, and manages them.
* Passenger load balances traffic between processes, shuts down
processes when they're no longer needed or when they misbehave, keeps them 
running and restarts them when they crash, etc.
* Initially, Passenger only spawns one application process.
* But sometimes it may decide to spawn multiple processes.
* Here are the reason why this is sometimes beneficial :
1. Performance : 
The more process you run , the better the CPU core utilization,
up until the hardware limit.

2. I/O concurrency : 
The more processes you run, the greater the amount of available I/O concurrency.
This makes your app perform better.

3. Stability : If an application process crashes, other processes are unaffected 
and can take over while Passenger restarts the crashed process.

4. Keeping problem in check : Many problem, such as leaking memory
or getting stuck, can be kept in check by restarting the process where 
the problem occurred.

## Some Basic Command  for Processes Management : 
#### Finding process id
```
import os
os.getpid()
```
#### Finding process name
```
import os
import psutil

process = psutil.Process(os.getpid())

process_name = process.name()

print("Process Name : ",process_name)
```
#### How to terminate Process
```
import os 
import psutil

p = psutil.Process(os.getpid())

p.terminate()
```
#### Id function in Python
```
str = "aditya"
print(id(str))
```
## File Subsystem Utility
* The Window Subsystem for Linux(WSL) is a new Windows 10 feature that
enables you to run native Linux command-lin tools directly on Windows, 
alongside your traditional Windows desktop and modern store apps.

#### Who is WSL for ?
* This is primarily a tool for developers --especially web 
developers and those who work on or with open source projects.
* This allows those who want/need to use Bash, common Linux tools and
many linux-first tools(Ruby , Python,etc) to use their toolchain on Windows.

#### What can I do with WSL ?
* WSL provides an application called Bash.exe that, when started, opens a Windows
console running the Bash shell. 
* Using BAsh, you can run command-line Linux tools and apps.
* For example, type lsb_release -a and hit enter; you'll see details
of the Linux distro currently running:
```
lsb_release -a 
``` 
* You can also access your local machine's filesystem from within the 
Linux Bash shell - you'll find your local drives mounted under the 
/mnt folder. For example your c: Drive is mounted under 
/mntc/ c :

#### What is Bash ?
* Bash is a popular text-based shell and command-language.
* It is the default shell included within Ubuntu and other Linux distros,
and macOS.
* Users type commands into a shell to execute scripts and/or run commands and tools
to accomplish many tasks.
#### Why would I use WSL rather than Linux in a VM ?
* WSL requires fewer resources(CPU, memory, and storage)than a full virtual
machine.
* WSL also allows you to run Linux command-line tools and apps
alongside your Windows command-line tools and apps alongside you Windows command-line, desktop
and store apps, and to access your Windows file from with Linux. 
* This enables you to use Windows apps and Linux Windows files from within
Linux. This enables you to use Windows apps and Linux command-line tools on the 
same set of files.
#### Why would I use, for example,Ruby on Linux instead of on Windows ?
* Some cross-platform tools were built assuming that the environment in whic
they run behaves like Linux.
* For example, som tools assume that they are able to access very long file 
paths or that specific files/folder exist.

#### How do I access my C: drive ?
* Mount points for hard drives on the local machine are automatically created and provide easy access to the
Windows filesystem.
```
/mnt/<drive letter>/
Example usage would be cd /mnt/c to access c:\
``` 
## File Checksum in Python
* Remember that a hash is a function that takes a variable length sequence of bytes
and converts it to a fixed length sequence.
* Calculating a hash for a file is always useful when you need to check if 
two files are identical, or to make sure that the contents of a file 
were not changed, and to check the integrity of file when it is transmitted over
a network.
* When you download a file on a website, the website will provide the MD5 or SHA
checksum, and this is helpful because you can verify the file downloaded well.
#### Hashing Algorithms
* The most used algorithms to hash a file are MD5 and SHA-1.
* They are used because they are fast and they provide a good way
to identify different files.
* The hash function only uses the contents of the file, not the name.
* Getting the same hash of two separating file means that there is a high 
probability the contents of the file are identical, even though they have 
different names.

#### MD5 Files Hash in Python
* The code above calculates the MD5 digest of the file.
* The file is opened in rb mode, which means that you are going to read 
the file in binary mode.
* This because the MD5 function needs to read the file as a sequence of bytes.
* This will make sure that you can hash any type of file, not only text files.
* It is important to notice the read function. When it is called with no arguments,
like in this case, it will read all the contents of the file and load them into
memory.
* This is dangerous if you are not sure of the file's size 


