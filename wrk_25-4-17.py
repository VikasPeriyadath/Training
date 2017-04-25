if hasattr(source, "read"):
       		return source

if source == '-':
        import sys
        return sys.stdin


from xml.dom import minidom
xmldoc = minidom.parse('sample.xml') 
title = xmldoc.getElementsByTagName('title')[0].firstChild.data
print title
convertedtitle = title.encode('koi8-r')
print convertedtitle


xmldoc = minidom.parse('binary.xml')
reflist = xmldoc.getElementsByTagName('ref')
bitref = reflist[0]
print bitref.toxml()
bitref.attributes.keys()


from xml.dom import minidom
fsock = open('binary.xml')    
xmldoc = minidom.parse(fsock) 
fsock.close()                 
print xmldoc.toxml() 

import sys
for i in range(3):
    sys.stdout.write('Dive in')  
for i in range(3):
    sys.stderr.write('Dive in')

print 'Dive in'                                          
saveout = sys.stdout                                     
fsock = open('out.log', 'w')                             
sys.stdout = fsock                                       
print 'This message will be logged instead of displayed' 
sys.stdout = saveout                                     
fsock.close()  
fsock = open('error.log', 'w')               
sys.stderr = fsock                           
raise Exception, 'this error will be logged' 

def loadGrammar(self, grammar):                         
        self.grammar = self._load(grammar)                  
        self.refs = {}                                       
        for ref in self.grammar.getElementsByTagName("ref"): 
            self.refs[ref.attributes["id"].value] = ref

def do_xref(self, node):
        id = node.attributes["id"].value
        self.parse(self.randomChildElement(self.refs[id]))         

def randomChildElement(self, node):
        choices = [e for e in node.childNodes
                   if e.nodeType == e.ELEMENT_NODE] 
        chosen = random.choice(choices)             
        return chosen    

def main(argv):                         
    grammar = "kant.xml"                 
    try:                                
        opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="]) 
    except getopt.GetoptError:           
        usage()                          
        sys.exit(2)                     


if __name__ == "__main__":
    main(sys.argv[1:])