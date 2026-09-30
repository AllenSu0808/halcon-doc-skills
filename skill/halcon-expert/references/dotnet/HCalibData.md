# HCalibData (Class)

## Name

`HCalibData` — Represents an instance of a camera calibration model.

## Constructors

|  |  |  |
| --- | --- | --- |
| `ReadCalibData` |  | Restore a calibration data model from a file. |
| `CreateCalibData` |  | Create a calibration data model. |

## Methods

|  |  |  |
| --- | --- | --- |
| `CalibrateCameras` |  | Determine all camera parameters by a simultaneous minimization process. |
| `CalibrateHandEye` |  | Perform a hand-eye calibration. |
| `ClearCalibData` |  | Free the memory of a calibration data model. |
| `CreateCalibData` |  | Create a calibration data model. |
| `DeserializeCalibData` |  | Deserialize a serialized calibration data model. |
| `FindCalibObject` |  | Find the calibration plate and set the extracted points and contours in a calibration data model. |
| `GetCalibData` |  | Query data stored or computed in a calibration data model. |
| `GetCalibDataObservContours` |  | Get contour-based observation data from a calibration data model. |
| `GetCalibDataObservPoints` |  | Get point-based observation data from a calibration data model. |
| `GetCalibDataObservPose` |  | Get observed calibration object poses from a calibration data model. |
| `QueryCalibDataObservIndices` |  | Query information about the relations between cameras, calibration objects, and calibration object poses. |
| `ReadCalibData` |  | Restore a calibration data model from a file. |
| `RemoveCalibData` |  | Remove a data set from a calibration data model. |
| `RemoveCalibDataObserv` |  | Remove observation data from a calibration data model. |
| `SerializeCalibData` |  | Serialize a calibration data model. |
| `SetCalibData` |  | Set data in a calibration data model. |
| `SetCalibDataCalibObject` |  | Define a calibration object in a calibration model. |
| `SetCalibDataCamParam` |  | Set type and initial parameters of a camera in a calibration data model. |
| `SetCalibDataObservPoints` |  | Set point-based observation data in a calibration data model. |
| `SetCalibDataObservPose` |  | Set observed calibration object poses in a calibration data model. |
| `WriteCalibData` |  | Store a calibration data model into a file. |
