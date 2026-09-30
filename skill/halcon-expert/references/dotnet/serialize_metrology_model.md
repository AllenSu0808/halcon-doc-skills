# SerializeMetrologyModel (Operator)

## Name

`SerializeMetrologyModel` — Serialize a metrology model.

## Signature

`static void HOperatorSet.SerializeMetrologyModel(HTuple metrologyHandle, out HTuple serializedItemHandle)`

`HSerializedItem HMetrologyModel.SerializeMetrologyModel()`

## Description

`SerializeMetrologyModel` serializes the data of a metrology
model (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization).

The same data that is written in a file by [`WriteMetrologyModel`](write_metrology_model.md) is
converted to a serialized item. The metrology model is defined by the handle
*`metrologyHandle`*. The serialized metrology model is returned by the
handle *`serializedItemHandle`* and can be deserialized by
[`DeserializeMetrologyModel`](deserialize_metrology_model.md).

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`metrologyHandle`** (input_control)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeMetrologyModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateMetrologyModel`,
`AddMetrologyObjectCircleMeasure`,
`AddMetrologyObjectEllipseMeasure`,
`AddMetrologyObjectLineMeasure`,
`AddMetrologyObjectRectangle2Measure`,
`SetMetrologyObjectParam`,
`SetMetrologyObjectFuzzyParam`,
`ReadMetrologyModel`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeMetrologyModel`

## Module

2D Metrology
