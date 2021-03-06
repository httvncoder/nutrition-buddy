from decimal import Decimal

class Measure:
    
    def __init__(self, value):
        self.value = Decimal(str(value))
        
    def __str__(self):
        return str(self.value)
 
class Factor(Measure):
    def __init__(self, value):
        Measure.__init__(self, value)
        
class Volume(Measure):
 
    def __init__(self, value, isMetric):
        Measure.__init__(self, value)
        self.isMetric = isMetric
        self.FACTOR = Decimal('29.5735296')
        
    def __str__(self):
        valueStr = "{0:.2f}{1}"
        
        if self.isMetric:
            unit = "mL"
        else:
            unit = "oz"
            
        return valueStr.format(self.value, unit)
        
    def ConvertToMetric(self):
        if not self.isMetric:
            self.value *= self.FACTOR
            self.isMetric = True
        return self.value
            
    def ConvertToImperial(self):
        if self.isMetric:
            self.value /= self.FACTOR
            self.isMetric = False
        return self.value
     
class Height(Measure):
    
    def __init__(self, value, isMetric):
        Measure.__init__(self, value)
        self.isMetric = isMetric
        self.FACTOR = Decimal('2.54')
        
    def __str__(self):
        valueStr = "{0:.2f}{1}"
        
        if self.isMetric:
            unit = "mL"
        else:
            unit = "ozs"
            
        return valueStr.format(self.value, unit)
        
    def ConvertToMetric(self):
        if not self.isMetric:
            self.value *= self.FACTOR
            self.isMetric = True
        return self.value
            
    def ConvertToImperial(self):
        if self.isMetric:
            self.value /= self.FACTOR
            self.isMetric = False
        return self.value
 
 
class Weight(Measure):

    def __init__(self, value, isMetric):
        Measure.__init__(self, value)
        self.isMetric = isMetric
        self.FACTOR = Decimal('2.2')
        
    def __str__(self):
        valueStr = "{0:.2f}{1}"
        
        if self.isMetric:
            unit = "kg"
        else:
            unit = "lbs"
            
        return valueStr.format(self.value, unit)
        
    def ConvertToMetric(self):
        if not self.isMetric:
            self.value /= self.FACTOR
            self.isMetric = True
        return Decimal(str(self.value))
            
    def ConvertToImperial(self):
        if self.isMetric:
            self.value *= self.FACTOR
            self.isMetric = False
        return Decimal(str(self.value))
    
class Age(Measure):
    pass

class Gender():
    
    def __init__(self, isMale):
        self.isMale = isMale
    
    def __str__(self):
        if self.isMale:
            return "Male"
        else:
            return "Female"


class Temperature(Measure):
    
    def __init__(self, value, isMetric):
        Measure.__init__(self, value)
        self.isMetric = isMetric
        
    def __str__(self):
        
        if self.isMetric:
            unit = "C"
        else:
            unit = "F"
            
        return "{0:.2f}{1}".format(self.value, unit)
        
    def ConvertToMetric(self):
        if not self.isMetric:
            self.value = (self.value - Decimal('32')) * (Decimal('5.0')/Decimal('9.0'))
            self.isMetric = True
        return self.value
            
    def ConvertToImperial(self):
        if self.isMetric:
            self.value = (self.value * (Decimal('9.0')/Decimal('5.0'))) + Decimal('32')
            self.isMetric = False
        return self.value
        
