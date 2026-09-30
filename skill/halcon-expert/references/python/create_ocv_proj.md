# create_ocv_proj (Operator)

## Name

`create_ocv_proj` — Create a new OCV tool based on gray value projections.

## Signature

`def create_ocv_proj(pattern_names: MaybeSequence[str]) -> HHandle`

## Description

`create_ocv_proj` creates a new OCV tool. This tool will
be used to train good-patterns for the optical character verification.
The training is done using the operator [`traind_ocv_proj`](traind_ocv_proj.md).
Thus [`traind_ocv_proj`](traind_ocv_proj.md) is normally called after
`create_ocv_proj`.

The pattern comparison is based on the gray projections:
For every training pattern the horizontal and vertical gray
projections are calculated by summing up the gray values along
the rows and columns inside the region of the pattern.
This operation is applied to the training patterns and the
test patterns. For the training patterns the result
is stored inside the OCV tool to save runtime while comparing patterns.
The OCV is done by comparing the corresponding projections.
The Quality is the similarity of the projections.

Input for `create_ocv_proj` are the names of the patterns
(*`pattern_names`*) which have to be trained.
The number and the names can be chosen arbitrary. In most case only
one pattern will be trained, thus only one name has to be
specified. The names will be used when doing the OCV
([`do_ocv_simple`](do_ocv_simple.md)). It is possible to specify more names than
actually used. These might be trained later.

To close the OCV tool, i.e. to free the memory,
the operator [`close_ocv`](close_ocv.md) is called.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`pattern_names`** (input_control)  string(-array) `→` MaybeSequence[str]

List of names for patterns to be trained.

Default:
"a"

**`ocvhandle`** (output_control)  ocv `→` HHandle

Handle of the created OCV tool.

## Example (C++)

```
create_ocv_proj("A",&ocv_handle);
draw_region(&ROI,window_handle);
reduce_domain(Image,ROI,&Sample);
traind_ocv_proj(Sample,ocv_handle,"A","single");
```

## Result

`create_ocv_proj` returns 2 (
H_MSG_TRUE)
, if
the parameters are correct.
Otherwise, an exception is raised.

## Possible Successors

`traind_ocv_proj`,
`write_ocv`,
`close_ocv`

## Alternatives

`read_ocv`

## See also

`create_ocr_class_box`

## Module

OCR/OCV
