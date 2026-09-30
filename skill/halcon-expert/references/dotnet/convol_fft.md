# ConvolFft (Operator)

## Name

`ConvolFft` — Multiply an image with a filter image in the frequency domain.

## Signature

`static void HOperatorSet.ConvolFft(HObject imageFFT, HObject imageFilter, out HObject imageConvol)`

`HImage HImage.ConvolFft(HImage imageFilter)`

## Description

As part of calculating the convolution of an image with a filter image,
`ConvolFft` multiplies the Fourier transform of an image
*`imageFFT`* with the Fourier transform of a
second image *`imageFilter`*, which serves as the filter.

According to the convolution theorem, the non-normalized
convolution of two images in pixel space can be obtained in three steps:

1. Transforming the images into frequency space using a
   Fourier transform (see, e.g., [`FftGeneric`](fft_generic.md)).
2. Multiplying one transformed image with the transformed filter image
   (pixel-wise).
3. Transforming the result back into pixel space using an inverse
   Fourier transform (see, e.g., [`FftGeneric`](fft_generic.md)).

The operator `ConvolFft` is used to perform the second step, i.e.,
*`imageFFT`* is pixel-wise multiplied with *`imageFilter`*.

## Attention

The filtering is always done on the entire image, i.e., the domain
of the image is ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`imageFFT`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (complex)

Complex input image.

**`imageFilter`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (real / complex)

Filter in frequency domain.

**`imageConvol`** (output_object)  image(-array) `→` [HImage](HImage.md) (complex)

Result in the frequency domain.

## Example (HDevelop)

```
gen_highpass(Highpass,0.2,'n','dc_edge',Width,Height)
fft_generic(Image,ImageFFT,'to_freq',-1,'none','dc_edge','complex')
convol_fft(ImageFFT,Highpass,ImageConvol)
fft_generic(ImageConvol,ImageResult,'from_freq',1,'none','dc_edge','byte')
```

## Result

`ConvolFft` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`FftImage`,
`FftGeneric`,
`RftGeneric`,
`GenHighpass`,
`GenLowpass`,
`GenBandpass`,
`GenBandfilter`

## Possible Successors

`PowerByte`,
`PowerReal`,
`PowerLn`,
`FftImageInv`,
`FftGeneric`,
`RftGeneric`

## Alternatives

`ConvolGabor`

## See also

`GenGabor`,
`GenHighpass`,
`GenLowpass`,
`GenBandpass`,
`ConvolGabor`,
`FftImageInv`

## Module

Foundation
