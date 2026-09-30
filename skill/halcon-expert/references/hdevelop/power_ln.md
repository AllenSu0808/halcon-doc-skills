# power_ln (Operator)

## Name

`power_ln` — Return the power spectrum of a complex image.

## Signature

`power_ln(Image : ImageResult : : )`

## Description

`power_ln` computes the power spectrum from the real and
imaginary parts of a Fourier-transformed image (see
[`fft_image`](fft_image.md)), i.e., the modulus of the frequencies.
Additionally, the natural logarithm is applied to the result. The
result image is of type `real`. The following formula is
used:
$$\ln\left(\sqrt{realpart^2 + imaginarypart^2}\right)$$ ![figure](../assets/cabb6519f90a9fab.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (complex)

Input image in frequency domain.

**`ImageResult`** (output_object)  image(-array) `→` object (real)

Power spectrum of the input image.

## Example (C)

```
read_image(&Image,"monkey");
disp_image(Image,WindowHandle);
fft_image(Image,&FFT);
power_ln(FFT,&Power);
disp_image(Power,WindowHandle);
```

## Result

`power_ln` returns 2 (
H_MSG_TRUE)
if the image is of correct
type. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`fft_image`,
`fft_generic`,
`rft_generic`,
`convol_fft`,
`convol_gabor`

## Possible Successors

`disp_image`,
`convert_image_type`,
`scale_image`

## Alternatives

`abs_image`,
`convert_image_type`,
`power_real`,
`power_byte`

## See also

`fft_image`,
`fft_generic`,
`rft_generic`

## Module

Foundation
