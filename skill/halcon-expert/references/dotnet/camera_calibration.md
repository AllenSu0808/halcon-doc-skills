# CameraCalibration (Operator)

## Name

`CameraCalibration` — Determine all camera parameters by a simultaneous minimization
process.

## Signature

`static void HOperatorSet.CameraCalibration(HTuple NX, HTuple NY, HTuple NZ, HTuple NRow, HTuple NCol, HTuple startCamParam, HTuple NStartPose, HTuple estimateParams, out HTuple cameraParam, out HTuple NFinalPose, out HTuple errors)`

`HCamPar HCamPar.CameraCalibration(HTuple NX, HTuple NY, HTuple NZ, HTuple NRow, HTuple NCol, HPose[] NStartPose, HTuple estimateParams, out HPose[] NFinalPose, out HTuple errors)`

`HCamPar HCamPar.CameraCalibration(HTuple NX, HTuple NY, HTuple NZ, HTuple NRow, HTuple NCol, HPose NStartPose, HTuple estimateParams, out HPose NFinalPose, out double errors)`

`static HCamPar HPose.CameraCalibration(HTuple NX, HTuple NY, HTuple NZ, HTuple NRow, HTuple NCol, HCamPar startCamParam, HPose[] NStartPose, HTuple estimateParams, out HPose[] NFinalPose, out HTuple errors)`

`HCamPar HPose.CameraCalibration(HTuple NX, HTuple NY, HTuple NZ, HTuple NRow, HTuple NCol, HCamPar startCamParam, HTuple estimateParams, out HPose NFinalPose, out double errors)`

## Description

`CameraCalibration` performs the calibration of a single camera.
For this, known 3D model points (with coordinates *`NX`*,
*`NY`*, *`NZ`*) are projected into the image and the sum
of the squared distances between the projected 3D-coordinates and
their corresponding image point coordinates (*`NRow`*,
*`NCol`*) is minimized.

As initial values for the minimization process the external
(*`NStartPose`*) and internal (*`startCamParam`*) camera
parameters are used.
Thereby *`NStartPose`* is an ordered tuple with all initial values for
the external camera parameters given in the form
$\mathrm{CCS} P_{\mathrm{wcs}}$ ![figure](../assets/4c18b1c4fb564c93.svg), where
*ccs* denotes the camera coordinate system and
*wcs* the world coordinate system (see
[Transformations / Poses](toc_transformations_poses.md)
and `“Solution Guide III-C - 3D Vision”`).
Individual camera parameters can be explicitly
included or excluded from the minimization with
*`estimateParams`*. For a detailed description of the available
camera models, the different sets of internal camera parameters, and
general requirements for the setup, see [Calibration](toc_calibration.md).

For a successful calibration, at least one calibration object with
accurately known metric properties is needed, e.g., a HALCON
calibration plate. Before calling `CameraCalibration`, take a
series of images of the calibration object in different orientations
and make sure that the whole field of view or measurement volume is
covered. The success of the calibration highly depends on the
quality of the calibration object and the images. So you might want
to exercise special diligence during the acquisition of the
calibration images. See the section “How to take a set of suitable
images?” in [Calibration](toc_calibration.md) for further details.

After a successful calibration, `CameraCalibration` returns
the optimized internal (*`cameraParam`*) and external
(*`NFinalPose`* $\mathrm{CCS} P_{\mathrm{wcs}}$ ![figure](../assets/4c18b1c4fb564c93.svg))
camera parameters of the camera. Additionally,
the root mean square error (RMSE) of the back projection of the
optimization is returned in *`errors`* (in pixels). This error
gives a general indication whether the optimization was successful.

### Preparation of the calibration process

- ****How to extract the calibration marks in the images?**** —

  If a HALCON calibration plate is used, you can use the operator
  [`FindCalibObject`](find_calib_object.md) to determine the coordinates of the
  calibration marks in each image and to compute a rough estimate for
  the external camera parameters. Using HALCON calibration plates with
  rectangularly arranged marks (see [`GenCaltab`](gen_caltab.md)), a combination
  of the two operators [`FindCaltab`](find_caltab.md) and
  [`FindMarksAndPose`](find_marks_and_pose.md) will have the same effect. In both
  cases, the hereby obtained values can directly be used as initial
  values for the external camera parameters (*`NStartPose`*).

  Obviously, images in which the segmentation of the calibration plate
  ([`FindCaltab`](find_caltab.md)) has failed or the calibration marks have not
  been determined successfully by [`FindMarksAndPose`](find_marks_and_pose.md) or
  [`FindCalibObject`](find_calib_object.md) should not be used.
- ****How do you get the required initial values for the
  calibration?**** —

  If you use a HALCON calibration plate, the input parameters
  *`NX`*, *`NY`*, and *`NZ`* are stored in the
  description file of the calibration plate. You can easily access
  them by calling the operator [`CaltabPoints`](caltab_points.md). Initial values
  for the internal camera parameters (*`startCamParam`*) can be
  obtained from the specifications of the used camera. Further
  information can be found in [Calibration](toc_calibration.md). Initial
  values for the poses of the calibration plate and the coordinates of
  the calibration marks *`NRow`* and *`NCol`* can be
  calculated using the operator [`FindCalibObject`](find_calib_object.md). The tuple
  *`NStartPose`* is set by the concatenation of all these poses.
