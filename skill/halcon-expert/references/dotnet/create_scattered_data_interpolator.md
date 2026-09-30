# CreateScatteredDataInterpolator (Operator)

## Name

`CreateScatteredDataInterpolator` — Creates an interpolator for the interpolation of scattered data.

## Signature

`static void HOperatorSet.CreateScatteredDataInterpolator(HTuple method, HTuple rows, HTuple columns, HTuple values, HTuple genParamName, HTuple genParamValue, out HTuple scatteredDataInterpolatorHandle)`

`public HScatteredDataInterpolator(string method, HTuple rows, HTuple columns, HTuple values, HTuple genParamName, HTuple genParamValue)`

`void HScatteredDataInterpolator.CreateScatteredDataInterpolator(string method, HTuple rows, HTuple columns, HTuple values, HTuple genParamName, HTuple genParamValue)`

## Description

`CreateScatteredDataInterpolator` creates the interpolator
*`scatteredDataInterpolatorHandle`* for the interpolation of
scattered data, given as data points in *`rows`* and
*`columns`* with the corresponding measurement *`values`*.
With the parameter *`method`* the algorithm
is specified, which should be used for the interpolation with
[`InterpolateScatteredData`](interpolate_scattered_data.md). So far, only the
*"thin_plate_splines"* are supported. This method interpolates on
a global scale, which means that all points are regarded for the
interpolation, no matter how far away they are. The influence of far points
is correlated to $r^{2}\cdot\log (r)$ where r defines
the distance of two points. In comparison to
[`InterpolateScatteredDataImage`](interpolate_scattered_data_image.md),
`CreateScatteredDataInterpolator` also supports subpixel
coordinates for *`rows`* and *`columns`*. After the creation,
[`InterpolateScatteredData`](interpolate_scattered_data.md) is called for the interpolation of the
unknown values. By splitting up the creation
(`CreateScatteredDataInterpolator`)
and the evaluation ([`InterpolateScatteredData`](interpolate_scattered_data.md)) of the interpolator,
interpolating at different data points in subsequent steps becomes more
efficient since the interpolator has to be created only once.

The following parameters can be adjusted with *`genParamName`* and
*`genParamValue`*:

- ***"alpha"*:** —

  The parameter *"alpha"* is a smoothing factor.
  For *"alpha"* = 0, all points passed in
  *`rows`*, *`columns`*, and *`values`*
  are interpolated exactly. With *"alpha"* getting larger, the
  interpolation smoothes the points in way that all interpolated points
  lie on a common plane.

  Default:
   *0*

  Restriction:
   *"alpha"* >= *0*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method for the interpolation

Default:
"thin_plate_splines"

Suggested values:
"thin_plate_splines"

**`rows`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of the points used
for the interpolation

**`columns`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of the points used
for the interpolation

**`values`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Values of the points used
for the interpolation

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters
that can be adjusted

Default:
[]

Suggested values:
"alpha"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / string / int / long)

Values of the generic parameters
that can be adjusted

Default:
[]

Suggested values:
0, 1.0, 10.0, 100.0

**`scatteredDataInterpolatorHandle`** (output_control)  scattered_data_interpolator `→` [HScatteredDataInterpolator](HScatteredDataInterpolator.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the scattered data interpolator

## Result

If the parameters are valid, the operator
`CreateScatteredDataInterpolator` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Successors

`InterpolateScatteredData`

## Module

Foundation
