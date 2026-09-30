# do_ocv_simple (Operator)

## Name

`do_ocv_simple` — Verification of a pattern using an OCV tool.

## Signature

`do_ocv_simple(Pattern : : OCVHandle, PatternName, AdaptPos, AdaptSize, AdaptAngle, AdaptGray, Threshold : Quality)`

## Description

`do_ocv_simple` evaluates the pattern in (*`Pattern`*).
Before the evaluation the good-pattern has to be trained by using
the operator [`traind_ocv_proj`](traind_ocv_proj.md). Both patterns should
have roughly the same (relative) extent and shape.
To specify which of the trained patterns is used as reference its
name is specified in *`PatternName`*.
The next four parameters influence the automatic adaption:
*`AdaptPos`* and *`AdaptSize`* refer to the geometry
of the pattern. *`AdaptPos`* specifies whether a shift of the
position will be adapted automatically. *`AdaptSize`*
is used to adapt to changes in the size of the pattern.
*`AdaptAngle`* is not implemented.
The parameter *`AdaptGray`* controls the adaption to changes of
the gray values. This comprises additive and multiplicative changes
of the intensity.

The parameter *`Threshold`* specifies the minimum difference of the
gray values to be treated as an error. In this case the
percentage of wrong pixels is returned. If the value is below 0
the sum of all errors normalized with respect to the size is returned.

The result of the operator is the *`Quality`* of the pattern
with a value between 0 and 1. The value 1 corresponds to a pattern
with no faults. The value 0 corresponds to a very big fault.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Pattern`** (input_object)  singlechannelimage(-array) `→` object (byte)

Characters to be verified.

**`OCVHandle`** (input_control)  ocv `→`  (handle)

Handle of the OCV tool.

**`PatternName`** (input_control)  string(-array) `→`  (string)

Name of the character.

Default:
'a'

**`AdaptPos`** (input_control)  string `→`  (string)

Adaption to vertical and horizontal translation.

Default:
'true'

List of values:
'false', 'true'

**`AdaptSize`** (input_control)  string `→`  (string)

Adaption to vertical and horizontal scaling of
the size.

Default:
'true'

List of values:
'false', 'true'

**`AdaptAngle`** (input_control)  string `→`  (string)

Adaption to changes of the orientation
(not implemented).

Default:
'false'

List of values:
'false'

**`AdaptGray`** (input_control)  string `→`  (string)

Adaption to additive and scaling gray value changes.

Default:
'true'

List of values:
'false', 'true'

**`Threshold`** (input_control)  number `→`  (real)

Minimum difference between objects.

Default:
10

Suggested values:
-1.0, 0.0, 1.0, 5.0, 10.0, 15.0, 20.0, 30.0, 40.0, 50.0, 60.0, 80.0, 100.0, 150.0

**`Quality`** (output_control)  real(-array) `→`  (real)

Evaluation of the character.

Value range:
`0.0
≤
Quality
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
