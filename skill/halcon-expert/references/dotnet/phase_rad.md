# PhaseRad (Operator)

## Name

`PhaseRad` — Return the phase of a complex image in radians.

## Signature

`static void HOperatorSet.PhaseRad(HObject imageComplex, out HObject imagePhase)`

`HImage HImage.PhaseRad()`

## Description

`PhaseRad` computes the phase of a complex image in
radians. The following formula is used:
$$\textit{phase}=\text{atan2}(\textit{ima ginary part},\textit{r eal part}).$$

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`imageComplex`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (complex)

Input image in frequency domain.

**`imagePhase`** (output_object)  image(-array) `→` [HImage](HImage.md) (real)

Phase of the image in radians.

## Example (C)

```
read_image(&Image,"monkey");
disp_image(Image,WindowHandle);
fft_image(Image,&FFT);
phase_rad(FFT,&Phase);
disp_image(Phase,WindowHandle);
```

## Result

`PhaseRad` returns 2 (
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

`PhaseDeg`

## See also

`FftImageInv`,
`FftGeneric`,
`RftGeneric`

## Module

Foundation
