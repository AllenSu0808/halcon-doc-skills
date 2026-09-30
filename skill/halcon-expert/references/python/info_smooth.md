# info_smooth (Operator)

## Name

`info_smooth` — Information on smoothing filter [`smooth_image`](smooth_image.md).

## Signature

`def info_smooth(filter: str, alpha: float) -> Tuple[int, Sequence[int]]`

## Description

The operator `info_smooth` returns an estimation of the
width of the smoothing filters used in routine [`smooth_image`](smooth_image.md).
For this purpose the underlying continuous impulse answers of
*`filter`* are scanned until a filter coefficient is smaller
than five percent of the maximum coefficient (at the origin).
*`alpha`* is the filter parameter (see [`smooth_image`](smooth_image.md)).
Currently four filters are supported (parameter *`filter`*):
'deriche1', 'deriche2', 'shen' and 'gauss'.
The gauss filter was conventionally implemented with filter masks
(the other three are recursive filters). In the case of the gauss
filter the filter coefficients (of the one-dimensional impulse
answer $f(n)\text{with}n\ge0$) are returned
in *`coeffs`* in addition to the filter size.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`filter`** (input_control)  string `→` str

Name of required filter.

Default:
"deriche2"

List of values:
"deriche1", "deriche2", "gauss", "shen"

**`alpha`** (input_control)  real `→` float

Filter parameter: small values effect strong
smoothing (reversed in case of 'gauss').

Default:
0.5

Suggested values:
0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 7.0, 10.0

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`Alpha > 0.0`

**`size`** (output_control)  integer `→` int

Width of filter is approx. size x size pixels.

**`coeffs`** (output_control)  integer-array `→` Sequence[int]

In case of gauss filter: coefficients of the “positive”
half of the 1D impulse answer.

## Result

If the parameter values are correct the operator
`info_smooth` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`read_image`

## Possible Successors

`smooth_image`

## See also

`smooth_image`

## Module

Foundation
