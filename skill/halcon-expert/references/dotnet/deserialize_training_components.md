# DeserializeTrainingComponents (Operator)

## Name

`DeserializeTrainingComponents` — Deserialize a component training result.

## Warning

**`DeserializeTrainingComponents` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.DeserializeTrainingComponents(HTuple serializedItemHandle, out HTuple componentTrainingID)`

`void HComponentTraining.DeserializeTrainingComponents(HSerializedItem serializedItemHandle)`

## Description

`DeserializeTrainingComponents` deserializes a component
training result, that was serialized by
[`SerializeTrainingComponents`](serialize_training_components.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized component
training result is defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
component training result with the handle *`componentTrainingID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`componentTrainingID`** (output_control)  component_training `→` [HComponentTraining](HComponentTraining.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training result.

## Result

If the parameters are valid, the operator
`DeserializeTrainingComponents` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
