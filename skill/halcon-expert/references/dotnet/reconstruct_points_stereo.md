# ReconstructPointsStereo (Operator)

## Name

`ReconstructPointsStereo` — Reconstruct 3D points from calibrated multi-view stereo images.

## Signature

`static void HOperatorSet.ReconstructPointsStereo(HTuple stereoModelID, HTuple row, HTuple column, HTuple covIP, HTuple cameraIdx, HTuple pointIdx, out HTuple x, out HTuple y, out HTuple z, out HTuple covWP, out HTuple pointIdxOut)`

`void HStereoModel.ReconstructPointsStereo(HTuple row, HTuple column, HTuple covIP, int cameraIdx, int pointIdx, out HTuple x, out HTuple y, out HTuple z, out HTuple covWP, out HTuple pointIdxOut)`

`void HStereoModel.ReconstructPointsStereo(double row, double column, HTuple covIP, int cameraIdx, int pointIdx, out double x, out double y, out double z, out double covWP, out int pointIdxOut)`

## Description

The operator `ReconstructPointsStereo` reconstructs 3D points
from point correspondences found in the images of a calibrated
multi-view stereo setup. The calibration information for the images
is provided in the camera setup model that is associated with the
stereo model *`stereoModelID`* during
its creation (see [`CreateStereoModel`](create_stereo_model.md)). Note that the stereo
model type must be *"points_3d"*, otherwise the operator will
return an error.

The point correspondences must be passed in the parameters *`row`*,
*`column`*, *`cameraIdx`*, and *`pointIdx`* in form of
tuples of the same length. Each set
`(Row[I],Column[I],CameraIdx[I],PointIdx[I])` represents the
image coordinates (*`row`*, *`column`*) of the 3D point
(*`pointIdx`*) in the image of a certain camera
(*`cameraIdx`*).

The reconstructed 3D point coordinates are returned in the
tuples *`x`*, *`y`*, and *`z`*, relative to the
coordinate system of the camera setup model (see
[`CreateCameraSetupModel`](create_camera_setup_model.md)). The tuple *`pointIdxOut`*
contains the corresponding point indices.

The reconstruction algorithm works as follows: First, it identifies
point correspondences for a given 3D point by collecting all
sets with the same *`pointIdx`*. Then, it uses the
*`row`*, *`column`*, and *`cameraIdx`* information
from the collected sets to project lines of sight from each
camera through the corresponding image point
`[Row,Column]`. If there are at least 2 lines of sight for the
point *`pointIdx`*, they are intersected and the result is
stored as the set `(X[J],Y[J],Z[J],PointIdxOut[J])`. The
intersection is performed with a least-squares algorithm, without
taking into account potentially invalid lines of sight (e.g., if an
image point was falsely specified as corresponding to a certain 3D point).

To compute the covariance matrices for the reconstructed 3D points,
statistical information about the extracted image coordinates, i.e.,
the covariance matrices of the image points
(see , e.g., [`PointsFoerstner`](points_foerstner.md)) are needed as input and must be
passed in the parameter *`covIP`*. Otherwise, if no covariance
matrices for the 3D points are needed or no covariance matrices for
the image points are available, an empty tuple can be passed
in *`covIP`*. Then no covariance matrix for the reconstructed
3D points is computed.

The covariance matrix of an image point is:

$$CovIP = \left[\begin{array}{cc} (\sigma_{r})^{2} & \sigma_{rc} \\ \sigma_{rc} & (\sigma_{c})^{2} \end{array}\right]$$ ![figure](../assets/59ef69e80b37e3fb.svg)

The covariance matrices are symmetric `2x2` matrices, whose entries in the
main diagonal represent the variances of the image point in row-direction
and column-direction, respectively.
For each image point, a covariance matrix must be passed in *`covIP`* in
form of a tuple with 4 elements:

$$[(sigma\_r)^{2},sigma\_rc,sigma\_rc,(sigma\_c)^{2}].$$

Thus, `|CovIP|=4*|Row|` and `CovIP[I*4:I*4+3]` is the
covariance matrix for the `I`-th image point.

The computed covariance matrix for a successfully reconstructed 3D
point is represented by a symmetric `3x3` matrix:

$$\mathrm{CovWP} = \left[\begin{array}{ccc}(\sigma a\_x)^2 & \sigma a\_x \sigma a\_y & \sigma a\_x \sigma a\_z\\ \sigma a\_y \sigma a\_x & (\sigma a\_y)^2 & \sigma a\_y \sigma a\_z\\ \sigma a\_z \sigma a\_x & \sigma a\_z \sigma a\_y & (\sigma a\_z)^2\end{array}\right]$$ ![figure](../assets/f713e7bd1f08765d.svg)

The diagonal entries represent the variances of the reconstructed
3D point in x-, y-, and z-direction. The computed matrices are
returned in the parameter *`covWP`* in form of
tuples each with 9 elements:

$$[(sigma\_x)^{2},sigma\_xy,sigma\_xz,sigma\_yx,(sigma\_y)^{2},sigma\_yz,sigma\_zx,sigma\_zy,(sigma\_z)^{2}].$$

Thus, `|CovWP|=9*|X|` and `CovWP[J*9:J*9+8]` is the covariance matrix
for the `J`-th 3D point. Note that if the camera setup
associated with the stereo model contains the covariance matrices for the
camera parameters, these covariance matrices are considered in the
computation of *`covWP`* too.

If the stereo model has a valid bounding box set (see
[`SetStereoModelParam`](set_stereo_model_param.md)), the resulting points are clipped to this
bounding box, i.e., points outside it are not returned. If the bounding box
associated with the stereo model is invalid, it is ignored and all points
that could be reconstructed are returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`stereoModelID`** (input_control)  stereo_model `→` [HStereoModel](HStereoModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the stereo model.

**`row`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of the detected points.

**`column`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of the detected points.

**`covIP`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Covariance matrices of the detected points.

Default:
[]

**`cameraIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Indices of the observing cameras.

Suggested values:
0, 1, 2

**`pointIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Indices of the observed world points.

Suggested values:
0, 1, 2

**`x`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinates of the reconstructed 3D points.

**`y`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the reconstructed 3D points.

**`z`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the reconstructed 3D points.

**`covWP`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Covariance matrices of the reconstructed 3D points.

**`pointIdxOut`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

Indices of the reconstructed 3D points.

## Alternatives

`ReconstructSurfaceStereo`,
`IntersectLinesOfSight`

## Module

3D Metrology
