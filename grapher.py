# Last updated 8 July, 2020
# Created by David Shuster

# This program parses and graphs some simple data on religiosity, cost of living, and math teacher salary in the US.

import csv
import matplotlib.pyplot as plt
import salary_scraper as scraper

def main():
    scraper.makeCSV()
    state_to_info = {}

    # read in cost of living data
    f = open('CoLData.csv', 'r')
    for line in f.readlines()[1:]:
        line = line.split(",")
        state_name = line[0]
        costIndex = float(line[1])
        state_to_info[state_name] = {'costIndex': costIndex, 'avgSalary':0, 'religiosity':0}
    f.close()

    # read in salary data
    f = open('salaries.csv', 'r')
    for line in f.readlines()[1:]:
        line = line.split(",", 1)
        state_name = line[0]
        avgSalary = int(line[1][2:-2].replace(",",""))
        state_to_info[state_name]['avgSalary'] = avgSalary
    f.close()

    # read in religiosity data
    f = open('religionByState.csv', 'r')
    for line in f.readlines()[3:]:
        line = line.split(",")
        state_name = line[0]
        religiosity = int(line[1]) + int(line[2])
        state_to_info[state_name]['religiosity'] = religiosity
    f.close()

    # create graph
    for name in state_to_info.keys():
        x = state_to_info[name]['religiosity']
        y = state_to_info[name]['avgSalary']/state_to_info[name]['costIndex']
        plt.scatter(x,y, color = 'tab:blue')

    # see a few interesting states labeled on the scatterplot
    for name in ['Vermont', 'Maine', 'Hawaii', 'California', 'Massachusetts', 'New Hampshire', 'Mississippi', 'Wyoming']:
        x = state_to_info[name]['religiosity']
        y = state_to_info[name]['avgSalary']/state_to_info[name]['costIndex']
        plt.text(x, y, name)
    plt.xlabel('% in State Identifying as Very or Moderately Religious')
    plt.ylabel('State\'s Avg. Annual Math Teacher Salary (USD)/Cost of Living Index')
    plt.title('Religiosity vs. Math Teacher Financial Ease in US States')
    plt.show()

if __name__ == '__main__':
    main()