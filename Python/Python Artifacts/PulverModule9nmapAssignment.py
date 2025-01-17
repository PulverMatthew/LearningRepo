#Imports optparse for program options, nmap for port scanning, and threading for multithreading.
import optparse
import nmap
from threading import *

#Synchronize threads one at a time.
screenLock = Semaphore(value=1)

#Defines the nmap scanning function acquires a lock then releases it when done.
#Runs an instance of nmap and scans a port specified in options -H and -P.
#Records if a port is open, closed, or filtered in the state variable.
#Prints results.
def nmapScan(tgtHost, tgtPort):
        nmScan = nmap.PortScanner()
        nmScan.scan(tgtHost, tgtPort)
        screenLock.acquire()
        state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
        print("[*] " + tgtHost + " tcp/"+tgtPort+" "+state)
        screenLock.release()
#Main functions, defines options -H and -P for the program and exits if an option is incorrectly used.   
def main():
    parser = optparse.OptionParser("usage%prog "+"-H <target host> -P <target port>")
    parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'specify target host')
    parser.add_option('-P', dest = 'tgtPort', type = 'string', help = 'specify target port[s] separated by commas')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost is None) or (tgtPorts[0] is None):
       print (parser.usage)
       exit(0)
    #Starts a multithreaded nmapScan process for every target port.
    for tgtPort in tgtPorts:
        t = Thread(target=nmapScan, args=(tgtHost,tgtPort))
        t.start()
if __name__ == '__main__':
    main()
