# CreateStructuredLightModel (Operator)

## Name

`CreateStructuredLightModel` — Create a structured light model.

## Signature

`static void HOperatorSet.CreateStructuredLightModel(HTuple modelType, out HTuple structuredLightModel)`

`public HStructuredLightModel(string modelType)`

`void HStructuredLightModel.CreateStructuredLightModel(string modelType)`

## Description

`CreateStructuredLightModel` creates a new structured light
model of type *`modelType`*. Currently, the types
*"deflectometry"* and *"3d_reconstruction"* are supported.

The parameters of the structured light model can be queried with
[`GetStructuredLightModelParam`](get_structured_light_model_param.md) and manipulated by calls to
[`SetStructuredLightModelParam`](set_structured_light_model_param.md).

For an explanation of the concept of structured light and its supported
applications, see the introduction of chapter
[Inspection / Structured Light](toc_inspection_structuredlight.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`modelType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

The type of the created structured light model.

Default:
"deflectometry"

List of values:
"3d_reconstruction", "deflectometry"

**`structuredLightModel`** (output_control)  structured_light_model `→` [HStructuredLightModel](HStructuredLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle for using and accessing the structured
light model.

## Example (HDevelop)

```
* Create the model
create_structured_light_model ('deflectometry', StructuredLightModel)
* Generate the patterns to project
gen_structured_light_pattern (PatternImages, StructuredLightModel)
* Decode the camera images
decode_structured_light_pattern (CameraImages, StructuredLightModel)
```

## Result

The operator `CreateStructuredLightModel` returns the value 2 (
H_MSG_TRUE)
if the structured light model can be allocated correctly. Otherwise, an
exception will be raised.

## Possible Successors

`SetStructuredLightModelParam`,
`GetStructuredLightModelParam`

## Module

3D Metrology
