import textract
import sys

'''
found that \xe2\x80\x94
indicates empty cell

cmd line args: python pdfReader.py fileName rows cols
'''
args = sys.argv
PREFIX = args[5]
SPLIT = int(sys.argv[4])
ROW_NUM = int(args[2])
COL_NUM= int(args[3])
MAX_LENGTH = 16
###the right way to make a matrix using lists

matrix = [["-" for i in range(COL_NUM)] for j in range(ROW_NUM)]

text = textract.process(args[1])
text = str(text)
splits = text.split('\\r\\n')
column_count = 0
row_count = 0
for i in splits:
    if(row_count == ROW_NUM):
        break
    if(len(i) < MAX_LENGTH):
        if i == "\\xe2\\x80\\x94" :

            matrix[row_count][column_count] = "-"
            column_count +=1 
            if column_count >=COL_NUM:
                column_count = 0
                row_count +=1
        elif PREFIX in i:

            matrix[row_count][column_count] = i
            column_count += 1
            if column_count >= COL_NUM:
                column_count = 0
                row_count += 1
for row in matrix:
    print(row)

def traverse_matrix(the_matrix:list,columns:int,split_index:int,starting_point:int):
    i = columns-1  
    original = starting_point 
    while i >=0:
        for w in range(starting_point,len(the_matrix)):
            print(i)
            print(w)

            row = matrix[w]
            if starting_point == split_index:
                break
            curr = row[i]
            if curr != "-":
                print(curr)
            starting_point +=1
        starting_point = original
        i -=1
# traverse_matrix(matrix,COL_NUM,SPLIT,0)
# traverse_matrix(matrix,COL_NUM,SPLIT,SPLIT+1)

