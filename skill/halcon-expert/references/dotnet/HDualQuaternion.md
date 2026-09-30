# HDualQuaternion (Class)

## Name

`HDualQuaternion` — Represents a dual quaternion.

## Constructors

|  |  |  |
| --- | --- | --- |
| `ScrewToDualQuat` |  | Convert a screw into a dual quaternion. |
| `PoseToDualQuat` |  | Convert a 3D pose to a unit dual quaternion. |

## Methods

|  |  |  |
| --- | --- | --- |
| `DeserializeDualQuat` |  | Deserialize a serialized dual quaternion. |
| `DualQuatCompose` |  | Multiply two dual quaternions. |
| `DualQuatConjugate` |  | Conjugate a dual quaternion. |
| `DualQuatInterpolate` |  | Interpolate two dual quaternions. |
| `DualQuatNormalize` |  | Normalize a dual quaternion. |
| `DualQuatToHomMat3d` |  | Convert a unit dual quaternion into a homogeneous transformation matrix. |
| `DualQuatToPose` |  | Convert a dual quaternion to a 3D pose. |
| `DualQuatToScrew` |  | Convert a unit dual quaternion into a screw. |
| `DualQuatTransLine3d` |  | Transform a 3D line with a unit dual quaternion. |
| `DualQuatTransPoint3d` |  | Transform a 3D point with a unit dual quaternion. |
| `PoseToDualQuat` |  | Convert a 3D pose to a unit dual quaternion. |
| `ScrewToDualQuat` |  | Convert a screw into a dual quaternion. |
| `SerializeDualQuat` |  | Serialize a dual quaternion. |
