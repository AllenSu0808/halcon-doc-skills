# EnergyGabor (Operator)

## Name

`EnergyGabor` — Calculate the energy of a two-channel image.

## Signature

`static void HOperatorSet.EnergyGabor(HObject imageGabor, HObject imageHilbert, out HObject energy)`

`HImage HImage.EnergyGabor(HImage imageHilbert)`

## Description

`EnergyGabor` calculates the local contrast
(*`energy`*) of the two input images. The energy of the
resulting image is then defined as
$$\texttt{Energy}=\text{channel1}^{2}+\text{channel2}^{2}.$$
Often the calculation of the energy is preceded by the convolution
of an image with a Gabor filter and the Hilbert transform of the
Gabor filter (see [`ConvolGabor`](convol_gabor.md)). In this case, the
first channel of the image passed to `EnergyGabor` is the
Gabor-filtered image, transformed back into the spatial domain (see
[`FftImageInv`](fft_image_inv.md)), and the second channel the result of the
convolution with the Hilbert transform, also transformed back into
the spatial domain. The local energy is a measure for the local
contrast of structures (e.g., edges and lines) in the image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`imageGabor`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / real)

1st channel of input image (usually: Gabor image).

**`imageHilbert`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / real)

2nd channel of input image (usually: Hilbert image).

**`energy`** (output_object)  image(-array) `→` [HImage](HImage.md) (real)

Image containing the local energy.

## Example (C)

```
fft_image(Image,&FFT);
gen_gabor(&Filter,1.4,0.4,1.0,1.5,512);
convol_gabor(FFT,Filter,&Gabor,&Hilbert);
fft_image_inv(Gabor,&GaborInv);
fft_image_inv(Hilbert,&HilbertInv);
energy_gabor(GaborInv,HilbertInv,&Energy);
```

## Result

`EnergyGabor` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`GenGabor`,
`ConvolGabor`,
`FftImageInv`

## Module

Foundation
