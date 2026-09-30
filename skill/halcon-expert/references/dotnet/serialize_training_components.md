# SerializeTrainingComponents (Operator)

## Name

`SerializeTrainingComponents` — Serialize a component training result.

## Warning

**`SerializeTrainingComponents` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.SerializeTrainingComponents(HTuple componentTrainingID, out HTuple serializedItemHandle)`

`HSerializedItem HComponentTraining.SerializeTrainingComponents()`

## Description

`SerializeTrainingComponents` serializes the data of a component
training result (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction
of the basic principle of serialization). The same data that is
written in a file by [`WriteTrainingComponents`](write_training_components.md) is converted to
a serialized item. The component training result is defined by the
handle *`componentTrainingID`*. The serialized component training
result is returned by the handle *`serializedItemHandle`* and
can be deserialized by [`DeserializeTrainingComponents`](deserialize_training_components.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`componentTrainingID`** (input_control)  component_training `→` [HComponentTraining](HComponentTraining.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training result.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeTrainingComponents` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
