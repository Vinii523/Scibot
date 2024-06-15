import spacy
import re
import math

# Gravitational constant in N*m^2/kg^2
GRAVITY_CONSTANT = 6.67430e-11

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

def calculate_gravity(mass1, mass2, distance):
    # Calculate the gravitational force
    gravitational_force = (GRAVITY_CONSTANT * mass1 * mass2) / (distance**2)
    return gravitational_force

def calculate_force(mass, acceleration):
    # Calculate the force due to acceleration
    force_acceleration = mass * acceleration
    return force_acceleration

def calculate_circle_area(radius):
    # Calculate the area of a circle
    area = math.pi * radius**2
    return area

def calculate_rectangle_area(length, width):
    # Calculate the area of a rectangle
    area = length * width
    return area

def calculate_square_area(side):
     # Calculate the area of a square
     area = side * side
     return  area  

def calculate_cube_volume(side):
    # Calculate the volume of a cube
    volume = side**3
    return volume

def calculate_cuboid_volume(length, width, height):
    # Calculate the volume of a cuboid
    volume = length * width * height
    return volume

def calculate_sphere_volume(radius):
    # Calculate the volume of a sphere
    volume = (4/3) * math.pi * radius**3
    return volume

def calculate_velocity(initial_velocity, acceleration, time):
    # Calculate velocity
    velocity = initial_velocity + (acceleration * time)
    return velocity

def convert_kilogram_to_gram(kilograms):
    # Convert kilograms to grams
    grams = kilograms * 1000
    return grams

def convert_meter_to_centimeter(meters):
    # Convert meters to centimeters
    centimeters = meters * 100
    return centimeters

def convert_kilometer_to_meter(kilometers):
    # Convert kilometers to meters
    meters = kilometers * 1000
    return meters

def convert_inch_to_foot(inches):
    # Convert inches to feet
    feet = inches / 12
    return feet

def convert_foot_to_meter(feet):
    # Convert feet to meters
    meters = feet * 0.3048
    return meters

def convert_foot_to_centimeter(feet):
    # Convert feet to centimeters
    centimeters = feet * 30.48
    return centimeters

def convert_inch_to_centimeter(inches):
    # Convert inches to centimeters
    centimeters = inches * 2.54
    return centimeters

def convert_inch_to_meter(inches):
    # Convert inches to meters
    meters = inches * 0.0254
    return meters

def convert_centimeter_to_meter(centimeters):
    # Convert centimeters to meters
    meters = centimeters * 0.01
    return meters

def convert_centimeter_to_inch(centimeters):
    # Convert centimeters to inches
    inches = centimeters / 2.54
    return inches

def convert_centimeter_to_feet(centimeters):
    # Convert centimeters to feet
    feet = centimeters / 30.48
    return feet

def convert_centimeter_to_meter(centimeters):
    # Convert centimeters to meters
    meters = centimeters / 100
    return meters

def convert_meter_to_kilometer(meters):
    # Convert meters to kilometers
    kilometers = meters / 1000
    return kilometers

def convert_feet_to_inch(feet):
    # Convert feet to inches
    inches = feet * 12
    return inches

def convert_gram_to_kilogram(grams):
    # Convert grams to kilograms
    kilograms = grams / 1000
    return kilograms

def convert_meter_to_inch(meters):
    # Convert meters to inches
    inches = meters / 0.0254
    return inches

def convert_kilometer_to_centimeter(kilometers):
    # Convert kilometers to centimeters
    centimeters = kilometers * 100000
    return centimeters

def calculate_speed(distance, time):
    # Calculate speed
    speed = distance / time
    return speed

def calculate_density(mass, volume):
    # Calculate density
    density = mass / volume
    return density

def calculate_pressure(force, area):
    # Calculate pressure
    pressure = force / area
    return pressure

def calculate_energy(mass, velocity):
    # Calculate kinetic energy
    energy = 0.5 * mass * velocity**2
    return energy

def calculate_temperature_conversion(celsius):
    # Convert Celsius to Fahrenheit and Kelvin
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

def extract_values(input_text, pattern):
    # Use regular expressions to find values based on a pattern
    match = re.search(pattern, input_text)
    value = float(match.group(1)) if match else None
    return value

