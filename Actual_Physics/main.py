"""
    <h1>Actual_Physics</h1>

    <h2>What it is</h2>
    This is a library that calculates things found in actual physics

    <h2>When to use it</h2>
    This library does <b>not</b> have much use-cases (if any) in data science, in any way shape or form, or AI development
    But it can be used in actual physics projects
    
    <h2>Credits</h2>
    EssamTheCoder: literally all the code
    
    TranslatorsCafe.com & Google.com: Length converion data

"""



from colorama import Fore

#Units of measure

def Length_Unit_Converter(num: float, input_unit: str, output_unit: str): 
    """
    <h1>Length Unit Converter</h1>
    
    <h2>Purpose</h2>
        To convert the <u>num</u>ber you inputted, in the input unit of your choice into the output unit of your choice

    <h2>Inputs</h2>
        <b>num</b> (float): The length of whatever you're trying to measure, in input_unit <br>
        <b>input_unit</b> (str): The unit of measure that num is measured in <br>
        <b>output_unit</b> (str): The unit of measure that the function translates the num into, then returns <br>
        
    <h2>Outputs</h2>
        If the input_unit and output_unit variables are valid:
            num, converted to output_unit
        
        If input_unit and/or output_unit are not valid:
            Invalid unit of measure
    
        <h2>All valid units of measure</h2>
            <b>Includes both full forms & abbreviated forms, which are in bold</b>
    
            <ul>
                <li>Exameter, <b>em</b>,</li>
                <li><b>petameter</b>,</li>
                <li>gigameter, <b>gm</b>,</li>
                <li><b>megameter</b>,</li>
                <li>kilometer, <b>km</b>,</li>
                <li>hectometer, <b>hm</b>,</li>
                <li>meter, <b>m</b>,</li>
                <li>centimeter, <b>cm</b>,</li>
                <li>millimeter, <b>mm</b>,</li>
                <li>micrometer, <b>micron</b>,</li>
                <li>nanometer, <b>nm</b>,</li>
                <li>picometer, <b>pm</b>,</li>
                <li>femtometer, <b>fm</b>,</li>
                <li>attometer, <b>am</b>,</li>
                <br>
                <li>mile, <b>mi</b>,</li>
                <li>yard, <b>yd</b>,</li>
                <li>foot, <b>ft</b>,</li>
                <li>inch, <b>in</b>,</li>
            </ul>
    """

    input_unit = input_unit.lower()
    output_unit = output_unit.lower()

    full_abbreviation_pairs = {
    "exameter": "em",
    "petameter": "petameter",
    "terameter": "tm",
    "gigameter": "gm",
    "megameter": "megameter",
    "kilometer": "km",
    "hectometer": "hm",
    "meter": "m",
    "centimeter": "cm",
    "millimeter": "mm",
    "micrometer": "micron",
    "nanometer": "nm",
    "picometer": "pm",
    "femtometer": "fm",
    "attometer": "am",
    
    "mile": "mi",
    "yard": "yd",
    "foot": "ft",
    "inch": "in"
}

    fulls = list( full_abbreviation_pairs.keys() )
    abbriviations = list( full_abbreviation_pairs.values() )

    #Input Unit Validity Check
    if input_unit in abbriviations:
        input_unit = input_unit
    
    elif input_unit in fulls:
        input_unit = full_abbreviation_pairs.get(input_unit)
    
    else:
        input_unit = "Invalid"

    #Output Unit Validity Check
    if output_unit in abbriviations:
        output_unit = output_unit
    
    elif output_unit in fulls:
        output_unit = full_abbreviation_pairs.get(output_unit)
    
    else:
        output_unit =  "Invalid"

    #Converion Process
    Meter_CRs = {
        #Metric
        "em": 1e+18,
        "petameter": 1e+15,
        "tm": 1e+12,
        "gm": 1e+9,
        "megameter": 1000000,
        "km": 1000,
        "hm": 100,

        "m": 1,

        "cm": 0.01,
        "mm": 0.001,
        "micron": 0.000001,"µm": 0.00001,
        "nm": 1e-9,
        "pm": 1e-12,
        "fm": 1e-15,
        "am": 1e-18,
        
        #Imperial
        "mi": 1609.34,
        "yd": 1.094,
        "ft": 0.3048,
        "in": 39.37,
    }

    if input_unit == "m":
        return num / Meter_CRs.get(output_unit)
    
    else:
        placeholder_num = num
        placeholder_num = placeholder_num / Meter_CRs.get(input_unit)
        
        return placeholder_num / Meter_CRs.get(output_unit)

