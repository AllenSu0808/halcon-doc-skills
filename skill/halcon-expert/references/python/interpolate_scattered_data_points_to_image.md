# interpolate_scattered_data_points_to_image (Operator)

## Name

`interpolate_scattered_data_points_to_image` — Creating an image from the interpolation of scattered data.

## Signature

`def interpolate_scattered_data_points_to_image(method: str, rows: Sequence[Union[float, int]], columns: Sequence[Union[float, int]], values: Sequence[Union[float, int]], width: int, height: int, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, int, float]]) -> HObject`

## Description

`interpolate_scattered_data_points_to_image` interpolates the
data points, given in *`rows`* and *`columns`* with the
corresponding measurement *`values`*,
and returns the result in *`image_interpolated`*. The size of the output
image is defined by its *`width`* and its *`height`* with the upper
left corner at (0,0). In order to interpolate at negative coordinates of
(*`rows`*,*`columns`*), simply translate all input points
accordingly. With the parameter *`method`* the interpolation algorithm
is specified. So far, only the
*"thin_plate_splines"* are supported. This method interpolates on
a global scale, which means that all points are regarded for the
interpolation, no matter how far away they are. The influence of far points
is correlated to $r^{2}\cdot\log (r)$ where r defines
the distance of two points. In comparison to
[`interpolate_scattered_data_image`](interpolate_scattered_data_image.md),
`interpolate_scattered_data_points_to_image` also supports subpixel
coordinates for *`rows`* and *`columns`*.
If the same data points (*`rows`*,*`columns`*,*`values`*)
are used for the interpolation of different output images in subsequent
steps, the operator [`create_scattered_data_interpolator`](create_scattered_data_interpolator.md) may be more
efficient.

The following parameters can be adjusted with *`gen_param_name`* and
*`gen_param_value`*:

- ***"alpha"*:** —

  The parameter *"alpha"* is a smoothing factor.
  For *"alpha"* = 0, all points passed in
  (*`rows`*,*`columns`*,*`values`*)
  are interpolated exactly. With *"alpha"* getting larger, the
  interpolation smoothes the points in way that all interpolated points of
  the result image *`image_interpolated`* lie on a common plane.

  Default:
   *0*.

  Restriction:
   *"alpha"* >= *0*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_interpolated`** (output_object)  singlechannelimage `→` HObject (real)

Interpolated image

**`method`** (input_control)  string `→` str

Method for the interpolation

Default:
"thin_plate_splines"

Suggested values:
"thin_plate_splines"

**`rows`** (input_control)  point.y-array `→` Sequence[Union[float, int]]

Row coordinates of the points used for the interpolation

**`columns`** (input_control)  point.x-array `→` Sequence[Union[float, int]]

Column coordinates of the points
used for the interpolation

**`values`** (input_control)  number-array `→` Sequence[Union[float, int]]

Values of the points used for the interpolation

**`width`** (input_control)  extent.x `→` int

Width of the interpolated image

Default:
640

**`height`** (input_control)  extent.y `→` int

Height of the interpolated image

Default:
480

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Names of the generic parameters that can be adjusted

Default:
[]

Suggested values:
"alpha"

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[str, int, float]]

Values of the generic parameters that can be adjusted

Default:
[]

Suggested values:
0, 1.0, 10.0, 100.0

## Result

If the parameters are valid, the operator
`interpolate_scattered_data_points_to_image` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Alternatives

`interpolate_scattered_data_image`

## Module

Foundation
