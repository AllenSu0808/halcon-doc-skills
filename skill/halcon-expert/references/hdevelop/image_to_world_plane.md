# image_to_world_plane (Operator)

## Name

`image_to_world_plane` — Rectify an image by transforming it into the plane z=0 of a world
coordinate system.

## Signature

`image_to_world_plane(Image : ImageWorld : CameraParam, WorldPose, Width, Height, Scale, Interpolation : )`

## Description

`image_to_world_plane` rectifies an image *`Image`* by
transforming it into the plane z=0 (plane of measurements) in a world
coordinate system. The resulting rectified image *`ImageWorld`* shows
neither radial nor perspective distortions; it corresponds to an image
acquired by a distortion-free camera that looks perpendicularly onto the
plane of measurements. The world coordinate system is chosen by passing its
3D pose relative to the camera coordinate system in *`WorldPose`*.
Hence, latter one is expected in the form
$\mathrm{CCS} P_{\mathrm{wcs}}$ ![figure](../assets/4c18b1c4fb564c93.svg), where
*ccs* denotes the camera coordinate system and
*wcs* the world coordinate system (see
[Transformations / Poses](toc_transformations_poses.md)
and `“Solution Guide III-C - 3D Vision”`).
In *`CameraParam`* you must pass the internal camera parameters (see
[Calibration](toc_calibration.md) for the sequence of the parameters and the
underlying camera model).

In many cases *`CameraParam`* and *`WorldPose`* are the result of
calibrating the camera with the operator [`calibrate_cameras`](calibrate_cameras.md). See
below for an example.

The pixel position of the upper left corner of the output image
*`ImageWorld`* is determined by the origin of the world coordinate
system. The size of the output image *`ImageWorld`* can be chosen by
the parameters *`Width`*, *`Height`*, and
*`Scale`*. *`Width`* and *`Height`* must be given in pixels.

The parameter *`Scale`* can be used to specify the size of a pixel in the
transformed image. There are two ways to use this parameter:

- **Scale pixels to metric units:** —

  Scale the image such that one pixel in the transformed image corresponds
  to a metric unit, e.g., setting *'mm'* determines that a pixel in the
  transformed image corresponds to the area 1mm x 1mm in the
  plane of measurements. For this, the original unit needs to be meters.
  This is the case if you use a standard calibration plate.

  List of values:
   *'m'*, *'cm'*, *'mm'*,
  *'microns'*, *'um'*.

  Default:
   *'m'*.
- **Control scaling manually:** —

  Scale the image by giving a number that determines the ratio of
  *original unit length* / *desired number of pixels*.
  E.g., if your original unit is meters and you want
  every pixel of your transformed image to represent 3mm x 3mm
  of the measuring plane, your scale is calculated
  $\texttt{Scale}=0.003/1=0.003$.
  If you want to perform a task like shape-based matching on your
  transformed image, it is useful to scale the image such that its content
  appears in a size similar to the original image.

  Restriction:
   *`Scale`* > *0*.

The parameter *`Interpolation`* specifies, whether bilinear
interpolation (*'bilinear'*) should be applied between the pixels in
the input image or whether the gray value of the nearest neighboring pixel
(*'nearest_neighbor'*) should be used.

If several images have to be rectified using the same parameters,
[`gen_image_to_world_plane_map`](gen_image_to_world_plane_map.md) in combination with [`map_image`](map_image.md)
is much more efficient than the operator `image_to_world_plane`
because the mapping function needs to be computed only once.

## Attention

`image_to_world_plane` can be executed on OpenCL devices if the input
image does not exceed the maximum size of image objects of the selected
device. There can be slight differences in the output compared to the
execution on the CPU.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / uint2 / real)

Input image.

**`ImageWorld`** (output_object)  (multichannel-)image(-array) `→` object (byte / uint2 / real)

Transformed image.

**`CameraParam`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters.

**`WorldPose`** (input_control)  pose `→`  (real / integer)

3D pose of the world coordinate system in camera
coordinates.

Number of elements:
7

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the resulting image in pixels.

Restriction:
`Width >= 1`

**`Height`** (input_control)  extent.y `→`  (integer)

Height of the resulting image in pixels.

Restriction:
`Height >= 1`

**`Scale`** (input_control)  number `→`  (string / integer / real)

Scale or unit.

Default:
'm'

Suggested values:
'm', 'cm', 'mm', 'microns', 'um', 1.0, 0.01, 0.001, 1.0e-6, 0.0254, 0.3048, 0.9144

Restriction:
`Scale > 0`

**`Interpolation`** (input_control)  string `→`  (string)

Type of interpolation.

Default:
'bilinear'

List of values:
'bilinear', 'nearest_neighbor'

## Example (HDevelop)

```
* Calibrate camera.
calibrate_cameras (CalibDataID, Error)
* Obtain camera parameters.
get_calib_data (CalibDataID, 'camera', 0, 'params', CamParam)
* Example values, if no calibration data is available:
CamParam := ['area_scan_division', 0.0087, -1859, 8.65e-006, 8.6e-006, \
             362.5, 291.6, 768, 576]
* Get reference pose (pose 4 of calibration object 0).
get_calib_data (CalibDataID, 'calib_obj_pose',\
                [0,4], 'pose', Pose)
* Example values, if no calibration data is available:
Pose := [-0.11, -0.21, 2.51, 352.73, 346.73, 336.48, 0]
* Compensate thickness of plate.
set_origin_pose (Pose, -1.125, -1.0, 0, PoseNewOrigin)
* Transform the image into the world plane.
read_image (Image, 'calib/calib-3d-coord-04')
image_to_world_plane (Image, ImageWorld, CamParam, PoseNewOrigin,\
                      900, 800, 0.0025, 'bilinear')
```

## Result

`image_to_world_plane` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`create_pose`,
`hom_mat3d_to_pose`,
`camera_calibration`,
`hand_eye_calibration`,
`set_origin_pose`

## Alternatives

`gen_image_to_world_plane_map`,
`map_image`

## See also

`contour_to_world_plane_xld`,
`image_points_to_world_plane`

## Module

Calibration
