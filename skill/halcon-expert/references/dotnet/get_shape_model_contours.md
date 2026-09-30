# GetShapeModelContours (Operator)

## Name

`GetShapeModelContours` — Return the contour representation of a shape model.

## Signature

`static void HOperatorSet.GetShapeModelContours(out HObject modelContours, HTuple modelID, HTuple level)`

`HXLDCont HShapeModel.GetShapeModelContours(int level)`

## Description

The operator `GetShapeModelContours` returns a
representation of the shape model *`modelID`* as XLD contours
in *`modelContours`*. The parameter *`level`* determines
for which pyramid level of the model the contour representation
should be returned. The contours can be used, for example, to
visualize the found instances of the model in an image. It should
be noted that the position of *`modelContours`* is normalized
such that the reference point of the model (see
[`SetShapeModelOrigin`](set_shape_model_origin.md)) lies at the pixel position (0,0).
Hence, the contours simply need to be translated to the found
position in the image (and possibly rotated and scaled around this
point).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelContours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Contour representation of the shape model.

**`modelID`** (input_control)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`level`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Pyramid level for which the contour representation
should be returned.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Restriction:
`Level >= 1`

## Result

If the handle of the model is valid, the operator
`GetShapeModelContours` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`CreateShapeModel`,
`CreateScaledShapeModel`,
`CreateAnisoShapeModel`,
`ReadShapeModel`

## Alternatives

`GetGenericShapeModelObject`

## See also

`FindShapeModel`,
`FindScaledShapeModel`,
`FindAnisoShapeModel`,
`FindShapeModels`,
`FindScaledShapeModels`,
`FindAnisoShapeModels`

## Module

Matching
