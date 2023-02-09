# Counts totals in column of data from the 2022 Stack Overflow Developers survey
import csv 

def main():
    file = open('pythonAnalysisFile.csv', 'r')
    csv_file = csv.reader(file)

    count = {}
    for line in csv_file:
        langs = line[0].split(';')
        
        for lang in langs:
            if lang in count:
                count[lang] += 1
            else:
                count[lang] = 1

    file.close()
    
    for lang in count:
        print(f'{lang}: {count[lang]}')

main()


# prints columns for copy/paste

# print('\nLeft:')
# for lang in count:
#     print(lang)

# print('\nRight:')
# for lang in count:
#     print(count[lang])