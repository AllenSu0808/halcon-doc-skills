# SobelAmp (Operator)

## Name

`SobelAmp` — Detect edges (amplitude) using the Sobel operator.

## Signature

`static void HOperatorSet.SobelAmp(HObject image, out HObject edgeAmplitude, HTuple filterType, HTuple size)`

`HImage HImage.SobelAmp(string filterType, HTuple size)`

`HImage HImage.SobelAmp(string filterType, int size)`

## Description

`SobelAmp` calculates first derivative of an image and is
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
$$\,'sum_sqrt' \\sqrt{a^2 + b^2}/4 '\sum_abs' (|a| + |b|)/4 '\thin_sum_abs' (\thin(a) + \thin(b))/4 '\thin_max_abs' max(\thin(|a|), \thin(|b|))/4 'x' \\nb/4 (b for real images) 'y' \\na/4 (a for real images)$$ ![figure](../assets/24824e1875472aa9.svg)
Here, thin(x) is equal to $x$ for a vertical
maximum (mask A) and a horizontal maximum (mask B), respectively,
and 0 otherwise. Thus, for *"thin_sum_abs"* and *"thin_max_abs"*
the gradient image is thinned. For the filter types *"x"* and
*"y"* if the input image is of type byte the output image is
of type int1, of type int2 otherwise. For a Sobel operator with
size 3x3, the corresponding filters A and B are
applied directly, while for larger filter sizes the input image is
first smoothed using a Gaussian filter (see [`GaussImage`](gauss_image.md)) or
a binomial filter (see [`BinomialFilter`](binomial_filter.md)) of size
*`size`*-2. The Gaussian filter is selected for the above
values of *`filterType`*. Here, *`size`* = 5, 7, 9, 11,
or 13 must be used. The binomial filter is selected by appending
*"_binomial"* to the above values of *`filterType`*.
Here, *`size`* can be selected between 5 and 39. Furthermore,
it is possible to select different amounts of smoothing the
column and row direction by passing two values in *`size`*.
Here, the first value of *`size`* corresponds to the mask width
(smoothing in the column direction), while the second value
corresponds to the mask height (smoothing in the row direction) of
the binomial filter. The binomial filter can only be used for
images of type byte, uint2 and real. Since smoothing reduces the edge
amplitudes, in this case the edge amplitudes are multiplied by a
factor of 2 to prevent information loss. Therefore,

|  |
| --- |
| `sobel_amp(I,E,FilterType,S)` |

for *`size`* > 3 is conceptually equivalent to

|  |
| --- |
| `scale_image(I,F,2,0)` |
| `gauss_image(F,G,S-2)` |
| `sobel_amp(G,E,FilterType,3)` |

or to

|  |
| --- |
| `scale_image(I,F,2,0)` |
| `binomial_filter(F,G,S[0]-2,S[1]-2)` |
| `sobel_amp(G,E,FilterType,3)`. |

For `SobelAmp` special optimizations are implemented
*`filterType`* = *"sum_abs"* that use SIMD technology.
The actual application of these special optimizations is controlled
by the system parameter *"sse2_enable"* and *"avx2_enable"*,
respectively (see [`SetSystem`](set_system.md)). If *"sse2_enable"* or
*"avx2_enable"*is set to *"true"*
(and the SIMD instruction set is available), the internal calculations are
performed using SIMD technology.
Note that SIMD technology performs best on large, compact input regions.
Depending on the input region and the capabilities of the hardware
the execution of `SobelAmp` might even take significantly
more time with SIMD technology than without.

`SobelAmp` can be executed on OpenCL devices for the filter
types *"sum_abs"*, *"sum_sqrt"*, *"x"* and *"y"*
(as well as their binomial variants). Note that when using Gaussian
filtering for *`size`* > 3, the results can vary from the CPU
implementation.

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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Input image.

**`edgeAmplitude`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (int1 / int2 / uint2 / real)

Edge amplitude (gradient magnitude) image.

**`filterType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Filter type.

Default:
"sum_abs"

List of values:
"sum_abs", "sum_abs_binomial", "sum_sqrt", "sum_sqrt_binomial", "thin_max_abs", "thin_max_abs_binomial", "thin_sum_abs", "thin_sum_abs_binomial", "x", "x_binomial", "y", "y_binomial"

List of values (for compute devices):
"sum_abs", "sum_sqrt", "x", "y", "sum_abs_binomial", "sum_sqrt_binomial", "x_binomial", "y_binomial"

**`size`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Size of filter mask.

Default:
3

List of values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39

## Example (HDevelop)

```
read_image(Image,'fabrik')
sobel_amp(Image,Amp,'sum_abs',3)
threshold(Amp,Edg,128,255)
```

## Result

`SobelAmp` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Predecessors

`BinomialFilter`,
`GaussFilter`,
`MeanImage`,
`AnisotropicDiffusion`,
`SigmaImage`

## Possible Successors

`Threshold`,
`NonmaxSuppressionAmp`,
`GraySkeleton`

## Alternatives

`FreiAmp`,
`Roberts`,
`KirschAmp`,
`PrewittAmp`,
`RobinsonAmp`

## See also

`Laplace`,
`HighpassImage`,
`BandpassImage`

## Module

Foundation