def calculate_numerical_solutions(user_input):
    # Use spaCy to parse the user's input
    doc = nlp(user_input)
    
    # Patterns to extract values
    volume_pattern = r"volume is (\d+(\.\d+)?) cubic units"
    force_pattern = r"force is (\d+(\.\d+)?) N"
    area_pattern = r"area is (\d+(\.\d+)?) square units"
    velocity_pattern = r"velocity is (\d+(\.\d+)?) m/s"
    radius_pattern = r"radius is (\d+(\.\d+)?) units"
    mass_pattern = r"mass is (\d+(\.\.\d+)?) kg"
    acceleration_pattern = r"acceleration is (\d+(\.\d+)?) km/hr"
    side_pattern = r"side is (\d+(\.\d+)?) units"
    length_pattern = r"length is (\d+(\.\d+)?) units"
    width_pattern = r"breadth is (\d+(\.\d+)?) units"
    initial_velocity_pattern = r"initial velocity is (\d+(\.\d+)?)"
    time_pattern = r"time is (\d+(\.\d+)?)"
    mass_conversion_pattern = r"(\d+(\.\d+)?) kilograms? (?:in|to) grams"
    length_conversion_pattern1 = r"(\d+(\.\d+)?) meters? (?:in|to) centimeters"
    length_conversion_pattern2 = r"(\d+(\.\d+)?) kilometers? (?:in|to) meters"
    length_conversion_pattern3 = r"(\d+(\.\d+)?) inches? (?:in|to) feet"
    length_conversion_pattern4 = r"(\d+(\.\d+)?) feet? (?:in|to) meters"
    length_conversion_pattern5 = r"(\d+(\.\d+)?) feet? (?:in|to) centimeters"
    length_conversion_pattern6 = r"(\d+(\.\d+)?) inches? (?:in|to) centimeters"
    length_conversion_pattern7 = r"(\d+(\.\d+)?) inches? (?:in|to) meters"
    length_conversion_pattern8 = r"(\d+(\.\d+)?) centimeters? (?:in|to) meters"
    length_conversion_pattern9 = r"(\d+(\.\d+)?) centimeters? (?:in|to) feet"
    length_conversion_pattern0 = r"(\d+(\.\d+)?) centimeters? (?:in|to) feet"
    length_conversion_pattern10 = r"(\d+(\.\d+)?) centimeters? (?:in|to) meters"
    length_conversion_pattern11 = r"(\d+(\.\d+)?) meters? (?:in|to) kilometers"
    length_conversion_pattern12 = r"(\d+(\.\d+)?) feet? (?:in|to) inches"
    length_conversion_pattern13 = r"(\d+(\.\d+)?) centimeters? (?:in|to) inches"
    length_conversion_pattern14 = r"(\d+(\.\d+)?) inches? (?:in|to) centimeters"
    mass_conversion_pattern1 = r"(\d+(\.\d+)?) grams? (?:in|to) kilograms"
    length_conversion_pattern15 = r"(\d+(\.\d+)?) meters? (?:in|to) inches"
    length_conversion_pattern16 = r"(\d+(\.\d+)?) kilometers? (?:in|to) centimeters"
    physics_pattern1 = r"speed is (\d+(\.\d+)?) m/s"
    physics_pattern2 = r"density is (\d+(\.\d+)?) kg/m\^3"
    physics_pattern3 = r"pressure is (\d+(\.\d+)?) N/m\^2"
    physics_pattern4 = r"kinetic energy is (\d+(\.\d+)?) J"
    chemistry_pattern1 = r"temperature is (\d+(\.\d+)?) Celsius"



    
    # Extract relevant values
    radius = extract_values(user_input, radius_pattern)
    mass = extract_values(user_input, mass_pattern)
    acceleration = extract_values(user_input, acceleration_pattern)
    side = extract_values(user_input, side_pattern)
    length = extract_values(user_input, length_pattern)
    width = extract_values(user_input, width_pattern)
    initial_velocity = extract_values(user_input, initial_velocity_pattern)
    time = extract_values(user_input, time_pattern)
    mass_conversion_match = re.search(mass_conversion_pattern, user_input)
    length_conversion_match1 = re.search(length_conversion_pattern1, user_input)
    length_conversion_match2 = re.search(length_conversion_pattern2, user_input)
    length_conversion_match3 = re.search(length_conversion_pattern3, user_input)
    length_conversion_match4 = re.search(length_conversion_pattern4, user_input)
    length_conversion_match5 = re.search(length_conversion_pattern5, user_input)
    length_conversion_match6 = re.search(length_conversion_pattern6, user_input)
    length_conversion_match7 = re.search(length_conversion_pattern7, user_input)
    length_conversion_match8 = re.search(length_conversion_pattern8, user_input)
    length_conversion_match9 = re.search(length_conversion_pattern9, user_input)
    length_conversion_match0 = re.search(length_conversion_pattern0, user_input)
    length_conversion_match10 = re.search(length_conversion_pattern10, user_input)
    length_conversion_match11 = re.search(length_conversion_pattern11, user_input)
    length_conversion_match12 = re.search(length_conversion_pattern12, user_input)
    length_conversion_match13 = re.search(length_conversion_pattern13, user_input)
    length_conversion_match14 = re.search(length_conversion_pattern14, user_input)
    mass_conversion_match1 = re.search(mass_conversion_pattern1, user_input)
    length_conversion_match15 = re.search(length_conversion_pattern15, user_input)
    length_conversion_match16 = re.search(length_conversion_pattern16, user_input)
    physics_match1 = re.search(physics_pattern1, user_input)
    physics_match2 = re.search(physics_pattern2, user_input)
    physics_match3 = re.search(physics_pattern3, user_input)
    physics_match4 = re.search(physics_pattern4, user_input)
    chemistry_match1 = re.search(chemistry_pattern1, user_input)




    
    results = {}
    
    if radius is not None:
        circle_area_result = calculate_circle_area(radius)
        results["circle_area_result"] = circle_area_result
    
    if mass is not None and acceleration is not None:
        force_result = calculate_force(mass, (acceleration * 1000) / 3600)
        results["force_result"] = force_result
    
    if side is not None:
        square_area_result = calculate_square_area(side)
        results["square_area_result"] =  square_area_result
    
    if length is not None and width is not None:
        rectangle_area_result = calculate_rectangle_area(length, width)
        results["rectangle_area_result"] = rectangle_area_result
    
    if initial_velocity is not None and acceleration is not None and time is not None:
        velocity_result = calculate_velocity(initial_velocity, acceleration, time)
        results["velocity_result"] = velocity_result
    
    if side is not None:
        cube_volume_result = calculate_cube_volume(side)
        results["cube_volume_result"] = cube_volume_result
    
    if length is not None and width is not None and side is not None:
        cuboid_volume_result = calculate_cuboid_volume(length, width, side)
        results["cuboid_volume_result"] = cuboid_volume_result
    
    if radius is not None:
        sphere_volume_result = calculate_sphere_volume(radius)
        results["sphere_volume_result"] = sphere_volume_result
    
    if mass_conversion_match:
        kilograms = float(mass_conversion_match.group(1))
        grams_result = convert_kilogram_to_gram(kilograms)
        results["mass_grams_result"] = grams_result

    if length_conversion_match1:
        meters = float(length_conversion_match1.group(1))
        centimeters_result = convert_meter_to_centimeter(meters)
        results["length_centimeters_result"] = centimeters_result

    if length_conversion_match2:
        kilometers = float(length_conversion_match2.group(1))
        meters_result = convert_kilometer_to_meter(kilometers)
        results["length_meters_result"] = meters_result

    if length_conversion_match3:
        inches = float(length_conversion_match3.group(1))
        feet_result = convert_inch_to_foot(inches)
        results["length_feet_result"] = feet_result

    if length_conversion_match4:
        feet = float(length_conversion_match4.group(1))
        meters_result = convert_foot_to_meter(feet)
        results["length_meters_result"] = meters_result

    if length_conversion_match5:
        feet = float(length_conversion_match5.group(1))
        centimeters_result = convert_foot_to_centimeter(feet)
        results["length_centimeters_result"] = centimeters_result

    if length_conversion_match6:
        inches = float(length_conversion_match6.group(1))
        centimeters_result = convert_inch_to_centimeter(inches)
        results["length_centimeters_result"] = centimeters_result

    if length_conversion_match7:
        inches = float(length_conversion_match7.group(1))
        meters_result = convert_inch_to_meter(inches)
        results["length_meters_result"] = meters_result

    if length_conversion_match8:
        centimeters = float(length_conversion_match8.group(1))
        meters_result = convert_centimeter_to_meter(centimeters)
        results["length_meters_result"] = meters_result

    if length_conversion_match9:
        centimeters = float(length_conversion_match9.group(1))
        feet_result = convert_centimeter_to_feet(centimeters)
        results["length_feet_result"] = feet_result

    if length_conversion_match0:
        centimeters = float(length_conversion_match0.group(1))
        feet_result = convert_centimeter_to_feet(centimeters)
        results["length_feet_result"] = feet_result

    if length_conversion_match10:
        centimeters = float(length_conversion_match10.group(1))
        meters_result = convert_centimeter_to_meter(centimeters)
        results["length_meters_result"] = meters_result

    if length_conversion_match11:
        meters = float(length_conversion_match11.group(1))
        kilometers_result = convert_meter_to_kilometer(meters)
        results["length_kilometers_result"] = kilometers_result

    if length_conversion_match12:
        feet = float(length_conversion_match12.group(1))
        inches_result = convert_feet_to_inch(feet)
        results["length_inches_result"] = inches_result

    if length_conversion_match13:
        centimeters = float(length_conversion_match13.group(1))
        inches_result = convert_centimeter_to_inch(centimeters)
        results["length_inches_result"] = inches_result

    if length_conversion_match14:
        inches = float(length_conversion_match14.group(1))
        centimeters_result = convert_inch_to_centimeter(inches)
        results["length_centimeters_result"] = centimeters_result

    if mass_conversion_match1:
        grams = float(mass_conversion_match1.group(1))
        kilograms_result = convert_gram_to_kilogram(grams)
        results["mass_kilograms_result"] = kilograms_result

    if length_conversion_match15:
        meters = float(length_conversion_match15.group(1))
        inches_result = convert_meter_to_inch(meters)
        results["length_inches_result"] = inches_result

    if length_conversion_match16:
        kilometers = float(length_conversion_match16.group(1))
        centimeters_result = convert_kilometer_to_centimeter(kilometers)
        results["length_centimeters_result"] = centimeters_result

    if physics_match1:
        distance = float(physics_match1.group(1))
        time_result = extract_values(user_input, time_pattern)
        if time_result:
            speed_result = calculate_speed(distance, time_result)
            results["speed_result"] = speed_result

    if physics_match2:
        mass = extract_values(user_input, mass_pattern)
        volume = extract_values(user_input, volume_pattern)
        if mass and volume:
            density_result = calculate_density(mass, volume)
            results["density_result"] = density_result

    if physics_match3:
        force = extract_values(user_input, force_pattern)
        area = extract_values(user_input, area_pattern)
        if force and area:
            pressure_result = calculate_pressure(force, area)
            results["pressure_result"] = pressure_result

    if physics_match4:
        mass = extract_values(user_input, mass_pattern)
        velocity = extract_values(user_input, velocity_pattern)
        if mass and velocity:
            energy_result = calculate_energy(mass, velocity)
            results["energy_result"] = energy_result

    if chemistry_match1:
        celsius = extract_values(user_input, chemistry_pattern1)
        if celsius:
            fahrenheit_result, kelvin_result = calculate_temperature_conversion(celsius)
            results["fahrenheit_result"] = fahrenheit_result
            results["kelvin_result"] = kelvin_result


    
    if not results:
        results["error"] = "Sorry, I couldn't extract relevant information from your input."
    
    return results

