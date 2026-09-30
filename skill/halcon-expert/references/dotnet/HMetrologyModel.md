# HMetrologyModel (Class)

## Name

`HMetrologyModel` — Represents an instance of a metrology model.

## Constructors

|  |  |  |
| --- | --- | --- |
| `ReadMetrologyModel` |  | Read a metrology model from a file. |
| `CreateMetrologyModel` |  | Create the data structure that is needed to measure geometric shapes. |

## Methods

|  |  |  |
| --- | --- | --- |
| `AddMetrologyObjectCircleMeasure` |  | Add a circle or a circular arc to a metrology model. |
| `AddMetrologyObjectEllipseMeasure` |  | Add an ellipse or an elliptic arc to a metrology model. |
| `AddMetrologyObjectGeneric` |  | Add a metrology object to a metrology model. |
| `AddMetrologyObjectLineMeasure` |  | Add a line to a metrology model. |
| `AddMetrologyObjectRectangle2Measure` |  | Add a rectangle to a metrology model. |
| `AlignMetrologyModel` |  | Alignment of a metrology model. |
| `ApplyMetrologyModel` |  | Measure and fit the geometric shapes of all metrology objects of a metrology model. |
| `ClearMetrologyModel` |  | Delete a metrology model and free the allocated memory. |
| `ClearMetrologyObject` |  | Delete metrology objects and free the allocated memory. |
| `CopyMetrologyModel` |  | Copy a metrology model. |
| `CopyMetrologyObject` |  | Copy metrology metrology objects of a metrology model. |
| `CreateMetrologyModel` |  | Create the data structure that is needed to measure geometric shapes. |
| `DeserializeMetrologyModel` |  | Deserialize a serialized metrology model. |
| `GetMetrologyModelParam` |  | Get parameters that are valid for the entire metrology model. |
| `GetMetrologyObjectFuzzyParam` |  | Get a fuzzy parameter of a metrology model. |
| `GetMetrologyObjectIndices` |  | Get the indices of the metrology objects of a metrology model. |
| `GetMetrologyObjectMeasures` |  | Get the measure regions and the results of the edge location for the metrology objects of a metrology model. |
| `GetMetrologyObjectModelContour` |  | Query the model contour of a metrology object in image coordinates. |
| `GetMetrologyObjectNumInstances` |  | Get the number of instances of the metrology objects of a metrology model. |
| `GetMetrologyObjectParam` |  | Get one or several parameters of a metrology model. |
| `GetMetrologyObjectResult` |  | Get the results of the measurement of a metrology model. |
| `GetMetrologyObjectResultContour` |  | Query the result contour of a metrology object. |
| `ReadMetrologyModel` |  | Read a metrology model from a file. |
| `ResetMetrologyObjectFuzzyParam` |  | Reset all fuzzy parameters and fuzzy functions of a metrology model. |
| `ResetMetrologyObjectParam` |  | Reset all parameters of a metrology model. |
| `SerializeMetrologyModel` |  | Serialize a metrology model. |
| `SetMetrologyModelImageSize` |  | Set the size of the image of metrology objects. |
| `SetMetrologyModelParam` |  | Set parameters that are valid for the entire metrology model. |
| `SetMetrologyObjectFuzzyParam` |  | Set fuzzy parameters or fuzzy functions for a metrology model. |
| `SetMetrologyObjectParam` |  | Set parameters for the metrology objects of a metrology model. |
| `TransformMetrologyObject` |  | Transform metrology objects of a metrology model, e.g., for alignment. |
| `WriteMetrologyModel` |  | Write a metrology model to a file. |
