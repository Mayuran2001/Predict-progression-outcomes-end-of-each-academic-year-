progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0
Total = 0
count = 0
dictionary_data = {
    "Progress":[],
    "Progress(module trailer)":[],
    "Do not progress-module retriever":[],
    "Exclude":[]
}

def validate(Pass, Defer, Fail):
   global progress_count, trailer_count, retriever_count, excluded_count
   if Pass==120 and Defer==0 and Fail==0:       #1
       progress_count += 1
       return 'Progress'
   elif Pass==100 and Defer==20 and Fail==0:    #2
       trailer_count += 1
       return 'Progress(module trailer)'
   elif Pass==100 and Defer==0 and Fail==20:    #3
       trailer_count += 1
       return 'Progress(module trailer)'
   elif Pass==80 and Defer==40 and Fail==0:     #4
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==80 and Defer==20 and Fail==20:    #5
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==80 and Defer==0 and Fail==40:     #6
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==60 and Defer==60 and Fail==0:     #7
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==60 and Defer==40 and Fail==20:    #8
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==60 and Defer==20 and Fail==40:    #9
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==60 and Defer==0 and Fail==60:     #10
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==40 and Defer==80 and Fail==0:     #11
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==40 and Defer==60 and Fail==20:    #12
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==40 and Defer==40 and Fail==40:    #13
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==40 and Defer==20 and Fail==60:    #14
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==40 and Defer==0 and Fail==80:     #15
       excluded_count += 1
       return 'Exclude'
   elif Pass==20 and Defer==100 and Fail==0:    #16
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==20 and Defer==80 and Fail==20:    #17
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==20 and Defer==60 and Fail==40:    #18
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==20 and Defer==40 and Fail==60:    #19
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==20 and Defer==20 and Fail==80:    #20
       excluded_count += 1
       return 'Exclude'
   elif Pass==20 and Defer==0 and Fail==100:    #21
       excluded_count += 1
       return 'Exclude'
   elif Pass==0 and Defer==120 and Fail==0:     #22
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==0 and Defer==100 and Fail==20:    #23
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==0 and Defer==80 and Fail==40:     #24
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==0 and Defer==60 and Fail==60:     #25
       retriever_count += 1
       return 'Do not progress-module retriever'
   elif Pass==0 and Defer==40 and Fail==80:     #26
       excluded_count += 1
       return 'Exclude'
   elif Pass==0 and Defer==20 and Fail==100:    #27
       excluded_count += 1
       return 'Exclude'
   elif Pass==0 and Defer==0 and Fail==120:     #28
       excluded_count += 1
       return 'Exclude'

def validate_input(user_input):
   global Total
   Total += user_input
   if user_input not in (0, 20, 40, 60, 80, 100, 120):
      print('Out of range!\n')
      main()
   elif not user_input <= 120 and Total != 120:
      print('Total incorrect!\n')
   elif count <= 2:
      return None
   
def main_staff(version):
   global count
   while True:
      Pass = 0
      Defer = 0
      Fail = 0
      count = 0
      try:   
         Pass = int(input('Please enter your credits at pass: '))
         count += 1
         if validate_input(Pass) == None:
            Defer = int(input('Please enter your credit at defer: '))
            count += 1
            if validate_input(Defer) == None:
               Fail = int(input('Please enter your credit at fail: '))
               count += 1
               if validate_input(Fail) == None:
                  if (Pass + Defer + Fail != 120):
                     print('Total incorrect!\n')
                     return sub_main(version)
                  else:
                     result = validate(Pass, Defer, Fail)
                     print(result)
                     Total_outcome = [Pass, Defer, Fail]
                     dictionary_data[result].append(Total_outcome)
                     option = str(input("\n\nwould you like to enter another data? \nEnter 'Y' for yes or 'q' to quit and view results: "))
                     if option == 'y':
                        continue
                     elif option == 'q':
                         if version == 1:
                            histogram()
                            return main()
                         elif version ==2:
                            histogram()
                            vertical_histogram(progress_count,trailer_count,retriever_count,excluded_count)
                            return main()
                         elif version == 3:
                            histogram()
                            vertical_histogram(progress_count,trailer_count,retriever_count,excluded_count)
                            progression_data()
                            return main()
                         else:
                            histogram()
                            vertical_histogram(progress_count,trailer_count,retriever_count,excluded_count)
                            progression_data()
                            write_to_file()
                            break
               return main_staff(version)
            return main_staff(version)
         return main_staff(version)
      except ValueError:
         print('Integer required!\n')
         continue

def progression_data():
    print('Progression Data\n')
    for key, value in dictionary_data.items():
        for x in range(len(value)):
            current_list = value[x]
            print('{0} - {1}, {2}, {3}'.format(key, current_list[0], current_list[1], current_list[2]))

