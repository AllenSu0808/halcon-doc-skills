# ProjHomMat2dToPose (Operator)

## Name

`ProjHomMat2dToPose` — Compute a pose out of a homography describing the relation between world
and image coordinates.

## Signature

`static void HOperatorSet.ProjHomMat2dToPose(HTuple homography, HTuple cameraMatrix, HTuple method, out HTuple pose)`

`static HPose HImage.ProjHomMat2dToPose(HHomMat2D homography, HHomMat2D cameraMatrix, string method)`

## Description

`ProjHomMat2dToPose` computes a pose out of a homography
*`homography`* that describes the relation between 2D world-
(unit meters) and 2D image coordinates. The homography can be
obtained by the use of [`VectorToProjHomMat2d`](vector_to_proj_hom_mat2d.md). To compute
a pose, a camera matrix (obtained by [`CamParToCamMat`](cam_par_to_cam_mat.md), for
example) has to be passed in *`cameraMatrix`*. By setting the
Parameter *`method`*, it is possible to choose which
computation algorithm is used. Currently a direct decomposition
(*`method`* = 'decomposition') and a singular value
decomposition based method (*`method`* = 'decomposition_svd')
are supported. In general due to numeric reasons, the direct
decomposition method returns more stable results.

The subsequent calls of [`VectorToProjHomMat2d`](vector_to_proj_hom_mat2d.md) and
`ProjHomMat2dToPose` are similar to [`VectorToPose`](vector_to_pose.md)
for 2D objects, whereas no refinement due to redundancy is
possible.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homography`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

The homography from world- to image coordinates.

**`cameraMatrix`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

The camera calibration matrix K.

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of pose computation.

Default:
"decomposition"

List of values:
"decomposition", "decomposition_svd"

**`pose`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Pose of the 2D object.

## Result

`ProjHomMat2dToPose` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct.

## Possible Predecessors

`ImagePointsToWorldPlane`,
`VectorToProjHomMat2d`

## See also

`VectorToProjHomMat2d`,
`ImagePointsToWorldPlane`,
`VectorToPose`,
`CameraCalibration`

## Module

Calibration
