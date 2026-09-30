# gen_image_to_world_plane_map (Operator)

## Name

`gen_image_to_world_plane_map` — Generate a projection map that describes the mapping between the image
plane and the plane z=0 of a world coordinate system.

## Signature

`def gen_image_to_world_plane_map(camera_param: Sequence[Union[int, float, str]], world_pose: Sequence[Union[int, float]], width_in: int, height_in: int, width_mapped: int, height_mapped: int, scale: Union[int, float, str], map_type: str) -> HObject`

## Description

`gen_image_to_world_plane_map` generates a projection map *`map`*,
which describes the mapping between the image plane and the plane z=0
(plane of measurements) in a world coordinate system. This map can be used
to rectify an image with the operator [`map_image`](map_image.md). The rectified
image shows neither radial nor perspective distortions; it corresponds to
an image acquired by a distortion-free camera that looks perpendicularly
onto the plane of measurements. The world coordinate system (*wcs*)
is chosen by passing its 3D pose relative to the camera coordinate system
(*ccs*) in
*`world_pose`*. Thus the pose is expected in the form
$\mathrm{CCS} P_{\mathrm{wcs}}$ ![figure](../assets/4c18b1c4fb564c93.svg)
(see [Transformations / Poses](toc_transformations_poses.md)
and `“Solution Guide III-C - 3D Vision”`).
In *`camera_param`* you must pass the internal camera
parameters (see [Calibration](toc_calibration.md) for the sequence of the
parameters and the underlying camera model).

In many cases *`camera_param`* and *`world_pose`* are the result of
calibrating the camera with the operator [`calibrate_cameras`](calibrate_cameras.md). See
below for an example.

The size of the images to be mapped can be specified by the parameters
*`width_in`* and *`height_in`*. The pixel position of the upper left
corner of the output image is determined by the origin of the world
coordinate system. The size of the output image can be chosen by the
parameters *`width_mapped`*, *`height_mapped`*, and
*`scale`*. *`width_mapped`* and *`height_mapped`* must be given
in pixels.

The parameter *`scale`* can be used to specify the size of a pixel in the
transformed image. There are two ways to use this parameter:

- **Scale pixels to metric units:** —

  Scale the image such that one pixel in the transformed image corresponds
  to a metric unit, e.g., setting *"mm"* determines that a pixel in the
  transformed image corresponds to the area 1mm x 1mm in the
  plane of measurements. For this, the original unit needs to be meters.
  This is the case if you use a standard calibration plate.

  List of values:
   *"m"*, *"cm"*, *"mm"*,
  *"microns"*, *"um"*.

  Default:
   *"m"*.
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
   *`scale`* > 0.

The mapping function is stored in the output image *`map`*.
*`map`* has the same size as the resulting images after the mapping.
*`map_type`* is used to specify the type of the output *`map`*.
If *"nearest_neighbor"* is chosen, *`map`* consists of one image
containing one channel, in which for each pixel of the resulting image the
linearized coordinate of the pixel of the input image is stored that is the
nearest neighbor to the transformed coordinates. If *"bilinear"*
interpolation is chosen, *`map`* consists of one image containing five
channels. In the first channel for each pixel in the resulting image the
linearized coordinates of the pixel in the input image is stored that is in
the upper left position relative to the transformed coordinates.
The four other channels contain the weights of the four neighboring pixels
of the transformed coordinates which are used for the bilinear
interpolation, in the following order:

|  |  |
| --- | --- |
| 2 | 3 |
| 4 | 5 |

The second channel, for example, contains the weights of the pixels that
lie to the upper left relative to the transformed coordinates.
If *"coord_map_sub_pix"* is chosen, *`map`* consists of
one vector field image of the semantic type 'vector_field_absolute', in
which for each pixel of the resulting image the subpixel precise
coordinates in the input image are stored.

If several images have to be mapped using the same camera parameters,
`gen_image_to_world_plane_map` in combination with [`map_image`](map_image.md)
is much more efficient than the operator [`image_to_world_plane`](image_to_world_plane.md)
because the mapping function needs to be computed only once.

If you want to re-use the created map in another program, you can save it as
a multi-channel image with the operator [`write_image`](write_image.md), using the
format *"tiff"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`map`** (output_object)  (multichannel-)image `→` HObject (int4 / int8 / uint2 / vector_field)

Image containing the mapping data.

**`camera_param`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters.

**`world_pose`** (input_control)  pose `→` Sequence[Union[int, float]]

3D pose of the world coordinate system in camera
coordinates.

Number of elements:
7

**`width_in`** (input_control)  extent.x `→` int

Width of the images to be transformed.

Restriction:
`WidthIn >= 1`

**`height_in`** (input_control)  extent.y `→` int

Height of the images to be transformed.

Restriction:
`HeightIn >= 1`

**`width_mapped`** (input_control)  extent.x `→` int

Width of the resulting mapped images in pixels.

Restriction:
`WidthMapped >= 1`

**`height_mapped`** (input_control)  extent.y `→` int

Height of the resulting mapped images in pixels.

Restriction:
`HeightMapped >= 1`

**`scale`** (input_control)  number `→` Union[int, float, str]

Scale or unit.

Default:
"m"

Suggested values:
"m", "cm", "mm", "microns", "um", 1.0, 0.01, 0.001, 1.0e-6, 0.0254, 0.3048, 0.9144

Restriction:
`Scale > 0`

**`map_type`** (input_control)  string `→` str

Type of the mapping.

Default:
"bilinear"

List of values:
"bilinear", "coord_map_sub_pix", "nearest_neighbor"

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
gen_image_to_world_plane_map (MapSingle, CamParam, PoseNewOrigin,\
                  CamParam[6], CamParam[7], 900, 800, 0.0025, 'bilinear')
map_image (Image, MapSingle, ImageMapped)
```

## Result

`gen_image_to_world_plane_map` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`create_pose`,
`hom_mat3d_to_pose`,
`camera_calibration`,
`hand_eye_calibration`,
`set_origin_pose`

## Possible Successors

`map_image`

## Alternatives

`image_to_world_plane`

## See also

`map_image`,
`contour_to_world_plane_xld`,
`image_points_to_world_plane`

## Module

Calibration
