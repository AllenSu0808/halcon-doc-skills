# HSheetOfLightModel (Class)

## Name

`HSheetOfLightModel` — Represents an instance of the data structure required to perform
3D measurements with the sheet-of-light technique.

## Constructors

|  |  |  |
| --- | --- | --- |
| `ReadSheetOfLightModel` |  | Read a sheet-of-light model from a file and create a new model. |
| `CreateSheetOfLightModel` |  | Create a model to perform 3D-measurements using the sheet-of-light technique. |

## Methods

|  |  |  |
| --- | --- | --- |
| `ApplySheetOfLightCalibration` |  | Apply the calibration transformations to the input disparity image. |
| `CalibrateSheetOfLight` |  | Calibrate a sheet-of-light setup with a 3D calibration object. |
| `ClearSheetOfLightModel` |  | Delete a sheet-of-light model and free the allocated memory. |
| `CreateSheetOfLightModel` |  | Create a model to perform 3D-measurements using the sheet-of-light technique. |
| `DeserializeSheetOfLightModel` |  | Deserialize a sheet-of-light model. |
| `GetSheetOfLightParam` |  | Get the value of a parameter, which has been set in a sheet-of-light model. |
| `GetSheetOfLightResult` |  | Get the iconic results of a measurement performed with the sheet-of light technique. |
| `GetSheetOfLightResultObjectModel3d` |  | Get the result of a calibrated measurement performed with the sheet-of-light technique as a 3D object model. |
| `MeasureProfileSheetOfLight` |  | Process the profile image provided as input and store the resulting disparity to the sheet-of-light model. |
| `QuerySheetOfLightParams` |  | For a given sheet-of-light model get the names of the generic iconic or control parameters that can be used in the different sheet-of-light operators. |
| `ReadSheetOfLightModel` |  | Read a sheet-of-light model from a file and create a new model. |
| `ResetSheetOfLightModel` |  | Reset a sheet-of-light model. |
| `SerializeSheetOfLightModel` |  | Serialize a sheet-of-light model. |
| `SetProfileSheetOfLight` |  | Set sheet of light profiles by measured disparities. |
| `SetSheetOfLightParam` |  | Set selected parameters of the sheet-of-light model. |
| `WriteSheetOfLightModel` |  | Write a sheet-of-light model to a file. |
