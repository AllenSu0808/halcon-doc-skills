# LocalMinMaxFunct1d (Operator)

## Name

`LocalMinMaxFunct1d` — Calculate the local minimum and maximum points of a function.

## Signature

`static void HOperatorSet.LocalMinMaxFunct1d(HTuple function, HTuple mode, HTuple interpolation, out HTuple min, out HTuple max)`

`void HFunction1D.LocalMinMaxFunct1d(string mode, string interpolation, out HTuple min, out HTuple max)`

## Description

`LocalMinMaxFunct1d` searches for the local minima
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

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Handling of plateaus

Default:
"strict_min_max"

List of values:
"plateaus_center", "strict_min_max"

**`interpolation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Interpolation of the input function

Default:
"true"

List of values:
"false", "true"

**`min`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Minimum points of the input function

**`max`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Maximum points of the input function

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`,
`SmoothFunct1dGauss`,
`SmoothFunct1dMean`

## Module

Foundation
