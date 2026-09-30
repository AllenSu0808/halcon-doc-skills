# SerializeComponentModel (Operator)

## Name

`SerializeComponentModel` — Serialize a component model.

## Warning

**`SerializeComponentModel` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.SerializeComponentModel(HTuple componentModelID, out HTuple serializedItemHandle)`

`HSerializedItem HComponentModel.SerializeComponentModel()`

## Description

`SerializeComponentModel` serializes the data of a component
model (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`WriteComponentModel`](write_component_model.md) is converted to a serialized
item. The component model is defined by the handle
*`componentModelID`*. The serialized component model is returned
by the handle *`serializedItemHandle`* and can be deserialized
by [`DeserializeComponentModel`](deserialize_component_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`componentModelID`** (input_control)  component_model `→` [HComponentModel](HComponentModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the component model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeComponentModel` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
