# GetDeformableSurfaceMatchingResult (Operator)

## Name

`GetDeformableSurfaceMatchingResult` — Get details of a result from deformable surface based matching.

## Signature

`static void HOperatorSet.GetDeformableSurfaceMatchingResult(HTuple deformableSurfaceMatchingResult, HTuple resultName, HTuple resultIndex, out HTuple resultValue)`

`HTuple HDeformableSurfaceMatchingResult.GetDeformableSurfaceMatchingResult(HTuple resultName, HTuple resultIndex)`

`HTuple HDeformableSurfaceMatchingResult.GetDeformableSurfaceMatchingResult(string resultName, int resultIndex)`

## Description

The operator `GetDeformableSurfaceMatchingResult` returns details about
the results of deformable surface based matching or the
deformable surface refinement.
The results are
stored in *`deformableSurfaceMatchingResult`*, which must have been created
by [`FindDeformableSurfaceModel`](find_deformable_surface_model.md) or
[`RefineDeformableSurfaceModel`](refine_deformable_surface_model.md).

The parameter *`resultName`* is used to select which result detail
shall be returned. For some result details, *`resultIndex`*
selects the index of the result detail.
*`resultIndex`* is ignored for certain values of *`resultName`*.

The following values are possible for *`resultName`*:

- ***"sampled_scene"*:** —

  A 3D object model handle is returned that
  contains the sampled scene points that were used in the
  matching or refinement.
  This is helpful for tuning the sampling distance of the scene
  (see parameter RelSamplingDistance of operators
  [`FindDeformableSurfaceModel`](find_deformable_surface_model.md) and
  [`RefineDeformableSurfaceModel`](refine_deformable_surface_model.md)).
  The parameter *`resultIndex`* is ignored.
- ***"rigid_pose"*:** —

  If *`deformableSurfaceMatchingResult`* was created by
  [`FindDeformableSurfaceModel`](find_deformable_surface_model.md), a rigid pose is returned
  that approximates the deformable matching result.
  The parameter *`resultIndex`* is ignored.
  This parameter is not available if
  *`deformableSurfaceMatchingResult`* was
  created by [`RefineDeformableSurfaceModel`](refine_deformable_surface_model.md).
- ***"reference_point_x"*:** —
- ***"reference_point_y"*:** —
- ***"reference_point_z"*:** —

  Returns the x-, y- or z-coordinates of a transformed reference point.
  The reference point must have been added to the deformable surface model
  using the operator [`AddDeformableSurfaceModelReferencePoint`](add_deformable_surface_model_reference_point.md).
  The indices of the reference points to be returned are passed in
  *`resultIndex`*.
  If *"all"* is passed in *`resultIndex`*, the position
  of all reference points is returned.
- ***"deformed_model"*:** —

  Returns a deformed variant of the 3D object model that was originally
  passed to [`CreateDeformableSurfaceModel`](create_deformable_surface_model.md).
  The 3D object model is deformed with the reconstructed deformation.
  Triangles, polygons and extended attributes contained in the original
  3D object model are maintained.
  The parameter *`resultIndex`* is ignored.
- ***"deformed_sampled_model"*:** —

  Returns a deformed variant of the 3D object model that was sampled
  by [`CreateDeformableSurfaceModel`](create_deformable_surface_model.md).
  The returned 3D object model has the same number of points as the
  original, undeformed sampled model, and the points are in the same
  order.
  Details about the sampling are described in
  [`CreateDeformableSurfaceModel`](create_deformable_surface_model.md).
  The original, undeformed sampled model can be obtained with
  [`GetDeformableSurfaceModelParam`](get_deformable_surface_model_param.md).
  The parameter *`resultIndex`* is ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`deformableSurfaceMatchingResult`** (input_control)  deformable_surface_matching_result `→` [HDeformableSurfaceMatchingResult](HDeformableSurfaceMatchingResult.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deformable
surface matching result.

**`resultName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the result property.

Default:
"sampled_scene"

List of values:
"deformed_model", "deformed_sampled_model", "reference_point_x", "reference_point_y", "reference_point_z", "rigid_pose", "sampled_scene"

**`resultIndex`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Index of the result property.

Default:
0

Suggested values:
0, 1, 2, 3, "all"

Restriction:
`ResultIndex >= 0`

**`resultValue`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string / double / HHandle)

Value of the result property.

## Result

If the handle of the result is valid, the operator
`GetDeformableSurfaceMatchingResult` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`FindDeformableSurfaceModel`,
`RefineDeformableSurfaceModel`

## Possible Successors

`ClearDeformableSurfaceModel`

## See also

`FindDeformableSurfaceModel`,
`RefineDeformableSurfaceModel`,
`ReadDeformableSurfaceModel`,
`WriteDeformableSurfaceModel`,
`ClearDeformableSurfaceModel`

## Module

3D Metrology