def Temprature_Unit_Converter(temprature: float, input_unit: str, output_unit: str):
    """
        <h1>Temprature Unit Converter</h1>
        
        <h2>Purpose</h2>
        To convert between the three main temprature units, Kelvin, Celsius, and Fahrenheit
        
        <h2>Inputs</h2>
            <b>temprature</b> (float): the temprature, measured in the input_unit <br>
            <b>input_unit</b> (str): the unit of measure you use to measure the temprature <br>
            <b>output_unit</b> (str): the unit of measure that you convert the temprature to
        
        <h2>Outputs</h2>
            If both units are valid:
                the temprature, converted to output_unit
            
        If one of the units is invalid:
            "one of your units is invalid, valid units of measure are: Celsius (C), Fahrenheit (F), and Kelvin (K)"
    """
    
    input_unit = input_unit.lower()
    output_unit = output_unit.lower()
    
    Absolute_0 = 273.15
    
    full_abbreviation_pairs = {
        "kelvin": 'k',
        "celsius": 'c',
        "fahrenheit": 'f'
    }
    
    abbreviations = full_abbreviation_pairs.values()
    fulls = full_abbreviation_pairs.keys()
    
    #Input Unit Validity Check
    if input_unit in abbreviations:
        input_unit = input_unit
    
    elif input_unit in fulls:
        input_unit = full_abbreviation_pairs.get(input_unit)
    
    else:
        input_unit = "Invalid"
    
    #Output Unit Validity Check
    if output_unit in abbreviations:
        output_unit = output_unit
    
    elif output_unit in fulls:
        output_unit = full_abbreviation_pairs.get(output_unit)
    
    else:
        output_unit = "Invalid"
    
    #Conversion process
    if input_unit == output_unit:
        return temprature
    
    if input_unit == 'k':
        Results = {
            'c': temprature-Absolute_0,
            'f': (temprature-Absolute_0)*1.8+32
        }
        
        return Results.get(output_unit)
    
    elif input_unit == 'c':
        Results = {
            'k': temprature+Absolute_0,
            'f': temprature*1.8+32
        }
        
        return Results.get(output_unit)
    
    elif input_unit == 'f':
        Results = {
            'k': (temprature-32)*(5/9)+Absolute_0,
            'c': (temprature-32)*(5/9)
        }
        
        return Results.get(output_unit)
    
    else:
        return "one of your units is invalid, valid units of measure are: Celsius (C), Fahrenheit (F), and Kelvin (K)"



# Efficiency
def efficiency(total: float, useful: float, print_waste: bool):
    """
        <h1>Efficiency</h1>
        
        <h2>Purpose</h2>
        This function calculates the energy efficiency of an appliance
        
        <h2>Inputs</h2>
        <b>total</b> (float), the total input energy <br>
        <b>useful</b> (float), the  total enrgy which is used correctly by an appliance <br>
        <b>print_waste</b> (boolean), if the amount of energy wasted is returned
        
        <h2>Outputs</h2>
            print_waste == False:
                efficiency (type: float), in percent form
            
            print_waste == True:
                efficency (type: float), in percent form
                wated energy (type: float), in pertcent form

    """
    efficiency_percent = (useful/total)*100
    if total >= useful and total >= 0:
        if print_waste == True:
            return efficiency_percent, 100-efficiency_percent
        
        elif print_waste == False:
            return efficiency_percent


def kinetic(mass: float, velocity: float):
    """
        <h1>Kinetic Energy</h1>

        <h2>Purpose</h2>
        To find the kinetic energy
        
        <h2>Inputs</h2>
        <b>mass</b> (float) <br>
        <b>velocity</b> (float), the speed of an object
        
        <h2>Output</h2>
        Kinetic energy, or mass/2 * velocity^2
    """

    return (mass/2) * (velocity**2)

def gpe(mass: float, height: float, gForce: float):   
        """    
        <h1>Gravitational Potential Energy</h1>
        
        <h2>Purpose</h2>
        Calculates the GPE of an object.
        
        <h2>Inputs</h2>
        <b>mass</b> (float), how heavy an object is <br>
        <b>height</b> (float), how high an object is <br>
        <b>gForce</b> (float), the gravitaional force, how strong gravity is
        
        <h2>Outputs</h2>
        mass * height * gForce
        """

        return mass*height*gForce  

#WAVES

