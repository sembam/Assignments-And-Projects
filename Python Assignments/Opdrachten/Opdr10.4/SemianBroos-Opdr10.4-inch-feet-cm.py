def cm_inch_feet(cm, inch, feet):
    cm = range(100, 200)
    cm_naar_inch = cm / 2.54
    inch_naar_feet = inch / 12
    cm_naar_feet = cm / 2.54 / 12

def schrijf_tabel_meet(i, cm, feet, inch):

    while cm <= 200:
        print('CM \t INCH \t  FEET ')        
        inch = cm / 2.54
        feet = inch / 12     
        print(f'{cm} \t {round(inch, 2)} \t  {round(feet, 2)} \n')
        cm += 1
        
        
schrijf_tabel_meet(i=0, cm=100, feet=0, inch=0)