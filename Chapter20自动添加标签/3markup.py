import re,sys
from 1handler import *
from util impoet *
from 2rule impoet *
class Parser:
    def __init__(self,handler):
        self.handler=handler
        self.rules=[]
        self.fliters=[]
    def addRule(self,rule):
        self.rules.append(rule)
    def addFilter(self,pattern,name):
        def fliter(block,file):
            return re.sub(pattern,handler,sub(name),block)
        self.fliters.append(fliter)
    def parse(self,file):
        self.handler.start('document')
        for block in blocks(file):
            for fliter in self.fliters:
                block=fliter(block,self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last: break
         self.handler.end('document')

class BasicTextParser(Parser):
    """
    在构造函数中添加规则和过滤器的Parser子类
    """

    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')
handler = HTMLRenderer()
parser = BasicTextParser(handler)
parser.parse(sys.stdin)