# interpolate_scattered_data (Operator)

## Name

`interpolate_scattered_data` — Interpolation of scattered data using a scattered data interpolator.

## Signature

`def interpolate_scattered_data(scattered_data_interpolator_handle: HHandle, row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]]) -> Sequence[Union[float, int]]`

`def interpolate_scattered_data_s(scattered_data_interpolator_handle: HHandle, row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]]) -> Union[float, int]`

## Description

`interpolate_scattered_data` interpolates the values of the scattered
data points (*`row`*,*`column`*) by using the scattered data
interpolator *`scattered_data_interpolator_handle`* and returns the result
in *`value_interpolated`*. In comparison to
[`interpolate_scattered_data_image`](interpolate_scattered_data_image.md),
`interpolate_scattered_data` also supports subpixel
coordinates for *`row`* and *`column`*. Before calling
`interpolate_scattered_data`, the scattered data interpolator must be
created with [`create_scattered_data_interpolator`](create_scattered_data_interpolator.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scattered_data_interpolator_handle`** (input_control)  scattered_data_interpolator `→` HHandle

Handle of the scattered data interpolator

**`row`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinates of points
to be interpolated

**`column`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinates of points
to be interpolated

**`value_interpolated`** (output_control)  number(-array) `→` Sequence[Union[float, int]]

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
