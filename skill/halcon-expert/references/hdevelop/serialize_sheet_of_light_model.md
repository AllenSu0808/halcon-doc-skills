# serialize_sheet_of_light_model (Operator)

## Name

`serialize_sheet_of_light_model` — Serialize a sheet-of-light model.

## Signature

`serialize_sheet_of_light_model( : : SheetOfLightModelID : SerializedItemHandle)`

## Description

`serialize_sheet_of_light_model` serializes a sheet-of-light model (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`write_sheet_of_light_model`](write_sheet_of_light_model.md) is converted to a serialized item.
The sheet-of-light model is defined by the handle
*`SheetOfLightModelID`*. The serialized model is returned by the handle
*`SerializedItemHandle`* and can be deserialized by
[`deserialize_sheet_of_light_model`](deserialize_sheet_of_light_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SheetOfLightModelID`** (input_control)  sheet_of_light_model `→`  (handle)

Handle of the sheet-of-light model.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

The operator `serialize_sheet_of_light_model` returns the value 2 (
H_MSG_TRUE)
if the passed handle of the sheet-of-light model is valid and if the model
can be serialized into the serialized item.
Otherwise, an exception is raised.

## Possible Predecessors

`create_sheet_of_light_model`,
`set_sheet_of_light_param`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_sheet_of_light_model`

## See also

`deserialize_sheet_of_light_model`

## Module

3D Metrology
