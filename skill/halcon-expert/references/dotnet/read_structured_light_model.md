# ReadStructuredLightModel (Operator)

## Name

`ReadStructuredLightModel` — Read a structured light model from a file.

## Signature

`static void HOperatorSet.ReadStructuredLightModel(HTuple fileName, out HTuple structuredLightModel)`

`void HStructuredLightModel.ReadStructuredLightModel(string fileName)`

## Description

`ReadStructuredLightModel` reads the structured light model
*`structuredLightModel`* that has been stored with
[`WriteStructuredLightModel`](write_structured_light_model.md). The default HALCON file extension
for the structured light model is 'hslm'.

It can be helpful to write a model after setting all the optimal parameters
for a particular setup. The model can be read later to easily regenerate
pattern images. The objects already generated in the model before
writing it can be also revisited later after reading the model.

For an explanation of the concept of structured light and its supported
applications, see the introduction of chapter
[Inspection / Structured Light](toc_inspection_structuredlight.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`hslm`

**`structuredLightModel`** (output_control)  structured_light_model `→` [HStructuredLightModel](HStructuredLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the structured light model.

## Example (HDevelop)

```
* Read the model
read_structured_light_model ('ExampleModel.hslm', StructuredLightModel)
* Get a previously decoded result
get_structured_light_object (CorrespondenceImages, StructuredLightModel, \
                             'correspondence_image')
* Decode new camera images
decode_structured_light_pattern (CameraImages, StructuredLightModel)
* Get the decoded result
get_structured_light_object (CorrespondenceImagesNew, StructuredLightModel, \
                             'correspondence_image')
```

## Result

The operator `ReadStructuredLightModel` returns the value
2 (
H_MSG_TRUE)
if the given parameters are valid. Otherwise, an exception will be
raised.

## Possible Predecessors

`WriteStructuredLightModel`

## See also

`CreateStructuredLightModel`,
`ClearStructuredLightModel`

## Module

3D Metrology
