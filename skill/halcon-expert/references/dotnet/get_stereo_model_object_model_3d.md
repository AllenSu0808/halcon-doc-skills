# GetStereoModelObjectModel3d (Operator)

## Name

`GetStereoModelObjectModel3d` — Get intermediate 3D object model of a stereo reconstruction

## Signature

`static void HOperatorSet.GetStereoModelObjectModel3d(HTuple stereoModelID, HTuple genParamName, out HTuple objectModel3D)`

`HObjectModel3D HStereoModel.GetStereoModelObjectModel3d(HTuple genParamName)`

`HObjectModel3D HStereoModel.GetStereoModelObjectModel3d(string genParamName)`

## Description

With the operator `GetStereoModelObjectModel3d` it is possible to
get a 3D object model *`objectModel3D`* that was reconstructed with
[`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md) as an intermediate result using the
method *"surface_fusion"*. The returned object model is
equal to the result of [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md) using
method *"surface_pairwise"*.

For this, a call to `GetStereoModelObjectModel3d` has to be
performed using the value *"m3d_pairwise"* for the parameter
*`genParamName`*. It should be noted that the model can only be queried if
the *"persistence"* mode for the stereo model
(see [`SetStereoModelParam`](set_stereo_model_param.md)) is enabled *before*
performing the reconstruction. Furthermore the object model can only be
queried if the stereo model has been created using the
method *"surface_fusion"*. Otherwise, an error is returned.
If no object model has been created, the operator returns -1.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`stereoModelID`** (input_control)  stereo_model `→` [HStereoModel](HStereoModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the stereo model.

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the model parameters.

List of values:
"m3d_pairwise"

**`objectModel3D`** (output_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Values of the model parameters.

## Possible Predecessors

`ReconstructSurfaceStereo`,
`SetStereoModelParam`

## See also

`SetStereoModelParam`

## Module

3D Metrology
