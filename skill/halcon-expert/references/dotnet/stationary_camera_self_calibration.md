# StationaryCameraSelfCalibration (Operator)

## Name

`StationaryCameraSelfCalibration` — Perform a self-calibration of a stationary projective camera.

## Signature

`static void HOperatorSet.StationaryCameraSelfCalibration(HTuple numImages, HTuple imageWidth, HTuple imageHeight, HTuple referenceImage, HTuple mappingSource, HTuple mappingDest, HTuple homMatrices2D, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple numCorrespondences, HTuple estimationMethod, HTuple cameraModel, HTuple fixedCameraParams, out HTuple cameraMatrices, out HTuple kappa, out HTuple rotationMatrices, out HTuple x, out HTuple y, out HTuple z, out HTuple error)`

`static HHomMat2D[] HHomMat2D.StationaryCameraSelfCalibration(int numImages, int imageWidth, int imageHeight, int referenceImage, HTuple mappingSource, HTuple mappingDest, HHomMat2D[] homMatrices2D, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple numCorrespondences, string estimationMethod, HTuple cameraModel, string fixedCameraParams, out HTuple kappa, out HHomMat2D[] rotationMatrices, out HTuple x, out HTuple y, out HTuple z, out HTuple error)`

`static HHomMat2D[] HHomMat2D.StationaryCameraSelfCalibration(int numImages, int imageWidth, int imageHeight, int referenceImage, HTuple mappingSource, HTuple mappingDest, HHomMat2D[] homMatrices2D, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple numCorrespondences, string estimationMethod, HTuple cameraModel, string fixedCameraParams, out double kappa, out HHomMat2D[] rotationMatrices, out HTuple x, out HTuple y, out HTuple z, out double error)`

## Description

`StationaryCameraSelfCalibration` performs a
self-calibration of a stationary projective camera. Here,
stationary means that the camera may only rotate around the optical
center and may zoom. Hence, the optical center may not move.
Projective means that the camera model is a pinhole camera that can
be described by a projective 3D-2D transformation. In particular,
radial distortions can only be modeled for cameras with constant
parameters. If the lens exhibits significant radial distortions
they should be removed, at least approximately, with
[`ChangeRadialDistortionImage`](change_radial_distortion_image.md).

The camera model being used can be described as follows:
$$X = P X$$ ![figure](../assets/c810b7d61e1246b4.svg)
Here, x is a homogeneous 2D vector,
X a homogeneous 3D vector, and P
a homogeneous 3x4 projection matrix. The projection
matrix P can be decomposed as follows:
$$P = K(R|t).$$ ![figure](../assets/7c3a2ffec5a0e80e.svg)
Here, R is a 3x3 rotation matrix
and t is an inhomogeneous 3D vector. These two
entities describe the position (pose) of the camera in 3D space.
This convention is analogous to the convention used in
[`CameraCalibration`](camera_calibration.md), i.e., for
R=I and t=0 the x
axis points to the right, the y axis downwards, and the z axis
points forward. K is the calibration matrix of
the camera (the camera matrix) which can be described as follows:
$$K = \begin{pmatrix} af & sf & u \\ 0 & f & v \\ 0 & 0 & 1 \end{pmatrix}.$$ ![figure](../assets/11d4ca9aaa536d6b.svg)
Here, f is the focal length of the camera in pixels, a the
aspect ratio of the pixels, s is a factor that models the skew of
the image axes, and (u,v) is the principal point of the camera in
pixels. In this convention, the x axis corresponds to the column
axis and the y axis to the row axis.

