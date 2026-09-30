# BinocularDisparityMs (Operator)

## Name

`BinocularDisparityMs` — Compute the disparities of a rectified stereo image pair using
multi-scanline optimization.

## Signature

`static void HOperatorSet.BinocularDisparityMs(HObject imageRect1, HObject imageRect2, out HObject disparity, out HObject score, HTuple minDisparity, HTuple maxDisparity, HTuple surfaceSmoothing, HTuple edgeSmoothing, HTuple genParamName, HTuple genParamValue)`

`HImage HImage.BinocularDisparityMs(HImage imageRect2, out HImage score, int minDisparity, int maxDisparity, int surfaceSmoothing, int edgeSmoothing, HTuple genParamName, HTuple genParamValue)`

`HImage HImage.BinocularDisparityMs(HImage imageRect2, out HImage score, int minDisparity, int maxDisparity, int surfaceSmoothing, int edgeSmoothing, string genParamName, string genParamValue)`

## Description

`BinocularDisparityMs` calculates the disparity between two
rectified stereo images *`imageRect1`* and *`imageRect2`*
using multi-scanline optimization. The resulting disparity image is
returned in *`disparity`*.
In contrast to [`BinocularDistanceMs`](binocular_distance_ms.md), the results are
not transformed into distance values.

For this task, the three operators [`BinocularDisparity`](binocular_disparity.md),
[`BinocularDisparityMg`](binocular_disparity_mg.md), and `BinocularDisparityMs`
can be used. [`BinocularDisparity`](binocular_disparity.md) returns robust results
in regions of sufficient texture but fails where there is none.
[`BinocularDisparityMg`](binocular_disparity_mg.md) interpolates low-texture regions
but blurs discontinuities. `BinocularDisparityMs` preserves
discontinuities and interpolates partially.

`BinocularDisparityMs` requires a reference image
*`imageRect1`* and a search image *`imageRect2`* which both
must be rectified, i.e., corresponding pixels must have the same
row coordinate. If this assumption is violated, the images
can be rectified by using the operators [`CalibrateCameras`](calibrate_cameras.md),
[`GenBinocularRectificationMap`](gen_binocular_rectification_map.md), and [`MapImage`](map_image.md).

*`imageRect1`* and *`imageRect2`* can have different widths
but must have the same height. Given a pixel in *`imageRect1`*,
the homologous pixel in *`imageRect2`* is selected by searching
along the corresponding row in *`imageRect2`*
and matching both pixels based on a similarity measure.
The disparity is the number of pixels
by which each pixel in *`imageRect1`* needs to be moved
to reach the homologous pixel in *`imageRect2`*.

The search space is confined by the minimum and maximum disparity
values *`minDisparity`* and *`maxDisparity`*. If the
minimum and maximum disparity values are set to an empty tuple, they
are automatically set to the maximum possible range for the
given images *`imageRect1`*.

To calculate the disparities from the similarity measure,
the intermediate results are optimized by a multi-scanline method.
The optimization increases the robustness in low-texture areas
without blurring discontinuities in the disparity image.
The optimization is controlled by the parameters
*`surfaceSmoothing`* and *`edgeSmoothing`*.
*`surfaceSmoothing`* controls the smoothness within surfaces.
High values suppress disparity differences of one pixel.
*`edgeSmoothing`* controls the occurrence and the shape of edges.
Low values allow many edges, high values lead to fewer and rounder edges.
For both parameters, reasonable values usually range between 0 and 100.
If both parameters are set to zero, no optimization is performed.

The calculation of the disparities can be controlled by generic
parameters. The following generic parameters *`genParamName`*
and the corresponding values *`genParamValue`* are supported:

- ***"consistency_check"*** —

  Activates an optional post-processing step to increase robustness.
  Concurrent direct and reverse matches between
  reference patterns in *`imageRect1`* and *`imageRect2`* are
  required for a disparity value to be returned.
  The check is switched off by setting *`genParamValue`*
  to *"false"*.

  List of values:
   *"true"*, *"false"*.

  Default:
   *"true"*.
- ***"disparity_offset"*** —

  Adapts the quality of the coarse-to-fine approach at discontinuities.
  The higher the value set in *`genParamValue`*, the more runtime is
  required.

  Suggested values:
   *2*, *3*, *4*.

  Default:
   *3*.
