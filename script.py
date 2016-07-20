from random import randrange

CHARSET = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
LENGTH = 16
MAX_TRIES = 32


code = ""

def generate_code():
    loop_num = 0
    unique = False

    while not unique:
        if loop_num < MAX_TRIES:
            new_code = ''
            for i in range(LENGTH): # TODO: change to xrange() for python 2
                new_code += CHARSET[randrange(0, len(CHARSET))]
                code = new_code
                unique = True
            loop_num += 1
            return new_code
        else:
            raise ValueError("Couldn't generate a unique code.")

def main():
    import csv

    with open("input.csv", 'rt', encoding="utf-8") as input, open('output.csv', 'wt', encoding="utf-8") as output:
        reader = csv.reader(input, delimiter = ',')
        writer = csv.writer(output, delimiter = ',')

        all = []
        row = next(reader)
        row.insert(9, 'UNICO')
        row.insert(10, 'URL')
        all.append(row)
        for k, row in enumerate(reader):
            UID = generate_code()
            URL = "http://reforestacion.redprecordillera.cl/trees/"+str(UID)+"/"

            row.insert(9, UID)
            row.insert(10,URL)

            all.append(row)
        writer.writerows(all)

main()

print("Thanks for use :)")
