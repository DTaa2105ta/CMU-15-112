_module = 'cs112_s22_week2_linter.py version 1.0'
# Place this file in the same folder as your Python files.
# While you need to use this file to do your exercises, students
# are not expected to look at nor to understand any code in this file.

# bannedTokens list for week 2
_bannedTokens = (
        'as,class,del,except,finally,' +
        'global,lambda,nonlocal,raise,repr,' +
        'try,with,' +
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,literal_eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,issubclass,iter,' +
        'list,map,memoryview,object,oct,' +
        'open,property,reversed,set,' +
        'setattr,slice,sorted,staticmethod,super,tuple,' +
        'vars,zip,importlib,imp,string,[,],{,}')

import math, sys, traceback, inspect, parser
import platform

class _AssertionError(AssertionError): pass

def _formatError(header, file, line, fn, text, msg, expl):
    messages = ['\n******************************']
    if (header): messages.append(header)
    if (file): messages.append('  File:     "%s"' % file)
    if (line): messages.append('  Line:     %d' % line)
    if (fn): messages.append('  Function: %s' % fn)
    if (text): messages.append('  Code:     %s' % text.strip())
    messages.append('  Error:    %s' % msg)
    if (expl): messages.append('  Hint:     %s' % expl)
    message = '\n'.join(messages)
    return message

class _LintError(Exception):
    def __init__(self, errors):
        messages = [ '' ]
        for i,e in enumerate(errors):
            (msg, file, line, fn, text, expl) = e
            header = 'LintError #%d of %d:' % (i+1, len(errors))
            message = _formatError(header, file, line, fn, text, msg, expl)
            messages.append(message)
        message = ''.join(messages)
        super().__init__(message)

