# deserialize_sheet_of_light_model (Operator)

## Name

`deserialize_sheet_of_light_model` — Deserialize a sheet-of-light model.

## Signature

`def deserialize_sheet_of_light_model(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_sheet_of_light_model` deserializes a sheet-of-light model
that was serialized by [`serialize_sheet_of_light_model`](serialize_sheet_of_light_model.md)
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized model is defined by the
handle *`serialized_item_handle`*. The deserialized values are stored
in a new sheet-of-light model with the handle *`sheet_of_light_model_id`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`sheet_of_light_model_id`** (output_control)  sheet_of_light_model `→` HHandle

Handle of the sheet-of-light model.

## Result

The operator `deserialize_sheet_of_light_model` returns the value 2 (
H_MSG_TRUE)
if the sheet-of-light model can be correctly deserialized.
Otherwise, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_sheet_of_light_model`

## Possible Successors

`measure_profile_sheet_of_light`

## Alternatives

`create_sheet_of_light_model`

## See also

`serialize_sheet_of_light_model`

## Module

3D Metrology
