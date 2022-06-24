from asyncio.windows_events import NULL
import json

from patient import *
    
def parse(fn):
    with open(fn) as fn:
        d = json.load(fn)

    for v in d.values():
        # 1. arguments for Patient class
        if v == 'PatientInformation':
            # from PatientInformation: name/surname, gender, diagnosis, implant_date
            # from LeadConfiguration: hemisphere, lead_location
            v = v['Initial']
            first_name = v['PatientFirstName']
            last_name = v['PatientLastName']
            gender = v['PatientGender']
            diagnosis = v['Diagnosis']
            patient = Patient(first_name, last_name, gender, diagnosis, NULL, NULL)
        elif v == 'DeviceInformation':   
            v = v['Initial']
            implant_date = v['ImplantDate']
            patient.implant_date = implant_date
        # 2. arguments for Session class
        elif v == 'EventSummary':
            # from EventSummary: start/end date, hemisphere
            start = v['SessionStartDate']
            end = v['SessionEndDate']
            hemisphere = v['LfpAndAmplitudeSummary']['Hemisphere']
            session = Session(start, end, hemisphere)
            patient.session = session
        # 3. arguments for DiagnosticData class
        elif v == 'DiagnosticData':
            # from DiagnosticData: (LFPTrendLogs: hemisphere): date/time, local_field_potential, amplitude
            v = v['LFPTrendLogs'][hemisphere] # this needs to go one level deeper and iterate
            for v1 in v.values():
                date = v1['DateTime']
                local_field_potential = v1['LFP']
                amplitude = v1['AmplitudeInMilliAmps']
                diagnostic_data = DiagnosticData(date, local_field_potential, amplitude)
                patient.add_data(patient, diagnostic_data)
