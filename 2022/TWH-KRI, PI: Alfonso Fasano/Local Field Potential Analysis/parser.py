from asyncio.windows_events import NULL
import json

from patient import *
    
def parse(fn):
    with open(fn) as fn:
        d = json.load(fn)

    for i in d:
        # 1. arguments for Patient class
        if i == 'PatientInformation':
            # from PatientInformation: name/surname, gender, diagnosis, implant_date
            # from LeadConfiguration: hemisphere, lead_location
            v = d[i]['Initial']
            first_name = v['PatientFirstName']
            last_name = v['PatientLastName']
            gender = v['PatientGender']
            diagnosis = v['Diagnosis']
            patient = Patient(first_name, last_name, gender, diagnosis, NULL, NULL)
        elif i == 'DeviceInformation':   
            v = d[i]['Initial']
            implant_date = v['ImplantDate']
            patient.implant_date = implant_date
        # 2. arguments for Session class
        elif i == 'EventSummary':
            # from EventSummary: start/end date, hemisphere
            start = d[i]['SessionStartDate']
            end = d[i]['SessionEndDate']
            hemisphere = d[i]['LfpAndAmplitudeSummary'][0]['Hemisphere']
            session = Session(start, end, hemisphere)
            patient.session = session
        # 3. arguments for DiagnosticData class
        elif i == 'DiagnosticData':
            # from DiagnosticData: (LFPTrendLogs: hemisphere): date/time, local_field_potential, amplitude
            v = d[i]['LFPTrendLogs'][hemisphere] # this needs to go one level deeper and iterate
            for v1 in v:
                for v2 in range(0,len(v[v1])):
                    date = v[v1][v2]['DateTime']
                    local_field_potential = v[v1][v2]['LFP']
                    amplitude = v[v1][v2]['AmplitudeInMilliAmps']
                    diagnostic_data = DiagnosticData(date, local_field_potential, amplitude)
                    patient.add_data(diagnostic_data)
            # debugging
            print(patient)
