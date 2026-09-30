# HDescriptorModel (Class)

## Name

`HDescriptorModel` — Represents an instance of a descriptor model.

## Constructors

|  |  |  |
| --- | --- | --- |
| `ReadDescriptorModel` |  | Read a descriptor model from a file. |
| `CreateCalibDescriptorModel` |  | Create a descriptor model for calibrated perspective matching. |
| `CreateUncalibDescriptorModel` |  | Prepare a descriptor model for interest point matching. |

## Methods

|  |  |  |
| --- | --- | --- |
| `ClearDescriptorModel` |  | Free the memory of a descriptor model. |
| `CreateCalibDescriptorModel` |  | Create a descriptor model for calibrated perspective matching. |
| `CreateUncalibDescriptorModel` |  | Prepare a descriptor model for interest point matching. |
| `DeserializeDescriptorModel` |  | Deserialize a descriptor model. |
| `FindCalibDescriptorModel` |  | Find the best matches of a calibrated descriptor model in an image and return their 3D pose. |
| `FindUncalibDescriptorModel` |  | Find the best matches of a descriptor model in an image. |
| `GetDescriptorModelOrigin` |  | Return the origin of a descriptor model. |
| `GetDescriptorModelParams` |  | Return the parameters of a descriptor model. |
| `GetDescriptorModelPoints` |  | Query the interest points of the descriptor model or the last processed search image. |
| `GetDescriptorModelResults` |  | Query alphanumerical results that were accumulated during descriptor-based matching. |
| `ReadDescriptorModel` |  | Read a descriptor model from a file. |
| `SerializeDescriptorModel` |  | Serialize a descriptor model. |
| `SetDescriptorModelOrigin` |  | Sets the origin of a descriptor model. |
| `WriteDescriptorModel` |  | Write a descriptor model to a file. |
