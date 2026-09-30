# create_scattered_data_interpolator (Operator)

## Name

`create_scattered_data_interpolator` — Creates an interpolator for the interpolation of scattered data.

## Signature

`def create_scattered_data_interpolator(method: str, rows: Sequence[Union[float, int]], columns: Sequence[Union[float, int]], values: Sequence[Union[float, int]], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, int, float]]) -> HHandle`

## Description

`create_scattered_data_interpolator` creates the interpolator
*`scattered_data_interpolator_handle`* for the interpolation of
scattered data, given as data points in *`rows`* and
*`columns`* with the corresponding measurement *`values`*.
With the parameter *`method`* the algorithm
is specified, which should be used for the interpolation with
[`interpolate_scattered_data`](interpolate_scattered_data.md). So far, only the
*"thin_plate_splines"* are supported. This method interpolates on
a global scale, which means that all points are regarded for the
interpolation, no matter how far away they are. The influence of far points
is correlated to $r^{2}\cdot\log (r)$ where r defines
the distance of two points. In comparison to
[`interpolate_scattered_data_image`](interpolate_scattered_data_image.md),
`create_scattered_data_interpolator` also supports subpixel
coordinates for *`rows`* and *`columns`*. After the creation,
[`interpolate_scattered_data`](interpolate_scattered_data.md) is called for the interpolation of the
unknown values. By splitting up the creation
(`create_scattered_data_interpolator`)
and the evaluation ([`interpolate_scattered_data`](interpolate_scattered_data.md)) of the interpolator,
interpolating at different data points in subsequent steps becomes more
efficient since the interpolator has to be created only once.

The following parameters can be adjusted with *`gen_param_name`* and
*`gen_param_value`*:

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

**`method`** (input_control)  string `→` str

Method for the interpolation

Default:
"thin_plate_splines"

Suggested values:
"thin_plate_splines"

**`rows`** (input_control)  point.y-array `→` Sequence[Union[float, int]]

Row coordinates of the points used
for the interpolation

**`columns`** (input_control)  point.x-array `→` Sequence[Union[float, int]]

Column coordinates of the points used
for the interpolation

**`values`** (input_control)  number-array `→` Sequence[Union[float, int]]

Values of the points used
for the interpolation

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Names of the generic parameters
that can be adjusted

Default:
[]

Suggested values:
"alpha"

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[str, int, float]]

Values of the generic parameters
that can be adjusted

Default:
[]

Suggested values:
0, 1.0, 10.0, 100.0

**`scattered_data_interpolator_handle`** (output_control)  scattered_data_interpolator `→` HHandle

Handle of the scattered data interpolator

## Result

If the parameters are valid, the operator
`create_scattered_data_interpolator` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Successors

`interpolate_scattered_data`

## Module

Foundation
