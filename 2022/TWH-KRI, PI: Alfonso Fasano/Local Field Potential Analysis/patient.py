from asyncio.windows_events import NULL
from contextlib import nullcontext
import imp

patients = []

class Patient:
    def __init__(self, first_name, last_name, gender, diagnosis, implant_date):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.diagnosis = diagnosis
        self.implant_date = implant_date
        self.sessions = []
        self.left_diagnostic_data = []
        self.right_diagnostic_data = []
        self.graphs = []

        patients.append(self)

    def __repr__(self):
        return "first name: %s, last name: %s, gender: %s, diagnosis: %s, implant date: %s" % (self.first_name, self.last_name, self.gender, self.diagnosis, self.implant_date)

class Session:
    def __init__(self, start, end, hemisphere):
        self.start = start
        self.end = end
        self.hemisphere = hemisphere

class DiagnosticData:
    def __init__(self, date, local_field_potential, amplitude):
        date_time = date.split('T')
        date = date_time[0]
        time = date_time[1].split('Z')[0].split(':')

        self.date = str(date) + "-" + str(time[0]) + "-" + str(time[1]) + "-" + str(time[2])
        self.local_field_potential = local_field_potential
        self.amplitude = amplitude
