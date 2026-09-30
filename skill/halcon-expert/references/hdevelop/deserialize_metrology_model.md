# deserialize_metrology_model (Operator)

## Name

`deserialize_metrology_model` — Deserialize a serialized metrology model.

## Signature

`deserialize_metrology_model( : : SerializedItemHandle : MetrologyHandle)`

## Description

`deserialize_metrology_model` deserializes a metrology model,
that was serialized by [`serialize_metrology_model`](serialize_metrology_model.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized metrology
model is defined by the handle *`SerializedItemHandle`*.
The deserialized values are stored in an automatically created
metrology model with the handle *`MetrologyHandle`*. Access
to the parameters of the metrology model is possible, e.g., with
the operators [`get_metrology_object_param`](get_metrology_object_param.md) or
[`get_metrology_object_fuzzy_param`](get_metrology_object_fuzzy_param.md).

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`MetrologyHandle`** (output_control)  metrology_model `→`  (handle)

Handle of the metrology model.

## Result

If the parameters are valid, the operator
`deserialize_metrology_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_metrology_model`

## Possible Successors

`get_metrology_object_param`,
`get_metrology_object_fuzzy_param`,
`apply_metrology_model`

## Module

2D Metrology
