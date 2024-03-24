# Part 1
def read_csv(filename: str) -> tuple:
  '''
  Opens CSV file and returns tuple containing the header and data

  Argument:
    filename: str

  Return:
    (header: list, data: list): tuple
  
  '''
  with open(filename,'r') as f:
    header = f.readline().strip().split(",")
    data = []
    for line in f:
      line_data = (line.strip().split(","))
      line_data[0] = int(line_data[0])
      line_data[3] = int(line_data[3])
      data.append(line_data)
    # f.close() is called automatically
  return (header,data)


# Part 2
def filter_gender(enrolment_by_age: list, sex: str) -> list:
  ''' 
  Filter enrolment_by_age by sex
  Arguments:
    enrolment_by_age : list
    sex: str
  Return 
    data: list
  
  '''
  data = []
  for record in enrolment_by_age:
    if record[2] == sex:
      data.append([record[0],record[1],record[3]])
  return data

# Part 3
def sum_by_year(enrolment: list) -> list:
  ''' 
  Add the number of enrolment in each year
  Argument: 
    enrolement: list
  Return:
    year_enrolment: list
  '''
  year = []
  enrolment_num = []
  for record in enrolment:
    if record[0] in year:
      x = year.index(record[0])
      enrolment_num[x] += int(record[-1])      
    else:
      enrolment_num.append(int(record[-1]))
      year.append(record[0])
    # f.close() is called automatically
  year_enrolment = []
  for x in range(len(year)):
    year_enrolment.append([year[x],enrolment_num[x]])
  return year_enrolment

# Part 4
def write_csv(filename: str, header: list, data: list) -> int:
  ''' 
  write 'header' and 'data' to 'filename'
  Arguments:
    filename: str
    header: list
    data: list
  Return:
    line: int
  '''
  with open(filename,'w') as f:
    f.writelines(",".join(header))
    f.writelines("\n")
    
    line = 1
    for x in data:
      x[0] = str(x[0])
      x[1] = str(x[1])
    for row in data:
      f.writelines(",".join(row))
      line += 1
      f.writelines("\n")
    # f.close() is called automatically
  return line
  
  # Type your code below
    


# TESTING
# You can write code below to call the above functions
# and test the output
'''
file = 'pre-u-enrolment-by-age.csv'
header,data = read_csv(file)
mf_enrolment = filter_gender(data, "MF")
enrolment_by_year = sum_by_year(mf_enrolment)

header = ["year", "total_enrolment"]
filename = 'total-enrolment-by-year.csv'
#print(write_csv(filename, header, enrolment_by_year))
'''