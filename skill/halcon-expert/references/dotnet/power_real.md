# PowerReal (Operator)

## Name

`PowerReal` — Return the power spectrum of a complex image.

## Signature

`static void HOperatorSet.PowerReal(HObject image, out HObject imageResult)`

`HImage HImage.PowerReal()`

## Description

`PowerReal` computes the power spectrum from the real and
imaginary parts of a Fourier-transformed image (see
[`FftImage`](fft_image.md)), i.e., the modulus of the frequencies. The
result image is of type `real`. The following formula is
used:
$$\sqrt{realpart^2 + imaginarypart^2}.$$ ![figure](../assets/832259183d3b7979.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (complex)

Input image in frequency domain.

**`imageResult`** (output_object)  image(-array) `→` [HImage](HImage.md) (real)

Power spectrum of the input image.

## Example (C)

```
read_image(&Image,"monkey");
disp_image(Image,WindowHandle);
fft_image(Image,&FFT);
power_real(FFT,&Power);
disp_image(Power,WindowHandle);
```

## Result

`PowerReal` returns 2 (
H_MSG_TRUE)
if the image is of correct
type. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`FftImage`,
`FftGeneric`,
`RftGeneric`,
`ConvolFft`,
`ConvolGabor`

## Possible Successors

`DispImage`,
`ConvertImageType`,
`ScaleImage`

## Alternatives

`AbsImage`,
`ConvertImageType`,
`PowerByte`,
`PowerLn`

## See also

`FftImage`,
`FftGeneric`,
`RftGeneric`

## Module

Foundation
