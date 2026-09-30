# DeserializeVariationModel (Operator)

## Name

`DeserializeVariationModel` — Deserialize a variation model.

## Signature

`static void HOperatorSet.DeserializeVariationModel(HTuple serializedItemHandle, out HTuple modelID)`

`void HVariationModel.DeserializeVariationModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeVariationModel` deserializes a variation model,
that was serialized by [`SerializeVariationModel`](serialize_variation_model.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized variation model is
defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
variation model with the handle *`modelID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`modelID`** (output_control)  variation_model `→` [HVariationModel](HVariationModel.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the variation model.

## Result

If the parameters are valid, the operator
`DeserializeVariationModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeVariationModel`

## Possible Successors

`CompareVariationModel`,
`CompareExtVariationModel`

## See also

`ReadVariationModel`,
`WriteVariationModel`

## Module

Matching
