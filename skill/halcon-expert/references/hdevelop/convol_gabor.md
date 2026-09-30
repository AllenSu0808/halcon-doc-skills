# convol_gabor (Operator)

## Name

`convol_gabor` — Convolve an image with a Gabor filter in the frequency domain.

## Signature

`convol_gabor(ImageFFT, GaborFilter : ImageResultGabor, ImageResultHilbert : : )`

## Description

`convol_gabor` convolves a Fourier-transformed image with a
Gabor filter *`GaborFilter`* (see [`gen_gabor`](gen_gabor.md)) and its
Hilbert transform in the frequency domain. The result image is of
type *'complex'*.

## Attention

The filtering is always done on the entire image, i.e., the domain
of the image is ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`ImageFFT`** (input_object)  (multichannel-)image(-array) `→` object (complex)

Input image.

**`GaborFilter`** (input_object)  multichannel-image `→` object (real)

Gabor/Hilbert-Filter.

**`ImageResultGabor`** (output_object)  image(-array) `→` object (complex)

Result of the Gabor filter.

**`ImageResultHilbert`** (output_object)  image(-array) `→` object (complex)

Result of the Hilbert filter.

## Example (HDevelop)

```
gen_gabor(Filter,1.4,0.4,1.0,1.5,'n','dc_edge',512,512)
fft_generic(Image,ImageFFT,'to_freq',-1,'none','dc_edge','complex')
convol_gabor(ImageFFT,Filter,Gabor,Hilbert)
fft_generic(Gabor,GaborInv,'from_freq',1,'none','dc_edge','byte')
fft_generic(Hilbert,HilbertInv,'from_freq',1,'none','dc_edge','byte')
energy_gabor(GaborInv,HilbertInv,Energy)
```

## Result

`convol_gabor` returns 2 (
H_MSG_TRUE)
if all images are of correct type.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`fft_image`,
`fft_generic`,
`gen_gabor`

## Possible Successors

`power_byte`,
`power_real`,
`power_ln`,
`fft_image_inv`,
`fft_generic`

## Alternatives

`convol_fft`

## See also

`convol_image`

## Module

Foundation
