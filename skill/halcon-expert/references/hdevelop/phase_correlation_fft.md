# phase_correlation_fft (Operator)

## Name

`phase_correlation_fft` — Compute the phase correlation of two images in the frequency domain.

## Signature

`phase_correlation_fft(ImageFFT1, ImageFFT2 : ImagePhaseCorrelation : : )`

## Description

`phase_correlation_fft` calculates the phase correlation of
the Fourier-transformed input images in the frequency domain. The
phase correlation is calculated by multiplying *`ImageFFT1`*
with the complex conjugate of *`ImageFFT2`* and dividing by the
absolute value of this product. It should be noted that in order to
achieve a correct scaling of the phase correlation in the spatial
domain, the operators [`fft_generic`](fft_generic.md) or [`rft_generic`](rft_generic.md)
with `Norm` = *'none'* must be used for the forward
transform and [`fft_generic`](fft_generic.md) or [`rft_generic`](rft_generic.md) with
`Norm` = *'n'* for the reverse transform. If
*`ImageFFT1`* and *`ImageFFT2`* contain the same number of
images, the corresponding images are phase-correlated pairwise.
Otherwise, *`ImageFFT2`* must contain only one single image.
In this case, the phase correlation is performed for each image of
*`ImageFFT1`* with *`ImageFFT2`* .

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

**`ImagePhaseCorrelation`** (output_object)  image(-array) `→` object (complex)

Phase correlation of the input images in the
frequency domain.

## Example (HDevelop)

```
* Compute the phase correlation of two images.
get_image_size(Image1,Width,Height)
rft_generic(Image1,ImageFFT1,'to_freq','none','complex',Width)
rft_generic(Image2,ImageFFT2,'to_freq','none','complex',Width)
phase_correlation_fft(ImageFFT1,ImageFFT2,PhaseCorrelationFFT)
rft_generic(PhaseCorrelationFFT,PhaseCorrelation,'from_freq','n', \
            'real',Width)
* Determine the translation between the two images.
local_max_sub_pix (PhaseCorrelation, 'facet', 1, 0.02, Row, Column)
```

## Result

`phase_correlation_fft` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`fft_generic`,
`fft_image`,
`rft_generic`

## Possible Successors

`fft_generic`,
`fft_image_inv`,
`rft_generic`

## Alternatives

`correlation_fft`

## References

C. D. Kuglin, D. C. Hines: “The Phase Correlation Image Alignment
Method”; IEEE International Conference on Cybernetics and
Society; pp. 163-165; 1975.

## Module

Foundation
