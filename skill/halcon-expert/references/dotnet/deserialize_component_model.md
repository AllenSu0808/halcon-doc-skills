# DeserializeComponentModel (Operator)

## Name

`DeserializeComponentModel` — Deserialize a serialized component model.

## Warning

**`DeserializeComponentModel` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.DeserializeComponentModel(HTuple serializedItemHandle, out HTuple componentModelID)`

`void HComponentModel.DeserializeComponentModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeComponentModel` deserializes a component model,
that was serialized by [`SerializeComponentModel`](serialize_component_model.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized component
model is defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
component model with the handle *`serializedItemHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`componentModelID`** (output_control)  component_model `→` [HComponentModel](HComponentModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the component model.

## Result

If the parameters are valid, the operator
`DeserializeComponentModel` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