Since the camera is stationary, it can be assumed that
t=0. With this convention, it is easy to see
that the fourth coordinate of the homogeneous 3D vector
X has no influence on the position of the
projected 3D point. Consequently, the fourth coordinate can be set
to 0, and it can be seen that X can be regarded as
a point at infinity, and hence represents a direction in 3D. With
this convention, the fourth coordinate of X can be
omitted, and hence X can be regarded as
inhomogeneous 3D vector which can only be determined up to scale
since it represents a direction. With this, the above projection
equation can be written as follows:
$$X = \mathbf{K}R\mathbf{X}.$$ ![figure](../assets/ae527c5d8d240959.svg)
If two images of the same point are taken with a stationary camera,
the following equations hold:
$$x_1 = K_1 R_1 X x_2 = K_2 R_2 X$$ ![figure](../assets/652ad0e21e891698.svg)
and consequently
$$X_2 = K_2 R_2 R_1^{-1} K_1^{-1} X_1 = K_2 R_{12} K_1^{-1} X_1 = H_{12} X_1.$$ ![figure](../assets/c844325218aba545.svg)
If the camera parameters do not change when taking the two images,
$K_{1}=K_{2}$ holds. Because of the above, the two
images of the same 3D point are related by a projective 2D
transformation. This transformation can be determined with
[`ProjMatchPointsRansac`](proj_match_points_ransac.md). It needs to be taken into account
that the order of the coordinates of the projective 2D
transformations in HALCON is the opposite of the above convention.
Furthermore, it needs to be taken into account that
[`ProjMatchPointsRansac`](proj_match_points_ransac.md) uses a coordinate system in which
the origin of a pixel lies in the upper left corner of the pixel,
whereas `StationaryCameraSelfCalibration` uses a coordinate
system that corresponds to the definition used in
[`CameraCalibration`](camera_calibration.md), in which the origin of a pixel lies in
the center of the pixel. For projective 2D transformations that are
determined with [`ProjMatchPointsRansac`](proj_match_points_ransac.md) the rows and
columns must be exchanged and a translation of (0.5,0.5) must be
applied. Hence, instead of $\texttt{H}_{12}=\texttt{K}_{2}\texttt{R}_{12}\texttt{K}_{1}^{-1}$ the
following equations hold in HALCON:
$$H_{12} =\begin{pmatrix}0 & 1 & 0.5\\ 1 & 0 & 0.5\\ 0 & 0 & 1\end{pmatrix} K_{2}R_{12}K_{1}^{-1} \begin{pmatrix}0 & 1 & -0.5\\ 1 & 0 & -0.5\\ 0 & 0 & 1\end{pmatrix}$$ ![figure](../assets/ecdff8477ade2168.svg)
and
$$K_2R_{12}K_1^{-1} = \begin{pmatrix}0 & 1 & -0.5\\1 & 0 & -0.5\\0 & 0 & 1\end{pmatrix} H_{12} \begin{pmatrix}0 & 1 & 0.5\\1 & 0 & 0.5\\0 & 0 & 1\end{pmatrix}.$$ ![figure](../assets/097c83e7be2fbe58.svg)

