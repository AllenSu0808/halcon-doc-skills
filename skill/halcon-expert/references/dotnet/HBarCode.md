# HBarCode (Class)

## Name

`HBarCode` — Represents an instance of a bar code reader.

## Constructors

|  |  |  |
| --- | --- | --- |
| `ReadBarCodeModel` |  | Read a bar code model from a file and create a new model. |
| `CreateBarCodeModel` |  | Create a model of a bar code reader. |

## Methods

|  |  |  |
| --- | --- | --- |
| `ClearBarCodeModel` |  | Delete a bar code model and free the allocated memory |
| `CreateBarCodeModel` |  | Create a model of a bar code reader. |
| `DecodeBarCodeRectangle2` |  | Decode bar code symbols within a rectangle. |
| `DeserializeBarCodeModel` |  | Deserialize a bar code model. |
| `FindBarCode` |  | Detect and read bar code symbols in an image. |
| `GetBarCodeObject` |  | Access iconic objects that were created during the search or decoding of bar code symbols. |
| `GetBarCodeParam` |  | Get one or several parameters that describe the bar code model. |
| `GetBarCodeParamSpecific` |  | Get parameters that are used by the bar code reader when processing a specific bar code type. |
| `GetBarCodeResult` |  | Get the alphanumerical results that were accumulated during the decoding of bar code symbols. |
| `QueryBarCodeParams` |  | Get the names of the parameters that can be used in set_bar_code* and get_bar_code* operators for a given bar code model |
| `ReadBarCodeModel` |  | Read a bar code model from a file and create a new model. |
| `SerializeBarCodeModel` |  | Serialize a bar code model. |
| `SetBarCodeParam` |  | Set selected parameters of the bar code model. |
| `SetBarCodeParamSpecific` |  | Set selected parameters of the bar code model for selected bar code types |
| `WriteBarCodeModel` |  | Write a bar code model to a file. |
