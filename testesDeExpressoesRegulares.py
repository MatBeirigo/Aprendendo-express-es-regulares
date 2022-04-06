import re 
def main():
    #-----------CORRESPONDENCIA DE VÁRIOS GRUPOS---------------------
    #heroRegex = re.compile(r'Batman|Tina Fey')
    #mo1 = heroRegex.search('Batman and Tina Fey.')
    #print(mo1.group())
    #mo2 = heroRegex.search('Tina Fey and Batman')
    #print(mo2.group())
    
    #batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    #mo = batRegex.search('Batmobile lost as wheel')
    #print(mo.group())
    #print(mo.group(1))
    #return
    
    #-------------GRUPOS OPCIONAIS----------------------
    batRegex = re.compile(r'Bat(wo)?man')
    mo1 = batRegex.search('The Adventures of Batman')
    mo2 = batRegex.search('The Adventures of Batwoman')
    print(mo1.group())
    print(mo2.group())
    
    phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
    mo1 = phoneRegex.search('My number is 415-555-4242')
    print(mo1.group())
    mo2 = phoneRegex.search('My number is 555-4242')
    print(mo2.group())
main()