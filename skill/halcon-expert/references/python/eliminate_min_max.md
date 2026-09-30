# eliminate_min_max (Operator)

## Name

`eliminate_min_max` — Smooth an image in the spatial domain to suppress noise.

## Signature

`def eliminate_min_max(image: HObject, mask_width: int, mask_height: int, gap: float, mode: int) -> HObject`

## Description

`eliminate_min_max` smooths an image by replacing gray values with
neighboring mean values, or local minima/maxima. In order to prevent
edges and lines from being smoothed, only those gray values that represent
local minima or maxima are replaced (if there is a line or edge within an
image there will be at least one neighboring pixel with a comparable
gray value). *`gap`* controls the strictness of replacement: Only
gray values that exceed all other values within their local neighborhood
more than *`gap`* and all values that fall below their neighboring
more than *`gap`* are replaced.

Thus, with $g(x,y)$ being the gray value at position
$(x,y)$ and $E(x,y)$ representing the gray values of a
$\texttt{MaskWidth}\times\texttt{MaskHeight}$
sized rectangular neighborhood of a pixel at position $(x,y)$,
containing all pixels within the neighborhood except the pixel itself,
a pixel is replaced

- if $g(x,y)\ge\texttt{Gap}+max(E(x,y))$, or
- else if $g(x,y)+\texttt{Gap}<=min(E(x,y))$.
- Elsewise $g(x,y)$ is adopted without change.

*`mode`* specifies how to perform the new value in case of a
replacement.

- *`mode`* = *1*:
  replace a local maximum with next minor local maximum and
  replace a local minimum with next bigger local minimum.
- *`mode`* = *2*:
  replace with mean value of all pixels within the local neighborhood
  (including the replaced pixel).
- *`mode`* = *3*:
  replace with median value of all pixels within the local neighborhood
  (including the replaced pixel (also used if *`mode`* has got
  any other value than *1* or *2*).

*`mask_width`* and *`mask_height`* specify the width and height of
the rectangular neighborhood.
Border treatment: Pixels outside the image border are not considered (e.g.,
with a local $3\times3$-mask the neighborhood of a pixel at
$(0,0)$ reduces to the pixels at $(1,0)$,
$(0,1)$, and $(1,1)$).

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

If *`mask_width`* or *`mask_height`* is an even
number, it is replaced by the next higher odd number (this allows the
unique extraction of the center of the filter mask).
Width/height of the mask may not exceed the image width/height.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Image to smooth.

**`filtered_image`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Smoothed image.

**`mask_width`** (input_control)  extent.x `→` int

Width of filter mask.

Default:
3

Suggested values:
3, 5, 7, 9

Value range:
`3
≤
mask_width
≤
width(Image)`

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskWidth)`

**`mask_height`** (input_control)  extent.y `→` int

Height of filter mask.

Default:
3

Suggested values:
3, 5, 7, 9

Value range:
`3
≤
mask_height
≤
width(Image)`

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskWidth)`

**`gap`** (input_control)  number `→` float

Gap between local maximum/minimum and all other
gray values of the neighborhood.

Default:
1.0

Suggested values:
1.0, 2.0, 5.0, 10.0

**`mode`** (input_control)  integer `→` int

Replacement rule.

Default:
3

List of values:
1, 2, 3

## Result

`eliminate_min_max` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty `eliminate_min_max` returns with
an error message.

## Possible Successors

`wiener_filter`,
`wiener_filter_ni`

## See also

`mean_sp`,
`mean_image`,
`median_image`,
`median_weighted`,
`binomial_filter`,
`gauss_filter`,
`smooth_image`

## References

M. Imme:“A Noise Peak Elimination Filter”; S. 204-211 in CVGIP
Graphical Models and Image Processing, Vol. 53, No. 2, March 1991
  
M. Lückenhaus:“Grundlagen des Wiener-Filters und seine Anwendung in der
Bildanalyse”; Diplomarbeit;
Technische Universität München, Institut für Informatik;
Lehrstuhl Prof. Radig; 1995.

## Module

Foundation
