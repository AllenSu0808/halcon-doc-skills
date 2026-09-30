# traind_ocv_proj (Operator)

## Name

`traind_ocv_proj` — Training of an OCV tool.

## Signature

`traind_ocv_proj(Pattern : : OCVHandle, Name, Mode : )`

## Description

`traind_ocv_proj` trains patterns for an OCV tool that
has been created using the operators [`create_ocv_proj`](create_ocv_proj.md) or
[`read_ocv`](read_ocv.md).
For this training one or multiple patterns are provided to the system.
Such a pattern consists of an image with a reduced domain (ROI)
for the area of the pattern.
Note that the pattern should not only contain foreground
pixels (e.g., dark pixels of a character) but also
background pixels. This can be implemented e.g., by
the smallest surrounding rectangle of the pattern. Without
this context an evaluation of the pattern is not possible.

If more than one pattern has to be trained this can be achieved by
multiple calls (one for each pattern) or by calling `traind_ocv_proj`
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

**`Pattern`** (input_object)  singlechannelimage(-array) `→` object (byte)

Pattern to be trained.

**`OCVHandle`** (input_control, state is modified)  ocv `→`  (handle)

Handle of the OCV tool to be trained.

**`Name`** (input_control)  string(-array) `→`  (string)

Name(s) of the object(s) to analyze.

Default:
'a'

**`Mode`** (input_control)  string `→`  (string)

Mode for training (only one mode implemented).

Default:
'single'

List of values:
'single'

## Example (C++)

```
create_ocv_proj("A",&ocv_handle);
draw_region(&ROI,window_handle);
reduce_domain(Image,ROI,&Sample);
traind_ocv_proj(Sample,ocv_handle,"A","single");
```

## Result

`traind_ocv_proj` returns 2 (
H_MSG_TRUE)
, if
the handle and the training pattern(s) are correct.
Otherwise, an exception is raised.

## Possible Predecessors

`write_ocr_trainf`,
`create_ocv_proj`,
`read_ocv`,
`threshold`,
`connection`,
`select_shape`

## Possible Successors

`close_ocv`

## See also

`traind_ocr_class_box`

## Module

OCR/OCV
