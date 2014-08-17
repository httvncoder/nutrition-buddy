from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

from Measures import Height, Weight, Age, Gender
from Calculator import NutritionCalculator


class EnergyNeedsScreen(Screen):
    pass

class WelcomeScreen(Screen):
    pass

class ConversionScreen(Screen):
    
    weightIsMetric = False
    heightIsMetric = False
    
    def ConvertMeasure(self, typeOfMeasure, measureToConvert):
        if measureToConvert.isdigit():
            
            if typeOfMeasure == 'weight':
                measure = Weight(measureToConvert, self.weightIsMetric)
                isMetric = self.weightIsMetric
            else:
                measure = Height(measureToConvert, self.heightIsMetric)
                isMetric = self.heightIsMetric
                
            if isMetric:
                return '{0:.2f}'.format(measure.ConvertToImperial())
            else:
                return '{0:.2f}'.format(measure.ConvertToMetric())
        return ''            

    def SetButtonText(self, buttonToChange):
        if buttonToChange.text[0] == 'K' or buttonToChange.text[0] == 'P':
            self.weightIsMetric = not self.weightIsMetric
            
            if self.weightIsMetric:
                buttonToChange.text = 'Kilograms \n    >>\nPounds'
            else:
                buttonToChange.text = 'Pounds \n   >>\nKilograms'
            
        if buttonToChange.text[0] == 'C' or buttonToChange.text[0] == 'I':
            self.heightIsMetric = not self.heightIsMetric
            
            if self.heightIsMetric:
                buttonToChange.text = 'Centimeters \n    >>\nInches'
            else:
                buttonToChange.text = 'Inches \n   >>\nCentimeters'   


class MifflinStJeorScreen(Screen):
    
    def Calculations(self, measures):
        for value in measures.itervalues():
            if not value.isalnum():
                return "Unable to process, check fields."
            
        if measures['wtUnit'] == 'kg':
            weight = Weight(measures['wtValue'], True)
        else:
            weight = Weight(measures['wtValue'], False)
        
        if measures['htUnit'] == 'cm':
            height = Height(measures['htValue'], True)
        else:
            height = Height(measures['htValue'], False)     
        
        if measures['gender'][0] == 'M':
             gender = Gender(True)
        else:
             gender = Gender(False)
        age = Age(measures['age'])
        
        print str(weight), str(height), str(gender), str(age)
       
        return "\n".join([self.CalculateEnergyNeeds(weight.ConvertToMetric(), 
                                                    height.ConvertToMetric(), 
                                                    age.value, gender),
                          self.CalculateBMI(weight.ConvertToMetric(), 
                                            height.ConvertToMetric()),
                          self.CalculateIdealWeight(weight, 
                                                    height.ConvertToImperial(), 
                                                    gender)])
    
    def CalculateBMI(self, weight, height):
        bmi = NutritionCalculator().BodyMassIndex(weight, height)
        bmiCategory = NutritionCalculator().BmiCategory(bmi)
        return "{0:.2f} - {1}".format(bmi, bmiCategory)
    
    def CalculateEnergyNeeds(self, weight, height, age, gender):  
        energyNeeds = NutritionCalculator().MifflinStJeor(weight, height, 
                                                          age, gender)
        caloriesPerKilogram = NutritionCalculator().CaloriesPerKilogram(energyNeeds, 
                                                                        weight)
        return "\n\n{0:.0f} Calories ({1:.0f}cal/kg)".format(energyNeeds, 
                                                           caloriesPerKilogram)
    
    def CalculateIdealWeight(self, weight, height, gender):
        idealWeight = Weight(NutritionCalculator().IdealBodyWeight(height, gender), False)
        percentIdeal = NutritionCalculator().PercentIdealBodyWeight(weight.ConvertToMetric(), 
                                                                    idealWeight.ConvertToMetric())
        if percentIdeal > 125.0:
            adjustedWeight = Weight(NutritionCalculator().AdjustedBodyWeight(weight.ConvertToMetric(), 
                                                                             idealWeight.ConvertToMetric()), 
                                                                             True)
            return "{0:.2f}kg or {1:.2f}lbs ({2:.2f}%)\n{3:.2f}kg or {4:.2f}lbs".format(idealWeight.ConvertToMetric(), 
                                                                                        idealWeight.ConvertToImperial(), 
                                                                                        percentIdeal,
                                                                                        adjustedWeight.ConvertToMetric(), 
                                                                                        adjustedWeight.ConvertToImperial())
        
        return "{0:.2f}kg or {1:.2f}lbs ({2:.2f}%)\nN/A".format(idealWeight.ConvertToMetric(), 
                                                           idealWeight.ConvertToImperial(),
                                                           percentIdeal)
    

    
class NutritionApp(App):
    title = "Nutrition Buddy"

    def build(self):
        calculatorScreenManager = ScreenManager()
        calculatorScreenManager.add_widget(WelcomeScreen(name="Welcome"))
        calculatorScreenManager.add_widget(ConversionScreen(name="Conversions"))
        calculatorScreenManager.add_widget(EnergyNeedsScreen(name="EnergyNeeds"))
        calculatorScreenManager.add_widget(MifflinStJeorScreen(name="Mifflin"))
        return calculatorScreenManager

    def on_pause(self):
        return True

if __name__ in ('__main__', '__android__'):
    NutritionApp().run()