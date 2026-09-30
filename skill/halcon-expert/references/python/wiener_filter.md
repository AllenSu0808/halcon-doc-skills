# wiener_filter (Operator)

## Name

`wiener_filter` — Image restoration by Wiener filtering.

## Signature

`def wiener_filter(image: HObject, psf: HObject, filtered_image: HObject) -> HObject`

## Description

`wiener_filter` produces an estimate of the original image
(= image without noise and blurring) by minimizing the mean square error
between estimated and original image.
`wiener_filter` can be used to restore images corrupted by
noise and/or blurring (e.g., motion blur, atmospheric turbulence or
out-of-focus blur).
Method and realization of this restoration technique bases on the
following model:
The corrupted image is interpreted as the output of a (disturbed) linear
system. Functionality of a linear system is determined by its specific
impulse response. So the convolution of original image and impulse response
results in the corrupted image. The specific impulse response describes
image acquisition and the occurred degradations. In the presence of additive
noise an additional noise term must be considered. So the corrupted image
can be modeled as the result of
[convolution(impulse_response,original_image)] + noise_term
The noise term encloses two different terms describing image-dependent and
image-independent noise.
According to this model, two terms must be known for restoration by Wiener
filtering:

1. degradation-specific impulse response
2. noise term

So `wiener_filter` needs a smoothed version of the input image
to estimate the power spectral density of noise and original image. One
can use one of the smoothing HALCON-filters (e.g., [`eliminate_min_max`](eliminate_min_max.md))
to get this version.
`wiener_filter` needs further the impulse response that describes
the specific degradation. This impulse response (represented in spatial
domain) must fit into an image of HALCON image type `real`. There
exist two HALCON-operators for generation of an impulse response for
motion blur and out-of-focus (see [`gen_psf_motion`](gen_psf_motion.md),
[`gen_psf_defocus`](gen_psf_defocus.md)). The representation of the impulse response
presumes the origin in the upper left corner. This results in the following
disposition of an NxM sized image:

- first rectangle (“upper left”):
  (image coordinates xb = 0..(N/2)-1, yb = 0..(M/2)-1)

  - conforms to the fourth quadrant of the Cartesian coordinate system,
  encloses values of the impulse response
  at position x = 0..N/2 and y = 0..-M/2
- second rectangle (“upper right”):
  (image coordinates xb = N/2..N-1, yb = 0..(M/2)-1)

  - conforms to the third quadrant of the Cartesian coordinate system,
  encloses values of the impulse response
  at position x = -N/2..-1 and y = -1..-M/2
- third rectangle (“lower left”):
  (image coordinates xb = 0..(N/2)-1, yb = M/2..M-1)

  - conforms to the first quadrant of the Cartesian coordinate system,
  encloses values of the impulse response
  at position x = 1..N/2 and y = M/2..0
- fourth rectangle (“lower right”):
  (image coordinates xb = N/2..N-1, yb = M/2..M-1)

  - conforms to the second quadrant of the Cartesian coordinate system,
  encloses values of the impulse response
  at position x = -N/2..-1 and y = M/2..1

`wiener_filter` works as follows:

- estimation of the power spectrum density of the original image by using
  the smoothed version of the corrupted image,
- estimation of the power spectrum density of each pixel by subtracting
  smoothed version from not smoothed version,
- building the Wiener filter kernel with the quotient of power spectrum
  densities of noise and original image and with the impulse response,
- processing the convolution of image and Wiener filter frequency response.

The result image has got image type `real`.

## Attention

*`psf`* must be of image type `real` and conform to *`image`*
and *`filtered_image`* in image width and height.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Corrupted image.

**`psf`** (input_object)  (multichannel-)image `→` HObject (real)

impulse response (PSF) of degradation (in spatial domain).

**`filtered_image`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Smoothed version of corrupted image.

**`restored_image`** (output_object)  image `→` HObject (real)

Restored image.

## Example (C)

```
/* Restoration of a noisy image (size=256x256), that was blurred by motion*/
Hobject object;
Hobject restored;
Hobject psf;
Hobject noisefiltered;
/* 1. Generate a Point-Spread-Function for a motion-blur with       */
/*    parameter a=10 and direction along the x-axis                 */
gen_psf_motion(&psf,256,256,10,0,3);
/* 2. Noisefiltering of the image                                   */
median_image(object,&noisefiltered,"circle",2,0);
/* 3. Wiener-filtering                                              */
wiener_filter(object,psf,noisefiltered,&restored);
```

## Result

`wiener_filter` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty `wiener_filter` returns with
an error message.

## Possible Predecessors

`gen_psf_motion`,
`simulate_motion`,
`simulate_defocus`,
`gen_psf_defocus`,
`optimize_fft_speed`

## Alternatives

`wiener_filter_ni`

## See also

`simulate_motion`,
`gen_psf_motion`,
`simulate_defocus`,
`gen_psf_defocus`

## References

M. Lückenhaus:“Grundlagen des Wiener-Filters und seine Anwendung
in der Bildanalyse”; Diplomarbeit;
Technische Universität München, Institut für Informatik;
Lehrstuhl Prof. Radig; 1995
  
Azriel Rosenfeld, Avinash C. Kak: Digital Picture Processing,
Computer Science and Aplied Mathematics, Academic Press New York/San
Francisco/London 1982

## Module

Foundation
