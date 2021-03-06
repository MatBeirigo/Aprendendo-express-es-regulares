import re

def isPhoneNumber(text):
        if len(text) != 12:
            return False
        for i in range(0, 3):
            if not text[i].isdecimal():
                return False
        if text[3] != '-':
            return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
        if text[7] != '-':
            return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True



def main():
    #message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    #for i in range(len(message)):
    #    chunk = message[i:i+12]
    #    if isPhoneNumber(chunk):
    #        print('Phone number found: ' + chunk)
    #print('Done')
    #return
    phoneNumberRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
    mo = phoneNumberRegex.search('My number is (415) 555-4242.')
    print('Phone number found: ' + mo.group(0))
    print('Phone number found: ' + mo.group(1))
    print('Phone number found: ' + mo.group(2))
    
    print(mo.groups())
    areaCode, mainNumber = mo.groups()
    print(areaCode)
    print(mainNumber)
main()