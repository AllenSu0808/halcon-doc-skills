# deserialize_component_model (Operator)

## Name

`deserialize_component_model` — Deserialize a serialized component model.

## Warning

**`deserialize_component_model` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`deserialize_component_model( : : SerializedItemHandle : ComponentModelID)`

## Description

`deserialize_component_model` deserializes a component model,
that was serialized by [`serialize_component_model`](serialize_component_model.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized component
model is defined by the handle *`SerializedItemHandle`*.
The deserialized values are stored in an automatically created
component model with the handle *`SerializedItemHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`ComponentModelID`** (output_control)  component_model `→`  (handle)

Handle of the component model.

## Result

If the parameters are valid, the operator
`deserialize_component_model` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
