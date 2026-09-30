# ClearObjectModel3d (Operator)

## Name

`ClearObjectModel3d` — Free the memory of a 3D object model.

## Signature

`static void HOperatorSet.ClearObjectModel3d(HTuple objectModel3D)`

`static void HObjectModel3D.ClearObjectModel3d(HObjectModel3D[] objectModel3D)`

`void HObjectModel3D.ClearObjectModel3d()`

## Description

The operator `ClearObjectModel3d` frees the memory of a 3D
object model that was previously created.
After calling `ClearObjectModel3d`, the model can no longer
be used. The handle *`objectModel3D`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- objectModel3D

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`objectModel3D`** (input_control, state is modified)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

## Result

If the handle of the model is valid, the operator
`ClearObjectModel3d` returns the value 2 (
H_MSG_TRUE)
. If necessary, an
exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`XyzToObjectModel3d`

## Module

3D Metrology
