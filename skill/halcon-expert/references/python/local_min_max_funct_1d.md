# local_min_max_funct_1d (Operator)

## Name

`local_min_max_funct_1d` — Calculate the local minimum and maximum points of a function.

## Signature

`def local_min_max_funct_1d(function: Sequence[Union[float, int]], mode: str, interpolation: str) -> Tuple[Sequence[float], Sequence[float]]`

## Description

`local_min_max_funct_1d` searches for the local minima
*`min`* and maxima *`max`* of the function
*`function`*.

Since the function values are only known at discrete sampling
points, the function can interpolated by parabolas between these
points. Setting the parameter *`interpolation`* to
*"true"*, enables this feature. If *`interpolation`* is
*"false"*, extrema are always sampling points.

If *`mode`* is set to *"strict_min_max"*, extrema are
only calculated close to points with a function value that is
strictly smaller or strictly greater than the values of its direct
neighbors.

If *`mode`* is set to *"plateaus_center"*, areas with a
function value that is constant throughout several sampling points
are also considered. If such an area is identified as being a flat
extremum, its center coordinate is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function

**`mode`** (input_control)  string `→` str

Handling of plateaus

Default:
"strict_min_max"

List of values:
"plateaus_center", "strict_min_max"

**`interpolation`** (input_control)  string `→` str

Interpolation of the input function

Default:
"true"

List of values:
"false", "true"

**`min`** (output_control)  real-array `→` Sequence[float]

Minimum points of the input function

**`max`** (output_control)  real-array `→` Sequence[float]

Maximum points of the input function

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`,
`smooth_funct_1d_gauss`,
`smooth_funct_1d_mean`

## Module

Foundation
