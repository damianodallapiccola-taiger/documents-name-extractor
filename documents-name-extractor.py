import os
import csv
import sys


def create_CSV(folder, datapoints):
    with open(os.path.abspath(os.path.join(folder, os.pardir))+'/documents-list.csv', mode='w') as names_file:
        names_file = csv.writer(names_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        names_file.writerow(datapoints)
        for name in os.listdir(folder):
            if(name[-4:] == ".pdf"):
                names_file.writerow([name[:-4]])

def main():
    if (len(sys.argv) == 1):
        print("- arg1: path of the PDF's folder\n- following arguments: names of the datapoints\nThe resulted \'documents-list.csv\' would be saved in the PDF's parent folder")
    else:
        folder = sys.argv[1]
        datapoints = [" "] + sys.argv[2:]
        create_CSV(folder, datapoints)


if __name__ == '__main__':
    sys.exit(main())

