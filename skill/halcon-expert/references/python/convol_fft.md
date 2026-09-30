# convol_fft (Operator)

## Name

`convol_fft` — Multiply an image with a filter image in the frequency domain.

## Signature

`def convol_fft(image_fft: HObject, image_filter: HObject) -> HObject`

## Description

As part of calculating the convolution of an image with a filter image,
`convol_fft` multiplies the Fourier transform of an image
*`image_fft`* with the Fourier transform of a
second image *`image_filter`*, which serves as the filter.

According to the convolution theorem, the non-normalized
convolution of two images in pixel space can be obtained in three steps:

1. Transforming the images into frequency space using a
   Fourier transform (see, e.g., [`fft_generic`](fft_generic.md)).
2. Multiplying one transformed image with the transformed filter image
   (pixel-wise).
3. Transforming the result back into pixel space using an inverse
   Fourier transform (see, e.g., [`fft_generic`](fft_generic.md)).

The operator `convol_fft` is used to perform the second step, i.e.,
*`image_fft`* is pixel-wise multiplied with *`image_filter`*.

## Attention

The filtering is always done on the entire image, i.e., the domain
of the image is ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`image_fft`** (input_object)  (multichannel-)image(-array) `→` HObject (complex)

Complex input image.

**`image_filter`** (input_object)  (multichannel-)image `→` HObject (real / complex)

Filter in frequency domain.

**`image_convol`** (output_object)  image(-array) `→` HObject (complex)

Result in the frequency domain.

## Example (HDevelop)

```
gen_highpass(Highpass,0.2,'n','dc_edge',Width,Height)
fft_generic(Image,ImageFFT,'to_freq',-1,'none','dc_edge','complex')
convol_fft(ImageFFT,Highpass,ImageConvol)
fft_generic(ImageConvol,ImageResult,'from_freq',1,'none','dc_edge','byte')
```

## Result

`convol_fft` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`fft_image`,
`fft_generic`,
`rft_generic`,
`gen_highpass`,
`gen_lowpass`,
`gen_bandpass`,
`gen_bandfilter`

## Possible Successors

`power_byte`,
`power_real`,
`power_ln`,
`fft_image_inv`,
`fft_generic`,
`rft_generic`

## Alternatives

`convol_gabor`

## See also

`gen_gabor`,
`gen_highpass`,
`gen_lowpass`,
`gen_bandpass`,
`convol_gabor`,
`fft_image_inv`

## Module

Foundation