From the above equation, constraints on the camera parameters can be
derived in two ways. First, the rotation can be eliminated from the
above equation, leading to equations that relate the camera matrices
with the projective 2D transformation between the two images. Let
$\texttt{H}_{ij}$ be the projective transformation from
image i to image j. Then,
$$K_j K_j^T = H_{ij} K_i K_j^T H_{ij} \\ K_j^{-T} K_j^{-1} = H_{ij}^T K_i^{-T} K_i^{-1} H_j^{-1}$$ ![figure](../assets/6c43da9188f89a4d.svg)
From the second equation, linear constraints on the camera
parameters can be derived. This method is used for
*`estimationMethod`* = *"linear"*. Here, all source
images i given by *`mappingSource`* and all destination
images j given by *`mappingDest`* are used to compute
constraints on the camera parameters. After the camera parameters
have been determined from these constraints, the rotation of the
camera in the respective images can be determined based on the
equation $\texttt{R}_{ij}=\texttt{K}_{j}^{-1}\texttt{H}_{ij}\texttt{K}_{i}$ and by constructing a chain of
transformations from the reference image *`referenceImage`* to
the respective image. From the first equation above, a nonlinear
method to determine the camera parameters can be derived by
minimizing the following error:
$$E = \sum_{(i,j)\in\{(s,d)\}} \Big\lVert K_j K_j^{\top} - H_{ij} K_i K_i^{\top} H_{ij}^{\top} \Big\rVert_{F}^{2}$$ ![figure](../assets/1aaea5252b321bc7.svg)
Here, analogously to the linear method, $\{(s,d)\}$ is
the set of overlapping images specified by *`mappingSource`*
and *`mappingDest`*. This method is used for
*`estimationMethod`* = *"nonlinear"*. To start the
minimization, the camera parameters are initialized with the results
of the linear method. These two methods are very fast and return
acceptable results if the projective 2D transformations
$\texttt{H}_{ij}$ are sufficiently accurate. For this, it
is essential that the images do not have radial distortions. It can
also be seen that in the above two methods the camera parameters are
determined independently from the rotation parameters, and
consequently the possible constraints are not fully exploited. In
particular, it can be seen that it is not enforced that the
projections of the same 3D point lie close to each other in all
images. Therefore, `StationaryCameraSelfCalibration`
offers a complete bundle adjustment as a third method
(*`estimationMethod`* = *"gold_standard"*). Here, the
camera parameters and rotations as well as the directions in 3D
corresponding to the image points (denoted by the vectors
X above), are determined in a single optimization
by minimizing the following error:
$$E = \sum_{i=1}^{n} \left( \sum_{j=1}^{m} \left\| x_{ij} - K_i R_i X_j \right\|^{2} + \frac{1}{\sigma^{2}} \left( u_i^{2} + v_i^{2} \right) \right)$$ ![figure](../assets/aa5e02565df3d234.svg)
In this equation, only the terms for which the reconstructed
direction $X_j$ ![figure](../assets/8e037184aa0c58a5.svg) is visible in image i are taken
into account. The starting values for the parameters in the bundle
adjustment are derived from the results of the nonlinear method.
Because of the high complexity of the minimization the bundle
adjustment requires a significantly longer execution time than the
two simpler methods. Nevertheless, because the bundle adjustment
results in significantly better results, it should be preferred.

In each of the three methods the camera parameters that should be
computed can be specified. The remaining parameters are set to a
constant value. Which parameters should be computed is determined
with the parameter *`cameraModel`* which contains a tuple of
values. *`cameraModel`* must always contain the value
*"focus"* that specifies that the focal length f is
computed. If *`cameraModel`* contains the value
*"principal_point"* the principal point (u,v) of the camera
is computed. If not, the principal point is set to
(*`imageWidth`*/2,*`imageHeight`*/2). If
*`cameraModel`* contains the value *"aspect"* the aspect
ratio a of the pixels is determined, otherwise it is set to 1. If
*`cameraModel`* contains the value *"skew"* the skew of
the image axes is determined, otherwise it is set to 0. Only the
following combinations of the parameters are allowed:
*"focus"*,
*["focus", "principal_point"]*,
*["focus", "aspect"]*,
*["focus", "principal_point", "aspect"]*, and
*["focus", "principal_point", "aspect", "skew"]*.

Additionally, it is possible to determine the parameter
*`kappa`*, which models radial lens distortions, if
*`estimationMethod`* = *"gold_standard"* has been
selected. In this case, *"kappa"* can also be included in
the parameter *`cameraModel`*. *`kappa`* corresponds to
the radial distortion parameter $\kappa$ of the division
model for lens distortions (see [`CameraCalibration`](camera_calibration.md)).

When using *`estimationMethod`* = *"gold_standard"* to
determine the principal point, it is possible to penalize
estimations far away from the image center. This can be done by
adding a sigma to the parameter *"principal_point:0.5"*. If
no sigma is given the penalty term in the above equation for
calculating the error is omitted.

The parameter *`fixedCameraParams`* determines whether the
camera parameters can change in each image or whether they should be
assumed constant for all images. To calibrate a camera so that it
can later be used for measuring with the calibrated camera, only
*`fixedCameraParams`* = *"true"* is useful. The mode
*`fixedCameraParams`* = *"false"* is mainly useful to
compute spherical mosaics with [`GenSphericalMosaic`](gen_spherical_mosaic.md) if the
camera zoomed or if the focus changed significantly when the mosaic
images were taken. If a mosaic with constant camera parameters
should be computed, of course *`fixedCameraParams`* =
*"true"* should be used. It should be noted that for
*`fixedCameraParams`* = *"false"* the camera
calibration problem is determined very badly, especially for long
focal lengths. In these cases, often only the focal length can be
determined. Therefore, it may be necessary to use
*`cameraModel`* = *"focus"* or to constrain the
position of the principal point by using a small Sigma for the
penalty term for the principal point.

