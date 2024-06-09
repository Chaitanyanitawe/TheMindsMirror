# EEG Data Format

The data is stored in a simple text format with the following fields:

- `[id]`: Numeric identifier for reference purposes.
- `[event]`: Integer identifier to distinguish the same event captured at different brain locations. Used only by multichannel devices.
- `[device]`: Two-character string to identify the device used to capture the signals.
- `[channel]`: String identifying the 10/20 brain location of the signal.
- `[code]`: Integer identifying the digit being thought/seen.
- `[size]`: Integer indicating the size in number of values captured in the 2 seconds of this signal.
- `[data]`: Comma-separated set of numbers representing the time-series amplitude of the signal.

## Device Codes

- **MindWave (MW)**: "FP1"
- **Interaxon Muse (MU)**: "TP9,"FP1,"FP2,"TP10"

## Code Values

- Digit codes: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
- `-1`: Random captured signals not related to any of the digits.

## Size Conversion

The size field indicates the number of values captured in the 2 seconds of the signal, considering the specific sampling rate of each device:

- MindWave (MW): Close to 512Hz
- Interaxon Muse (MU): 220Hz

## Data Precision

- MindWave (MW) and Interaxon Muse (MU) use integers to represent the electrical potential captured from the brain.

