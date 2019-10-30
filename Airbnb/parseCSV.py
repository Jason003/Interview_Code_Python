'''
Assumption:
1. input is a string, return the parsed input
2. remove " " between word, replace , with |
3. if nested "", just remove the most outer ""

Approach:
The idea is we need to distinguish most outer quote with nested quote. This can be done by maintain a state.
If we not in a quote, we just append character and replace , with |, if we reach a ", we mark the state to
indicate we are in quote. If we then reach another quote, we check if this is a back quote or a nested quote,
if is a nested quote, we need append, otherwise, ignore.

Time: O(n) where n is the length of string
Space: O(n) for stringbuilder
'''
def parseCSV(str):
    res = []
    inQuote = False
    n = len(str)
    for i, c in enumerate(str):
        if inQuote:
            if c == '"':
                if i + 1 < n and str[i + 1] == '"': # inner quote
                    res.append('"')
                else:
                    inQuote = False
            else:
                res.append(c)
        else:
            if c == '"':
                inQuote = True
            elif c == ',':
                res.append('|')
            else:
                res.append(c)
    return ''.join(res)

print(parseCSV('"Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1 """Alexandra Alex"""'))