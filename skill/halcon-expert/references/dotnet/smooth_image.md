# SmoothImage (Operator)

## Name

`SmoothImage` — Smooth an image using various filters.

## Signature

`static void HOperatorSet.SmoothImage(HObject image, out HObject imageSmooth, HTuple filter, HTuple alpha)`

`HImage HImage.SmoothImage(string filter, double alpha)`

## Description

`SmoothImage` smooths gray images using recursive filters
originally developed by Deriche and Shen and using the non-recursive
Gaussian filter. The following filters can be chosen via the
parameter *`filter`*:
'deriche1', 'deriche2', 'shen' and 'gauss'.
The “filter width” (i.e., the range of the filter and thereby
result of the filter) can be of any size. In the case that the
Deriche or Shen is chosen it decreases by increasing the filter
parameter *`alpha`* and increases in the case of the Gauss
filter (and *`alpha`* corresponds to the standard deviation
of the Gaussian function). An approximation of the appropriate size
of the filter width *`alpha`* is performed by the operator
[`InfoSmooth`](info_smooth.md).

Non-recursive filters like the Gaussian filter are often implemented
using filter-masks. In this case the runtime of the operator
increases with increasing size of the filter mask. The runtime of
the recursive filters remains constant; except the border treatment
becomes a little bit more time consuming. The Gaussian filter
becomes slow in comparison to the recursive ones but is in contrast
to them isotropic (the filter 'deriche2' is only weakly direction
sensitive). A comparable result of the smoothing is achieved by
choosing the following values for the parameter:
Alpha(deriche2) = Alpha(deriche1) / 2,
Alpha(shen) = Alpha(deriche1) / 2,
Alpha(gauss) = 1.77 / Alpha(deriche1).

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Image to be smoothed.

**`imageSmooth`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Smoothed image.

**`filter`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Filter.

Default:
"deriche2"

List of values:
"deriche1", "deriche2", "gauss", "shen"

**`alpha`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Filter parameter: small values cause strong
smoothing (vice versa by using
*"gauss"*).

Default:
0.5

Suggested values:
0.1, 0.2, 0.3, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 7.0, 10.0

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`Alpha > 0`

## Example (HDevelop)

```
info_smooth('deriche2',0.5,Size,Coeffs)
smooth_image(Input,Smooth,'deriche2',7)
```

## Result

If the parameter values are correct the operator `SmoothImage`
returns the value 2 (
H_MSG_TRUE)
. The behavior in case of empty input (no
input images available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`ReadImage`

## Possible Successors

`Threshold`,
`DynThreshold`,
`Regiongrowing`

## Alternatives

`BinomialFilter`,
`GaussFilter`,
`MeanImage`,
`DerivateGauss`,
`IsotropicDiffusion`

## See also

`InfoSmooth`,
`MedianImage`,
`SigmaImage`,
`AnisotropicDiffusion`

## References

R.Deriche: “Fast Algorithms for Low-Level Vision”; IEEE Transactions
on Pattern Analysis and Machine Intelligence; PAMI-12, no. 1;
S. 78-87; 1990.

## Module

Foundation
