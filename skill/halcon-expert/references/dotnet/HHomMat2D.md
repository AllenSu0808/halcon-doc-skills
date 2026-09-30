# HHomMat2D (Class)

## Name

`HHomMat2D` — Represents a homogeneous 2D transformation matrix.

## Constructors

|  |  |  |
| --- | --- | --- |
| `HomMat2dIdentity` |  | Generate the homogeneous transformation matrix of the identical 2D transformation. |

## Methods

|  |  |  |
| --- | --- | --- |
| `AffineTransContourXld` |  | Apply an arbitrary affine 2D transformation to XLD contours. |
| `AffineTransImage` |  | Apply an arbitrary affine 2D transformation to images. |
| `AffineTransImageSize` |  | Apply an arbitrary affine 2D transformation to an image and specify the output image size. |
| `AffineTransPixel` |  | Apply an arbitrary affine 2D transformation to pixel coordinates. |
| `AffineTransPoint2d` |  | Apply an arbitrary affine 2D transformation to points. |
| `AffineTransPolygonXld` |  | Apply an arbitrary affine transformation to XLD polygons. |
| `AffineTransRegion` |  | Apply an arbitrary affine 2D transformation to regions. |
| `BundleAdjustMosaic` |  | Perform a bundle adjustment of an image mosaic. |
| `CamMatToCamPar` |  | Compute the internal camera parameters from a camera matrix. |
| `CamParToCamMat` |  | Compute a camera matrix from internal camera parameters. |
| `DeserializeHomMat2d` |  | Deserialize a serialized homogeneous 2D transformation matrix. |
| `EssentialToFundamentalMatrix` |  | Compute the fundamental matrix from an essential matrix. |
| `GenBinocularProjRectification` |  | Compute the projective rectification of weakly calibrated binocular stereo images. |
| `HomMat2dCompose` |  | Multiply two homogeneous 2D transformation matrices. |
| `HomMat2dDeterminant` |  | Compute the determinant of a homogeneous 2D transformation matrix. |
| `HomMat2dIdentity` |  | Generate the homogeneous transformation matrix of the identical 2D transformation. |
| `HomMat2dInvert` |  | Invert a homogeneous 2D transformation matrix. |
| `HomMat2dReflect` |  | Add a reflection to a homogeneous 2D transformation matrix. |
| `HomMat2dReflectLocal` |  | Add a reflection to a homogeneous 2D transformation matrix. |
| `HomMat2dRotate` |  | Add a rotation to a homogeneous 2D transformation matrix. |
| `HomMat2dRotateLocal` |  | Add a rotation to a homogeneous 2D transformation matrix. |
| `HomMat2dScale` |  | Add a scaling to a homogeneous 2D transformation matrix. |
| `HomMat2dScaleLocal` |  | Add a scaling to a homogeneous 2D transformation matrix. |
| `HomMat2dSlant` |  | Add a slant to a homogeneous 2D transformation matrix. |
| `HomMat2dSlantLocal` |  | Add a slant to a homogeneous 2D transformation matrix. |
| `HomMat2dToAffinePar` |  | Compute the affine transformation parameters from a homogeneous 2D transformation matrix. |
| `HomMat2dTranslate` |  | Add a translation to a homogeneous 2D transformation matrix. |
| `HomMat2dTranslateLocal` |  | Add a translation to a homogeneous 2D transformation matrix. |
| `HomMat2dTranspose` |  | Transpose a homogeneous 2D transformation matrix. |
| `HomVectorToProjHomMat2d` |  | Compute a homogeneous transformation matrix using given point correspondences. |
| `MatchEssentialMatrixRansac` |  | Compute the essential matrix for a pair of stereo images by automatically finding correspondences between image points. |
| `MatchFundamentalMatrixDistortionRansac` |  | Compute the fundamental matrix and the radial distortion coefficient for a pair of stereo images by automatically finding correspondences between image points. |
| `MatchFundamentalMatrixRansac` |  | Compute the fundamental matrix for a pair of stereo images by automatically finding correspondences between image points. |
| `PointLineToHomMat2d` |  | Approximate an affine transformation from point-to-line correspondences. |
| `ProjMatchPointsDistortionRansac` |  | Compute a projective transformation matrix between two images and the radial distortion coefficient by automatically finding correspondences between points. |
| `ProjMatchPointsDistortionRansacGuided` |  | Compute a projective transformation matrix and the radial distortion coefficient between two images by finding correspondences between points based on known approximations of the projective transformation matrix and the radial distortion coefficient. |
| `ProjMatchPointsRansac` |  | Compute a projective transformation matrix between two images by finding correspondences between points. |
| `ProjMatchPointsRansacGuided` |  | Compute a projective transformation matrix between two images by finding correspondences between points based on a known approximation of the projective transformation matrix. |
| `ProjectiveTransContourXld` |  | Apply a projective transformation to an XLD contour. |
| `ProjectiveTransImage` |  | Apply a projective transformation to an image. |
| `ProjectiveTransImageSize` |  | Apply a projective transformation to an image and specify the output image size. |
| `ProjectiveTransPixel` |  | Project pixel coordinates using a homogeneous projective transformation matrix. |
| `ProjectiveTransPoint2d` |  | Project a homogeneous 2D point using a projective transformation matrix. |
| `ProjectiveTransRegion` |  | Apply a projective transformation to a region. |
| `ReadWorldFile` |  | Read the geo coding from an ARC/INFO world file. |
| `Reconst3dFromFundamentalMatrix` |  | Compute the projective 3d reconstruction of points based on the fundamental matrix. |
| `RelPoseToFundamentalMatrix` |  | Compute the fundamental matrix from the relative orientation of two cameras. |
| `SerializeHomMat2d` |  | Serialize a homogeneous 2D transformation matrix. |
| `StationaryCameraSelfCalibration` |  | Perform a self-calibration of a stationary projective camera. |
| `VectorAngleToRigid` |  | Compute a rigid affine transformation from points and angles. |
| `VectorFieldToHomMat2d` |  | Approximate an affine map from a displacement vector field. |
| `VectorToAniso` |  | Approximate an anisotropic similarity transformation from point correspondences. |
| `VectorToEssentialMatrix` |  | Compute the essential matrix given image point correspondences and known camera matrices and reconstruct 3D points. |
| `VectorToFundamentalMatrix` |  | Compute the fundamental matrix given a set of image point correspondences and reconstruct 3D points. |
| `VectorToFundamentalMatrixDistortion` |  | Compute the fundamental matrix and the radial distortion coefficient given a set of image point correspondences and reconstruct 3D points. |
| `VectorToHomMat2d` |  | Approximate an affine transformation from point correspondences. |
| `VectorToProjHomMat2d` |  | Compute a projective transformation matrix using given point correspondences. |
| `VectorToProjHomMat2dDistortion` |  | Compute a projective transformation matrix and the radial distortion coefficient using given image point correspondences. |
| `VectorToRigid` |  | Approximate a rigid affine transformation from point correspondences. |
| `VectorToSimilarity` |  | Approximate an similarity transformation from point correspondences. |
