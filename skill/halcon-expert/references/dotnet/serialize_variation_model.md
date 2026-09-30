# SerializeVariationModel (Operator)

## Name

`SerializeVariationModel` — Serialize a variation model.

## Signature

`static void HOperatorSet.SerializeVariationModel(HTuple modelID, out HTuple serializedItemHandle)`

`HSerializedItem HVariationModel.SerializeVariationModel()`

## Description

`SerializeVariationModel` serializes the data of a variation model
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`WriteVariationModel`](write_variation_model.md) is converted to a serialized
item. The variation model is defined by the handle
*`modelID`*. The serialized variation model is returned by the
handle *`serializedItemHandle`* and can be deserialized by
[`DeserializeVariationModel`](deserialize_variation_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  variation_model `→` [HVariationModel](HVariationModel.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the variation model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeVariationModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainVariationModel`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeVariationModel`

## See also

`ReadVariationModel`,
`WriteVariationModel`

## Module

Matching
