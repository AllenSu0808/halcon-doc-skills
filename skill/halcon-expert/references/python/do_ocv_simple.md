# do_ocv_simple (Operator)

## Name

`do_ocv_simple` — Verification of a pattern using an OCV tool.

## Signature

`def do_ocv_simple(pattern: HObject, ocvhandle: HHandle, pattern_name: MaybeSequence[str], adapt_pos: str, adapt_size: str, adapt_angle: str, adapt_gray: str, threshold: float) -> Sequence[float]`

`def do_ocv_simple_s(pattern: HObject, ocvhandle: HHandle, pattern_name: MaybeSequence[str], adapt_pos: str, adapt_size: str, adapt_angle: str, adapt_gray: str, threshold: float) -> float`

## Description

`do_ocv_simple` evaluates the pattern in (*`pattern`*).
Before the evaluation the good-pattern has to be trained by using
the operator [`traind_ocv_proj`](traind_ocv_proj.md). Both patterns should
have roughly the same (relative) extent and shape.
To specify which of the trained patterns is used as reference its
name is specified in *`pattern_name`*.
The next four parameters influence the automatic adaption:
*`adapt_pos`* and *`adapt_size`* refer to the geometry
of the pattern. *`adapt_pos`* specifies whether a shift of the
position will be adapted automatically. *`adapt_size`*
is used to adapt to changes in the size of the pattern.
*`adapt_angle`* is not implemented.
The parameter *`adapt_gray`* controls the adaption to changes of
the gray values. This comprises additive and multiplicative changes
of the intensity.

The parameter *`threshold`* specifies the minimum difference of the
gray values to be treated as an error. In this case the
percentage of wrong pixels is returned. If the value is below 0
the sum of all errors normalized with respect to the size is returned.

The result of the operator is the *`quality`* of the pattern
with a value between 0 and 1. The value 1 corresponds to a pattern
with no faults. The value 0 corresponds to a very big fault.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pattern`** (input_object)  singlechannelimage(-array) `→` HObject (byte)

Characters to be verified.

**`ocvhandle`** (input_control)  ocv `→` HHandle

Handle of the OCV tool.

**`pattern_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Name of the character.

Default:
"a"

**`adapt_pos`** (input_control)  string `→` str

Adaption to vertical and horizontal translation.

Default:
"true"

List of values:
"false", "true"

**`adapt_size`** (input_control)  string `→` str

Adaption to vertical and horizontal scaling of
the size.

Default:
"true"

List of values:
"false", "true"

**`adapt_angle`** (input_control)  string `→` str

Adaption to changes of the orientation
(not implemented).

Default:
"false"

List of values:
"false"

**`adapt_gray`** (input_control)  string `→` str

Adaption to additive and scaling gray value changes.

Default:
"true"

List of values:
"false", "true"

**`threshold`** (input_control)  number `→` float

Minimum difference between objects.

Default:
10

Suggested values:
-1.0, 0.0, 1.0, 5.0, 10.0, 15.0, 20.0, 30.0, 40.0, 50.0, 60.0, 80.0, 100.0, 150.0

**`quality`** (output_control)  real(-array) `→` Sequence[float]

Evaluation of the character.

Value range:
`0.0
≤
quality
≤
1.0`

## Result

`do_ocv_simple` returns 2 (
H_MSG_TRUE)
, if
the handle and the characters are correct.
Otherwise, an exception is raised.

## Possible Predecessors

`traind_ocr_class_box`,
`trainf_ocr_class_box`,
`read_ocv`,
`threshold`,
`connection`,
`select_shape`

## Possible Successors

`close_ocv`

## See also

`create_ocv_proj`

## Module

OCR/OCV
