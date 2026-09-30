# ClearScene3d (Operator)

## Name

`ClearScene3d` — Delete a 3D scene and free all allocated memory.

## Signature

`static void HOperatorSet.ClearScene3d(HTuple scene3D)`

`static void HScene3D.ClearScene3d(HScene3D[] scene3D)`

`void HScene3D.ClearScene3d()`

## Description

`ClearScene3d` deletes the 3D scene *`scene3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- scene3D

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`scene3D`** (input_control, state is modified)  scene_3d(-array) `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

## Result

`ClearScene3d` returns 2 (
H_MSG_TRUE)
if the scene was valid and could
be deleted. If necessary, an exception is raised.

## Possible Predecessors

`DisplayScene3d`

## Module

3D Metrology
