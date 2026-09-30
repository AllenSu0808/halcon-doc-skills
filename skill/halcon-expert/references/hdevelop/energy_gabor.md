# energy_gabor (Operator)

## Name

`energy_gabor` — Calculate the energy of a two-channel image.

## Signature

`energy_gabor(ImageGabor, ImageHilbert : Energy : : )`

## Description

`energy_gabor` calculates the local contrast
(*`Energy`*) of the two input images. The energy of the
resulting image is then defined as
$$\texttt{Energy}=\text{channel1}^{2}+\text{channel2}^{2}.$$
Often the calculation of the energy is preceded by the convolution
of an image with a Gabor filter and the Hilbert transform of the
Gabor filter (see [`convol_gabor`](convol_gabor.md)). In this case, the
first channel of the image passed to `energy_gabor` is the
Gabor-filtered image, transformed back into the spatial domain (see
[`fft_image_inv`](fft_image_inv.md)), and the second channel the result of the
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

**`ImageGabor`** (input_object)  (multichannel-)image(-array) `→` object (byte / real)

1st channel of input image (usually: Gabor image).

**`ImageHilbert`** (input_object)  (multichannel-)image(-array) `→` object (byte / real)

2nd channel of input image (usually: Hilbert image).

**`Energy`** (output_object)  image(-array) `→` object (real)

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

`energy_gabor` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`gen_gabor`,
`convol_gabor`,
`fft_image_inv`

## Module

Foundation
