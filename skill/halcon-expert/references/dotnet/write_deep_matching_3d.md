# WriteDeepMatching3d (Operator)

## Name

`WriteDeepMatching3d` — Write a Deep 3D Matching model in a file.

## Signature

`static void HOperatorSet.WriteDeepMatching3d(HTuple deep3DMatchingModel, HTuple fileName)`

`void HDeepMatching3D.WriteDeepMatching3d(string fileName)`

## Description

`WriteDeepMatching3d` writes the Deep 3D Matching model
*`deep3DMatchingModel`* to the file given by *`fileName`*.
Please note that the runtime specific parameters *"device"* and
*"batch_size"* of the deep learning models are not written.

The default HALCON file extension for Deep 3D Matching models is
`'.dm3'`.

The Deep 3D Matching model can be read with [`ReadDeepMatching3d`](read_deep_matching_3d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deep3DMatchingModel`** (input_control)  deep_matching_3d `→` [HDeepMatching3D](HDeepMatching3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the Deep 3D Matching model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Filename

File extension:
.`dm3`

## Result

If the parameters are valid, the operator `WriteDeepMatching3d`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateDeepMatching3d`,
`SetDeepMatching3dParam`

## Possible Successors

`ClearHandle`

## Module

3D Metrology
