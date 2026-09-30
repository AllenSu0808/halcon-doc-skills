# SetMetrologyModelImageSize (Operator)

## Name

`SetMetrologyModelImageSize` — Set the size of the image of metrology objects.

## Signature

`static void HOperatorSet.SetMetrologyModelImageSize(HTuple metrologyHandle, HTuple width, HTuple height)`

`void HMetrologyModel.SetMetrologyModelImageSize(int width, int height)`

## Description

`SetMetrologyModelImageSize` is used to set or change the
size of the image in which the edge detection that is related to a
metrology model will be performed.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`metrologyHandle`*. The
image width must be specified by the parameter *`width`*. The image
height must specified by the parameter *`height`*.

## Attention

Note that the operator `SetMetrologyModelImageSize` should
be called before adding metrology objects to the metrology model
using the operators [`AddMetrologyObjectGeneric`](add_metrology_object_generic.md),
[`AddMetrologyObjectCircleMeasure`](add_metrology_object_circle_measure.md),
[`AddMetrologyObjectEllipseMeasure`](add_metrology_object_ellipse_measure.md),
[`AddMetrologyObjectLineMeasure`](add_metrology_object_line_measure.md),
or [`AddMetrologyObjectRectangle2Measure`](add_metrology_object_rectangle2_measure.md). Otherwise, all
measure regions of existing metrology objects will be
recomputed automatically upon calling `SetMetrologyModelImageSize`
or [`ApplyMetrologyModel`](apply_metrology_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- metrologyHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`metrologyHandle`** (input_control, state is modified)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the image to be processed.

Default:
640

Suggested values:
128, 192, 256, 512, 640, 768, 1024, 1280, 2048

Value range:
`0
≤
width` (lin)

Minimum increment:
1

Recommended increment:
16

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the image to be processed.

Default:
480

Suggested values:
128, 192, 256, 512, 640, 768, 1024, 1280, 2048

Value range:
`0
≤
height` (lin)

Minimum increment:
1

Recommended increment:
16

## Result

If the parameters are valid, the operator
`SetMetrologyModelImageSize` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`CreateMetrologyModel`

## Possible Successors

`SetMetrologyModelParam`,
`AddMetrologyObjectCircleMeasure`,
`AddMetrologyObjectEllipseMeasure`,
`AddMetrologyObjectLineMeasure`,
`AddMetrologyObjectRectangle2Measure`,
`AddMetrologyObjectGeneric`

## Module

2D Metrology
