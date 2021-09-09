import requests
import jason
x = requests.get('https://api.imgflip.com/get_memes')
print(x)
print(x.content)
print(x.jason())
prof = {}
for i in range (2019,2022):
    print("year",i)
    n = int(input("number of students "))
    a_f1 = int(input("no of professors "))
    a_f2 = int(input("no of associate professor "))
    a_f3 = int(input("no of assistant professor "))
    rf1 = (1/9)*(n/15)
    rf2 = (2/9)*(n/15)
    rf3 = (6/9)*(n/15)
    prof[i] = {}
    prof[i]['students'] = n
    prof[i]['professor'] = a_f1
    prof[i]['associate professor'] = a_f2
    prof[i]['assistant professor'] = a_f3
    prof[i]['requried professor'] = rf1
    prof[i]['required associate professor'] = rf2
    prof[i]['required assistant professor'] = rf3
      

A_a_f1 =  (prof[2019]['professor']+prof[2020]['professor']+ prof[2021]['professor'])/3
A_a_f2 = (prof[2019]['associate professor']+ prof[2020]['associate professor']+prof[2021]['associate professor'])/3
A_a_f3 = (prof[2019]['assistant professor']+prof[2020]['assistant professor']+prof[2021]['assistant professor'])/3
A_rf1 = (prof[2019]['requried professor']+prof[2020]['requried professor']+prof[2021]['requried professor'])/3
A_rf2 = (prof[2019]['required associate professor']+prof[2020]['required associate professor']+prof[2021]['required associate professor'])/3
A_rf3 = (prof[2019]['required assistant professor']+prof[2020]['required assistant professor']+prof[2021]['required assistant professor'])/3
 

prof['output'] = {}
prof['output']['aaf1'] = A_a_f1
prof['output']['aaf2'] = A_a_f2
prof['output']['aaf3'] = A_a_f3
prof['output']['Arf1'] = A_rf1
prof['output']['Arf2'] = A_rf2
prof['output']['Arf3'] = A_rf3


if(a_f3 == a_f2== 0 ):
     Cadre_Ratio_Marks = 0
     print(Cadre_Ratio_Marks + "Marks")
else:
    Cadre_Ratio_Marks = (A_a_f1/ A_rf1) + ((A_a_f2*0.6)/( A_rf2))+ ((A_a_f3*0.4)/(A_rf3))*12.5
    if (Cadre_Ratio_Marks <= 25):
        print("Cadre Ratio Marks = " + str(Cadre_Ratio_Marks) + "Marks")
    else: 
        Cadre_Ratio_Marks = 25
        print(str(Cadre_Ratio_Marks) + " Marks")
prof['CDR'] = Cadre_Ratio_Marks

print(prof)
