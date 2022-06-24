from asyncio.windows_events import NULL
import json

from patient import *

patients = []
    
def parse(fn):
    with open(fn) as fn:
        d = json.load(fn)

    for i in d:
        # 1. arguments for Patient class
        if i == 'PatientInformation':
            # from PatientInformation: name/surname, gender, diagnosis, implant_date
            # from LeadConfiguration: hemisphere, lead_location
            v = d[i]['Initial']
            patient = Patient(v['PatientFirstName'], v['PatientLastName'], v['PatientGender'], v['Diagnosis'], NULL, NULL)
        elif i == 'DeviceInformation':   
            v = d[i]['Initial']
            patient.implant_date = v['ImplantDate']
        # 2. arguments for Session class
        elif i == 'EventSummary':
            # from EventSummary: start/end date, hemisphere
            hemisphere =  d[i]['LfpAndAmplitudeSummary'][0]['Hemisphere']
            session = Session(d[i]['SessionStartDate'], d[i]['SessionEndDate'], hemisphere)
            patient.session = session
        # 3. arguments for DiagnosticData class
        elif i == 'DiagnosticData':
            # from DiagnosticData: (LFPTrendLogs: hemisphere): date/time, local_field_potential, amplitude
            v = d[i]['LFPTrendLogs'][hemisphere] # this needs to go one level deeper and iterate
            for v1 in v:
                for v2 in range(0,len(v[v1])):
                    diagnostic_data = DiagnosticData(v[v1][v2]['DateTime'], v[v1][v2]['LFP'], v[v1][v2]['AmplitudeInMilliAmps'])
                    patient.add_data(diagnostic_data)
            patients.append(patient)
            # debugging
            # print(patient)  