- ****Which camera parameters are estimated?**** —

  The input parameter *`estimateParams`* is used to select which
  camera parameters to estimate. Usually, this parameter is set to
  *"all"*, i.e., all 6 external camera parameters (translation
  and rotation) and all internal camera parameters are determined. If
  the internal camera parameters already have been determined (e.g.,
  by a previous call to `CameraCalibration`), it is often
  desired to only determine the pose of the world coordinate system in
  camera coordinates (i.e., the external camera parameters). In this
  case, *`estimateParams`* can be set to *"pose"*. This
  has the same effect as *`estimateParams`* =
  *["alpha","beta","gamma","transx","transy","transz"]*.
  Otherwise, *`estimateParams`* contains a tuple of strings that
  indicates the combination of parameters to estimate. In addition,
  parameters can be excluded from estimation by using the prefix
  ~. For example, the values
  *["pose","~transx"]*
  have the same effect as
  *["alpha","beta","gamma","transy","transz"]*. As a different
  example,
  *["all","~focus"]*
  determines all internal and external parameters except the
  focus. The prefix ~ can be used with all parameter
  values except *"all"*.
- ****Which limitations exist for the determination of the
  camera parameters?**** —

  For additional information about general limitations when
  determining camera parameters, please see the section
  “Further Limitations Related to Specific Camera Types” in the chapter
  [Calibration](toc_calibration.md).
- ****What is the order within the individual parameters?**** —

  The length of the tuple *`NStartPose`* depends on the number of
  calibration images, e.g., using 15 images leads to a length of the
  tuple *`NStartPose`* equal to $15\cdot7=105$
  (15 times the 7 external camera parameters). The first 7 values
  correspond to the pose of the calibration plate in the first image,
  the next 7 values to the pose in the second image, etc.

  This fixed number of calibration images must be considered within
  the tuples with the coordinates of the 3D model marks and the
  extracted 2D marks. If 15 images are used, the length of the tuples
  *`NRow`* and *`NCol`* is 15 times the length of the tuples
  with the coordinates of the 3D model marks (*`NX`*,
  *`NY`*, and *`NZ`*). If every image consists 49 marks,
  the length of the tuples *`NRow`* and *`NCol`* is
  $15\cdot49=735$, while the length of the tuples
  *`NX`*, *`NY`*, and *`NZ`* is 49. The order of the
  values in *`NRow`* and *`NCol`* is “image after image”,
  i.e., using 49 marks the first 3D model point corresponds to the
  1st, 50th, 99th, 148th, 197th, 246th, etc. extracted 2D mark.
- ****What is the meaning of the output parameters?**** —

  If the camera calibration process has finished successfully, the
  output parameters *`cameraParam`* and *`NFinalPose`*
  contain the adjusted values for the internal and external camera
  parameters. The length of the tuple *`NFinalPose`* corresponds
  to the length of the tuple *`NStartPose`*.

  The representation types of *`NFinalPose`* correspond to the
  representation type of the first tuple of *`NStartPose`* (see
  [`CreatePose`](create_pose.md)). You can convert the representation type by
  [`ConvertPoseType`](convert_pose_type.md).

  As an additional parameter, the root mean square error (RMSE)
  (*`errors`*) of the back projection of the optimization is
  returned. This parameter reflects the accuracy of the calibration.
  The error value (root mean square error of the position) is measured
  in pixels. If only a single camera is calibrated, an Error in the
  order of 0.1 pixel (the typical detection error by extraction of the
  coordinates of the projected calibration markers) is an indication
  that the optimization fits the observation data well. If
  *`errors`* strongly differs from 0.1 pixels, the calibration
  did not perform well. Reasons for this might be, e.g., a poor image
  quality, an insufficient number of calibration images, or an
  inaccurate calibration plate.
- ****Do I have to use a planar calibration object?**** —

  No. The operator `CameraCalibration` is designed in a way
  that the input tuples *`NX`*, *`NY`*, *`NZ`*,
  *`NRow`*, and *`NCol`* can contain any 3D/2D
  correspondences. The order of the single parameters is explained in
  the paragraph “What is the order within the individual
  parameters?”.

  Thus, it makes no difference how the required 3D model marks and the
  corresponding 2D marks are determined. On the one hand, it is
  possible to use a 3D calibration object, on the other hand, you also
  can use any characteristic points (e.g., natural landmarks) with
  known position in the world. By setting *`estimateParams`* to
  *"pose"*, it is thus possible to compute the pose of an
  object in camera coordinates! For this, at least three
  3D/2D-correspondences are necessary as input. *`NStartPose`*
  can, e.g., be generated directly as shown in the program example for
  [`CreatePose`](create_pose.md).

