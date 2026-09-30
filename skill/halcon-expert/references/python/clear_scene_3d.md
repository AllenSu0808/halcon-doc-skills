# clear_scene_3d (Operator)

## Name

`clear_scene_3d` — Delete a 3D scene and free all allocated memory.

## Signature

`def clear_scene_3d(scene_3d: MaybeSequence[HHandle]) -> None`

## Description

`clear_scene_3d` deletes the 3D scene *`scene_3d`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- scene_3d

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`scene_3d`** (input_control, state is modified)  scene_3d(-array) `→` MaybeSequence[HHandle]

Handle of the 3D scene.

## Result

`clear_scene_3d` returns 2 (
H_MSG_TRUE)
if the scene was valid and could
be deleted. If necessary, an exception is raised.

## Possible Predecessors

`display_scene_3d`

## Module

3D Metrology
