# interpolate_scattered_data_image (Operator)

## Name

`interpolate_scattered_data_image` — Interpolation of an image.

## Signature

`interpolate_scattered_data_image(Image, RegionInterpolate : ImageInterpolated : Method, GenParamName, GenParamValue : )`

## Description

`interpolate_scattered_data_image` interpolates the *`Image`*
at the region *`RegionInterpolate`* and returns the result in
*`ImageInterpolated`*. The difference of the domain of the
*`Image`* and the region *`RegionInterpolate`* specifies the valid
data points that can be used for the interpolation whereas
*`RegionInterpolate`* specifies the points, where the
gray values of the *`Image`* should be determined.
With the parameter *`Method`* the interpolation algorithm
is specified. So far, only the
*'thin_plate_splines'* are supported. This method interpolates on
a global scale, which means that all points are regarded for the
interpolation, no matter how far away they are. The influence of far points
is correlated to $r^{2}\cdot\log (r)$ where r defines
the distance of two points. If the same *`Image`* is interpolated at
different points in subsequent steps, the operator
[`create_scattered_data_interpolator`](create_scattered_data_interpolator.md) may be more efficient.

The following parameters can be adjusted with *`GenParamName`* and
*`GenParamValue`*:

- ***'alpha'*:** —

  The parameter *'alpha'* is a smoothing factor.
  For *'alpha'* = 0, all points in the image *`Image`*
  are interpolated exactly. With *'alpha'* getting larger, the
  interpolation smoothes the image points in way that all interpolated
  points of the result image *`ImageInterpolated`* lie on a common
  plane.

  Default:
   is *0*

  Restriction:
   *'alpha'* >= *0*

`interpolate_scattered_data_image` is best used with very few data
points, e.g, less than 1000. In order to reconstruct
destroyed image data in the region *`RegionInterpolate`*, the data
points should be reduced to an appropriate number, e.g., by only using the
border pixels of the hole regions. An example program is shown below.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2 / real)

Image to interpolate

**`RegionInterpolate`** (input_object)  region `→` object

Region to interpolate

**`ImageInterpolated`** (output_object)  singlechannelimage `→` object (real)

Interpolated image

**`Method`** (input_control)  string `→`  (string)

Method for the interpolation

Default:
'thin_plate_splines'

Suggested values:
'thin_plate_splines'

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Names of the generic parameters that can be adjusted

Default:
[]

Suggested values:
'alpha'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (string / integer / real)

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
