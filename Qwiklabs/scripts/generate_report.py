#!/usr/bin/env python3

import csv
import os, sys

def read_employees(csv_file_location):
    ## Dialect object
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')

    employee_list = []
    for data in employee_file:
        employee_list.append(data)

    return employee_list



def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    
    return department_data


def write_report(dictionary, report_file):

    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()

## Main line
this_script_path=(os.path.dirname(sys.argv[0]))
this_script_name=(os.path.basename(sys.argv[0]))

data_dir=os.path.join(this_script_path,"../data")

infile=os.path.join(data_dir,'employees.csv')
outfile=os.path.join(data_dir,'test_report.txt')

employee_list = read_employees(infile)
dictionary = process_data(employee_list)
write_report(dictionary, outfile)


#print(employee_list)

