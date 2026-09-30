# PowerByte (Operator)

## Name

`PowerByte` — Return the power spectrum of a complex image.

## Signature

`static void HOperatorSet.PowerByte(HObject image, out HObject powerByte)`

`HImage HImage.PowerByte()`

## Description

`PowerByte` computes the power spectrum from the real and
imaginary parts of a Fourier-transformed image (see
[`FftImage`](fft_image.md)), i.e., the modulus of the frequencies. The
result image is of type *"byte"*. The following formula is
used:
$$\sqrt{realpart^2 + imaginarypart^2}.$$ ![figure](../assets/832259183d3b7979.svg)

Please note, that resulting gray values that exceed the value of 255
are clipped at 255 because of the resulting image type *"byte"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (complex)

Input image in frequency domain.

**`powerByte`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte)

Power spectrum of the input image.

## Example (C)

```
read_image(&Image,"monkey");
disp_image(Image,WindowHandle);
fft_image(Image,&FFT);
power_byte(FFT,&Power);
disp_image(Power,WindowHandle);
```

## Result

`PowerByte` returns 2 (
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

`DispImage`

## Alternatives

`AbsImage`,
`ConvertImageType`,
`PowerReal`,
`PowerLn`

## See also

`FftImage`,
`FftGeneric`,
`RftGeneric`

## Module

Foundation
