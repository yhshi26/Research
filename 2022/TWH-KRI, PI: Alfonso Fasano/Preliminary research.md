# Preliminary research
## Hardware and software
- [Medtronic](https://www.medtronic.com/ca-en/index.html) is a medical device company
- Medtronic's [Percept PC Neurostimulator](https://www.medtronic.com/ca-en/healthcare-professionals/products/neurological/deep-brain-stimulation-systems/percept-pc.html) is used in **Deep Brain Stimulation (DBS) therapy** 
    - Comes with software to record and keep track of objective data: patient programmer, clinician programmer
    - **Patient programmer** is used by patients to record different things: took medication, start exercise, dyskenisia, etc.
        - "DBS patient programmer is enhanced so patients can more easily and conveniently engage with their therapy", they "can easily adjust and customize their therapy to their desired activities"
    - **Clinician programmer** is used by clinicians to keep track of events over time and correlate events with brain signals

### Additional on software
- **Brainsense survey**
- **Event (capturing) function**
    - Patient programmer: 4 options selected specifically for patient's concerns
    - Clinician programmer: data on 4 options recorded by patient programmer

## Deep Brain Stimulation (DBS) therapy
- For Parkinson's disease, essential tremor, dystonia and epilepsy
- Involves implanting of DBS leads (electrodes) into the **subthalamic nucleus** of the thalamus 
    - The subthalamic nucleus has a recognisable, periodic on/off high activity behaviour that, when reached by continuously recording leads helps neurosurgeons implant the DBS leads in the correct location    

## 1. Using Beta as a marker of sleep time vs. bed time
- Patients monitored simultaneously by implanted DBS lead local field potential (LFP) recordings in subthalamic nucleus and fitbit movement recordings
    - Fitbit records movement (if no movement, sleep but if movement not sleep)
- Data that will be collected in a (weekly?) survey filled by patients:
    - REM BFH disease (RBD) (acting out dreams)
    - Sleep quality
    - Daytime sleepiness
- **Are fluctuations in DBS lead beta recordings indicative of something during sleep?**
    - E.g. sleep phases (which rotate from stage 1-2-3 to REM)

## 2. Beta vs. "lesion effects"
- Probably an easier project
- In patients with Parkinson's disease, essential tremor, dystonia and epilepsy, the **subthalamic nucleus is overactive**
    - When the DBS lead is impanted in the subthalamic nucleus, neuron activity in the area is **temporarily reduced due** to the mechanical shock
        - This results in improved symptoms for a period that varies by patient for a certain amount of time
    - Then, the neurons slowly regain overactivity, symptoms return, and after 1.5 months **stimulation begins**
- While stimulation gives the idea of increasing activity, in DBS it is really decreasing activity by confusing neurons with higher electric currents (DBS is also called **high-frequency simulation or HFS**)
    - By confusing neurons we really mean disrupting their transmission (which we have too much of)
- **Can we look at beta DBS lead recordings to predict when "lesion effects" wear off?**
