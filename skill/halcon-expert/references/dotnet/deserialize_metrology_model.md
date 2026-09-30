# DeserializeMetrologyModel (Operator)

## Name

`DeserializeMetrologyModel` — Deserialize a serialized metrology model.

## Signature

`static void HOperatorSet.DeserializeMetrologyModel(HTuple serializedItemHandle, out HTuple metrologyHandle)`

`void HMetrologyModel.DeserializeMetrologyModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeMetrologyModel` deserializes a metrology model,
that was serialized by [`SerializeMetrologyModel`](serialize_metrology_model.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized metrology
model is defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
metrology model with the handle *`metrologyHandle`*. Access
to the parameters of the metrology model is possible, e.g., with
the operators [`GetMetrologyObjectParam`](get_metrology_object_param.md) or
[`GetMetrologyObjectFuzzyParam`](get_metrology_object_fuzzy_param.md).

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`metrologyHandle`** (output_control)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

## Result

If the parameters are valid, the operator
`DeserializeMetrologyModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeMetrologyModel`

## Possible Successors

`GetMetrologyObjectParam`,
`GetMetrologyObjectFuzzyParam`,
`ApplyMetrologyModel`

## Module

2D Metrology
