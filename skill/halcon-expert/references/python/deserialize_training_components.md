# deserialize_training_components (Operator)

## Name

`deserialize_training_components` — Deserialize a component training result.

## Warning

**`deserialize_training_components` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`def deserialize_training_components(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_training_components` deserializes a component
training result, that was serialized by
[`serialize_training_components`](serialize_training_components.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized component
training result is defined by the handle *`serialized_item_handle`*.
The deserialized values are stored in an automatically created
component training result with the handle *`component_training_id`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`component_training_id`** (output_control)  component_training `→` HHandle

Handle of the training result.

## Result

If the parameters are valid, the operator
`deserialize_training_components` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
