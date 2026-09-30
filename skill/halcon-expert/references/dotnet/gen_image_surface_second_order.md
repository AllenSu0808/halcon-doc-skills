# GenImageSurfaceSecondOrder (Operator)

## Name

`GenImageSurfaceSecondOrder` — Create a curved gray surface with second order polynomial.

## Signature

`static void HOperatorSet.GenImageSurfaceSecondOrder(out HObject imageSurface, HTuple type, HTuple alpha, HTuple beta, HTuple gamma, HTuple delta, HTuple epsilon, HTuple zeta, HTuple row, HTuple column, HTuple width, HTuple height)`

`void HImage.GenImageSurfaceSecondOrder(string type, double alpha, double beta, double gamma, double delta, double epsilon, double zeta, double row, double column, int width, int height)`

## Description

The operator `GenImageSurfaceSecondOrder` creates a curved
gray value surface according to the following equation:
$$ImageSurface(r,c) = Alpha(r-Row)^2 + Beta(c-Column)^2 + Gamma(r-Row) * (c-Column) + Delta(r-Row) + Epsilon(c-Column) + Zeta$$ ![figure](../assets/6afc183f59ea95c8.svg)
The size of the image is determined by *`width`* and *`height`*.
The parameters *`row`* and *`column`* define the reference point
of the created gray surface. If [`FitSurfaceSecondOrder`](fit_surface_second_order.md) was used to
determine the parameters of the gray surface, this reference point should
correspond to the center of gravity that is used in the surface equation
(see [`FitSurfaceSecondOrder`](fit_surface_second_order.md)). Its coordinates can be computed as
follows:

|  |
| --- |
| [`Intersection(ROI, Image, RegionIntersection)`](intersection.md) |
| `fit_surface_second_order(RegionIntersection, Image, Algorithm, Iterations, ClippingFactor, Alpha, Beta, Gamma, Delta, Epsilon, Zeta)` |
| [`AreaCenter(RegionIntersection, Area, Row, Column)`](area_center.md) |
| `GenImageSurfaceSecondOrder(ImageSurface, Type, Alpha, Beta, Gamma, Delta, Epsilon, Zeta, Row, Column, Width, Height)` |

The gray values are of the type *`type`* (see [`GenImageConst`](gen_image_const.md)
for a detailed description of the pixel types).
Gray values outside the valid area are clipped.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageSurface`** (output_object)  image `→` [HImage](HImage.md) (byte / uint2 / real)

Created image with new image matrix.

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Pixel type.

Default:
"byte"

List of values:
"byte", "real", "uint2"

**`alpha`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Second order coefficient in vertical direction.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`beta`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Second order coefficient in horizontal direction.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`gamma`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Mixed second order coefficient.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`delta`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

First order coefficient in vertical direction.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`epsilon`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

First order coefficient in horizontal direction.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`zeta`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Zero order coefficient.

Default:
1.0

Suggested values:
-2.0, -1.0, -0.5, -0.0, 0.5, 1.0, 2.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`row`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the reference point of the surface.

Default:
256.0

Suggested values:
0.0, 128.0, 256.0, 512.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`column`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the reference point of the surface.

Default:
256.0

Suggested values:
0.0, 128.0, 256.0, 512.0

Minimum increment:
0.000001

Recommended increment:
-0.005

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of image.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
width` (lin)

Minimum increment:
1

Recommended increment:
10

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of image.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
height` (lin)

Minimum increment:
1

Recommended increment:
10

## Example (HDevelop)

```
* Adjust an inhomogeneous illumination
* using gen_image_surface_second_order
read_image (Image, 'cap_illumination/cap_illumination_01')
get_image_size (Image, Width, Height)
gen_circle (Circle, 495, 630, 350.5)
difference (Image, Circle, RegionDifference)
fit_surface_second_order (RegionDifference, Image, 'regression', 5, 2, \
                          Alpha, Beta, Gamma, Delta, Epsilon, Zeta)
area_center (RegionDifference, Area, Row, Column)
gen_image_surface_second_order (ImageSurface, 'byte', Alpha, Beta, \
                                Gamma, Delta, Epsilon, Zeta, Row, Column, \
                                Width, Height)
sub_image (Image, ImageSurface, ImageSub, 1, 128)
```

## Result

If the parameter values are correct `GenImageSurfaceSecondOrder`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`FitSurfaceSecondOrder`

## Possible Successors

`SubImage`

## See also

`GenImageGrayRamp`,
`GenImageSurfaceFirstOrder`,
`GenImageConst`

## Module

Foundation
