# DeserializeSheetOfLightModel (Operator)

## Name

`DeserializeSheetOfLightModel` — Deserialize a sheet-of-light model.

## Signature

`static void HOperatorSet.DeserializeSheetOfLightModel(HTuple serializedItemHandle, out HTuple sheetOfLightModelID)`

`void HSheetOfLightModel.DeserializeSheetOfLightModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeSheetOfLightModel` deserializes a sheet-of-light model
that was serialized by [`SerializeSheetOfLightModel`](serialize_sheet_of_light_model.md)
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized model is defined by the
handle *`serializedItemHandle`*. The deserialized values are stored
in a new sheet-of-light model with the handle *`sheetOfLightModelID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`sheetOfLightModelID`** (output_control)  sheet_of_light_model `→` [HSheetOfLightModel](HSheetOfLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the sheet-of-light model.

## Result

The operator `DeserializeSheetOfLightModel` returns the value 2 (
H_MSG_TRUE)
if the sheet-of-light model can be correctly deserialized.
Otherwise, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeSheetOfLightModel`

## Possible Successors

`MeasureProfileSheetOfLight`

## Alternatives

`CreateSheetOfLightModel`

## See also

`SerializeSheetOfLightModel`

## Module

3D Metrology
