# serialize_training_components (Operator)

## Name

`serialize_training_components` — Serialize a component training result.

## Warning

**`serialize_training_components` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`serialize_training_components( : : ComponentTrainingID : SerializedItemHandle)`

## Description

`serialize_training_components` serializes the data of a component
training result (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction
of the basic principle of serialization). The same data that is
written in a file by [`write_training_components`](write_training_components.md) is converted to
a serialized item. The component training result is defined by the
handle *`ComponentTrainingID`*. The serialized component training
result is returned by the handle *`SerializedItemHandle`* and
can be deserialized by [`deserialize_training_components`](deserialize_training_components.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ComponentTrainingID`** (input_control)  component_training `→`  (handle)

Handle of the training result.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_training_components` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