def Get_Wave_Speed(frequency: float, wavelength: float):
    """
        <h1>Get Wave Speed</h1>
        
        <h2>Purpose</h2>
        To find the wave speed (standard unit of measure: m/s)
        
        <h2>Inputs</h2>
        <b>frequency</b> (float) <br>
        <b>wavelength</b> (float) <br>
        
        <h2>Output</h2>
        frequency * wavelength
    """
    
    return frequency * wavelength

def Get_Wavelength(frequency: float, wave_speed: float):
    """
        <h1>Get Wavelength</h1>
        
        <h2>Purpose</h2>
        To find the wavelength (standard unit of measure: m)
        
        <h2>Inputs</h2>
        <b>frequency</b> (float) <br>
        <b>wave_speed</b> (float) <br>
        
        <h2>Output</h2>
        wavelength / frequency
    """
    
    return wave_speed / frequency

def Get_Frequency(wave_speed: float, wavelength: float):
    """
        <h1>Get Frequency</h1>
        
        <h2>Purpose</h2>
        To find the frequency (standard unit of measure: hz)
        
        <h2>Inputs</h2>
        <b>wave_speed</b> (float) <br>
        <b>wavelength</b> (float) <br>
        
        <h2>Output</h2>
        wave_speed / wavelength
    """
    
    return wave_speed / wavelength

def Get_Wave_Type(wavelength: float, unit_of_measure: str):
    """
    <h1>Get Wave Type</h1>
    
    <h2>Purpose</h2>
    To get the type of wave that has the specific wavelength you inputted. It is, for some weird reason, measured in 
    meters.

    <h2>Inputs</h2>
        wavelength (float): how long the wave is. <br>
        unit_of_measure (str): If you want the wavelength not to be measured in meters, rater, millimeters, micrometer (microns), nanometers, or picometers input the name of the unit of measure you want to use as this parameter's value. If the value is invalid, or blank, it will automatically be set to meters (m)

    <h2>Output</h2>
    Will return wave type as a string.
    """


#Power

def Get_KWh(time: float, time_unit: str, power: float, power_unit: str, price_per_KW: float):
    """
    <h1>Get Kilowatt Hours</h1>
    
    <h2>Purpose</h2>
        To get the kilowatt hours, which is the time (in hours), multiplied by the power (in kilowatts), 
        multiplied by the cost of each kilowatt.
    
    <h2>Input</h2>
        <b>time</b> (float): the amount of time <br>
        <b>time_unit</b> (str): the unit of time used. Day for days, hr for hours, min for minutes, sec for seconds. <br>

        <b>power</b> (float): the amount of power used <br>
        <b>power_unit</b> (str): the unit of power used. W for watt, kW for kilowatt. <br>

        <b>price_per_KW</b> (float): the price, in any currency, of each kw used.
    
    <h2>Output<h2>
        time (converted to hours) * power (converted to kW) * price_per_KW
    """
    
    #Power
    Power_Units = ["kw","w"] #All valid power units
    real_power_unit = power_unit.lower() #The power unit inputted, but in lowercase
    
    #Time
    Time_Units = ["day","hr","min","sec"] #All vaild time units
    real_time_unit = time_unit.lower() #The time unit inputted, but in lowecase
    
    def Power_Unit_Converter(num: float, input_unit: str):
        Power_Unit_Conversion = {
            "kw": 1,
            "w": 1000
        }
        
        return num / Power_Unit_Conversion.get(input_unit) 
    
    def Time_Unit_Converter(num: float, input_unit: str):
        Time_Unit_Conversion = {
            "day": 1/24,
            "hr": 1,
            "min": 60,
            "sec": 3600
        }

        return num / Time_Unit_Conversion.get(input_unit)

    
        
    if (real_power_unit in Power_Units) and (real_time_unit in Time_Units): #Both valid
        return Power_Unit_Converter(power,real_power_unit) * Time_Unit_Converter(time,real_time_unit) * price_per_KW
    
    elif (real_power_unit in Power_Units) and (real_time_unit not in Time_Units): #Power valid, time invalid
        print(Fore.RED,"Time unit must be valid",Fore.RESET)
    
    elif (real_power_unit not in Power_Units) and (real_time_unit in Time_Units): #Power invalid, time valid
        print(Fore.RED,"Power unit must be valid",Fore.RESET)
    
    elif (real_power_unit not in Power_Units) and (real_time_unit not in Time_Units): #Both invalid
        print(Fore.RED,"Power and time units must be valid",Fore.RESET)
