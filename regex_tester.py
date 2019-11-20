def main():
    string = 'This\xa0should print well'
    string = string.replace('\\xa0', '[space]')
    print(string)


if __name__ == '__main__':
    main()
