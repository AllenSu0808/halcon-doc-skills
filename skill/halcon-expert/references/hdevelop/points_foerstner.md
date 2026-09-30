# points_foerstner (Operator)

## Name

`points_foerstner` — Detect points of interest using the Förstner operator.

## Signature

`points_foerstner(Image : : SigmaGrad, SigmaInt, SigmaPoints, ThreshInhom, ThreshShape, Smoothing, EliminateDoublets : RowJunctions, ColumnJunctions, CoRRJunctions, CoRCJunctions, CoCCJunctions, RowArea, ColumnArea, CoRRArea, CoRCArea, CoCCArea)`

## Description

`points_foerstner` extracts significant points from an image.
Significant points are points that differ from their neighborhood,
i.e., points where the image function changes in two dimensions. These
changes occur on the one hand at the intersection of image edges (called
junction points), and on the other hand at places where color or brightness
differs from the surrounding neighborhood (called area points).

The point extraction takes place in two steps: In the first step the point
regions, i.e., the inhomogeneous, isotropic regions, are extracted from the
image. To do so, the smoothed matrix
$$M = S_\*(\left(\sum_{c=1}^{n} I_{x,c}^{2} \right) \left(\sum_{c=1}^{n} I_{x,c} I_{y,c} \right) \left(\sum_{c=1}^{n} I_{x,c} I_{y,c} \right)??)$$ ![figure](../assets/9c885751614fb401.svg)
is calculated, where $I_{x,c}$ and $I_{y,c}$ are the
first derivatives of each image channel and S stands for a smoothing. If
*`Smoothing`* is *'gauss'*, the derivatives are computed with
Gaussian derivatives of size *`SigmaGrad`* and the smoothing is
performed by a Gaussian of size *`SigmaInt`*. If *`Smoothing`*
is *'mean'*, the derivatives are computed with a
3 x 3 Sobel filter (and hence *`SigmaGrad`* is ignored)
and the smoothing is performed by a *`SigmaInt`* x *`SigmaInt`* mean filter.
Then
inhomogeneity = Trace(M)
is the degree of inhomogeneity in the image and
$$isotropy = 4 \cdot \frac{DetM}{(TraceM)^2}$$ ![figure](../assets/57ad36918d5cc325.svg)
is the degree of the isotropy of the texture in the image. Image points that
have an inhomogeneity greater or equal to *`ThreshInhom`* and at the
same time an isotropy greater or equal to *`ThreshShape`* are
subsequently examined further.

In the second step, two optimization functions are calculated for the
resulting points. Essentially, these optimization functions average for each
point the distances to the edge directions (for junction points) and the
gradient directions (for area points) within an observation window around
the point. If *`Smoothing`* is *'gauss'*, the averaging is
performed by a Gaussian of size *`SigmaPoints`*, if *`Smoothing`*
is *'mean'*, the averaging is performed by a *`SigmaPoints`* x *`SigmaPoints`*
mean filter. The local minima of the optimization
functions determine the extracted points. Their subpixel precise position is
returned in (*`RowJunctions`*, *`ColumnJunctions`*) and
(*`RowArea`*, *`ColumnArea`*).

In addition to their position, for each extracted point the elements
*`CoRRJunctions`*, *`CoRCJunctions`*, and *`CoCCJunctions`*
(and *`CoRRArea`*, *`CoRCArea`*, and *`CoCCArea`*,
respectively) of the corresponding covariance matrix are returned. This
matrix facilitates conclusions about the precision of the calculated point
position. To obtain the actual values, it is necessary to estimate the amount
of noise in the input image and to multiply all components of the covariance
matrix with the variance of the noise. (To estimate the amount of noise,
apply [`intensity`](intensity.md) to homogeneous image regions or
[`plane_deviation`](plane_deviation.md) to image regions, where the gray values form a
plane. In both cases the amount of noise is returned in the
parameter Deviation.) This is illustrated by the example program
`points_foerstner_ellipses.hdev`.

It lies in the nature of this operator that corners often result in two
distinct points: One junction point, where the edges of the corner actually
meet, and one area point inside the corner. Such doublets will be eliminated
automatically, if *`EliminateDoublets`* is *'true'*. To do so,
each pair of one junction point and one area point is examined. If the
points lie within each others' observation window of the optimization
function, for both points the precision of the point position is calculated
and the point with the lower precision is rejected. If
*`EliminateDoublets`* is *'false'*, every detected point is
returned.

## Attention

Note that only odd values for *`SigmaInt`* and
*`SigmaPoints`* are allowed, if *`Smoothing`* is
*'mean'*. Even values automatically will be replaced by the
next larger odd value.

