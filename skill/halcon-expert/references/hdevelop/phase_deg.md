# phase_deg (Operator)

## Name

`phase_deg` — Return the phase of a complex image in degrees.

## Signature

`phase_deg(ImageComplex : ImagePhase : : )`

## Description

`phase_deg` computes the phase of a complex image in
degrees. The following formula is used:
$$\text{phase} = \frac{90}{\pi}\ \mathrm{atan2}(\mathrm{imaginary\ part},\ \mathrm{real\ part})$$ ![figure](../assets/9f63bdab61197a78.svg)
Hence, *`ImagePhase`* contains half the phase angle. For
negative phase angles, 180 is added.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`ImageComplex`** (input_object)  (multichannel-)image(-array) `→` object (complex)

Input image in frequency domain.

**`ImagePhase`** (output_object)  image(-array) `→` object (direction)

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

`phase_deg` returns 2 (
H_MSG_TRUE)
if the image is of correct
type. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`fft_image`,
`fft_generic`,
`rft_generic`

## Possible Successors

`disp_image`

## Alternatives

`phase_rad`

## See also

`fft_image_inv`

## Module

Foundation
