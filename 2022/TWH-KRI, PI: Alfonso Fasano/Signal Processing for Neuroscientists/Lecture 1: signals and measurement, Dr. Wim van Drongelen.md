# Lecture 1: signals and measurement, Dr. Wim van Drongelen
[Signal Processing for Neuroscientists by Wim van Drongelen](https://faculty.washington.edu/seattle/brain-physics/textbooks/drongelen.pdf)

## Chapter 1: introduction
**Signal processing:** "to enhance signal components in noisy measurements or to transform measured data sets such that new features become visible"

"Golden trio" of signal processing:
1. Signal averaging (chapter 4)
2. Fourier analysis (chapter 5-7)
3. Filtering (chapter 10-13)

**1.5 Analog to digital conversion (A/D converter or ADC)**
- Signals are analog (continuous amplitude and time) but computers read digital (discrete amplitude and time) 
    - i.e. signals cannot be read by a computer with infinite resolution
- To process analog signals digitally, computers read collect measurements between time intervals and use ADC on amplitude
![](https://i.imgur.com/FeLoG2b.png =500x)

**1.6 Moving signals to MATLAB analysis environment**
1. **Reformat filetype** to appropriate for reading
    - Can be done in MATLAB using: ```fopen``` and ```fread``` commands
    - Header and data can be in same file or separate, if same file then **only store data in a text file** (.txt)
2. **Load file** to MATLAB using:
    - If working with **action potentials**: ```load Action_
Potentials.txt -ascii```
    - If working with **electroencephalography (EEG)**:
    ``` MATLAB
    % pr1_1.m
    sr=400; % Sample Rate
    Nyq_freq=sr/2; % Nyquist Frequency
    fneeg=input(‘Filename (with path and extension) :’, ‘s’);
    t=input(‘How many seconds in total of EEG ? : ‘);
    ch=input(‘How many channels of EEG ? : ‘);
    le=t*sr; % Length of the Recording
    fi d=fopen(fneeg, ‘r’, ‘l’); % *) Open the file to read(‘r’) and
    little-endian (‘l’)
    EEG=fread(fi d,[ch,le],’int16’); % Read Data -> EEG Matrix
    fclose (‘all’); % Close all open Files
    ```
    
    ```plot(-EEG(1,:)), plot(-EEG(16,:)) % Both display noisy EEG channels```

## Chapter 2: data acquisition
"Data acquisition **necessarily precedes** signal processing. In any recording setup, the devices that are interconnected and coupled to the biological process form **a so-called measurement chain**."

**2.2 The measurement chain**
![](https://i.imgur.com/CioDPTm.png =500x)

**2.2.1 Analog components**
"When connecting equipment, one has to follow the rule of **low output impedance–high input impedance.**"
- Equation calculating biopotential: i=V/(R~i~+R~o~) shows that to measure V and minimize current drawn from preparation, **R~i~+R~o~ must be large**. 
- Equation relating oscilloscope potential (V') to real potential (V): V'=(R~i~/(R~i~+R~o~))V shows that **V' is close to V if R~i~>>R~o~** as that factor approaches 1.

1. **Preamplifier:** amplifies weak signal to strong signal such that electrode impedence (or noise) becomes negligible/resolved
2. **Amplifier:** increases signal amplitude to match range of analog to digital converter (but increases noise amplitude simultaneously, which needs to be taken care of by filters)
3. **Band filter:** filters out signals not within a specified band of frequencies
4. **Notch filter:** filters out signals within a specified band of frequencies
5. **Anti-alias filter:** reduces aliasing that occurs when sampling the signal
6. **S/H (sample hold):** stores signal being recorded constant for an amount of time (when we have multiple channels)
7. **MUX (multiplexer):** passes on signals stored by S/H to the ADC in order (such that a signal is passed in and finishes converting before another signal is)

**2.2.2 ADC (analog to digital conversion):**
- ADC converts a **continuous** signal's time and amplitude **discrete** time and amplitude 
- Time interval (T~s~) or sample frequency (F~s~=1/T~s~)
  ![](https://i.imgur.com/cztF6sp.png =500x) 
  ![](https://i.imgur.com/XCyy1fg.png =500x)
  
**Figure 2.5 code:**
  ``` MATLAB
    % pr2_1.m
    % Aliasing
    % example signal
    t=0:0.001:1; % 1 sec divided into ms steps
    f=20; % Frequency in Hertz
    signal=sin(2*pi*f*t);
    % Simulate different sample rates and plot
    fi gure
    for skip=2:5:50;
     plot(t,signal,’r’); hold; % The Original Signal
     plot(t(1:skip:1000),signal(1:skip:1000));
     tt=[‘Sine’ num2str(f) ‘ Hz: space bar to continue: SAMPLE RATE = ‘
     num2str(1000/skip)];
     title(tt);
     drawnow
     pause;
     clf;
    end;
    ```
