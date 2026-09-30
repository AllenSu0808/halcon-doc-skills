# read_deep_matching_3d (Operator)

## Name

`read_deep_matching_3d` — Read a Deep 3D Matching model from a file.

## Signature

`def read_deep_matching_3d(file_name: str) -> HHandle`

## Description

The operator `read_deep_matching_3d` reads a Deep 3D Matching model.
Such models have to be in the HALCON format.
As a result, the handle *`deep_3dmatching_model`* is returned.

The model is loaded from the file *`file_name`*.
The default HALCON file extension for Deep 3D Matching models is
`'.dm3'`.

Please note that the values of runtime specific parameters are not written
to file, see [`write_deep_matching_3d`](write_deep_matching_3d.md).
As a consequence when reading a model these parameters are initialized with
their default value, see [`get_deep_matching_3d_param`](get_deep_matching_3d_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

Filename

File extension:
.`dm3`

**`deep_3dmatching_model`** (output_control)  deep_matching_3d `→` HHandle

Handle of the Deep 3D Matching model.

## Result

If the parameters are valid, the operator `read_deep_matching_3d`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_deep_matching_3d`

## Possible Successors

`set_deep_matching_3d_param`,
`get_deep_matching_3d_param`,
`apply_deep_matching_3d`

## Alternatives

`create_deep_matching_3d`

## Module

3D Metrology
