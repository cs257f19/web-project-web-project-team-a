from lxml import html
import requests
from lxml.html import fromstring
import csv


def getDeptList():
    deptList = ['africana-studies', 'american-music', 'american-studies', 'archaeology', 'art', 'asian-languages',
                'asian-studies', 'biochemistry', 'biology', 'chemistry', 'cinema-media-studies', 'classics',
                'cognitive-science', 'computer-science', 'cross-cultural-studies', 'digital-arts-humanities',
                'economics', 'educational-studies', 'english', 'environmental-studies', 'european-studies', 'french',
                'geology', 'german', 'russian', 'history', 'judaic-studies', 'latin-american-studies', 'linguistics',
                'math', 'medieval-renaissance-studies', 'middle-east-studies', 'middle-eastern languages', 'music',
                'neuroscience', 'philosophy', 'physical-education', 'physics-astronomy', 'political-science',
                'psychology', 'public-policy', 'religion', 'sociology-anthropology', 'spanish', 'theater-dance',
                "womens-gender-studies"]

    return deptList


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def getNumofCourses(tree):
    classNames = tree.xpath('//div[@id="courses"]/ul[*]/li[*]/div/h3/text()')

    return len(classNames)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def getDeptTags(tree):
    classesRaw = tree.xpath('//span[@class="courseDeptNumber"]/text()')
    deptCode = []
    for item in classesRaw:
        if "CS" in item:
            deptCode.append("CS")
        if "ARBC" in item:
            deptCode.append("ARBC")
        if "AFAM" in item:
            deptCode.append("AFAM")
        if "AFST" in item:
            deptCode.append("AFST")
        if "AMMU" in item:
            deptCode.append("AMMU")
        if "AMST" in item:
            deptCode.append("AMST")
        if "ARCN" in item:
            deptCode.append("ARCN")
        if "ARTH" in item:
            deptCode.append("ARTH")
        if "ASLN" in item:
            deptCode.append("ASLN")
        if "ASST" in item:
            deptCode.append("ASST")
        if "ASTR" in item:
            deptCode.append("ASTR")
        if "BIOL" in item:
            deptCode.append("BIOL")
        if "CHEM" in item:
            deptCode.append("CHEM")
        if "CHIN" in item:
            deptCode.append("CHIN")
        if "CAMS" in item:
            deptCode.append("CAMS")
        if "CLAS" in item:
            deptCode.append("CLAS")
        if "CGSC" in item:
            deptCode.append("CGSC")
        if "CCST" in item:
            deptCode.append("CCST")
        if "DANC" in item:
            deptCode.append("DANC")
        if "DGAH" in item:
            deptCode.append("DGAH")
        if "ECON" in item:
            deptCode.append("ECON")
        if "EDUC" in item:
            deptCode.append("EDUC")
        if "ENGL" in item:
            deptCode.append("ENGL")
        if "ENTS" in item:
            deptCode.append("ENTS")
        if "EUST" in item:
            deptCode.append("EUST")
        if "FREN" in item:
            deptCode.append("FREN")
        if "GEOL" in item:
            deptCode.append("GEOL")
        if "GERM" in item:
            deptCode.append("GERM")
        if "GRK" in item:
            deptCode.append("GRK")
        if "HEBR" in item:
            deptCode.append("HEBR")
        if "HIST" in item:
            deptCode.append("HIST")
        if "IDSC" in item:
            deptCode.append("IDSC")
        if "JAPN" in item:
            deptCode.append("JAPN")
        if "LATN" in item:
            deptCode.append("LATN")
        if "LTAM" in item:
            deptCode.append("LTAM")
        if "LING" in item:
            deptCode.append("LING")
        if "LCST" in item:
            deptCode.append("LCST")
        if "MATH" in item:
            deptCode.append("MATH")
        if "MARS" in item:
            deptCode.append("MARS")
        if "MEST" in item:
            deptCode.append("MEST")
        if "MELA" in item:
            deptCode.append("MELA")
        if "MUSC" in item:
            deptCode.append("MUSC")
        if "NEUR" in item:
            deptCode.append("NEUR")
        if "PHIL" in item:
            deptCode.append("PHIL")
        if "PE" in item:
            deptCode.append("PE")
        if "PHYS" in item:
            deptCode.append("PHYS")
        if "POSC" in item:
            deptCode.append("POSC")
        if "PSYC" in item:
            deptCode.append("PSYC")
        if "RELG" in item:
            deptCode.append("RELG")
        if "RUSS" in item:
            deptCode.append("RUSS")
        if "SOAN" in item:
            deptCode.append("SOAN")
        if "SPAN" in item:
            deptCode.append("SPAN")
        if "ARTS" in item:
            deptCode.append("ARTS")
        if "THEA" in item:
            deptCode.append("THEA")
        if "WGST" in item:
            deptCode.append("WGST")

    return deptCode


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def getClassNums(tree):
    classesRaw = tree.xpath('//span[@class="courseDeptNumber"]/text()')
    classNums = []
    for item in classesRaw:
        classNums.append(item[-4:-1])
    return classNums


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def getClassName(tree):
    classNames = tree.xpath('//div[@id="courses"]/ul[*]/li[*]/div/h3/text()')
    for i in range(0, len(classNames)):
        classNames[i] = classNames[i][1::]
    return classNames


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def getDescs(tree, numCourses):
    courseDescList = []

    for i in range(1, numCourses + 1):
        desc = tree.xpath('//div[@id="courses"]/ul[2]/li[' + str(i) + ']/div/span[1]/p/text()')
        if desc == []:
            desc = tree.xpath('//div[@id="courses"]/ul[2]/li[' + str(i) + ']/div/span[1]/text()')
        for item in desc:
            if '\n' in item:
                desc = []
        courseDescList.append(str(desc)[2:-2])

    return courseDescList


