# TraindOcvProj (Operator)

## Name

`TraindOcvProj` — Training of an OCV tool.

## Signature

`static void HOperatorSet.TraindOcvProj(HObject pattern, HTuple OCVHandle, HTuple name, HTuple mode)`

`void HImage.TraindOcvProj(HOCV OCVHandle, HTuple name, string mode)`

`void HImage.TraindOcvProj(HOCV OCVHandle, string name, string mode)`

`void HOCV.TraindOcvProj(HImage pattern, HTuple name, string mode)`

`void HOCV.TraindOcvProj(HImage pattern, string name, string mode)`

## Description

`TraindOcvProj` trains patterns for an OCV tool that
has been created using the operators [`CreateOcvProj`](create_ocv_proj.md) or
[`ReadOcv`](read_ocv.md).
For this training one or multiple patterns are provided to the system.
Such a pattern consists of an image with a reduced domain (ROI)
for the area of the pattern.
Note that the pattern should not only contain foreground
pixels (e.g., dark pixels of a character) but also
background pixels. This can be implemented e.g., by
the smallest surrounding rectangle of the pattern. Without
this context an evaluation of the pattern is not possible.

If more than one pattern has to be trained this can be achieved by
multiple calls (one for each pattern) or by calling `TraindOcvProj`
once with all patterns and a tuple of the corresponding names.
The result will be in both cases the same. However using multiple
calls will normally result in a longer execution time than using one
call with all patterns.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- OCVHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`pattern`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Pattern to be trained.

**`OCVHandle`** (input_control, state is modified)  ocv `→` [HOCV](HOCV.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCV tool to be trained.

**`name`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Name(s) of the object(s) to analyze.

Default:
"a"

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode for training (only one mode implemented).

Default:
"single"

List of values:
"single"

## Example (C++)

```
create_ocv_proj("A",&ocv_handle);
draw_region(&ROI,window_handle);
reduce_domain(Image,ROI,&Sample);
traind_ocv_proj(Sample,ocv_handle,"A","single");
```

## Result

`TraindOcvProj` returns 2 (
H_MSG_TRUE)
, if
the handle and the training pattern(s) are correct.
Otherwise, an exception is raised.

## Possible Predecessors

`WriteOcrTrainf`,
`CreateOcvProj`,
`ReadOcv`,
`Threshold`,
`Connection`,
`SelectShape`

## Possible Successors

`CloseOcv`

## See also

`TraindOcrClassBox`

## Module

OCR/OCV
