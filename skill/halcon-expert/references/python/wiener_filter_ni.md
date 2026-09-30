# wiener_filter_ni (Operator)

## Name

`wiener_filter_ni` — Image restoration by Wiener filtering.

## Signature

`def wiener_filter_ni(image: HObject, psf: HObject, noise_region: HObject, mask_width: int, mask_height: int) -> HObject`

## Description

`wiener_filter_ni` (ni = noise-estimation integrated) produces an
estimate of the original image (= image without noise and blurring) by
minimizing the mean square error between estimated and original image.
[`wiener_filter`](wiener_filter.md) can be used to restore images corrupted by
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

`wiener_filter_ni` estimates the noise term as follows:
The user defines a region that is suitable for noise estimation within the
image (homogeneous as possible, as edges or textures aggravate noise
estimation). After smoothing within this region by an (unweighted) median
filter and subtracting smoothed version from unsmoothed, the average noise
amplitude of the region is processed within `wiener_filter_ni`. This
amplitude together with the average gray value within the region allows
estimating the quotient of the power spectral densities of noise and
original image (in contrast to [`wiener_filter`](wiener_filter.md) `wiener_filter_ni`
assumes a rather constant quotient within the whole image). The user can
define width and height of the rectangular (median-)filter mask to
influence the noise estimation (*`mask_width`*, *`mask_height`*).
`wiener_filter_ni` needs further the impulse response that describes
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

[`wiener_filter`](wiener_filter.md) works as follows:

- estimating the quotient of the power spectrum densities of noise
  and original image,
- building the Wiener filter kernel with the quotient of power spectrum
  densities of noise and original image and with the impulse response,
- processing the convolution of image and Wiener filter frequency response.

The result image has got image type `real`.

## Attention

*`psf`* must be of image type `real` and conform to *`image`*
in width and height.
The Region used for noise estimation must lie completely within the
image.
If *`mask_width`* or *`mask_height`* is an even number,
it is replaced by the next higher odd number (this allows the unique
extraction of the center of the filter mask).
Width/height of the mask may not exceed the image width/height or be less
than null.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Corrupted image.

**`psf`** (input_object)  (multichannel-)image `→` HObject (real)

impulse response (PSF) of degradation (in spatial domain).

**`noise_region`** (input_object)  region(-array) `→` HObject

Region for noise estimation.

**`restored_image`** (output_object)  image `→` HObject (real)

Restored image.

**`mask_width`** (input_control)  integer `→` int

Width of filter mask.

Default:
3

Suggested values:
3, 5, 7, 9

Value range:
`0
≤
mask_width
≤
width(Image)`

**`mask_height`** (input_control)  integer `→` int

Height of filter mask.

Default:
3

Suggested values:
3, 5, 7, 9

Value range:
`0
≤
mask_height
≤
height(Image)`

## Example (C)

```
/* Restoration of a noisy image (size=256x256), that was blurred by motion*/
Hobject object;
Hobject restored;
Hobject psf;
Hobject noise_region;
/* 1. Generate a Point-Spread-Function for a motion-blur with       */
/*    parameter a=10 and direction of the x-axis                    */
gen_psf_motion(&psf,256,256,10,0,3);
/* 2. Segmentation of a region for the noise-estimation             */
open_window(0,0,256,256,0,"visible",&WindowHandle);
disp_image(object,WindowHandle);
draw_region(&noise_region,draw_region);
/* 3. Wiener-filtering                                              */
wiener_filter_ni(object,psf,noise_region,&restored,3,3);
```

## Result

`wiener_filter_ni` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty `wiener_filter_ni` returns with
an error message.

## Possible Predecessors

`gen_psf_motion`,
`simulate_motion`,
`simulate_defocus`,
`gen_psf_defocus`,
`optimize_fft_speed`

## Alternatives

`wiener_filter`

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