The number of images that are used for the calibration is passed in
*`numImages`*. Based on the number of images, several
constraints for the camera model must be observed. If only two
images are used, even under the assumption of constant parameters
not all camera parameters can be determined. In this case, the skew
of the image axes should be set to 0 by *not* adding
*"skew"* to *`cameraModel`*. If
*`fixedCameraParams`* = *"false"* is used, the full
set of camera parameters can never be determined, no matter how many
images are used. In this case, the skew should be set to 0 as well.
Furthermore, it should be noted that the aspect ratio can only be
determined accurately if at least one image is rotated around the
optical axis (the z axis of the camera coordinate system) with
respect to the other images. If this is not the case the
computation of the aspect ratio should be suppressed by *not*
adding *"aspect"* to *`cameraModel`*.

As described above, to calibrate the camera it is necessary that the
projective transformation for each overlapping image pair is
determined with [`ProjMatchPointsRansac`](proj_match_points_ransac.md). For example, for
a 2x2 block of images in the following layout

|  |  |
| --- | --- |
| 1 | 2 |
| 3 | 4 |

the following projective transformations should be determined,
assuming that all images overlap each other: 1->2,
1->3, 1->4, 2->3,
2->4 and 3->4. The indices of the
images that determine the respective transformation are given by
*`mappingSource`* and *`mappingDest`*. The indices are
start at 1. Consequently, in the above example
*`mappingSource`* = *[1,1,1,2,2,3]* and
*`mappingDest`* = *[2,3,4,3,4,4]* must be used. The
number of images in the mosaic is given by *`numImages`*. It
is used to check whether each image can be reached by a chain of
transformations. The index of the reference image is given by
*`referenceImage`*. On output, this image has the identity
matrix as its transformation matrix.

The 3x3 projective transformation matrices that
correspond to the image pairs are passed in *`homMatrices2D`*.
Additionally, the coordinates of the matched point pairs in the
image pairs must be passed in *`rows1`*, *`cols1`*,
*`rows2`*, and *`cols2`*. They can be determined from the
output of [`ProjMatchPointsRansac`](proj_match_points_ransac.md) with [`TupleSelect`](tuple_select.md)
or with the HDevelop function `subset`. To enable
`StationaryCameraSelfCalibration` to determine which point
pair belongs to which image pair, *`numCorrespondences`* must
contain the number of found point matches for each image pair.

The computed camera matrices $K_{i}$ are returned in
*`cameraMatrices`* as 3x3 matrices. For
*`fixedCameraParams`* = *"false"*, *`numImages`*
matrices are returned. Since for *`fixedCameraParams`* =
*"true"* all camera matrices are identical, a single camera
matrix is returned in this case. The computed rotations
$R_{i}$ are returned in *`rotationMatrices`* as
3x3 matrices. *`rotationMatrices`* always
contains *`numImages`* matrices.

If *`estimationMethod`* = *"gold_standard"* is used,
(*`x`*, *`y`*, *`z`*) contains the reconstructed
directions $X_j$ ![figure](../assets/8e037184aa0c58a5.svg). In addition, *`error`*
contains the average projection error of the reconstructed
directions. This can be used to check whether the optimization has
converged to useful values.

