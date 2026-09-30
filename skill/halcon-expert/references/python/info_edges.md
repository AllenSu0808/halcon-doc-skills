# info_edges (Operator)

## Name

`info_edges` — Return the filter coefficients of a filter in [`edges_image`](edges_image.md).

## Signature

`def info_edges(filter: str, mode: str, alpha: float) -> Tuple[int, Sequence[int]]`

## Description

`info_edges` returns the coefficients *`coeffs`* and an estimate
of the width *`size`* of any of the filters used in [`edges_image`](edges_image.md).
To do so, the corresponding continuous impulse responses of the filters are
sampled until the first filter coefficient is smaller than five
percent of the largest coefficient. *`alpha`* is the filter
parameter (see [`edges_image`](edges_image.md)). Seven edge operators are
supported (parameter *`filter`*):

*"deriche1"*, *"lanser1"*, *"deriche2"*,
*"lanser2"*, *"shen"*, *"mshen"* and *"canny"*.

The parameter *`mode`* (*"edge"*/*"smooth"*) is used to
determine whether the corresponding edge or smoothing operator is to be
sampled.

The Canny operator (which uses Gaussian smoothing)
is implemented using conventional filter masks. Therefore, for the Canny
filter, the coefficients *`coeffs`* of the one-dimensional impulse
responses are returned as $f(n)\text{with}n\ge0$. All
other filters are implemented recursively; here, the *`coeffs`* are
coefficients of a corresponding non-recursive filter.

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

Name of the edge operator.

Default:
"lanser2"

List of values:
"canny", "deriche1", "deriche2", "lanser1", "lanser2", "mshen", "shen"

**`mode`** (input_control)  string `→` str

1D edge filter ('edge') or 1D smoothing filter
('smooth').

Default:
"edge"

List of values:
"edge", "smooth"

**`alpha`** (input_control)  real `→` float

Filter parameter: small values result in strong
smoothing, and thus less detail (opposite for
'canny').

Default:
0.5

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`Alpha > 0.0`

**`size`** (output_control)  integer `→` int

Filter width in pixels.

**`coeffs`** (output_control)  integer-array `→` Sequence[int]

For Canny filters: Coefficients of the “positive”
half of the 1D impulse response.
All others: Coefficients of a corresponding non-recursive
filter.

## Result

`info_edges` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Successors

`edges_image`,
`threshold`,
`skeleton`

## See also

`edges_image`

## Module

Foundation
