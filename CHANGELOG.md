# Changelog

### [1.3.0] - 2020-12-03
-  **Added:** Encoding and decoding PNG (RGB Mode)
-  **Added:** Images modes optional argument. `[-m --mode {1, L, P, RGB, RGBA}]`. Current available modes;
    - png: {L, RGB} / "RGB" is the default
    - gif: {L} / "L" is the default

### [1.2.0.rc] - 2020-12-02
-  **Added:** Encoding and decoding PNG (L Mode)

### [1.1.0.dev1] - 2020-11-28

-  **Added:** Encoding and decoding WAV

### [1.0.0.dev1] - 2020-11-25

- **Changed:** The output file will be saved in the same folder as the input file.
- **Changed:** Now, there is no byte difference between the embedded file and the extracted file.
- **Changed:** Code refactoring

### [0.1.0.dev1] - 2020-11-24

- **Added:** Encoding and decoding grayscale GIF (L mode)