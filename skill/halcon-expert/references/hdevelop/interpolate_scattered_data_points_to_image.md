# interpolate_scattered_data_points_to_image (Operator)

## Name

`interpolate_scattered_data_points_to_image` — Creating an image from the interpolation of scattered data.

## Signature

`interpolate_scattered_data_points_to_image( : ImageInterpolated : Method, Rows, Columns, Values, Width, Height, GenParamName, GenParamValue : )`

## Description

`interpolate_scattered_data_points_to_image` interpolates the
data points, given in *`Rows`* and *`Columns`* with the
corresponding measurement *`Values`*,
and returns the result in *`ImageInterpolated`*. The size of the output
image is defined by its *`Width`* and its *`Height`* with the upper
left corner at (0,0). In order to interpolate at negative coordinates of
(*`Rows`*,*`Columns`*), simply translate all input points
accordingly. With the parameter *`Method`* the interpolation algorithm
is specified. So far, only the
*'thin_plate_splines'* are supported. This method interpolates on
a global scale, which means that all points are regarded for the
interpolation, no matter how far away they are. The influence of far points
is correlated to $r^{2}\cdot\log (r)$ where r defines
the distance of two points. In comparison to
[`interpolate_scattered_data_image`](interpolate_scattered_data_image.md),
`interpolate_scattered_data_points_to_image` also supports subpixel
coordinates for *`Rows`* and *`Columns`*.
If the same data points (*`Rows`*,*`Columns`*,*`Values`*)
are used for the interpolation of different output images in subsequent
steps, the operator [`create_scattered_data_interpolator`](create_scattered_data_interpolator.md) may be more
efficient.

The following parameters can be adjusted with *`GenParamName`* and
*`GenParamValue`*:

- ***'alpha'*:** —

  The parameter *'alpha'* is a smoothing factor.
  For *'alpha'* = 0, all points passed in
  (*`Rows`*,*`Columns`*,*`Values`*)
  are interpolated exactly. With *'alpha'* getting larger, the
  interpolation smoothes the points in way that all interpolated points of
  the result image *`ImageInterpolated`* lie on a common plane.

  Default:
   *0*.

  Restriction:
   *'alpha'* >= *0*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ImageInterpolated`** (output_object)  singlechannelimage `→` object (real)

Interpolated image

**`Method`** (input_control)  string `→`  (string)

Method for the interpolation

Default:
'thin_plate_splines'

Suggested values:
'thin_plate_splines'

**`Rows`** (input_control)  point.y-array `→`  (real / integer)

Row coordinates of the points used for the interpolation

**`Columns`** (input_control)  point.x-array `→`  (real / integer)

Column coordinates of the points
used for the interpolation

**`Values`** (input_control)  number-array `→`  (real / integer)

Values of the points used for the interpolation

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the interpolated image

Default:
640

**`Height`** (input_control)  extent.y `→`  (integer)

Height of the interpolated image

Default:
480

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Names of the generic parameters that can be adjusted

Default:
[]

Suggested values:
'alpha'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (real / string / integer)

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
