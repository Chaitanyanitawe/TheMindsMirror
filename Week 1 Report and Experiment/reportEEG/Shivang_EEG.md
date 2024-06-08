# EEG Basics

## What is EEG?
An EEG tracks and records brain wave patterns. Small flat metal discs called electrodes are attached to your scalp with wires. The electrodes analyze the electrical impulses in your brain and send signals to a computer that records the results.

The electrical impulses in an EEG recording look like wavy lines with peaks and valleys. These lines allow doctors to quickly assess whether there are abnormal patterns. Irregularities may be a sign of seizures or other brain disorders.

To simply speak EEG is just a time series data that is recorded by detecting electrical signals from the skull.

## Why is an EEG performed?
EEGs have been used to detect problems in the electrical activity of the brain that are associated with certain brain disorders. The measurements given by an EEG are used to confirm or rule out various conditions, including:

    1. Seizure disorders (such as epilepsy)
    2. Head injury
    3. Encephalitis (inflammation of the brain)
    4. Brain tumor
    5. Encephalopathy (disease that causes brain dysfunction)
    6. Sleep disorders
    7. Stroke
    8. Dementia

When someone is in a coma, an EEG may be performed to determine their level of brain activity. The test can also be used to monitor activity during brain surgery.

## International 10-20 system
The 10–20 system or International 10–20 system is an internationally recognized method to describe and apply the location of scalp electrodes in the context of an EEG exam, polysomnograph sleep study, or voluntary lab research. This method was developed to maintain standardized testing methods ensuring that a subject's study outcomes (clinical or research) could be compiled, reproduced, and effectively analyzed and compared using the scientific method. The system is based on the relationship between the location of an electrode and the underlying area of the brain, specifically the cerebral cortex.

## Naming of the Electrodes
The electrodes at the centre are marked with lower numbers and the electrodes at the boundaries are marked with higher numberes.

## How EEG is measured?
It is done using a differential amplifier that takes two inputs and give their diffrence as output

### How good is it at filtering (CMRR)?
The Common-Mode Rejection Ratio (CMRR) measures a differential amplifier's ability to suppress or reduce the common-mode voltage (VCM), which is a voltage that remains constant on both the positive and negative inputs of the amplifier. At the same time, it amplifies the differential mode voltage (VDM), which is the voltage difference between the positive and negative inputs 


## Analyzing information (ft. Montages)
### Bipolar Montages
In a bipolar montage, each electrode's voltage is linked and compared to an adjacent one to form a chain of electrodes. There are multiple types, but the most common bipolar montage is the double banana, in which each electrode is linked and compared to the one behind it

### Referential or Common Reference Montage
Referential montages compare all of the electrodes to single reference point. This reference point can be any number of things, but most commonly you'll see it being the average of the voltage of all electrodes (termed an average montage), or the electrically silent auricle of the ear. The referential montages used across this site are generally all of the average type.

### Laplacian Montage
In Laplace montage,we compare one electrode position to an average of its nearest neighbours which helps avoid reference contamination.
Laplacian montages are not good for broad electrical fields.
(K-complex) which are obsereved during sleeping.

## Waveforms in EEG
1. Delta Waves
2. Theta Waves
3. Alpha Waves
4. Beta Waves
5. Gamma Waves

## Signal Processing
1. Low-pass filter: Allows only signal below a certain threshold 
2. High-pass filter: Allows only signal above a certain threshold 
3. 60-Hz notch filter: Allows only signals from slightly above or below the 60 Hz to pass.
