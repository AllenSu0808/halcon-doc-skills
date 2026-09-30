# read_distance_transform_xld (Operator)

## Name

`read_distance_transform_xld` — Read an XLD distance transform from a file.

## Signature

`def read_distance_transform_xld(file_name: str) -> HHandle`

## Description

`read_distance_transform_xld` reads an XLD distance transform
which previously has been stored with
[`write_distance_transform_xld`](write_distance_transform_xld.md) from the file given by
*`file_name`* and returns the handle *`distance_transform_id`*.
The default HALCON extension for the XLD distance
transform is 'hdtc'.

[`get_distance_transform_xld_contour`](get_distance_transform_xld_contour.md)
can be used to get the reference contour that was used
to build the XLD distance transform *`distance_transform_id`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.write `→` str

Name of the file.

File extension:
.`hdtc`

**`distance_transform_id`** (output_control)  xld_dist_trans `→` HHandle

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
