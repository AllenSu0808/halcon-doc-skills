# InfoEdges (Operator)

## Name

`InfoEdges` — Return the filter coefficients of a filter in [`EdgesImage`](edges_image.md).

## Signature

`static void HOperatorSet.InfoEdges(HTuple filter, HTuple mode, HTuple alpha, out HTuple size, out HTuple coeffs)`

`static int HMisc.InfoEdges(string filter, string mode, double alpha, out HTuple coeffs)`

## Description

`InfoEdges` returns the coefficients *`coeffs`* and an estimate
of the width *`size`* of any of the filters used in [`EdgesImage`](edges_image.md).
To do so, the corresponding continuous impulse responses of the filters are
sampled until the first filter coefficient is smaller than five
percent of the largest coefficient. *`alpha`* is the filter
parameter (see [`EdgesImage`](edges_image.md)). Seven edge operators are
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

**`filter`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the edge operator.

Default:
"lanser2"

List of values:
"canny", "deriche1", "deriche2", "lanser1", "lanser2", "mshen", "shen"

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

1D edge filter ('edge') or 1D smoothing filter
('smooth').

Default:
"edge"

List of values:
"edge", "smooth"

**`alpha`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

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

**`size`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Filter width in pixels.

**`coeffs`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

For Canny filters: Coefficients of the “positive”
half of the 1D impulse response.
All others: Coefficients of a corresponding non-recursive
filter.

## Example (HDevelop)

```
read_image(Image,'fabrik')
info_edges('lanser2','edge',0.5,Size,Coeffs)
edges_image(Image,Amp,Dir,'lanser2',0.5,'none',-1,-1)
hysteresis_threshold(Amp,Margin,20,30,30)
```

## Result

`InfoEdges` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Successors

`EdgesImage`,
`Threshold`,
`Skeleton`

## See also

`EdgesImage`

## Module

Foundation
