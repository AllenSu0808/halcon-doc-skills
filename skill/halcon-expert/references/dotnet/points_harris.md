# PointsHarris (Operator)

## Name

`PointsHarris` — Detect points of interest using the Harris operator.

## Signature

`static void HOperatorSet.PointsHarris(HObject image, HTuple sigmaGrad, HTuple sigmaSmooth, HTuple alpha, HTuple threshold, out HTuple row, out HTuple column)`

`void HImage.PointsHarris(double sigmaGrad, double sigmaSmooth, double alpha, HTuple threshold, out HTuple row, out HTuple column)`

`void HImage.PointsHarris(double sigmaGrad, double sigmaSmooth, double alpha, double threshold, out HTuple row, out HTuple column)`

## Description

`PointsHarris` extracts points of interest from an image. The Harris
operator is based upon the smoothed matrix
$$M = G_{\sigma}^*\left(\begin{array}{cc} \sum_{c=1}^{n} I_{x,c}^2 & \sum_{c=1}^{n} I_{x,c}I_{y,c}\\ \sum_{c=1}^{n} I_{x,c}I_{y,c} & \sum_{c=1}^{n} I_{y,c}^2 \end{array}\right),$$ ![figure](../assets/8ee09fb30ad7e7c1.svg)
where $G_{\sigma}$ stands for a Gaussian smoothing of size
*`sigmaSmooth`* and $I_{x,c}$ and $I_{y,c}$ are
the first derivatives of each image channel, computed with Gaussian
derivatives of size *`sigmaGrad`*. The resulting points are the
positive local extrema of
$$\mathrm{Det}M-\texttt{Alpha}\ast(\mathrm{Trace}M)^{2}.$$
If necessary, they can be restricted to points with a minimum filter
response of *`threshold`*. The coordinates of the points are
calculated with subpixel accuracy.

## Attention

`PointsHarris` uses a special implementation that is
optimized using SSE2 instructions if the system
parameter *"sse2_enable"* is set to *"true"* (which is
default if SSE2 is available on your machine). This implementation is
slightly inaccurate compared to the pure C version due to numerical issues
(for 'byte' images the difference in *`row`* and *`column`* is in
order of magnitude of 1.0e-5). If you prefer accuracy over performance
you can set *"sse2_enable"* to *"false"* (using
[`SetSystem`](set_system.md)) before you call `PointsHarris`. This way
`PointsHarris` does not use SSE2 accelerations. Don't forget to set
*"sse2_enable"* back to *"true"* afterwards.

`PointsHarris` can be executed on an OpenCL device if both
*`sigmaGrad`* and *`sigmaSmooth`* induce a filter size of no more
than 129 pixels. This corresponds to a value of less than 20.7 for
both parameters. As with the SSE2 version, the results of the OpenCL
implementation may diverge slightly from that of pure C version due to
numerical issues.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte* / uint2* / real*) **allowed for compute devices*

Input image.

**`sigmaGrad`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Amount of smoothing used for the calculation of the
gradient.

Default:
0.7

Suggested values:
0.7, 0.8, 0.9, 1.0, 1.2, 1.5, 2.0, 3.0

Recommended increment:
0.1

Restriction:
`SigmaGrad > 0.0`

**`sigmaSmooth`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Amount of smoothing used for the integration of the
gradients.

Default:
2.0

Suggested values:
0.7, 0.8, 0.9, 1.0, 1.2, 1.5, 2.0, 3.0

Recommended increment:
0.1

Restriction:
`SigmaSmooth > 0.0`

**`alpha`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Weight of the squared trace of the squared gradient
matrix.

Default:
0.08

Suggested values:
0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08

Value range:
`0.0
≤
alpha`

Minimum increment:
0.001

Recommended increment:
0.01

**`threshold`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum filter response for the points.

Default:
1000.0

Restriction:
`Threshold >= 0.0`

**`row`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the detected points.

**`column`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the detected points.

## Result

`PointsHarris` returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during the execution. If the input is empty the
behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Successors

`GenCrossContourXld`

## Alternatives

`PointsFoerstner`,
`PointsLepetit`,
`PointsHarrisBinomial`

## References

C. Harris, M. Stephens: “A combined corner and edge
detector”. Proceedings of the 4th Alvey Vision Conference,
pp. 147-151, 1988.
  
V. Gouet, N.Boujemaa: “Object-based queries using color points of
interest”. IEEE Workshop on Content-Based Access of Image and Video
Libraries, CVPR/CBAIVL 2001, Hawaii, USA, 2001.

## Module

Foundation
