# interpolate_scattered_data_image (Operator)

## Name

`interpolate_scattered_data_image` — Interpolation of an image.

## Signature

`def interpolate_scattered_data_image(image: HObject, region_interpolate: HObject, method: str, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, int, float]]) -> HObject`

## Description

`interpolate_scattered_data_image` interpolates the *`image`*
at the region *`region_interpolate`* and returns the result in
*`image_interpolated`*. The difference of the domain of the
*`image`* and the region *`region_interpolate`* specifies the valid
data points that can be used for the interpolation whereas
*`region_interpolate`* specifies the points, where the
gray values of the *`image`* should be determined.
With the parameter *`method`* the interpolation algorithm
is specified. So far, only the
*"thin_plate_splines"* are supported. This method interpolates on
a global scale, which means that all points are regarded for the
interpolation, no matter how far away they are. The influence of far points
is correlated to $r^{2}\cdot\log (r)$ where r defines
the distance of two points. If the same *`image`* is interpolated at
different points in subsequent steps, the operator
[`create_scattered_data_interpolator`](create_scattered_data_interpolator.md) may be more efficient.

The following parameters can be adjusted with *`gen_param_name`* and
*`gen_param_value`*:

- ***"alpha"*:** —

  The parameter *"alpha"* is a smoothing factor.
  For *"alpha"* = 0, all points in the image *`image`*
  are interpolated exactly. With *"alpha"* getting larger, the
  interpolation smoothes the image points in way that all interpolated
  points of the result image *`image_interpolated`* lie on a common
  plane.

  Default:
   is *0*

  Restriction:
   *"alpha"* >= *0*

`interpolate_scattered_data_image` is best used with very few data
points, e.g, less than 1000. In order to reconstruct
destroyed image data in the region *`region_interpolate`*, the data
points should be reduced to an appropriate number, e.g., by only using the
border pixels of the hole regions. An example program is shown below.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2 / real)

Image to interpolate

**`region_interpolate`** (input_object)  region `→` HObject

Region to interpolate

**`image_interpolated`** (output_object)  singlechannelimage `→` HObject (real)

Interpolated image

**`method`** (input_control)  string `→` str

Method for the interpolation

Default:
"thin_plate_splines"

Suggested values:
"thin_plate_splines"

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

## Example (HDevelop)

```
* This example program shows how to use the scattered data interpolator
* to fill holes in an image
gen_image_surface_second_order (ImageData, 'real', 1, 1, 0, 0, 0, 1, \
                                24, 24, 48, 48)
gen_circle (Circle, 12, 12, 6)
difference (ImageData, Circle, Region)
reduce_domain (ImageData, Region, ImageReduced)
dev_clear_window ()
dev_display (ImageReduced)
stop()
*
* Select only border pixels for the interpolation
dilation_circle (Circle, CircleDilation, 1.5)
intersection (CircleDilation, Region, RegionBorderData)
dev_clear_window ()
dev_display (ImageReduced)
dev_display (RegionBorderData)
stop()
*
* Interpolate pixels
reduce_domain (ImageData, RegionBorderData, ImageReducedBorder)
interpolate_scattered_data_image (ImageReducedBorder, Circle, \
                                  ImageInterpolated, \
                                  'thin_plate_splines', [], [])
paint_gray (ImageInterpolated, ImageData, ImageFilled)
dev_clear_window ()
dev_display (ImageFilled)
```

## Result

If the parameters are valid, the operator
`interpolate_scattered_data_image` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Alternatives

`interpolate_scattered_data_points_to_image`

## Module

Foundation
