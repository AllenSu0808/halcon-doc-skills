# read_surface_model (Operator)

## Name

`read_surface_model` — Read a surface model from a file.

## Signature

`def read_surface_model(file_name: str) -> HHandle`

## Description

The operator `read_surface_model` reads the surface model, which has
been written with [`write_surface_model`](write_surface_model.md), from the file
*`file_name`*.
The handle of the surface model is returned in *`surface_model_id`*.
If no absolute path is given in *`file_name`*, the file is searched
in the current directory of the HALCON process.
The default HALCON file extension for the surface model (SFM) file is
'sfm'.
If no file named *`file_name`* exists, the default file extension is
appended to *`file_name`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

Name of the SFM file.

File extension:
.`sfm`

**`surface_model_id`** (output_control)  surface_model `→` HHandle

Handle of the read surface model.

## Result

`read_surface_model` returns 2 (
H_MSG_TRUE)
if all parameters are
correct and the file can be read.
If the file is not a surface model file, the error 9506 is raised.
If the file has a version that can not be read by this version of HALCON,
the error 9507 is raised.
If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`

## Possible Successors

`find_surface_model`,
`refine_surface_model_pose`,
`get_surface_model_param`,
`clear_surface_model`,
`find_surface_model_image`,
`refine_surface_model_pose_image`

## Alternatives

`create_surface_model`

## See also

`create_surface_model`,
`write_surface_model`

## Module

3D Metrology
