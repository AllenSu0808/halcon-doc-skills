# write_deep_matching_3d (Operator)

## Name

`write_deep_matching_3d` — Write a Deep 3D Matching model in a file.

## Signature

`write_deep_matching_3d( : : Deep3DMatchingModel, FileName : )`

## Description

`write_deep_matching_3d` writes the Deep 3D Matching model
*`Deep3DMatchingModel`* to the file given by *`FileName`*.
Please note that the runtime specific parameters *'device'* and
*'batch_size'* of the deep learning models are not written.

The default HALCON file extension for Deep 3D Matching models is
`'.dm3'`.

The Deep 3D Matching model can be read with [`read_deep_matching_3d`](read_deep_matching_3d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Deep3DMatchingModel`** (input_control)  deep_matching_3d `→`  (handle)

Handle of the Deep 3D Matching model.

**`FileName`** (input_control)  filename.write `→`  (string)

Filename

File extension:
.`dm3`

## Result

If the parameters are valid, the operator `write_deep_matching_3d`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_deep_matching_3d`,
`set_deep_matching_3d_param`

## Possible Successors

`clear_handle`

## Module

3D Metrology