def getDescBool(tree, numCourses):
    list = getDescs(tree, numCourses)
    descBool = []
    for item in list:
        if item != '':
            descBool.append(1)
        else:
            descBool.append(0)

    return descBool


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def getPreReqs(tree, numCourses, descBool):
    preReqsRaw = []

    for i in range(0, numCourses):
        if descBool[i] == 0:
            span = '[1]'
        else:
            span = '[2]'
        preReq = tree.xpath('//div[@id="courses"]/ul[2]/li[' + str(i + 1) + ']/div/span' + span + '/text()')
        if preReq != [] and 'Pre' in \
                tree.xpath('//div[@id="courses"]/ul[2]/li[' + str(i + 1) + ']/div/span' + span + '/text()')[0]:
            preReqsRaw.append(str(
                tree.xpath('//div[@id="courses"]/ul[2]/li[' + str(i + 1) + ']/div/span' + span + '/text()')[0]).replace(
                'Prerequisites: ', ''))
        else:
            preReqsRaw.append('None')

    return preReqsRaw


def getPreReqsBool(tree, numCourses, descBool):
    preReqsStr = getPreReqs(tree, numCourses, descBool)
    preReqsBool = []

    for item in preReqsStr:
        if "None" in item:
            preReqsBool.append(0)
        else:
            preReqsBool.append(1)

    return preReqsBool


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def getReqsFilled(tree):
    reqsFilled = tree.xpath('//*[@id="courses"]/ul[*]/li[*]/div/span[*]/em/text()[1]')

    reqsFilledShort = []
    for item in reqsFilled:
        reqs = []
        if "Formal" in item:
            reqs.append("FSR")
        if "Quantitative" in item:
            reqs.append("QRE")
        if "Argument and Inquiry" in item:
            reqs.append("A&I")
        if "Writing Requirement" in item:
            reqs.append("WRC")
        if "Intercultural Dom" in item:
            reqs.append("IDS")
        if "Social" in item:
            reqs.append("SOC")
        if "Humanistic" in item:
            reqs.append("HUM")
        if "International" in item:
            reqs.append("INS")
        if "Lab" in item:
            reqs.append("LAB")
        if "Arts" in item:
            reqs.append("ARP")
        if "Literary" in item:
            reqs.append("LAA")
        if "PE" in item:
            reqs.append("PER")

        reqsFilledShort.append(str(reqs)[1:-1].replace('\'', ''))

    return reqsFilledShort


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def getTermsOffered(tree, num_courses, desc_bool, pre_reqs_bool):
    terms_offered = []

    # iterate through every class in the department
    for i in range(0, num_courses):

        # if the course has a description
        if desc_bool[i] == 1:

            # if the course has a preReq
            if pre_reqs_bool[i] == 1:
                span = '[3]'
            # if the course has no preReq
            else:
                span = '[2]'

        # if the course does not have a description
        else:

            # if the course has a preReq
            if pre_reqs_bool[i] == 1:
                span = '[2]'
            # if the course has no preReq
            else:
                span = '[1]'

        xpath = '//*[@id="courses"]/ul[2]/li[' + str(i + 1) + ']/div/span' + span + '/em/a/text()'
        terms_offered.append(str(tree.xpath(xpath))[1:-1].replace('\'', ''))

    return terms_offered


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


def main():
    deptList = ['physics-astronomy']

    # iterate through each department:
    with open('classes.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['DeptTag', 'CourseNum', 'CourseName', 'PreReqs', 'reqsFilled', 'TermsOffered'])
        for item in deptList:
            # the URL of each department
            url = 'https://www.carleton.edu/' + item + '/courses/'
            page = requests.get(url)
            tree = fromstring(page.content)

            numOfCourses = getNumofCourses(tree)
            deptTags = getDeptTags(tree)
            classNumbers = getClassNums(tree)
            classNames = getClassName(tree)

            descBool = getDescBool(tree, numOfCourses)

            preReqs = getPreReqs(tree, numOfCourses, descBool)
            preReqsBool = getPreReqsBool(tree, numOfCourses, descBool)
            # for i in range(0, numOfCourses):
            #     print(classNumbers[i] + ' ' + str(preReqs[i]))

            reqsFilled = getReqsFilled(tree)

            termsOffered = getTermsOffered(tree, numOfCourses, descBool, preReqsBool)

            print('~~~~~~~~~~~~~')
            print(item)
            print(numOfCourses)
            print(len(deptTags))
            print(len(classNumbers))
            print(len(classNames))
            print(len(descBool))
            print(len(preReqs))
            print(len(reqsFilled))
            print(len(termsOffered))

            for j in range(0, numOfCourses):
                filewriter.writerow(
                    [deptTags[j], classNumbers[j], classNames[j], preReqs[j], reqsFilled[j], termsOffered[j]])
                print(classNumbers[j] + ': ' + str(reqsFilled[j]))

            print(tree.xpath('//*[@id="courses"]/ul[2]/li[16]/div/span[3]/em/text()'))


if __name__ == '__main__':
    main()
