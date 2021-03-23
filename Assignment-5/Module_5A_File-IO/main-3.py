def main():
    inputfile = open('/Users/crissyp/projects/ITMD-413/Assignment-5/Module_5A_File-IO/presidents.txt',
                     'r')  # open an existing file
    outfile = open('/Users/crissyp/projects/ITMD-413/Assignment-5/Module_5A_File-IO/result.txt', 'w')

    for line in inputfile:
        outfile.write(line + '\n')

    outfile.write('Computer programming is exciting!\n')
    inputfile.close()
    outfile.close()


main()
