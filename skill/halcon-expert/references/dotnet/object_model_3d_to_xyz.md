# ObjectModel3dToXyz (Operator)

## Name

`ObjectModel3dToXyz` — Transform 3D points from a 3D object model to images.

## Signature

`static void HOperatorSet.ObjectModel3dToXyz(out HObject x, out HObject y, out HObject z, HTuple objectModel3D, HTuple type, HTuple camParam, HTuple pose)`

`static HImage HObjectModel3D.ObjectModel3dToXyz(out HImage y, out HImage z, HObjectModel3D[] objectModel3D, string type, HCamPar camParam, HPose pose)`

`HImage HObjectModel3D.ObjectModel3dToXyz(out HImage y, out HImage z, string type, HCamPar camParam, HPose pose)`

`HImage HCamPar.ObjectModel3dToXyz(out HImage y, out HImage z, HObjectModel3D[] objectModel3D, string type, HPose pose)`

`HImage HCamPar.ObjectModel3dToXyz(out HImage y, out HImage z, HObjectModel3D objectModel3D, string type, HPose pose)`

## Description

The operator `ObjectModel3dToXyz` transforms the 3D points of
the 3D object model *`objectModel3D`* into the three images
*`x`*, *`y`*, and *`z`*.

Three transformation modes are possible. The parameter *`type`* is
used to select one of them. Note that multiple 3D object models can be
passed in *`objectModel3D`* only for the mode *"cartesian_faces"*.
All other modes expect a single 3D object model.

- ***"cartesian"*:** —

  First, each point is transformed into the camera coordinate system
  using the given *`pose`*. Then, these coordinates are projected
  into the image coordinate system based on the internal camera parameters
  *`camParam`*.

  The internal camera parameters *`camParam`* describe the
  projection characteristics of the camera (see
  [Calibration](toc_calibration.md)).
  The *`pose`* is in the form $\mathrm{ccs} \mathbf{P}_{\mathrm{mcs}}$ ![figure](../assets/36630faf4c6dcd27.svg),
  where *ccs* denotes camera coordinate system and
  *mcs* the model coordinate system (which is a 3D world coordinate
  system), see [Transformations / Poses](toc_transformations_poses.md) and
  `“Solution Guide III-C - 3D Vision”`.
  Hence, it describes the
  position and orientation of the model coordinate system relative
  to the camera coordinate system.

  The X-, Y-, and Z-coordinates of the transformed point are written into
  the corresponding image at the position of the projection.
  If multiple points are projected to the same image coordinates, the
  point with the smallest Z-value is written (hidden-point removal).
  The dimensions of the returned images are defined by the camera
  parameters.

  The returned images show the object as it would look like when seeing it
  with the specified camera under the specified pose.
- ***"cartesian_faces"*:** —

  In order to use this transformation, the input 3D object models need to
  contain faces (triangles or polygons), otherwise, the 3D object model
  without faces is disregarded.
  Note that if the 3D object models have polygon faces, those are converted
  internally to triangles. This conversion can be done beforehand to speed
  up this operator.
  For this, [`ReadObjectModel3d`](read_object_model_3d.md) can be called with the
  `genParamName` *"convert_to_triangles"* set to
  *"true"*, to convert all faces to triangles.
  Alternatively, [`TriangulateObjectModel3d`](triangulate_object_model_3d.md) can be called prior
  to this operator.

  First, each face of the 3D object models *`objectModel3D`* is
  transformed into the camera coordinate system
  using the given *`pose`*. Then, these coordinates are projected
  into the image coordinate system based on the internal camera parameters
  *`camParam`*, while keeping the 3D information (X-, Y-, and
  Z-coordinates) for each of those pixels. For a more detailed explanation
  of *`camParam`* and *`pose`* please refer to the section
  *"cartesian"*.
  If multiple faces are projected to the same image coordinates, the
  value with the smallest Z-value is written (hidden-point removal).
  The dimensions of the returned images are defined by the camera
  parameters.

  The returned images show the objects as they would look like when seeing
  them with the specified camera under the specified pose.

  In case that OpenGL 2.1, GLSL 1.2, and the OpenGL
  extensions GL_EXT_framebuffer_object and GL_EXT_framebuffer_blit are
  available, speed increases.

  This *`type`* can be used to create 3D object models containing
  2D mapping data, by creating a 3D object model from the returned images
  using [`XyzToObjectModel3d`](xyz_to_object_model_3d.md).
  Note that in many cases, it is recommended to use the 2D mapping data,
  if available, for speed and robustness reasons. This is beneficial for
  example when using [`SampleObjectModel3d`](sample_object_model_3d.md),
  [`SurfaceNormalsObjectModel3d`](surface_normals_object_model_3d.md), or when preparing a 3D object
  model for surface-based matching, e.g., smoothing, removing outliers, and
  reducing the domain.
- ***"cartesian_faces_no_opengl"*:** —

  This transformation mode works in the same way as the method
  *"cartesian_faces"* but does not use OpenGL.
  In general, *"cartesian_faces"* automatically determines
  if OpenGL is available.
  Thus, it is usually not required to use
  *"cartesian_faces_no_opengl"* explicitly.
  It can make sense, however, to use it in cases where the automatic mode
  selection does not work due to, for example, driver issues with OpenGL,
  or for higher accuracy when using camera parameters with distortion or
  tilt.
- ***"from_xyz_map"*:** —

  This transformation mode works only if the 3D object model was created
  with the operator [`XyzToObjectModel3d`](xyz_to_object_model_3d.md).
  It writes each 3D point to the image coordinate where it originally
  came from, using the mapping attribute that is stored within the
  3D object model.

  The parameters *`camParam`* and *`pose`* are ignored.
  The dimensions of the returned images are equal to the dimensions of the
  original images that were used with [`XyzToObjectModel3d`](xyz_to_object_model_3d.md) to
  create the 3D object model and can be queried from
  [`GetObjectModel3dParams`](get_object_model_3d_params.md) with *"mapping_size"*.

  This transformation mode is faster than *"cartesian"*.
  It is suitable, e.g., to visualize the results of a segmentation done with
  [`SegmentObjectModel3d`](segment_object_model_3d.md).

## Attention

Cameras with hypercentric lenses are not supported.
For displaying large faces with a non-zero distortion
in *`camParam`*, note that the distortion is only applied to the
points of the model. In the projection, these points are subsequently
connected by straight lines. For a good approximation of the distorted
lines, please use a triangulation with sufficiently small triangles.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`x`** (output_object)  singlechannelimage `→` [HImage](HImage.md) (real)

Image with the X-Coordinates of the 3D points.

**`y`** (output_object)  singlechannelimage `→` [HImage](HImage.md) (real)

Image with the Y-Coordinates of the 3D points.

**`z`** (output_object)  singlechannelimage `→` [HImage](HImage.md) (real)

Image with the Z-Coordinates of the 3D points.

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of the conversion.

Default:
"cartesian"

List of values:
"cartesian", "cartesian_faces", "cartesian_faces_no_opengl", "from_xyz_map"

**`camParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Camera parameters.

**`pose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Pose of the 3D object model.

Number of elements:
Pose == 0 || Pose == 7 || Pose == 12

## Result

The operator `ObjectModel3dToXyz` returns the value
2 (
H_MSG_TRUE)
if the given parameters are correct. Otherwise, an exception
will be raised.

## Possible Predecessors

`ReadObjectModel3d`,
`XyzToObjectModel3d`,
`TriangulateObjectModel3d`

## Alternatives

`ProjectObjectModel3d`

## See also

`XyzToObjectModel3d`,
`GetObjectModel3dParams`

## Module

3D Metrology
