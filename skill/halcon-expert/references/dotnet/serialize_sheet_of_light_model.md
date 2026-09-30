# SerializeSheetOfLightModel (Operator)

## Name

`SerializeSheetOfLightModel` — Serialize a sheet-of-light model.

## Signature

`static void HOperatorSet.SerializeSheetOfLightModel(HTuple sheetOfLightModelID, out HTuple serializedItemHandle)`

`HSerializedItem HSheetOfLightModel.SerializeSheetOfLightModel()`

## Description

`SerializeSheetOfLightModel` serializes a sheet-of-light model (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`WriteSheetOfLightModel`](write_sheet_of_light_model.md) is converted to a serialized item.
The sheet-of-light model is defined by the handle
*`sheetOfLightModelID`*. The serialized model is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeSheetOfLightModel`](deserialize_sheet_of_light_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`sheetOfLightModelID`** (input_control)  sheet_of_light_model `→` [HSheetOfLightModel](HSheetOfLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the sheet-of-light model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

The operator `SerializeSheetOfLightModel` returns the value 2 (
H_MSG_TRUE)
if the passed handle of the sheet-of-light model is valid and if the model
can be serialized into the serialized item.
Otherwise, an exception is raised.

## Possible Predecessors

`CreateSheetOfLightModel`,
`SetSheetOfLightParam`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeSheetOfLightModel`

## See also

`DeserializeSheetOfLightModel`

## Module

3D Metrology
