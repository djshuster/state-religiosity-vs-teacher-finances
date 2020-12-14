# Last updated 6 July, 2020
# Created by David Shuster

# This program retrieves data from ZipRecruiter on teacher salaries by state
# and outputs a CSV file containing the information.

from bs4 import BeautifulSoup
import requests
import csv


def makeCSV():
    siteName = 'https://www.ziprecruiter.com/Salaries/What-Is-the-Average-Math-Teacher-Salary-by-State'
    source = requests.get(siteName).text
    soup=BeautifulSoup(source, 'lxml')

    fileName = "salaries.csv"
    csv_file=open(fileName, 'w', newline='')
    csv_writer=csv.writer(csv_file)

    csv_writer.writerow(['State', 'Salary'])

    for entry in soup.find_all('tr'):
        try:
            state = entry.find('td', class_="col1").text
            salary = entry.find('td', class_="col2").text
            csv_writer.writerow([state, salary])
        except Exception as e:
            pass

    csv_file.close()

def main():
    makeCSV()

if __name__ == '__main__':
    main()

'''
ACKNOWLEDGMENTS

Thanks to ZipRecruiter for the data.

Thanks to Corey Schafer (coreyms.com) for helpful instructions 
on web scraping (https://www.youtube.com/watch?v=ng2o98k983k).
'''