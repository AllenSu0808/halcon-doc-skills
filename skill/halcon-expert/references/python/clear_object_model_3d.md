# clear_object_model_3d (Operator)

## Name

`clear_object_model_3d` — Free the memory of a 3D object model.

## Signature

`def clear_object_model_3d(object_model_3d: MaybeSequence[HHandle]) -> None`

## Description

The operator `clear_object_model_3d` frees the memory of a 3D
object model that was previously created.
After calling `clear_object_model_3d`, the model can no longer
be used. The handle *`object_model_3d`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- object_model_3d

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`object_model_3d`** (input_control, state is modified)  object_model_3d(-array) `→` MaybeSequence[HHandle]

Handle of the 3D object model.

## Result

If the handle of the model is valid, the operator
`clear_object_model_3d` returns the value 2 (
H_MSG_TRUE)
. If necessary, an
exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`

## Module

3D Metrology