def histogram():
    print('_ '*40,'Horizontal Histogram\n')
    print('Progress {0}  : {1}'.format(progress_count, '*'*progress_count))
    print('Trailer {0}   : {1}'.format(trailer_count, '*'*trailer_count))
    print('Retriever {0} : {1}'.format(retriever_count, '*'*retriever_count))
    print('Excluded {0}  : {1}'.format(excluded_count, '*'*excluded_count))
    print(progress_count+trailer_count+retriever_count+excluded_count,"Number of students in total")
    print('_ '*40)

def vertical_histogram(progress,trailer,retriever,excluded):
    print('_ '*40,'\nVertical Histogram\n')
    print('Progress {0} | Trailer {1} | Retriever {2} | Excluded {3}'.format(
       progress,trailer,retriever,excluded))
    while progress != 0 or trailer != 0 or retriever != 0 or excluded != 0:
        if progress > 0:
            print('{:^6}'.format('*'), end='\t')
            progress -= 1
        else:
            print('{:^6}'.format(' '), end='\t') 
        if trailer > 0:
            print('{:^12}'.format('*'), end='\t')
            trailer -= 1
        else:
            print('{:^12}'.format(' '), end='\t') 
        if retriever > 0:
            print('{:^15}'.format('*'), end='\t')
            retriever -= 1
        else:
            print('{:^15}'.format(' '), end='\t') 
        if excluded > 0:
            print('{:^18}'.format('*'), end='\n')
            excluded -= 1
        else:
            print('{:^18}'.format(' '), end='\n') 
    print("{0},Number of students in total".format(progress_count+trailer_count+retriever_count+excluded_count))
    print('_ '*40)

def read_file():
    with open ('studentdata.txt','r') as f:
        print('Reading from studentdata.txt...')
        print(f.read())
        f.close()

def write_to_file():
    f = open('studentdata.txt', 'w')
    f.write('Progression Data\n')
    for key, value in dictionary_data.items():
        for x in range(len(value)):
            current_list = value[x]
            f.write('{0} - {1}, {2}, {3}\n'.format(key, current_list[0], current_list[1], current_list[2]))
    f.write('\n{0} Number of students in total'.format(progress_count+trailer_count+retriever_count+excluded_count))
    f.close()

def main_student(version):
   global count
   while True:
      Pass = 0
      Defer = 0
      Fail = 0
      count = 0
      try:   
         Pass = int(input('Please enter your credits at pass: '))
         count += 1
         if validate_input(Pass) == None:
            Defer = int(input('Please enter your credit at defer: '))
            count += 1
            if validate_input(Defer) == None:
               Fail = int(input('Please enter your credit at fail: '))
               count += 1
               if validate_input(Fail) == None:
                  if (Pass + Defer + Fail != 120):
                     print('Total incorrect!\n')
                     return main_student(version)
                  else:
                     print(validate(Pass, Defer, Fail))
                     option = str(input("\n\nwould you like to enter another data? \nEnter 'y' for yes or 'q' to quit and view results: "))
                     input('Press any key to exit to main menu')
                     return sub_main(version)
               return main_student(version)
            return main_student(version)
         return main_student(version)
      except ValueError:
         print('Integer required!\n')
         continue

def sub_main(version):
    option = input('''
1. Press 1 to enter Student version
2. Press 2 to enter Staff version
3. Press 3 to view preview student record

4. Press 'q' to quit

Enter option: ''')
    while option != 'q':
        try:
            if option=='1':
                return main_student(version)
            elif option=='2':
                return main_staff(version)
            elif option=='3':
                read_file()
                input('Press any key to continue')
                return sub_main(version)
            elif option=='4':
                histogram()
                vertical_histogram(progress_count,trailer_count,retriever_count,excluded_count)
                progression_data()
                write_to_file()
                break    
            else:
                print('option not included')
            option = input('Enter option: ')
        except ValueError:
            print('required valid integer')

def main():
    option = input('''
1. Press 1 to enter part 1 "Horizontal Histogram"
2. Press 2 to enter Part 2 "Horizontal Histogram and Vertical Histogram"
3. Press 3 to enter Part 3 "Horizontal Histogram and Vertical Histogram and Dictionery Data
4. Press 4 to enter Part 4 "All Data + write to file

5. Press 'q' to quit

Enter option: ''')
    while option != 'q':
        try:
            if option=='1':
                return sub_main(1)
            elif option=='2':
                return sub_main(2)
            elif option=='3':
                return sub_main(3)
            elif option=='4':
                return sub_main(4)
            elif option=='5':
                quit
            else:
                print('option not included')
            option = input('Enter option: ')
        except ValueError:
            print('required valid integer')

main()
