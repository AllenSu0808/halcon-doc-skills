# HHomMat3D (Class)

## Name

`HHomMat3D` — Represents a homogeneous 3D transformation matrix.

## Constructors

|  |  |  |
| --- | --- | --- |
| `HomMat3dIdentity` |  | Generate the homogeneous transformation matrix of the identical 3D transformation. |

## Methods

|  |  |  |
| --- | --- | --- |
| `AffineTransPoint3d` |  | Apply an arbitrary affine 3D transformation to points. |
| `DeserializeHomMat3d` |  | Deserialize a serialized homogeneous 3D transformation matrix. |
| `HomMat3dCompose` |  | Multiply two homogeneous 3D transformation matrices. |
| `HomMat3dDeterminant` |  | Compute the determinant of a homogeneous 3D transformation matrix. |
| `HomMat3dIdentity` |  | Generate the homogeneous transformation matrix of the identical 3D transformation. |
| `HomMat3dInvert` |  | Invert a homogeneous 3D transformation matrix. |
| `HomMat3dProject` |  | Project an affine 3D transformation matrix to a 2D projective transformation matrix. |
| `HomMat3dRotate` |  | Add a rotation to a homogeneous 3D transformation matrix. |
| `HomMat3dRotateLocal` |  | Add a rotation to a homogeneous 3D transformation matrix. |
| `HomMat3dScale` |  | Add a scaling to a homogeneous 3D transformation matrix. |
| `HomMat3dScaleLocal` |  | Add a scaling to a homogeneous 3D transformation matrix. |
| `HomMat3dToPose` |  | Convert a homogeneous transformation matrix into a 3D pose. |
| `HomMat3dTranslate` |  | Add a translation to a homogeneous 3D transformation matrix. |
| `HomMat3dTranslateLocal` |  | Add a translation to a homogeneous 3D transformation matrix. |
| `HomMat3dTranspose` |  | Transpose a homogeneous 3D transformation matrix. |
| `PointPlueckerLineToHomMat3d` |  | Approximate a 3D affine transformation from 3D point-to-line correspondences. |
| `ProjectHomPointHomMat3d` |  | Project a homogeneous 3D point using a 3×4 projection matrix. |
| `ProjectPointHomMat3d` |  | Project a 3D point using a 3×4 projection matrix. |
| `ProjectiveTransHomPoint3d` |  | Project a homogeneous 3D point using a projective transformation matrix. |
| `ProjectiveTransPoint3d` |  | Project a 3D point using a projective transformation matrix. |
| `SerializeHomMat3d` |  | Serialize a homogeneous 3D transformation matrix. |
| `VectorToHomMat3d` |  | Approximate a 3D transformation from point correspondences. |
