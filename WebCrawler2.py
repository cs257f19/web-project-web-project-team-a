from lxml import html
import requests
from lxml.html import fromstring
import csv

master_list = []


class Course:

    def __init__(self, dept, num, name, term, reqs, periods):
        self.dept = dept
        self.num = num
        self.name = name
        self.term = term
        self.reqs = reqs
        self.periods = periods

    # def __init__(self):
    #     self.dept = 'DEPT'
    #     self.num = 0.0
    #     self.terms = 'TERMS'
    #     self.reqs = 'REQS'
    #     self.periods = 'PERIODS'

    def set_dept(self, dept):
        self.dept = dept

    def set_num(self, num):
        self.num = num

    def set_name(self, name):
        self.name = name

    def set_term(self, term):
        self.term = term

    def add_term(self, term):
        self.term = self.term + ', ' + term

    def set_reqs(self, req):
        self.reqs = req

    def add_req(self, req):
        self.reqs = self.reqs + ', ' + req

    def set_period(self, period):
        self.periods = period

    def add_period(self, period):
        self.periods = self.periods + ', ' + period

    def to_string(self):
        return 'Dept: ' + self.dept + ', Number: ' + self.num


subjects = ['AFST', 'AMMU', 'AMST', 'ARBC', 'ARCN', 'ARTH', 'ASLN', 'ASST', 'ASTR', 'BIOL', 'CHEM', 'CHIN', 'CAMS',
            'CLAS', 'CGSC', 'CS', 'CCST', 'DANC', 'DGAH', 'ECON', 'EDUC', 'ENGL', 'ENTS', 'EUST', 'FREN', 'GEOL',
            'GERM', 'GRK', 'HEBR', 'HIST', 'IDSC', 'JAPN', 'LATN', 'LTAM', 'LING', 'LCST', 'MATH', 'MARS', 'MEST',
            'MELA', 'MUSC', 'NEUR', 'PHIL', 'PE', 'PHYS', 'POSC', 'PSYC', 'RELG', 'RUSS', 'SOAN', 'SPAN', 'ANCE',
            'ARTS', 'THEA', 'WGST']

terms = ['19FA', '20WI', '20SP']


def collect_dept(dept_iter):
    return subjects[dept_iter]


def collect_nums(tree, i):
    string = str(tree.xpath('//*[@id="enrollModule"]/div[1]/div[' + str(i) + ']/h3/span[1]/text()'))
    number = float(''.join(filter(lambda x: x.isdigit() or x == '.', string)))
    return number


# def collect_num_suffix(tree):
#     nums_list = []
#
#     # iterate through the page collecting the course numbers
#     for i in range(1, get_number_offered_for_term(tree) + 1):
#         string = str(tree.xpath('//*[@id="enrollModule"]/div[1]/div[' + str(i) + ']/h3/span[1]/text()'))
#         number = float(''.join(filter(lambda x: x.isdigit() or x == '.', string))[3::])
#         nums_list.append(number)
#
#     return nums_list


def collect_name(tree, i):
    string = str(tree.xpath('//*[@id="enrollModule"]/div/div[' + str(i) + ']/h3/text()')[0])
    return string[1:-1]


def collect_terms(term_iter):
    if term_iter == 0:
        return 'Fall 2019'
    elif term_iter == 1:
        return 'Winter 2020'
    elif term_iter == 2:
        return 'Spring 2020'
    return 'Term not found'


def collect_reqs(tree, course_iter):
    reqs = []
    for i in range(1, 4):
        string = str(tree.xpath('//*[@id="enrollModule"]/div/div[' + str(course_iter) + ']/div[1]/div[2]/ul/li[' + str(i) + ']/a/text()'))
        if "Formal" in string:
            reqs.append("FSR")
        if "Quantitative" in string:
            reqs.append("QRE")
        if "Argument & Inquiry" in string:
            reqs.append("A&I")
        if "Writing " in string:
            reqs.append("WRC")
        if "Intercultural Dom" in string:
            reqs.append("IDS")
        if "Social" in string:
            reqs.append("SOC")
        if "Humanistic" in string:
            reqs.append("HUM")
        if "International" in string:
            reqs.append("INS")
        if "Lab" in string:
            reqs.append("LAB")
        if "Arts" in string:
            reqs.append("ARP")
        if "Literary" in string:
            reqs.append("LAA")
        if "PE" in string:
            reqs.append("PER")

    return str(reqs).replace('\'', '').replace('[', '').replace(']', '')


def collect_period(tree, course_iter):
    start_time = str(tree.xpath('//*[@id="enrollModule"]/div/div[' + str(course_iter) + ']/div[1]/div[1]/table/tbody/tr/td[1]/span[1]/text()'))

    # the class is MWF
    if start_time != '[]':
        if '8:30' in start_time:
            return '1a'
        elif '9:50' in start_time:
            return '2a'
        elif '11:10' in start_time:
            return '3a'
        elif '12:30' in start_time:
            return '4a'
        elif '1:50' in start_time:
            return '5a'
        elif '3:10' in start_time:
            return '6a'

    # the class is T/Th
    else:
        start_time = str(tree.xpath('//*[@id="enrollModule"]/div/div[1]/div[1]/div[1]/table/tbody/tr/td[2]/span[1]/text()'))
        if '8:15' in start_time:
            return '1/2c'
        elif '10:10' in start_time:
            return '2/3c'
        elif '1:15' in start_time:
            return '4/5c'
        elif '3:10' in start_time:
            return '5/6c'

    return 'Unable to determine class period'


def get_number_offered_for_term(tree):
    string = str(tree.xpath('//*[@id="enrollModule"]/p[3]/text()'))
    if 'found' in string:
        index = string.index('found') + 6
    elif 'found' not in string:
        string = str(tree.xpath('//*[@id="enrollModule"]/p[2]/text()'))
        if 'found' in string:
            index = string.index('found') + 6
        else:
            return 0

    number_offered = int(''.join(filter(lambda x: x.isdigit(), string[index:index + 2])))
    return number_offered


def create_csv(course_list):
    with open('newClasses.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['DeptTag', 'CourseNum', 'CourseName', 'Term', 'reqsFilled', 'period'])
        for item in course_list:
            filewriter.writerow(
                [item.dept, item.num, item.name, item.term, item.reqs, item.periods])


def test():
    page = requests.get('https://apps.carleton.edu/campus/registrar/schedule/enroll/?term=19FA&subject=BIOL')
    tree = fromstring(page.content)
    print(get_number_offered_for_term(tree))
    print(collect_nums(tree, 1))
    print(collect_reqs(tree, 1))
    print(collect_period(tree, 2))


def crawl_page(page, dept_iter, term_iter):
    tree = fromstring(page.content)
    num_courses = get_number_offered_for_term(tree)

    # iterates through a subject during a specific term
    for i in range(1, num_courses + 1):
        course = Course(collect_dept(dept_iter), collect_nums(tree, i), collect_name(tree, i), collect_terms(term_iter), collect_reqs(tree, i),
                        collect_period(tree, i))
        master_list.append(course)


def crawl_subject(dept_iter):
    # iterates over all three terms
    for j in range(0, 3):
        term = terms[j]
        url = 'https://apps.carleton.edu/campus/registrar/schedule/enroll/?term=' + term + '&subject=' + subjects[dept_iter]
        page = requests.get(url)
        crawl_page(page, dept_iter, j)


def main():
    for i in range(0, len(subjects)):
        crawl_subject(i)
    create_csv(master_list)


if __name__ == '__main__':
    main()
