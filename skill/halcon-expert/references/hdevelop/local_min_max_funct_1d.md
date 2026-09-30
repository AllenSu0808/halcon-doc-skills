# local_min_max_funct_1d (Operator)

## Name

`local_min_max_funct_1d` — Calculate the local minimum and maximum points of a function.

## Signature

`local_min_max_funct_1d( : : Function, Mode, Interpolation : Min, Max)`

## Description

`local_min_max_funct_1d` searches for the local minima
*`Min`* and maxima *`Max`* of the function
*`Function`*.

Since the function values are only known at discrete sampling
points, the function can interpolated by parabolas between these
points. Setting the parameter *`Interpolation`* to
*'true'*, enables this feature. If *`Interpolation`* is
*'false'*, extrema are always sampling points.

If *`Mode`* is set to *'strict_min_max'*, extrema are
only calculated close to points with a function value that is
strictly smaller or strictly greater than the values of its direct
neighbors.

If *`Mode`* is set to *'plateaus_center'*, areas with a
function value that is constant throughout several sampling points
are also considered. If such an area is identified as being a flat
extremum, its center coordinate is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function

**`Mode`** (input_control)  string `→`  (string)

Handling of plateaus

Default:
'strict_min_max'

List of values:
'plateaus_center', 'strict_min_max'

**`Interpolation`** (input_control)  string `→`  (string)

Interpolation of the input function

Default:
'true'

List of values:
'false', 'true'

**`Min`** (output_control)  real-array `→`  (real)

Minimum points of the input function

**`Max`** (output_control)  real-array `→`  (real)

Maximum points of the input function

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`,
`smooth_funct_1d_gauss`,
`smooth_funct_1d_mean`

## Module

Foundation
