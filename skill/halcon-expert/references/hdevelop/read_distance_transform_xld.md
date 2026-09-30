# read_distance_transform_xld (Operator)

## Name

`read_distance_transform_xld` — Read an XLD distance transform from a file.

## Signature

`read_distance_transform_xld( : : FileName : DistanceTransformID)`

## Description

`read_distance_transform_xld` reads an XLD distance transform
which previously has been stored with
[`write_distance_transform_xld`](write_distance_transform_xld.md) from the file given by
*`FileName`* and returns the handle *`DistanceTransformID`*.
The default HALCON extension for the XLD distance
transform is 'hdtc'.

[`get_distance_transform_xld_contour`](get_distance_transform_xld_contour.md)
can be used to get the reference contour that was used
to build the XLD distance transform *`DistanceTransformID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.write `→`  (string)

Name of the file.

File extension:
.`hdtc`

**`DistanceTransformID`** (output_control)  xld_dist_trans `→`  (handle)

Handle of the XLD distance transform.

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Successors

`apply_distance_transform_xld`,
`get_distance_transform_xld_contour`,
`get_distance_transform_xld_param`

## See also

`write_distance_transform_xld`,
`serialize_distance_transform_xld`,
`deserialize_distance_transform_xld`,
`create_distance_transform_xld`,
`set_distance_transform_xld_param`,
`clear_distance_transform_xld`

## Module

Foundation