class _Linter(object):
    def __init__(self, code=None, filename=None, bannedTokens=None):
        self.code = code
        self.filename = filename
        self.bannedTokens = set(bannedTokens or [ ])
        self.issuedRoundOopsMessage = False

    def roundOops(self, node):
        msg = 'Do not use builtin "round" in Python 3'
        if (self.issuedRoundOopsMessage):
            msg += ' (see above for details)'
            expl = ''
        else:
            self.issuedRoundOopsMessage = True
            expl= '''The behavior of "round" in Python 3 may be unexpected.  
\t\t\tFor example:
\t\t\t   round(1.5) returns 2
\t\t\t   round(2.5) returns 2

\t\t\tInstead, in 15-112, use the roundHalfUp(d) function provided.
'''
        self.oops(msg, expl, node=node)

    def oops(self, msg, expl=None, line=None, fn=None, text=None, node=None):
        if (node != None) and (type(node) in (list, tuple)):
            (nodeTid, nodeText, nodeLine, nodeCol) = node
            line = nodeLine
        if ((text == None) and
            (line != None) and
            (1 <= line <= len(self.lines))):
            text = self.lines[line-1]
        self.errors.append((msg, self.filename, line, fn, text, expl))

    def lintLineWidths(self):
        for i in range(len(self.lines)):
            line = self.lines[i]
            if (len(line) > 80):
                msg = 'Line width is >80 characters'
                expl = "You may not have a line of code longer than 80 characters."
                self.oops(msg, expl,
                          line=i+1, text='\n'+line[:81]+'...')

    def lintTopLevel(self):
        # only allow import, from...import, def, class, and if...main()
        for topLevelNodeList in self.astList:
            if (not isinstance(topLevelNodeList, list)):
                msg = 'Non-list top-level node list!'
                expl = ("You are doing something strange and you program is "
                       "invalid. Go to Office Hours.")
                self.oops(msg, expl, node=topLevelNode)
            topLevelNode = topLevelNodeList[0]
            if (isinstance(topLevelNode, int)):
                # it's a top-level string, or some such
                if (topLevelNode == 3):
                    text = 'top-level-string'
            elif isinstance(topLevelNode, list) and \
                isinstance(topLevelNode[0], list) and \
                len(topLevelNode[0]) == 4 and topLevelNode[0][1] == "@":
                (tid, text, line, col) = topLevelNode[0]
            elif ((type(topLevelNode) not in [list,tuple]) or
                  (len(topLevelNode) != 4)):
                msg = 'Unknown type of top-level code: %r' % topLevelNode
                expl = ("You are doing something strange and you program is "
                       "invalid. Go to Office Hours.")                      
                self.oops(msg, expl)
                continue
            else:
                (tid, text, line, col) = topLevelNode
            if (text not in ['@', 'import', 'from', 'def',
                             'class', 'top-level-string']):
                msg = "Top-level code that is not import, def, or class."
                expl = ("All of your code should be inside of a function. "
                       "If you want to make sure\n\t\t\tsomething runs "
                       "everytime, add it to main().")
                self.oops(msg, expl, node=topLevelNode)

    def lintAllLevels(self, astList):
        if (isinstance(astList[0], list)):
            for node in astList: self.lintAllLevels(node)
        else:
            node = astList
            (tid, text, line, col) = node
            if (text == 'round'):
                self.roundOops(node=node)
            if (text in self.bannedTokens):
                msg = 'Disallowed token: "%s"' % text
                expl = ("You are using a feature of Python that is not allowed "
                       "in this\n\t\t\tassignment. You will need to solve this "
                       "assignment without using\n\t\t\tthat feature.")
                self.oops(msg, expl, node=node)            

    def lint(self):
        print('Linting... ', end='')
        self.errors = [ ]
        if (self.code == None):
            with open(self.filename, 'rt', encoding="utf-8") as f:
                try: self.code = f.read()
                except e:
                    msg = 'Error when trying to read file:\n' + str(e)
                    expl = ("This usually means something got corrupted in "
                            "your file\n\t\t\t and you should remove the "
                            "corrupted portions or\n\t\t\t start a new file.")
                    self.oops(msg,expl)
                    raise _LintError(self.errors)
        if (self.code in [None,'']):
            self.oops('Could not read code from "%s"' % self.filename)
            raise _LintError(self.errors)
        self.lines = self.code.splitlines()
        self.st = parser.suite(self.code)
        self.stList = parser.st2list(self.st, line_info=True, col_info=True)
        self.astList = self.buildSimpleAST(self.stList, textOnly=False)
        self.astTextOnlyList = self.buildSimpleAST(self.stList, textOnly=True)
        # allow if...main() last line...
        if (self.astTextOnlyList[-1] in [
            ['if', ['__name__', '==', "'__main__'"],
                   ':', ['main', ['(', ')']]],
            ['if', ['(', ['__name__', '==', "'__main__'"], ')'],
                   ':', ['main', ['(', ')']]],
            ['if', ['__name__', '==', '"__main__"'],
                   ':', ['main', ['(', ')']]],
            ['if', ['(', ['__name__', '==', '"__main__"'], ')'],
                   ':', ['main', ['(', ')']]]
            ]):
            # just remove it...
            self.astTextOnlyList.pop()
            self.astList.pop()
        # now do the actual linting...
        self.lintLineWidths()
        self.lintTopLevel() # just import, def, class, or if...main()
        self.lintAllLevels(self.astList)
        if (self.errors != [ ]):
            raise _LintError(self.errors)
        print("Passed!")

    def buildSimpleAST(self, ast, textOnly):
        if (not isinstance(ast, list)): return None
        if (not isinstance(ast[1], list)):
            result = ast[1]
            if (result == ''): result = None
            if ((not textOnly) and (result != None)): result = ast
            return result
        result = [ ]
        for val in ast:
            node = self.buildSimpleAST(val, textOnly)
            if (node != None):
                result.append(node)
        if (len(result) == 1): result = result[0]
        return result

def lint(code=None, filename=None, bannedTokens=_bannedTokens):
    if (isinstance(bannedTokens, str)):
        bannedTokens = bannedTokens.split(',')
    if ((code == None) and (filename == None)):
        try:
            module = None
            frame = inspect.stack()[1]
            module = inspect.getmodule(frame[0])
            if ((module == None) or (module.__file__ == None)):
                # this may help, or maybe not (sigh)
                module = sys.modules['__main__']
            # the next line may fail (sigh)
            filename = module.__file__
        except:
            raise Exception('lint cannot find module/file to lint!')
    try:
        _Linter(code=code, filename=filename, bannedTokens=bannedTokens).lint()
    except _LintError as lintError:
        # just 'raise lintError' for cleaner traceback
        lintError.__traceback__ = None
        raise lintError

def _printImportReport():
    #print('Importing %s in Python %s' % (_module, platform.python_version()))
    (major, minor, micro, releaselevel, serial) = sys.version_info
    if (major < 3):
        raise Exception("You must use Python 3, not Python 2!")
    if (minor < 7):
        raise Exception("You must use Python 3.7 or newer!")

if (__name__ != '__main__'):
    _printImportReport()
