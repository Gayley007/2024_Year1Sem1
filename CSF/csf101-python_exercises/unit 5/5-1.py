#function to read input.txt
def read_txt_file(filepath):
    data=()
    with open("./input.txt",'r') as f:
          data=f.readlines()
    return data

#function tht prints out whats on each line
def main():
    text_data=read_txt_file("./input.txt")
    print("Line 691 data from input:", text_data[690])
main()

#Sum of first column
def sums(input_data):
    sum=0
    #looping through 1 line at a time
    for line in input_data:
         print ('line:', line)
         counter=0
         for char in line:
              counter +=1
              if char =="":
                   break
              
    first_number_str = line[0:counter]
    first_num_int=int(first_number_str)
    sum= sum + first_num_int
    print('first_number:', first_number_str)
    print('===========')
    print('sum:', sum)

#Sum of second column
def sum_of_2nd(input_data):
    for line in input_data:
         index = 0
         counter=0
         for char in line:
              index +=1
              if char =="":
                   if counter == 0:
                        firstcounter= index
                        counter+=1
                   elif counter == 1:
                        secondcounter = index
         secondnumber= line[firstcounter:secondcounter]
         print('second number:',secondnumber )
         print('===========')