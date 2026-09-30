# write_structured_light_model (Operator)

## Name

`write_structured_light_model` — Write a structured light model to a file.

## Signature

`def write_structured_light_model(structured_light_model: HHandle, file_name: str) -> None`

## Description

`write_structured_light_model` writes the structured light model
*`structured_light_model`* to the file given by *`file_name`*. The
default HALCON file extension for the structured light model is 'hslm'.
The structured light model can be then read with
[`read_structured_light_model`](read_structured_light_model.md). It should be noted that
`write_structured_light_model` does *not* write any
previously generated pattern images in the structured light model. In other
words, only the parameters of the model and objects that were already
generated will be written in the file. The list of structured light objects
and how to generate each can be found in
[`get_structured_light_object`](get_structured_light_object.md).

For an explanation of the concept of structured light and its supported
applications, see the introduction of chapter
[Inspection / Structured Light](toc_inspection_structuredlight.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`structured_light_model`** (input_control)  structured_light_model `→` HHandle

Handle of the structured light model.

**`file_name`** (input_control)  filename.write `→` str

File name.

File extension:
.`hslm`

## Example (HDevelop)

```
* Create the model
create_structured_light_model ('deflectometry', StructuredLightModel)
* Generate the patterns to project
gen_structured_light_pattern (PatternImages, StructuredLightModel)
* Decode the camera images
decode_structured_light_pattern (CameraImages, StructuredLightModel)
* Write the model
write_structured_light_model (StructuredLightModel, 'ExampleModel.hslm')
```

## Result

The operator `write_structured_light_model` returns the value
2 (
H_MSG_TRUE)
if the given parameters are valid. Otherwise, an exception will be
raised.

## Possible Successors

`clear_structured_light_model`

## See also

`create_structured_light_model`,
`clear_structured_light_model`

## Module

3D Metrology
