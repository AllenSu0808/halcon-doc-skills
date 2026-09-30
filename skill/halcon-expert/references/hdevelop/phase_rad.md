# phase_rad (Operator)

## Name

`phase_rad` — Return the phase of a complex image in radians.

## Signature

`phase_rad(ImageComplex : ImagePhase : : )`

## Description

`phase_rad` computes the phase of a complex image in
radians. The following formula is used:
$$\textit{phase}=\text{atan2}(\textit{ima ginary part},\textit{r eal part}).$$

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`ImageComplex`** (input_object)  (multichannel-)image(-array) `→` object (complex)

Input image in frequency domain.

**`ImagePhase`** (output_object)  image(-array) `→` object (real)

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

`phase_rad` returns 2 (
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

`phase_deg`

## See also

`fft_image_inv`,
`fft_generic`,
`rft_generic`

## Module

Foundation