`points_foerstner` with *`Smoothing`* = *'gauss'* uses a
special implementation that is optimized using SSE2 instructions if the
system parameter *'sse2_enable'* is set to *'true'* (which is
default if SSE2 is available on your machine). This implementation is
slightly inaccurate compared to the pure C version due to numerical issues
(for 'byte' images the difference in *`RowJunctions`* and
*`ColumnJunctions`* is in order of magnitude of 1.0e-5). If you prefer
accuracy over performance you can set *'sse2_enable'* to
*'false'* (using [`set_system`](set_system.md)) before you call
`points_foerstner`. This way `points_foerstner` does not use
SSE2 accelerations. Don't forget to set *'sse2_enable'* back
to *'true'* afterwards.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  (multichannel-)image `→` object (byte / uint2 / real)

Input image.

**`SigmaGrad`** (input_control)  number `→`  (real / integer)

Amount of smoothing used for the calculation of the
gradient. If *`Smoothing`* is 'mean',
*`SigmaGrad`* is ignored.

Default:
1.0

Suggested values:
0.7, 0.8, 0.9, 1.0, 1.2, 1.5, 2.0, 3.0

Value range:
`0.0
≤
SigmaGrad`

Recommended increment:
0.1

**`SigmaInt`** (input_control)  number `→`  (real / integer)

Amount of smoothing used for the integration of the
gradients.

Default:
2.0

Suggested values:
0.7, 0.8, 0.9, 1.0, 1.2, 1.5, 2.0, 3.0

Recommended increment:
0.1

Restriction:
`SigmaInt > 0`

**`SigmaPoints`** (input_control)  number `→`  (real / integer)

Amount of smoothing used in the optimization
functions.

Default:
3.0

Suggested values:
0.7, 0.8, 0.9, 1.0, 1.2, 1.5, 2.0, 3.0

Recommended increment:
0.1

Restriction:
`SigmaPoints >= SigmaInt && SigmaPoints > 0.6`

**`ThreshInhom`** (input_control)  number `→`  (real / integer)

Threshold for the segmentation of inhomogeneous image
areas.

Default:
200

Suggested values:
50, 100, 200, 500, 1000

Value range:
`0.0
≤
ThreshInhom`

**`ThreshShape`** (input_control)  real `→`  (real)

Threshold for the segmentation of point areas.

Default:
0.3

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5, 0.7

Value range:
`0.01
≤
ThreshShape
≤
1`

Minimum increment:
0.01

Recommended increment:
0.1

**`Smoothing`** (input_control)  string `→`  (string)

Used smoothing method.

Default:
'gauss'

List of values:
'gauss', 'mean'

**`EliminateDoublets`** (input_control)  string `→`  (string)

Elimination of multiply detected points.

Default:
'false'

List of values:
'false', 'true'

**`RowJunctions`** (output_control)  point.y-array `→`  (real)

Row coordinates of the detected junction points.

**`ColumnJunctions`** (output_control)  point.x-array `→`  (real)

Column coordinates of the detected junction points.

**`CoRRJunctions`** (output_control)  number-array `→`  (real)

Row part of the covariance matrix of the detected
junction points.

**`CoRCJunctions`** (output_control)  number-array `→`  (real)

Mixed part of the covariance matrix of the detected
junction points.

**`CoCCJunctions`** (output_control)  number-array `→`  (real)

Column part of the covariance matrix of the detected
junction points.

**`RowArea`** (output_control)  point.y-array `→`  (real)

Row coordinates of the detected area points.

**`ColumnArea`** (output_control)  point.x-array `→`  (real)

Column coordinates of the detected area points.

**`CoRRArea`** (output_control)  number-array `→`  (real)

Row part of the covariance matrix of the detected
area points.

**`CoRCArea`** (output_control)  number-array `→`  (real)

Mixed part of the covariance matrix of the detected
area points.

**`CoCCArea`** (output_control)  number-array `→`  (real)

Column part of the covariance matrix of the detected
area points.

## Result

`points_foerstner` returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during the execution. If the input is empty the
behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Successors

`gen_cross_contour_xld`,
`disp_cross`

## Alternatives

`points_harris`,
`points_lepetit`,
`points_harris_binomial`

## References

W. Förstner, E. Gülch: “A Fast Operator for Detection and Precise
Location of Distinct Points, Corners and Circular features”. In
Proceedings of the Intercommission Conference on Fast Processing of
Photogrametric Data, Interlaken, pp. 281-305, 1987.
  
W. Förstner: “Statistische Verfahren für die automatische
Bildanalyse und ihre Bewertung bei der Objekterkennung und
-vermessung”. Volume 370, Series C, Deutsche Geodätische
Kommission, München, 1991.
  
W. Förstner: “A Framework for Low Level Feature
Extraction”. European Conference on Computer Vision, LNCS 802,
pp. 383-394, Springer Verlag, 1994.
  
C. Fuchs: “Extraktion polymorpher Bildstrukturen und ihre
topologische und geometrische Gruppierung”. Volume 502, Series C,
Deutsche Geodätische Kommission, München, 1998.

## Module

Foundation
