goodtopspeed = 120
goodmpg = 40


class Cars:
    def __init__(self,name,yearmade,kmperliter,topspeed):
        self.name = name
        self.yearmade  = yearmade
        self.kmperliter = kmperliter
        self.topspeed = topspeed
    def analyze(self):
        mpg = self.kmperliter*2.352145 
        if self.topspeed <goodtopspeed and mpg<goodmpg:
            print('The '+str(self.name)+' was inrtoduced in '+str(self.yearmade)+ ' and has a below averge top speed of '
            +str(self.topspeed)+' kilometers per hour,\n'+' and also lacks in the amount of miles traveled with 1 gallon with '
            +str(mpg)+' miles per gallon.')
        if self.topspeed <goodtopspeed and mpg>goodmpg:
            print('The '+str(self.name)+' was inrtoduced in '+str(self.yearmade)+ ' and has a below averge top speed of '
            +str(self.topspeed)+' kilometers per hour,\n'+' but makes up for that in the amount of miles traveled with 1 gallon with '
            +str(mpg)+' miles per gallon.')
        if self.topspeed >goodtopspeed and mpg<goodmpg:
            print('The '+str(self.name)+' was inrtoduced in '+str(self.yearmade)+ ' and has an above averge top speed of '
            +str(self.topspeed)+' kilometers per hour,\n'+' but lacks  in the amount of miles traveled with 1 gallon with '
            +str(mpg)+' miles per gallon.')
        if self.topspeed >goodtopspeed and mpg>goodmpg:
            print('The '+str(self.name)+' was inrtoduced in '+str(self.yearmade)+ ' and is an outstanding car. It has an above averge top speed of '
            +str(self.topspeed)+' kilometers per hour,\n'+' and excels in the amount of miles traveled with 1 gallon with '
            +str(mpg)+' miles per gallon.')
        
        
Ford =  Cars('Ford Bronco','1996',5.35,160)

Ford.analyze()