# PhaseDeg (Operator)

## Name

`PhaseDeg` — Return the phase of a complex image in degrees.

## Signature

`static void HOperatorSet.PhaseDeg(HObject imageComplex, out HObject imagePhase)`

`HImage HImage.PhaseDeg()`

## Description

`PhaseDeg` computes the phase of a complex image in
degrees. The following formula is used:
$$\text{phase} = \frac{90}{\pi}\ \mathrm{atan2}(\mathrm{imaginary\ part},\ \mathrm{real\ part})$$ ![figure](../assets/9f63bdab61197a78.svg)
Hence, *`imagePhase`* contains half the phase angle. For
negative phase angles, 180 is added.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`imageComplex`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (complex)

Input image in frequency domain.

**`imagePhase`** (output_object)  image(-array) `→` [HImage](HImage.md) (direction)

Phase of the image in degrees.

## Example (C)

```
read_image(&Image,"monkey");
disp_image(Image,WindowHandle);
fft_image(Image,&FFT);
phase_deg(FFT,&Phase);
disp_image(Phase,WindowHandle);
```

## Result

`PhaseDeg` returns 2 (
H_MSG_TRUE)
if the image is of correct
type. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`FftImage`,
`FftGeneric`,
`RftGeneric`

## Possible Successors

`DispImage`

## Alternatives

`PhaseRad`

## See also

`FftImageInv`

## Module

Foundation
