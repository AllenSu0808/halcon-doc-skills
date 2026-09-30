# ConvolGabor (Operator)

## Name

`ConvolGabor` — Convolve an image with a Gabor filter in the frequency domain.

## Signature

`static void HOperatorSet.ConvolGabor(HObject imageFFT, HObject gaborFilter, out HObject imageResultGabor, out HObject imageResultHilbert)`

`HImage HImage.ConvolGabor(HImage gaborFilter, out HImage imageResultHilbert)`

## Description

`ConvolGabor` convolves a Fourier-transformed image with a
Gabor filter *`gaborFilter`* (see [`GenGabor`](gen_gabor.md)) and its
Hilbert transform in the frequency domain. The result image is of
type *"complex"*.

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

Input image.

**`gaborFilter`** (input_object)  multichannel-image `→` [HImage](HImage.md) (real)

Gabor/Hilbert-Filter.

**`imageResultGabor`** (output_object)  image(-array) `→` [HImage](HImage.md) (complex)

Result of the Gabor filter.

**`imageResultHilbert`** (output_object)  image(-array) `→` [HImage](HImage.md) (complex)

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

`ConvolGabor` returns 2 (
H_MSG_TRUE)
if all images are of correct type.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`FftImage`,
`FftGeneric`,
`GenGabor`

## Possible Successors

`PowerByte`,
`PowerReal`,
`PowerLn`,
`FftImageInv`,
`FftGeneric`

## Alternatives

`ConvolFft`

## See also

`ConvolImage`

## Module

Foundation
