import re
import sys

def title(name, style):
    print "%s\n%s" % (name, style * len(name))

def chapter(rem, line, lines):
    title(rem[0], "=")

def section(rem, line, lines):
    title(rem[0], "-")

def subsection(rem, line, lines):
    title(rem[0], "`")

def description(rem, line, lines):
    ending = re.compile(r'\\end{description}')
    item = re.compile(r'\\item\s*\[(.*)\]\s(.*)$')
    line = lines.pop(0)

    while not ending.match(line):
        if line.startswith(r'\item'):
            word, define = item.match(line).groups()
            print "%s\n    %s\n" % (word.strip(), define.strip())
        else:
            print "    %s" % line.strip()

        line = lines.pop(0)

def aside(rem, line, lines):
    ending = re.compile(r'\\end{aside}')
    print ".. note:: \n"
    line = lines.pop(0)
    while not ending.match(line):
        print "    %s" % line.strip()
        line = lines.pop(0)

def code(rem, line, lines):
    ending = re.compile(r'\\end{(code|Terminal)}')
    dline = re.compile(r'''<< d\[['"](.*)(|l)?["']\] >>''')
    lstlisting = re.compile(r'\\(begin|end){(Verbatim|lstlisting)}')
    line = lines.pop(0)

    if lstlisting.match(line):
        line = lines.pop(0)

    try:
        source = dline.match(line).groups()[0]
        print "{{ ork.code('%s') }}" % source
    except AttributeError:
        print "::\n\n    %s" % line.strip()

        while not ending.match(line) and not lstlisting.match(line):
            print "    %s" % line.strip()
            line = lines.pop(0)

    line = lines.pop(0)
    if lstlisting.match(line): line = lines.pop(0)

    assert ending.match(line), "Code not formatted right: %s" % source

def quote(rem, line, lines):
    ending = re.compile(r'\\end{quote}')
    line = lines.pop(0)
    while not ending.match(line):
        print "    %s" % line.strip()
        line = lines.pop(0)

def enum(rem, line, lines):
    ending = re.compile(r'\\end{enumerate}')
    line = lines.pop(0)

    while not ending.match(line):
        if line.startswith(r'\item '):
            text = line.split(' ', 1)[1]
            print "* %s" % text.strip()
        else:
            print "  %s" % line.strip()

        line = lines.pop(0)

def href(rem, line, lines):
    print "`%s <%s>`_" % (rem[1].strip(), rem[0].strip())

def default(rem, line, lines):
     print line,

def verbatim(rem, line, lines):
    ending = re.compile(r'\\end{Verbatim}')
    print "::"
    line = lines.pop(0)
    while not ending.match(line):
        print "    %s" % line.strip()
        line = lines.pop(0)

roots = (
    (re.compile(r'\\chapter\*?{(.*)}'), chapter),
    (re.compile(r'\\begin{enumerate}'), enum),
    (re.compile(r'\\section\*?{(.*)}'), section),
    (re.compile(r'\\subsection\*?{(.*)}'), subsection),
    (re.compile(r'\\begin{description}'), description),
    (re.compile(r'\\begin{aside}{(.*)}'), aside),
    (re.compile(r'\\begin{(code|Terminal)}{(.*)}'), code),
    (re.compile(r'\\begin{quote}'), quote),
    (re.compile(r'\\href{([^}]*)}{([^}]*)}'), href),
    (re.compile(r'\\begin{Verbatim}'), verbatim),
    (re.compile(r'^.*$'), default),
)

txt = open(sys.argv[1], 'r').readlines()

print '{% import "macros/ork.jinja" as ork with context %}'

while txt:
    line = txt.pop(0)

    for r,f in roots:
        rem = r.match(line)

        if rem:
            f(rem.groups(), line, txt)
            break