## Attention

The minimization process of the calibration depends on the initial
values of the internal (*`startCamParam`*) and external
(*`NStartPose`*) camera parameters. The computed average errors
*`errors`* give an impression of the accuracy of the
calibration. The errors (deviations in x- and y-coordinates) are
measured in pixels.

For line scan cameras, it is possible to set the start value for the
internal camera parameter Sy to the value 0.0. In this case, it is
not possible to determine the position of the principal point in
y-direction. Therefore, *`estimateParams`* must contain the
term *"~cy"*. The effective
distance of the principle point from the sensor line is then always
$p_{v}=S_{y}\cdot C_{y}=0.0$. Further
information can be found in the section “Further Limitations Related
to Specific Camera Types” of [Calibration](toc_calibration.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`NX`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Ordered tuple with all x coordinates
of the calibration marks (in meters).

**`NY`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Ordered tuple with all y coordinates
of the calibration marks (in meters).

Number of elements:
NY == NX

**`NZ`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Ordered tuple with all z coordinates
of the calibration marks (in meters).

Number of elements:
NZ == NX

**`NRow`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Ordered tuple with all row coordinates
of the extracted calibration marks (in pixels).

**`NCol`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Ordered tuple with all column coordinates
of the extracted calibration marks (in pixels).

Number of elements:
NCol == NRow

**`startCamParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Initial values for the internal camera parameters.

**`NStartPose`** (input_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Ordered tuple with all initial values for the
external camera parameters.

Number of elements:
NStartPose == 7 * NRow / NX

**`estimateParams`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Camera parameters to be estimated.

Default:
"all"

List of values:
"all", "alpha", "beta", "camera", "cx", "cy", "focus", "gamma", "image_plane_dist", "k1", "k2", "k3", "kappa", "magnification", "poly", "poly_tan_2", "pose", "sx", "sy", "tilt", "transx", "transy", "transz", "vx", "vy", "vz"

**`cameraParam`** (output_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

**`NFinalPose`** (output_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Ordered tuple with all external camera parameters.

Number of elements:
NFinalPose == 7 * NRow / NX

**`errors`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Average error distance in pixels.

## Example (HDevelop)

```
* Read calibration images.
read_image(Image1, 'calib/grid_space.cal.k.000')
read_image(Image2, 'calib/grid_space.cal.k.001')
read_image(Image3, 'calib/grid_space.cal.k.002')
*  Find calibration pattern.
find_caltab(Image1, CalPlate1, 'caltab_big.descr', 3, 112, 5)
find_caltab(Image2, CalPlate2, 'caltab_big.descr', 3, 112, 5)
find_caltab(Image3, CalPlate3, 'caltab_big.descr', 3, 112, 5)
*  Find calibration marks and start poses.
StartCamPar := ['area_scan_division', 0.008, 0.0, 0.000011, 0.000011, \
                384, 288, 768, 576]
find_marks_and_pose(Image1, CalPlate1, 'caltab_big.descr', StartCamPar, \
                    128, 10, 18, 0.9, 15.0, 100.0, RCoord1, CCoord1, \
                    StartPose1)
find_marks_and_pose(Image2, CalPlate2, 'caltab_big.descr', StartCamPar, \
                    128, 10, 18, 0.9, 15.0, 100.0, RCoord2, CCoord2, \
                    StartPose2)
find_marks_and_pose(Image3, CalPlate3, 'caltab_big.descr', StartCamPar, \
                    128, 10, 18, 0.9, 15.0, 100.0, RCoord3, CCoord3, \
                    StartPose3)
*  Read 3D positions of calibration marks.
caltab_points('caltab_big.descr', NX, NY, NZ)
*  Camera calibration.
camera_calibration(NX, NY, NZ, [RCoord1, RCoord2, RCoord3], \
                   [CCoord1, CCoord2, CCoord3], StartCamPar, \
                   [StartPose1, StartPose2, StartPose3], 'all', \
                   CameraParam, NFinalPose, Errors)
*  Write internal camera parameters to file.
write_cam_par(CameraParam, 'campar.dat')
```

## Result

`CameraCalibration` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct and the desired camera parameters have been determined by
the minimization algorithm. If necessary, an exception is raised.

## Possible Predecessors

`FindMarksAndPose`,
`CaltabPoints`,
`ReadCamPar`

## Possible Successors

`WritePose`,
`PoseToHomMat3d`,
`DispCaltab`,
`SimCaltab`

## Alternatives

`CalibrateCameras`

## See also

`FindCaltab`,
`FindMarksAndPose`,
`DispCaltab`,
`SimCaltab`,
`WriteCamPar`,
`ReadCamPar`,
`CreatePose`,
`ConvertPoseType`,
`WritePose`,
`ReadPose`,
`PoseToHomMat3d`,
`HomMat3dToPose`,
`CaltabPoints`,
`GenCaltab`,
`CalibrateCameras`

## Module

Calibration
