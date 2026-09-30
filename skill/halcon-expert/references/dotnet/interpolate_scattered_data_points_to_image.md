# InterpolateScatteredDataPointsToImage (Operator)

## Name

`InterpolateScatteredDataPointsToImage` — Creating an image from the interpolation of scattered data.

## Signature

`static void HOperatorSet.InterpolateScatteredDataPointsToImage(out HObject imageInterpolated, HTuple method, HTuple rows, HTuple columns, HTuple values, HTuple width, HTuple height, HTuple genParamName, HTuple genParamValue)`

## Description

`InterpolateScatteredDataPointsToImage` interpolates the
data points, given in *`rows`* and *`columns`* with the
corresponding measurement *`values`*,
and returns the result in *`imageInterpolated`*. The size of the output
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
[`InterpolateScatteredDataImage`](interpolate_scattered_data_image.md),
`InterpolateScatteredDataPointsToImage` also supports subpixel
coordinates for *`rows`* and *`columns`*.
If the same data points (*`rows`*,*`columns`*,*`values`*)
are used for the interpolation of different output images in subsequent
steps, the operator [`CreateScatteredDataInterpolator`](create_scattered_data_interpolator.md) may be more
efficient.

The following parameters can be adjusted with *`genParamName`* and
*`genParamValue`*:

- ***"alpha"*:** —

  The parameter *"alpha"* is a smoothing factor.
  For *"alpha"* = 0, all points passed in
  (*`rows`*,*`columns`*,*`values`*)
  are interpolated exactly. With *"alpha"* getting larger, the
  interpolation smoothes the points in way that all interpolated points of
  the result image *`imageInterpolated`* lie on a common plane.

  Default:
   *0*.

  Restriction:
   *"alpha"* >= *0*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageInterpolated`** (output_object)  singlechannelimage `→` [HImage](HImage.md) (real)

Interpolated image

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method for the interpolation

Default:
"thin_plate_splines"

Suggested values:
"thin_plate_splines"

**`rows`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of the points used for the interpolation

**`columns`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of the points
used for the interpolation

**`values`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Values of the points used for the interpolation

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the interpolated image

Default:
640

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the interpolated image

Default:
480

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters that can be adjusted

Default:
[]

Suggested values:
"alpha"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / string / int / long)

Values of the generic parameters that can be adjusted

Default:
[]

Suggested values:
0, 1.0, 10.0, 100.0

## Result

If the parameters are valid, the operator
`InterpolateScatteredDataPointsToImage` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Alternatives

`InterpolateScatteredDataImage`

## Module

Foundation
