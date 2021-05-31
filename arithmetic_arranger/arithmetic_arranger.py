def arithmetic_arranger(problems, toggle = False):
    # error - too many problems 
    if len(problems) > 5:
        return 'Error: Too many problems.'
    # dividing problems list into separate [int, 'sign', int] objects
    separate_lists = []
    for p in problems:
        separate_lists.append(p.split())
    
    digit_spaces = []
    
    # print('debug 1', separate_lists)
    # errors - wrong operator, not number, > 4 digits
    for l in separate_lists:
        
        if len(l[0]) > 4 or len(l[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        try:
            l[0] = int(l[0])
            l[2] = int(l[2])
        except:
            return 'Error: Numbers must only contain digits.'
        
        if l[1] == '+':
            l.append(l[0]+l[2])
        elif l[1] == '-':
            l.append(l[0]-l[2])
        else:
            return "Error: Operator must be '+' or '-'."
            
            ### PREPARE LIST OF FORMATTING PARAMETERS -> NXT LOOP
        if len(str(l[0])) > len(str(l[2])):
            digit_spaces.append('{1:>'+ str(len(str(l[0]))+1)+'}')
        else:
            digit_spaces.append('{1:>'+ str(len(str(l[2]))+1)+'}')

        ### PREPARE THE PRINTING FORMAT
    # print('debug: ', digit_spaces)
    result = ''
    first = True
    for i in range(len(separate_lists)):
        if first == True:
            result += ('{0:1}'+str(digit_spaces[i])).format('',separate_lists[i][0])
            first = False
        else:
            result += ('{0:>5}'+str(digit_spaces[i])).format(' ',separate_lists[i][0])
    result += '\n'
    first = True

    for i in range(len(separate_lists)):
        if first == True:
            result += ('{0}' + str(digit_spaces[i])).format(separate_lists[i][1], separate_lists[i][2])
            first = False

        else:
            result += ('{0:>5}' + str(digit_spaces[i])).format(separate_lists[i][1], separate_lists[i][2])
        # print('debug 4',separate_lists[i][2] )
    result += '\n'
    first = True
    for i in range(len(separate_lists)):
        if first == True:
            result += ('{0}'+'{1:-<'+ str(int(digit_spaces[i][4])+1)+'}').format('','')
            first = False

        else:
            result += ('{0:>4}'+'{1:-<'+ str(int(digit_spaces[i][4])+1)+'}').format('','')
    # print('debug: ', separate_lists)
    first = True
    if toggle == True:
        result += '\n'
        for i in range(len(separate_lists)):
            if first == True:
                result += ('{0:1}'+str(digit_spaces[i])).format('',separate_lists[i][3])
                first = False
            else:
                result += ('{0:>5}'+str(digit_spaces[i])).format('',separate_lists[i][3])
        # print('debug: ',separate_lists[i][3])

    return result
