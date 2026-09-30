# InterpolateScatteredData (Operator)

## Name

`InterpolateScatteredData` — Interpolation of scattered data using a scattered data interpolator.

## Signature

`static void HOperatorSet.InterpolateScatteredData(HTuple scatteredDataInterpolatorHandle, HTuple row, HTuple column, out HTuple valueInterpolated)`

`HTuple HScatteredDataInterpolator.InterpolateScatteredData(HTuple row, HTuple column)`

`double HScatteredDataInterpolator.InterpolateScatteredData(double row, double column)`

## Description

`InterpolateScatteredData` interpolates the values of the scattered
data points (*`row`*,*`column`*) by using the scattered data
interpolator *`scatteredDataInterpolatorHandle`* and returns the result
in *`valueInterpolated`*. In comparison to
[`InterpolateScatteredDataImage`](interpolate_scattered_data_image.md),
`InterpolateScatteredData` also supports subpixel
coordinates for *`row`* and *`column`*. Before calling
`InterpolateScatteredData`, the scattered data interpolator must be
created with [`CreateScatteredDataInterpolator`](create_scattered_data_interpolator.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scatteredDataInterpolatorHandle`** (input_control)  scattered_data_interpolator `→` [HScatteredDataInterpolator](HScatteredDataInterpolator.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the scattered data interpolator

**`row`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of points
to be interpolated

**`column`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of points
to be interpolated

**`valueInterpolated`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Values of interpolated points

## Result

If the parameters are valid, the operator
`InterpolateScatteredData` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`CreateScatteredDataInterpolator`

## Possible Successors

`ClearScatteredDataInterpolator`,
`GenObjectModel3dFromPoints`

## Module

Foundation