def generate_response(results):
    response = ""
    
    if "force_result" in results:
        response += f"\nTo calculate the force, we use the formula:\n"
        response += "Force = Mass * Acceleration"
        response += f"\nForce = {results['force_result']} Newtons"
    
    if "circle_area_result" in results:
        response += f"\nTo calculate the area of a circle, we use the formula:\n"
        response += "Area = π * Radius^2"
        response += f"\nArea = {results['circle_area_result']} square units"

    if "square_area_result" in results:
        response += f"\nTo calculate the area of a square, we use the formula:\n"
        response += "Area = side * side "
        response += f"\nArea = {results['square_area_result']} square units"
    
    if "rectangle_area_result" in results:
        response += f"\nTo calculate the area of a rectangle, we use the formula:\n"
        response += "Area = Length * Width"
        response += f"\nArea = {results['rectangle_area_result']} square units"
    
    if "velocity_result" in results:
        response += f"\nTo calculate velocity, we use the formula:\n"
        response += "Velocity = Initial Velocity + (Acceleration * Time)"
        response += f"\nVelocity = {results['velocity_result']} m/s"
    
    if "cube_volume_result" in results:
        response += f"\nTo calculate the volume of a cube, we use the formula:\n"
        response += "Volume = Side^3"
        response += f"\nVolume = {results['cube_volume_result']} cubic units"
    
    if "cuboid_volume_result" in results:
        response += f"\nTo calculate the volume of a cuboid, we use the formula:\n"
        response += "Volume = Length * Width * Height"
        response += f"\nVolume = {results['cuboid_volume_result']} cubic units"
    
    if "sphere_volume_result" in results:
        response += f"\nTo calculate the volume of a sphere, we use the formula:\n"
        response += "Volume = (4/3) * π * Radius^3"
        response += f"\nVolume = {results['sphere_volume_result']} cubic units"

    if "mass_grams_result" in results:
        response += f"\nTo convert kilograms to grams, we use the conversion:\n"
        response += "Grams = Kilograms * 1000"
        response += f"\nResult = {results['mass_grams_result']} grams"

    if "length_centimeters_result" in results:
        response += f"\nTo convert meters to centimeters, we use the conversion:\n"
        response += "Centimeters = Meters * 100"
        response += f"\nResult = {results['length_centimeters_result']} centimeters"

    if "length_meters_result" in results:
        response += f"\nTo convert kilometers to meters, inches to feet, feet to meters, feet to centimeters,\n"
        response += "inches to centimeters, inches to meters, or centimeters to meters, we use the respective conversions:\n"
        response += "Meters = Kilometers * 1000, Feet = Inches / 12, Meters = Feet * 0.3048, Centimeters = Feet * 30.48,\n"
        response += "Centimeters = Inches * 2.54, Meters = Inches * 0.0254, Meters = Centimeters * 0.01"
        response += f"\nResult = {results['length_meters_result']} meters"
    
    if "length_feet_result" in results:
        response += f"\nTo convert centimeters to feet, we use the conversion:\n"
        response += "Feet = Centimeters / 30.48"
        response += f"\nResult = {results['length_feet_result']} feet"
    
    if "length_feet_result" in results:
        response += f"\nTo convert centimeters to feet, we use the conversion:\n"
        response += "Feet = Centimeters / 30.48"
        response += f"\nResult = {results['length_feet_result']} feet"

    if "length_meters_result" in results:
        response += f"\nTo convert centimeters to meters, we use the conversion:\n"
        response += "Meters = Centimeters / 100"
        response += f"\nResult = {results['length_meters_result']} meters"

    if "length_kilometers_result" in results:
        response += f"\nTo convert meters to kilometers, we use the conversion:\n"
        response += "Kilometers = Meters / 1000"
        response += f"\nResult = {results['length_kilometers_result']} kilometers"

    if "length_inches_result" in results:
        response += f"\nTo convert feet to inches, centimeters to inches, or meters to inches, we use the respective conversions:\n"
        response += "Inches = Feet * 12, Inches = Centimeters / 2.54, Inches = Meters / 0.0254"
        response += f"\nResult = {results['length_inches_result']} inches"

    if "length_centimeters_result" in results:
        response += f"\nTo convert centimeters to inches, inches to centimeters, or kilometers to centimeters, we use the respective conversions:\n"
        response += "Inches = Centimeters / 2.54, Centimeters = Inches * 2.54, Centimeters = Kilometers * 100000"
        response += f"\nResult = {results['length_centimeters_result']} centimeters"

    if "mass_kilograms_result" in results:
        response += f"\nTo convert grams to kilograms, we use the conversion:\n"
        response += "Kilograms = Grams / 1000"
        response += f"\nResult = {results['mass_kilograms_result']} kilograms"

    if "speed_result" in results:
        response += f"\nTo calculate speed, we use the formula:\n"
        response += "Speed = Distance / Time"
        response += f"\nSpeed = {results['speed_result']} m/s"

    if "density_result" in results:
        response += f"\nTo calculate density, we use the formula:\n"
        response += "Density = Mass / Volume"
        response += f"\nDensity = {results['density_result']} kg/m^3"

    if "pressure_result" in results:
        response += f"\nTo calculate pressure, we use the formula:\n"
        response += "Pressure = Force / Area"
        response += f"\nPressure = {results['pressure_result']} N/m^2"

    if "energy_result" in results:
        response += f"\nTo calculate kinetic energy, we use the formula:\n"
        response += "Energy = 0.5 * Mass * Velocity^2"
        response += f"\nEnergy = {results['energy_result']} J"

    if "fahrenheit_result" in results and "kelvin_result" in results:
        response += f"\nTo convert Celsius to Fahrenheit and Kelvin, we use the conversions:\n"
        response += "Fahrenheit = (Celsius * 9/5) + 32, Kelvin = Celsius + 273.15"
        response += f"\nFahrenheit = {results['fahrenheit_result']}, Kelvin = {results['kelvin_result']}"

    if "error" in results:
        response += f"\n{results['error']}"
    
    return response

def get_parameter(input_text, parameter):
    parameter_match = re.search(f"{parameter} is (\d+(\.\d+)?)", input_text)
    if parameter_match:
        return

