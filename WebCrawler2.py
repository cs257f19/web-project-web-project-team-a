import requests
from lxml.html import fromstring
import csv

master_list = []


class Course:
    """
    Course subclass with instance variables for metadata of the course
    """

    def __init__(self, dept, num, name, term, reqs, periods, prof, desc):
        """
        Course object constructor
        :param dept: department code
        :param num: course number
        :param name: course name
        :param term: term offered
        :param reqs: liberal arts requirements fulfilled by course
        :param periods: class period(s) offered
        :param prof: professor who teaches the course
        :param desc: the course description
        """
        self.dept = dept
        self.num = num
        self.name = name
        self.term = term
        self.reqs = reqs
        self.periods = periods
        self.prof = prof
        self.desc = desc


departments = ['AFST', 'AMMU', 'AMST', 'ARBC', 'ARCN', 'ARTH', 'ASLN', 'ASST', 'ASTR', 'BIOL', 'CHEM', 'CHIN', 'CAMS',
               'CLAS', 'CGSC', 'CS', 'CCST', 'DANC', 'DGAH', 'ECON', 'EDUC', 'ENGL', 'ENTS', 'EUST', 'FREN', 'GEOL',
               'GERM', 'GRK', 'HEBR', 'HIST', 'IDSC', 'JAPN', 'LATN', 'LTAM', 'LING', 'LCST', 'MATH', 'MARS', 'MEST',
               'MELA', 'MUSC', 'NEUR', 'PHIL', 'PE', 'PHYS', 'POSC', 'PSYC', 'RELG', 'RUSS', 'SOAN', 'SPAN', 'ANCE',
               'ARTS', 'THEA', 'WGST']

terms = ['19FA', '20WI', '20SP']


def collect_dept(dept_iter):
    """
    returns the department code for a given department iteration
    :param dept_iter: location within departments list as it's being iterated through
    :return: department code
    """
    return departments[dept_iter]


def collect_nums(tree, i):
    """
    returns the course number contained within the XPath
    :param tree: tree containing all HTML elements of the current page
    :param i: iterator variable for current course being inspected
    :return: course number associated with course at position i in the list of courses w/in the tree
    """
    string = str(tree.xpath('//*[@id="enrollModule"]/div[1]/div[' + str(i) + ']/h3/span[1]/text()'))
    number = float(''.join(filter(lambda x: x.isdigit() or x == '.', string)))
    return number


def collect_name(tree, i):
    """
    returns the course name contained within the XPath
    :param tree: tree containing all HTML elements of the current page
    :param i: iterator variable for current course being inspected
    :return: course name associated with course at position i in the list of courses w/in the tree
    """
    string = str(tree.xpath('//*[@id="enrollModule"]/div/div[' + str(i) + ']/h3/text()')[0])
    return string[1:-1]


def collect_terms(term_iter):
    """
    retrieves the term based on the iteration of the for-loop running in crawl_department
    :param term_iter: iterative variable associated with Fall, Winter or Spring
    :return: the term the course is offered in
    """
    if term_iter == 0:
        return 'Fall 2019'
    elif term_iter == 1:
        return 'Winter 2020'
    elif term_iter == 2:
        return 'Spring 2020'
    return 'Term not found'


def collect_reqs(tree, course_iter):
    """
    returns the liberal arts requirements contained within the XPath, associated with the course at course_iter
    :param tree: the tree containing all HTML elements of the page currently being crawled
    :param course_iter: iterative variable to point at the element within the XPath for the current course
    :return: liberal arts requirements fulfilled by the course
    """
    reqs = []
    for i in range(1, 4):
        string = str(tree.xpath(
            '//*[@id="enrollModule"]/div[1]/div[' + str(course_iter) + ']/div[1]/div[2]/ul/li[' + str(
                i) + ']/a/text()'))
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
    """
    returns the class periods for which the course is offered contained within the XPath, associated with the course at
    course_iter
    :param tree: the tree containing all HTML elements of the page currently being crawled
    :param course_iter: iterative variable to point at the element within the XPath for the current course
    :return: class period for which the course is offered
    """
    start_time = str(tree.xpath('//*[@id="enrollModule"]/div/div[' + str(course_iter) + ']/div[1]/div['
                                                                                        '1]/table/tbody/tr/td['
                                                                                        '1]/span[1]/text()'))

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
        start_time = str(tree.xpath('//*[@id="enrollModule"]/div/div[' + str(course_iter) + ']/div[1]/div['
                                                                                            '1]/table/tbody/tr/td['
                                                                                            '2]/span[1]/text()'))
        if '8:15' in start_time:
            return '1/2c'
        elif '10:10' in start_time:
            return '2/3c'
        elif '1:15' in start_time:
            return '4/5c'
        elif '3:10' in start_time:
            return '5/6c'

    return 'Unable to determine class period'


def collect_professor(tree, course_iter):
    prof = str(tree.xpath('//*[@id="enrollModule"]/div[1]/div[' + str(course_iter) + ']/div[2]/p[1]/a/text()')).replace(
        '[\'', '').replace('\']', '')
    return prof


def collect_desc(tree, course_iter):
    desc = str(tree.xpath('//*[@id="enrollModule"]/div[1]/div[' + str(course_iter) + ']/div[2]/p[2]/text()')).replace(
        '[\'', '').replace('\']', '')
    return desc


def get_number_offered_for_term(tree):
    """
    returns how many courses are offered for a certain department within a specific term
    :param tree: the tree containing all HTML elements of the page currently being crawled
    :return: the number of courses offered by a specific department for a specific term
    """
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
    """
    Creates the CSV file containing all courses offered at Carleton for the 2019-2020 school year
    :param course_list: list of all courses offered at Carleton, containing Course objects
    :return: None, but writes a CSV file
    """
    with open('courses.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Department', 'Course Number', 'Course Name', 'Term', 'Liberal Arts Requirements',
                             'Class Period', 'Professor', 'Description'])
        for item in course_list:
            filewriter.writerow(
                [item.dept, item.num, item.name, item.term, item.reqs, item.periods, item.prof, item.desc])


def crawl_page(page, dept_iter, term_iter):
    """
    Crawls a specific page on Carleton's ENROLL tool
    :param page: the current page from Carleton ENROLL
    :param dept_iter: iterative variable representing which department is currently being crawled
    :param term_iter: iterative variable representing which term is currently being crawled
    :return: None
    """
    tree = fromstring(page.content)
    num_courses = get_number_offered_for_term(tree)

    # iterates through a department during a specific term
    for i in range(1, num_courses + 1):
        course = Course(collect_dept(dept_iter), collect_nums(tree, i), collect_name(tree, i), collect_terms(term_iter),
                        collect_reqs(tree, i), collect_period(tree, i), collect_professor(tree, i), collect_desc(tree, i))
        master_list.append(course)


def crawl_department(dept_iter):
    """
    Crawls a specific department's offerings for the year at Carleton
    :param dept_iter: iterative variable representing the location within list:departments to retrieve the current dept
    :return: None
    """
    # iterates over all three terms
    for j in range(0, 3):
        term = terms[j]
        url = 'https://apps.carleton.edu/campus/registrar/schedule/enroll/?term=' + term + '&subject=' + departments[
            dept_iter]
        page = requests.get(url)
        crawl_page(page, dept_iter, j)


def main():
    """
    Main method for WebCrawler2.py
    Executes a web crawl over all departments for all three terms during the 2019-2020 school year
    :return: none
    """
    for i in range(0, len(departments)):
        crawl_department(i)
    create_csv(master_list)


if __name__ == '__main__':
    main()
