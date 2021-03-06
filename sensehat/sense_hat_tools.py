import environ
import importlib
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

def get_cpu_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return float((temp.replace("temp=","")).replace("'C",""))

def get_sense_hat_data():

    sense_hat_data = {
        'pressure': 993,
        'temperature': 21,
        'temperatureFromPressure': 21,
        'humidity': 30,
        'pitch': 0,
        'roll': 0,
        'yaw': 0,
        'cpuTemp': 46
    }

    if not env.bool('IS_RASPBERRY_PI') or importlib.util.find_spec("sense_hat") is None:
        return sense_hat_data

    from sense_hat import SenseHat

    sense = SenseHat()

    sense_hat_data['pressure'] = sense.get_pressure()
    sense_hat_data['temperature'] = sense.get_temperature()
    sense_hat_data['temperatureFromPressure'] = sense.get_temperature_from_pressure()
    sense_hat_data['humidity'] = sense.get_humidity()
    sense_hat_data['pitch'] = sense.get_orientation()["pitch"]()
    sense_hat_data['roll'] = sense.get_orientation()["roll"]()
    sense_hat_data['yaw'] = sense.get_orientation()["yaw"]()
    sense_hat_data['cpuTemp'] = get_cpu_temp()

    return sense_hat_data

