# get_ncc_model_region (Operator)

## Name

`get_ncc_model_region` — Return the region used to create an NCC model.

## Signature

`def get_ncc_model_region(model_id: HHandle) -> HObject`

## Description

The operator `get_ncc_model_region` returns the
region used to create the NCC model *`model_id`* in
*`model_region`*. This region can be used, for example, to
visualize the found instances of the model in an image. It should
be noted that the position of *`model_region`* is normalized
such that the reference point of the model (see [`set_ncc_model_origin`](set_ncc_model_origin.md))
lies at the pixel position (0,0).
Hence, the region simply needs to be translated to the found
position in the image (and possibly rotated around this
point).
`get_ncc_model_region` ignores the value of the system
parameter *"clip_region"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`model_region`** (output_object)  region `→` HObject

Model region of the NCC model.

**`model_id`** (input_control)  ncc_model `→` HHandle

Handle of the model.

## Result

If the handle of the NCC model is valid, the operator
`get_ncc_model_region` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`create_ncc_model`

## Module

Matching
