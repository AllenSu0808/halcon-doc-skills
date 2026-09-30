# CorrelationFft (Operator)

## Name

`CorrelationFft` — Multiply one image with the complex conjugate of another image in the
frequency domain.

## Signature

`static void HOperatorSet.CorrelationFft(HObject imageFFT1, HObject imageFFT2, out HObject imageCorrelation)`

`HImage HImage.CorrelationFft(HImage imageFFT2)`

## Description

As part of calculating the correlation between two images,
`CorrelationFft` multiplies the Fourier transform of the first image
*`imageFFT1`* with the complex conjugate of the Fourier-transformed
second image *`imageFFT2`*.

According to the correlation theorem, the non-normalized
correlation of two images in pixel space can be obtained in three steps:

1. Transforming the images into frequency space using a
   Fourier transform (see, e.g., [`FftGeneric`](fft_generic.md)).
2. Multiplying one transformed image with the complex conjugate of
   the other transformed image (pixel-wise).
3. Transforming the result back into pixel space using an
   inverse Fourier transform (see, e.g., [`FftGeneric`](fft_generic.md)).

The operator `CorrelationFft` is used to perform the second step,
i.e., *`imageFFT1`* is pixel-wise multiplied with the complex
conjugate of *`imageFFT2`*.

It should be noted that in order to achieve a correct scaling of the
correlation in the spatial domain, the operators
[`FftGeneric`](fft_generic.md) or [`RftGeneric`](rft_generic.md) with
`norm` = *"none"* must be used for the forward
transform (step 1) and [`FftGeneric`](fft_generic.md) or [`RftGeneric`](rft_generic.md) with
`norm` = *"n"* for the reverse transform (step 3).
If *`imageFFT1`* and *`imageFFT2`* contain the same number
of images, the corresponding images are multiplied pairwise.
Otherwise, *`imageFFT2`* must contain only one single image.
In this case, the multiplication is performed for each image of
*`imageFFT1`* with *`imageFFT2`*.

## Attention

The filtering is always performed on the entire image, i.e., the domain
of the image is ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`imageFFT1`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (complex)

Fourier-transformed input image 1.

**`imageFFT2`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (complex)

Fourier-transformed input image 2.

Number of elements:
ImageFFT2 == ImageFFT1 || ImageFFT2 == 1

**`imageCorrelation`** (output_object)  image(-array) `→` [HImage](HImage.md) (complex)

Result in the frequency domain.

## Example (HDevelop)

```
* Compute the auto-correlation of an image.
get_image_size(Image,Width,Height)
rft_generic(Image,ImageFFT,'to_freq','none','complex',Width)
correlation_fft(ImageFFT,ImageFFT,Correlation)
rft_generic(Correlation,AutoCorrelation,'from_freq','n','real',Width)
```

## Result

`CorrelationFft` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`FftGeneric`,
`FftImage`,
`RftGeneric`

## Possible Successors

`FftGeneric`,
`FftImageInv`,
`RftGeneric`

## Alternatives

`PhaseCorrelationFft`

## Module

Foundation
