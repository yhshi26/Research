from asyncio.windows_events import NULL
import json

from patient import *

patients = []
    
def parse(fn):
    with open(fn) as fn:
        d = json.load(fn)

    for i in d:
        if i == 'PatientInformation':
            # from PatientInformation: name/surname, gender, diagnosis, implant_date
            # from LeadConfiguration: hemisphere, lead_location
            v = d[i]['Initial']
            patient = Patient(v['PatientFirstName'], v['PatientLastName'], v['PatientGender'], v['Diagnosis'], NULL)
        elif i == 'DeviceInformation':   
            v = d[i]['Initial']
            patient.implant_date = v['ImplantDate']
        elif i == 'EventSummary':
            # from EventSummary: start/end date, hemisphere
            left =  d[i]['LfpAndAmplitudeSummary'][0]['Hemisphere'] 
            right =  d[i]['LfpAndAmplitudeSummary'][1]['Hemisphere']
            left_session = Session(d[i]['SessionStartDate'], d[i]['SessionEndDate'], left)
            right_session = Session(d[i]['SessionStartDate'], d[i]['SessionEndDate'], right)
            patient.sessions.append(left_session)
            patient.sessions.append(right_session)
        elif i == 'DiagnosticData':
            # from DiagnosticData: (LFPTrendLogs: hemisphere): date/time, local_field_potential, amplitude
            v = d[i]['LFPTrendLogs'][left] # this needs to go one level deeper and iterate
            for v1 in v:
                for v2 in range(0,len(v[v1])):
                    left_diagnostic_data = DiagnosticData(v[v1][v2]['DateTime'], v[v1][v2]['LFP'], v[v1][v2]['AmplitudeInMilliAmps'])
                    patient.left_diagnostic_data.append(left_diagnostic_data)
            v = d[i]['LFPTrendLogs'][right] # this needs to go one level deeper and iterate
            for v1 in v:
                for v2 in range(0,len(v[v1])):
                    right_diagnostic_data = DiagnosticData(v[v1][v2]['DateTime'], v[v1][v2]['LFP'], v[v1][v2]['AmplitudeInMilliAmps'])
                    patient.right_diagnostic_data.append(right_diagnostic_data)
            patients.append(patient)
