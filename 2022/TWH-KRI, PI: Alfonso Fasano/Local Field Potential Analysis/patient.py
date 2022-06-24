from asyncio.windows_events import NULL
from contextlib import nullcontext
import imp

class Patient:
  def __init__(self, first_name, last_name, gender, diagnosis, implant_date, session):
    self.first_name = first_name
    self.last_name = last_name
    self.gender = gender
    self.diagnosis = diagnosis
    self.implant_date = implant_date
    self.session = session
    self.diagnostic_data = []
  
  def add_data(diagnostic_data):
    self.diagnostic_data.append(diagnostic_data)

class Session:
  def __init__(self, start, end, hemisphere):
    self.start = start
    self.end = end
    self.hemisphere = hemisphere

class DiagnosticData:
  def __init__(self, date, local_field_potential, amplitude):
    self.date = date
    self.local_field_potential = local_field_potential
    self.amplitude = amplitude