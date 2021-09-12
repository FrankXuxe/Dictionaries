codes = {'A' : '1', 'a' : '27',
        'B' : '2', 'b' : '28',
        'C' : '3', 'c' : '29',
        'D' : '4', 'd' : '30',
        'E' : '5', 'e' : '31',
        'F' : '6', 'f' : '32',
        'G' : '7', 'g' : '33',
        'H' : '8', 'h' : '34',
        'I' : '9', 'i' : '35',
        'J' : '10', 'j' : '36',
        'K' : '11', 'k' : '37',
        'L' : '12', 'l' : '38',
        'M' : '13', 'm' : '39',
        'N' : '14', 'n' : '40',
        'O' : '15', 'o' : '41',
        'P' : '16', 'p' : '42',
        'Q' : '17', 'q' : '43',
        'R' : '18', 'r' : '44',
        'S' : '19', 's' : '45',
        'T' : '20', 't' : '46',
        'U' : '21', 'u' : '47',
        'V' : '22', 'v' : '48',
        'W' : '23', 'w' : '49',
        'X' : '24', 'x' : '50',
        'Y' : '25', 'y' : '51',
        'Z' : '26', 'z' : '52',
        ' ': ' '}

#info_security = open('info_security.txt', 'r')
#outfile = open('NewFile.txt', 'w')

#letter = 1
#while letter <= 10000000000:
#    Letter = info_security.read(letter)
#    outfile.write(codes[Letter])
#    letter + 1


#outfile.close()
#info_security.close()

info_security = open('info_security.txt','r')
file_read = info_security.read()
outfile = open('NewFile.txt', 'w')

Encript = ''

for i in file_read:
    if i in codes.keys():
        x = codes[i]
        Encript += x

outfile.write(Encript)

outfile.close
    


