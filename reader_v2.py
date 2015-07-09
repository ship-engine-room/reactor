def read_file( fname ):
    f = open( fname, 'r' )
    text = f.read()
    f.close()
    return text


def get_csv_list( fname ):
    text = read_file( fname )
    lines = text.split('\n')
    line_list = []
    for line in lines:
        line_list.append( line.split(',') )
    return line_list


def get_csv_dict( fname ):
    text = read_file( fname )
    lines = text.split('\n')
    line_dict = {}
    for line in lines:
        line_list = line.split(',')
        key = line_list[0]
        value = line_list[1:]
        line_dict[ key ] = value
    return line_dict


if __name__ == '__main__':
    text = read_file( 'wordlist.csv' )
    lines = get_csv_list( 'wordlist.csv' )

    print text
    print '\n'

    print lines
    print '\n'
    
    print words
    print '\n'