- ***"method"*:** —

  Determines the method used to calculate the disparities. The following
  parameters *`genParamValue`* can be set:

  - *"accurate"*:
    Most accurate calculation method, but requires more runtime and memory
    compared to the remaining methods.
  - *"fast"*:
    Uses a coarse-to-fine scheme to improve the runtime.
    The coarse-to-fine scheme works in a similar way to the scheme explained
    in [`BinocularDisparity`](binocular_disparity.md).

    The coarse-to-fine method requires
    significantly less memory and is significantly faster
    than the *"accurate"* method, especially for large
    images or a large range of *`minDisparity`* and
    *`maxDisparity`*.
    The coarse-to-fine scheme has the further advantage that it
    automatically estimates the range of *`minDisparity`* and
    *`maxDisparity`* while traversing through the pyramid. As a
    consequence, neither *`minDisparity`*
    nor *`maxDisparity`* needs to be set. However, the generated
    disparity images are less accurate for the *"fast"* method
    than for the default *"accurate"* approach. Especially
    at sharp disparity jumps the *"fast"* method preserves
    discontinuities less accurately.
  - *"very_fast"*:
    Also uses a coarse-to-fine scheme to improve the runtime even further.
    However, this approach makes numerous assumptions that may lead
    to a smoothing of the disparities at discontinuities. Per default,
    the number of levels of the coarse-to-fine scheme is estimated
    automatically. It is possible to set the number of levels
    explicitly (see *"num_levels"*).

  The runtime of the operator is approximately linear to the image width,
  the image height, and the disparity range. Consequently, the disparity
  range should be chosen as narrow as possible for large images. The
  runtime of the coarse-to-fine scheme (which is used for
  *"fast"* or *"very_fast"*) is approximately linear to
  the image width and the image height. For small images and small
  disparity ranges the runtime of the coarse-to-fine scheme may be
  larger than that of the *"accurate"* scheme.

  List of values:
   *"accurate"*, *"fast"*, *"very_fast"*.

  Default:
   *"accurate"*.
- ***"num_levels"*:** —

  Determines the number of pyramid levels that are used for the coarse-to-fine
  scheme. By setting *`genParamValue`* to *"auto"*, the number of
  pyramid levels is automatically calculated.

  Suggested values:
   *2*, *3*, *"auto"*.

  Default:
   *"auto"*.
- ***"similarity_measure"*:** —

  Sets the similarity measure to be used.
  For both options *"census_dense"* (default) and
  *"census_sparse"*, the similarity measure is based on the
  Census transform.
  A Census transformed image contains for every pixel information
  about the intensity topology within a support window around it.

  - *"census_dense"*:
    Uses a dense 9 x 7 pixels window and is more suitable for fine structures.
  - *"census_sparse"*:
    Uses a sparse 15 x 15 pixels window where only a subset of the pixels
    is evaluated. Is more robust in low-texture areas.

  List of values:
   *"census_dense"*, *"census_sparse"*.

  Default:
   *"census_dense"*.
- ***"sub_disparity"*:** —

  Activates sub-pixel refinement of disparities when set to *"true"*.
  Can be deactivated by setting *"false"*.

  List of values:
   *"true"*, *"false"*.

  Default:
   *"true"*.

The resulting disparity is returned in the single-channel image
*`disparity`*. A quality measure for each disparity value
is returned in *`score`*, containing the best (lowest) result
of the optimized similarity measure of a reference pixel.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`imageRect1`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte*) **allowed for compute devices*

Rectified image of camera 1.

**`imageRect2`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte*) **allowed for compute devices*

Rectified image of camera 2.

**`disparity`** (output_object)  singlechannelimage `→` [HImage](HImage.md) (real)

Disparity map.

**`score`** (output_object)  singlechannelimage `→` [HImage](HImage.md) (real)

Score of the calculated disparity.

**`minDisparity`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum of the expected disparities.

Default:
-30

Value range:
`-32768
≤
minDisparity
≤
32768`

Restriction:
`MinDisparity <= MaxDisparity`

**`maxDisparity`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum of the expected disparities.

Default:
30

Value range:
`-32768
≤
maxDisparity
≤
32768`

Restriction:
`MinDisparity <= MaxDisparity`

**`surfaceSmoothing`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Smoothing of surfaces.

Default:
50

Suggested values:
20, 50, 100

Restriction:
`SurfaceSmoothing >= 0`

**`edgeSmoothing`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Smoothing of edges.

Default:
50

Suggested values:
20, 50, 100

Restriction:
`EdgeSmoothing >= 0`

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Parameter name(s) for the multi-scanline algorithm.

Default:
[]

List of values:
"consistency_check", "disparity_offset", "method", "num_levels", "similarity_measure", "sub_disparity"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string*)

Parameter value(s) for the multi-scanline algorithm.

Default:
[]

Suggested values:
"accurate", "fast", "very_fast", "census_dense", "census_sparse", "true", "false", "auto"

## Example (HDevelop)

```
read_image (BaseballL, 'stereo/epipolar/baseball_l')
read_image (BaseballR, 'stereo/epipolar/baseball_r')
binocular_disparity_ms (BaseballL, BaseballR, Disparity, Score, \
                        -40, -10, 50, 50, [], [])
```

## Result

If the parameter values are correct, `BinocularDisparityMs`
returns the value 2 (
H_MSG_TRUE)
. If the input is empty (no input images are
available) the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`MapImage`

## Possible Successors

`Threshold`,
`DisparityToDistance`,
`DisparityImageToXyz`

## Alternatives

`BinocularDisparity`,
`BinocularDisparityMg`,
`BinocularDistance`,
`BinocularDistanceMg`,
`BinocularDistanceMs`

## See also

`MapImage`,
`GenBinocularRectificationMap`,
`BinocularCalibration`

## Module

3D Metrology
