import fileio_v1 as fileio
import sys

FOOTER_LINE = 'End of the Project Gutenberg EBook'
HEADER_LINE = ' ***'

def remove_headers( s ):
    head_pos = s.find( HEADER_LINE ) + len(HEADER_LINE)
    foot_pos = s.find( FOOTER_LINE )
    return s[ head_pos : foot_pos ]

def cleanup(fname):
    text = fileio.read_file(fname)    
    text = remove_headers( text )
    words = text.split()
    new_text = ''
    for word in words:
        new_text+= word + '\n'
    new_fname = fname[:fname.find('.txt')] + '_clean.txt'





    
    fileio.write_file( new_text, new_fname )


fname = sys.argv[1]
cleanup( fname )