If the computed camera parameters are used to project 3D points or
3D directions into the image i the respective camera matrix should
be multiplied with the corresponding rotation matrix (with
[`HomMat2dCompose`](hom_mat2d_compose.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`numImages`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of different images that are used for
the calibration.

Restriction:
`NumImages >= 2`

**`imageWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the images from which the points were
extracted.

Restriction:
`ImageWidth > 0`

**`imageHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the images from which the points were
extracted.

Restriction:
`ImageHeight > 0`

**`referenceImage`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the reference image.

**`mappingSource`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of the source images of the transformations.

**`mappingDest`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of the target images of the transformations.

**`homMatrices2D`** (input_control)  hom_mat2d-array `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Array of 3x3 projective
transformation matrices.

**`rows1`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of corresponding points in the
respective source images.

**`cols1`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of corresponding points in
the respective source images.

**`rows2`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of corresponding points in the
respective destination images.

**`cols2`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of corresponding points in
the respective destination images.

**`numCorrespondences`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Number of point correspondences in the
respective image pair.

**`estimationMethod`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Estimation algorithm for the calibration.

Default:
"gold_standard"

List of values:
"gold_standard", "linear", "nonlinear"

**`cameraModel`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Camera model to be used.

Default:
["focus","principal_point"]

List of values:
"aspect", "focus", "kappa", "principal_point", "skew"

**`fixedCameraParams`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Are the camera parameters identical for all
images?

Default:
"true"

List of values:
"false", "true"

**`cameraMatrices`** (output_control)  hom_mat2d-array `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

(Array of) 3x3 projective
camera matrices that determine the internal
camera parameters.

**`kappa`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Radial distortion of the camera.

**`rotationMatrices`** (output_control)  hom_mat2d-array `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Array of 3x3
transformation matrices that determine
rotation of the camera in the respective
image.

**`x`** (output_control)  point3d.x-array `→` [HTuple](HTuple.md) (*double*)

X-Component of the direction vector of each point if
*`estimationMethod`* = *"gold_standard"*
is used.

**`y`** (output_control)  point3d.y-array `→` [HTuple](HTuple.md) (*double*)

Y-Component of the direction vector of each point if
*`estimationMethod`* = *"gold_standard"*
is used.

**`z`** (output_control)  point3d.z-array `→` [HTuple](HTuple.md) (*double*)

Z-Component of the direction vector of each point if
*`estimationMethod`* = *"gold_standard"*
is used.

**`error`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Average error per reconstructed point if
*`estimationMethod`* =
*"gold_standard"* is used.

## Example (HDevelop)

```
* Assume that Images contains four images in the layout given in the
* above description.  Then the following example performs the camera
* self-calibration using these four images.
From := [1,1,1,2,2,3]
To := [2,3,4,3,4,4]
HomMatrices2D := []
Rows1 := []
Cols1 := []
Rows2 := []
Cols2 := []
NumMatches := []
for J := 0 to |From|-1 by 1
    select_obj (Images, ImageF, From[J])
    select_obj (Images, ImageT, To[J])
    points_foerstner (ImageF, 1, 2, 3, 100, 0.1, 'gauss', 'true', \
                      RowsF, ColsF, _, _, _, _, _, _, _, _)
    points_foerstner (ImageT, 1, 2, 3, 100, 0.1, 'gauss', 'true', \
                      RowsT, ColsT, _, _, _, _, _, _, _, _)
    proj_match_points_ransac (ImageF, ImageT, RowsF, ColsF, RowsT, ColsT, \
                              'ncc', 10, 0, 0, 480, 640, 0, 0.5, \
                              'gold_standard', 2, 42, HomMat2D, \
                              Points1, Points2)
    HomMatrices2D := [HomMatrices2D,HomMat2D]
    Rows1 := [Rows1,subset(RowsF,Points1)]
    Cols1 := [Cols1,subset(ColsF,Points1)]
    Rows2 := [Rows2,subset(RowsT,Points2)]
    Cols2 := [Cols2,subset(ColsT,Points2)]
    NumMatches := [NumMatches,|Points1|]
endfor
stationary_camera_self_calibration (4, 640, 480, 1, From, To, \
                                    HomMatrices2D, Rows1, Cols1, \
                                    Rows2, Cols2, NumMatches, \
                                    'gold_standard', \
                                    ['focus','principal_point'], \
                                    'true', CameraMatrix, Kappa, \
                                    RotationMatrices, X, Y, Z, Error)
```

## Result

If the parameters are valid, the operator
`StationaryCameraSelfCalibration` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`ProjMatchPointsRansac`,
`ProjMatchPointsRansacGuided`

## Possible Successors

`GenSphericalMosaic`

## See also

`GenProjectiveMosaic`

## References

Lourdes Agapito, E. Hayman, I. Reid: “Self-Calibration of Rotating
and Zooming Cameras”; International Journal of Computer Vision;
vol. 45, no. 2; pp. 107--127; 2001.

## Module

Calibration
