# HDeformableModel (Class)

## Name

`HDeformableModel` — Represents an instance of a deformable model for matching.

## Constructors

|  |  |  |
| --- | --- | --- |
| `ReadDeformableModel` |  | Read a deformable model from a file. |
| `CreatePlanarCalibDeformableModelXld` |  | Prepare a deformable model for planar calibrated matching from XLD contours. |
| `CreatePlanarUncalibDeformableModelXld` |  | Prepare a deformable model for planar uncalibrated matching from XLD contours. |
| `CreatePlanarCalibDeformableModel` |  | Create a deformable model for calibrated perspective matching. |
| `CreatePlanarUncalibDeformableModel` |  | Creates a deformable model for uncalibrated, perspective matching. |

## Methods

|  |  |  |
| --- | --- | --- |
| `ClearDeformableModel` |  | Free the memory of a deformable model. |
| `CreateLocalDeformableModel` |  | Creates a deformable model for local, deformable matching. |
| `CreateLocalDeformableModelXld` |  | Prepare a deformable model for local deformable matching from XLD contours. |
| `CreatePlanarCalibDeformableModel` |  | Create a deformable model for calibrated perspective matching. |
| `CreatePlanarCalibDeformableModelXld` |  | Prepare a deformable model for planar calibrated matching from XLD contours. |
| `CreatePlanarUncalibDeformableModel` |  | Creates a deformable model for uncalibrated, perspective matching. |
| `CreatePlanarUncalibDeformableModelXld` |  | Prepare a deformable model for planar uncalibrated matching from XLD contours. |
| `DeserializeDeformableModel` |  | Deserialize a deformable model. |
| `FindLocalDeformableModel` |  | Find the best matches of a local deformable model in an image. |
| `FindPlanarCalibDeformableModel` |  | Find the best matches of a calibrated deformable model in an image and return their 3D pose. |
| `FindPlanarUncalibDeformableModel` |  | Find the best matches of a planar projective invariant deformable model in an image. |
| `GetDeformableModelContours` |  | Return the contour representation of a deformable model. |
| `GetDeformableModelOrigin` |  | Return the origin (reference point) of a deformable model. |
| `GetDeformableModelParams` |  | Return the parameters of a deformable model. |
| `ReadDeformableModel` |  | Read a deformable model from a file. |
| `SerializeDeformableModel` |  | Serialize a deformable model. |
| `SetDeformableModelOrigin` |  | Set the origin (reference point) of a deformable model. |
| `SetDeformableModelParam` |  | Set selected parameters of the deformable model. |
| `SetLocalDeformableModelMetric` |  | Set the metric of a local deformable model that was created from XLD contours. |
| `SetPlanarCalibDeformableModelMetric` |  | Set the metric of a planar calibrated deformable model that was created from XLD contours. |
| `SetPlanarUncalibDeformableModelMetric` |  | Set the metric of a planar uncalibrated deformable model that was created from XLD contours. |
| `WriteDeformableModel` |  | Write a deformable model to a file. |
