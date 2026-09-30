# serialize_component_model (Operator)

## Name

`serialize_component_model` — Serialize a component model.

## Warning

**`serialize_component_model` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`def serialize_component_model(component_model_id: HHandle) -> HHandle`

## Description

`serialize_component_model` serializes the data of a component
model (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`write_component_model`](write_component_model.md) is converted to a serialized
item. The component model is defined by the handle
*`component_model_id`*. The serialized component model is returned
by the handle *`serialized_item_handle`* and can be deserialized
by [`deserialize_component_model`](deserialize_component_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`component_model_id`** (input_control)  component_model `→` HHandle

Handle of the component model.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_component_model` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
