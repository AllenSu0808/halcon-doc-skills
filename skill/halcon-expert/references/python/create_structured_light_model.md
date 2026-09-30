# create_structured_light_model (Operator)

## Name

`create_structured_light_model` — Create a structured light model.

## Signature

`def create_structured_light_model(model_type: str) -> HHandle`

## Description

`create_structured_light_model` creates a new structured light
model of type *`model_type`*. Currently, the types
*"deflectometry"* and *"3d_reconstruction"* are supported.

The parameters of the structured light model can be queried with
[`get_structured_light_model_param`](get_structured_light_model_param.md) and manipulated by calls to
[`set_structured_light_model_param`](set_structured_light_model_param.md).

For an explanation of the concept of structured light and its supported
applications, see the introduction of chapter
[Inspection / Structured Light](toc_inspection_structuredlight.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`model_type`** (input_control)  string `→` str

The type of the created structured light model.

Default:
"deflectometry"

List of values:
"3d_reconstruction", "deflectometry"

**`structured_light_model`** (output_control)  structured_light_model `→` HHandle

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

The operator `create_structured_light_model` returns the value 2 (
H_MSG_TRUE)
if the structured light model can be allocated correctly. Otherwise, an
exception will be raised.

## Possible Successors

`set_structured_light_model_param`,
`get_structured_light_model_param`

## Module

3D Metrology
