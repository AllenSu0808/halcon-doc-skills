# correlation_fft (Operator)

## Name

`correlation_fft` — Multiply one image with the complex conjugate of another image in the
frequency domain.

## Signature

`correlation_fft(ImageFFT1, ImageFFT2 : ImageCorrelation : : )`

## Description

As part of calculating the correlation between two images,
`correlation_fft` multiplies the Fourier transform of the first image
*`ImageFFT1`* with the complex conjugate of the Fourier-transformed
second image *`ImageFFT2`*.

According to the correlation theorem, the non-normalized
correlation of two images in pixel space can be obtained in three steps:

1. Transforming the images into frequency space using a
   Fourier transform (see, e.g., [`fft_generic`](fft_generic.md)).
2. Multiplying one transformed image with the complex conjugate of
   the other transformed image (pixel-wise).
3. Transforming the result back into pixel space using an
   inverse Fourier transform (see, e.g., [`fft_generic`](fft_generic.md)).

The operator `correlation_fft` is used to perform the second step,
i.e., *`ImageFFT1`* is pixel-wise multiplied with the complex
conjugate of *`ImageFFT2`*.

It should be noted that in order to achieve a correct scaling of the
correlation in the spatial domain, the operators
[`fft_generic`](fft_generic.md) or [`rft_generic`](rft_generic.md) with
`Norm` = *'none'* must be used for the forward
transform (step 1) and [`fft_generic`](fft_generic.md) or [`rft_generic`](rft_generic.md) with
`Norm` = *'n'* for the reverse transform (step 3).
If *`ImageFFT1`* and *`ImageFFT2`* contain the same number
of images, the corresponding images are multiplied pairwise.
Otherwise, *`ImageFFT2`* must contain only one single image.
In this case, the multiplication is performed for each image of
*`ImageFFT1`* with *`ImageFFT2`*.

## Attention

The filtering is always performed on the entire image, i.e., the domain
of the image is ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`ImageFFT1`** (input_object)  (multichannel-)image(-array) `→` object (complex)

Fourier-transformed input image 1.

**`ImageFFT2`** (input_object)  (multichannel-)image(-array) `→` object (complex)

Fourier-transformed input image 2.

Number of elements:
ImageFFT2 == ImageFFT1 || ImageFFT2 == 1

**`ImageCorrelation`** (output_object)  image(-array) `→` object (complex)

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

`correlation_fft` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`fft_generic`,
`fft_image`,
`rft_generic`

## Possible Successors

`fft_generic`,
`fft_image_inv`,
`rft_generic`

## Alternatives

`phase_correlation_fft`

## Module

Foundation
