from SOAPpy import SOAPProxy
url = 'http://services.xmethods.net:80/soap/servlet/rpcrouter'
n = 'urn:xmethods-Temperature'
server = SOAPProxy(url, namespace=n)     
server.config.dumpSOAPOut = 1            
server.config.dumpSOAPIn = 1
temperature = server.getTemp('27502')  



from SOAPpy import WSDL          
wsdlFile = ('http://www.xmethods.net/sd/2001/TemperatureService.wsdl')
server = WSDL.Proxy(wsdlFile)
server.methods.keys()  