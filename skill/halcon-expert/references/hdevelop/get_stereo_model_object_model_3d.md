# get_stereo_model_object_model_3d (Operator)

## Name

`get_stereo_model_object_model_3d` — Get intermediate 3D object model of a stereo reconstruction

## Signature

`get_stereo_model_object_model_3d( : : StereoModelID, GenParamName : ObjectModel3D)`

## Description

With the operator `get_stereo_model_object_model_3d` it is possible to
get a 3D object model *`ObjectModel3D`* that was reconstructed with
[`reconstruct_surface_stereo`](reconstruct_surface_stereo.md) as an intermediate result using the
method *'surface_fusion'*. The returned object model is
equal to the result of [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md) using
method *'surface_pairwise'*.

For this, a call to `get_stereo_model_object_model_3d` has to be
performed using the value *'m3d_pairwise'* for the parameter
*`GenParamName`*. It should be noted that the model can only be queried if
the *'persistence'* mode for the stereo model
(see [`set_stereo_model_param`](set_stereo_model_param.md)) is enabled *before*
performing the reconstruction. Furthermore the object model can only be
queried if the stereo model has been created using the
method *'surface_fusion'*. Otherwise, an error is returned.
If no object model has been created, the operator returns -1.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`StereoModelID`** (input_control)  stereo_model `→`  (handle)

Handle of the stereo model.

**`GenParamName`** (input_control)  string(-array) `→`  (string)

Names of the model parameters.

List of values:
'm3d_pairwise'

**`ObjectModel3D`** (output_control)  object_model_3d `→`  (handle)

Values of the model parameters.

## Possible Predecessors

`reconstruct_surface_stereo`,
`set_stereo_model_param`

## See also

`set_stereo_model_param`

## Module

3D Metrology
