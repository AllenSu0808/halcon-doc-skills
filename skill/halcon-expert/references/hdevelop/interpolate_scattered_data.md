# interpolate_scattered_data (Operator)

## Name

`interpolate_scattered_data` — Interpolation of scattered data using a scattered data interpolator.

## Signature

`interpolate_scattered_data( : : ScatteredDataInterpolatorHandle, Row, Column : ValueInterpolated)`

## Description

`interpolate_scattered_data` interpolates the values of the scattered
data points (*`Row`*,*`Column`*) by using the scattered data
interpolator *`ScatteredDataInterpolatorHandle`* and returns the result
in *`ValueInterpolated`*. In comparison to
[`interpolate_scattered_data_image`](interpolate_scattered_data_image.md),
`interpolate_scattered_data` also supports subpixel
coordinates for *`Row`* and *`Column`*. Before calling
`interpolate_scattered_data`, the scattered data interpolator must be
created with [`create_scattered_data_interpolator`](create_scattered_data_interpolator.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ScatteredDataInterpolatorHandle`** (input_control)  scattered_data_interpolator `→`  (handle)

Handle of the scattered data interpolator

**`Row`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinates of points
to be interpolated

**`Column`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinates of points
to be interpolated

**`ValueInterpolated`** (output_control)  number(-array) `→`  (real / integer)

Values of interpolated points

## Result

If the parameters are valid, the operator
`interpolate_scattered_data` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`create_scattered_data_interpolator`

## Possible Successors

`clear_scattered_data_interpolator`,
`gen_object_model_3d_from_points`

## Module

Foundation
