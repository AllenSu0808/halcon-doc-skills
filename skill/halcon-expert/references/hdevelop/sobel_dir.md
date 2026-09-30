# sobel_dir (Operator)

## Name

`sobel_dir` — Detect edges (amplitude and direction) using the Sobel operator.

## Signature

`sobel_dir(Image : EdgeAmplitude, EdgeDirection : FilterType, Size : )`

## Description

`sobel_dir` calculates first derivative of an image and is
used as an edge detector. The filter is based on the following
filter masks:
A =
1 2 1
0 0 0
-1 -2 -1
B =
1 0 -1
2 0 -2
1 0 -1
These masks are used differently, according to the selected filter
type. (In the following, a and b denote the results of
convolving an image with A and B for one particular pixel.)

- *'sum_sqrt'*: $\sqrt{a^2 + b^2}/4$ ![figure](../assets/59622c203c889bc4.svg)
- *'sum_abs'*: $(|a|+|b|)/4$

For a Sobel operator with size 3x3, the
corresponding filters A and B are applied directly, while for
larger filter sizes the input image is first smoothed using a
Gaussian filter (see [`gauss_image`](gauss_image.md)) or a binomial filter (see
[`binomial_filter`](binomial_filter.md)) of size *`Size`*-2. The Gaussian
filter is selected for the above values of *`FilterType`*.
Here, *`Size`* = 5, 7, 9, 11, or 13 must be used. The binomial
filter is selected by appending *'_binomial'* to the above
values of *`FilterType`*. Here, *`Size`* can be selected
between 5 and 39. Furthermore, it is possible to select different
amounts of smoothing the column and row direction by passing two
values in *`Size`*. Here, the first value of *`Size`*
corresponds to the mask width (smoothing in the column direction),
while the second value corresponds to the mask height (smoothing in
the row direction) of the binomial filter. The binomial filter can
only be used for images of type byte, uint2 and real. Since smoothing
reduces the edge amplitudes, in this case the edge amplitudes are
multiplied by a factor of 2 to prevent information loss. Therefore,

|  |
| --- |
| `sobel_dir(I,Amp,Dir,FilterType,S)` |

for *`Size`* > *3* is conceptually equivalent to

|  |
| --- |
| `scale_image(I,F,2,0)` |
| `gauss_image(F,G,S-2)` |
| `sobel_dir(G,Amp,Dir,FilterType,3)` |

or to

|  |
| --- |
| `scale_image(I,F,2,0)` |
| `binomial_filter(F,G,S[0]-2,S[1]-2)` |
| `sobel_dir(G,Amp,Dir,FilterType,3)`. |

The edge directions are returned in *`EdgeDirection`*, and
are stored in 2-degree steps, i.e., an edge direction of $x$
degrees in mathematically positive sense and with respect to the
horizontal axis is stored as x / 2
in the edge direction image. Furthermore, the direction
of the change of intensity is taken into account. Let
$[E_{x},E_{y}]$ denote the image gradient. Then the
following edge directions $r$ are returned as $r/2$:

| intensity increase | $E\_x/E\_y$ | edge direction $r$ [deg] |
| --- | --- | --- |
| from bottom to top | 0 / + | 0 |
| from lower right to upper left | - / + | ]0,90[ |
| from right to left | - / 0 | 90 |
| from upper right to lower left | - / - | ]90,180[ |
| from top to bottom | 0 / - | 180 |
| from upper left to lower right | + / - | ]180,270[ |
| from left to right | + / 0 | 270 |
| from lower left to upper right | + / + | ]270,360[. |

Points with edge amplitude 0 are assigned the edge direction 255
(undefined direction).

[`sobel_amp`](sobel_amp.md) can be executed on OpenCL devices. Note that when using
Gaussian filtering for *`Size`* > 3, the results can vary from the
CPU implementation.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / real)

Input image.

**`EdgeAmplitude`** (output_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / real)

Edge amplitude (gradient magnitude) image.

**`EdgeDirection`** (output_object)  (multichannel-)image(-array) `→` object (direction)

Edge direction image.

**`FilterType`** (input_control)  string `→`  (string)

Filter type.

Default:
'sum_abs'

List of values:
'sum_abs', 'sum_abs_binomial', 'sum_sqrt', 'sum_sqrt_binomial'

List of values (for compute devices):
'sum_abs', 'sum_sqrt', 'sum_abs_binomial', 'sum_sqrt_binomial'

**`Size`** (input_control)  integer(-array) `→`  (integer)

Size of filter mask.

Default:
3

List of values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39

## Example (HDevelop)

```
read_image(Image,'fabrik')
sobel_dir(Image,Amp,Dir,'sum_abs',3)
threshold(Amp,Edg,128,255)
```

## Result

`sobel_dir` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`mean_image`,
`anisotropic_diffusion`,
`sigma_image`

## Possible Successors

`nonmax_suppression_dir`,
`hysteresis_threshold`,
`threshold`

## Alternatives

`edges_image`,
`frei_dir`,
`kirsch_dir`,
`prewitt_dir`,
`robinson_dir`

## See also

`roberts`,
`laplace`,
`highpass_image`,
`bandpass_image`

## Module

Foundation
