# DoOcvSimple (Operator)

## Name

`DoOcvSimple` — Verification of a pattern using an OCV tool.

## Signature

`static void HOperatorSet.DoOcvSimple(HObject pattern, HTuple OCVHandle, HTuple patternName, HTuple adaptPos, HTuple adaptSize, HTuple adaptAngle, HTuple adaptGray, HTuple threshold, out HTuple quality)`

`HTuple HImage.DoOcvSimple(HOCV OCVHandle, HTuple patternName, string adaptPos, string adaptSize, string adaptAngle, string adaptGray, double threshold)`

`double HImage.DoOcvSimple(HOCV OCVHandle, string patternName, string adaptPos, string adaptSize, string adaptAngle, string adaptGray, double threshold)`

`HTuple HOCV.DoOcvSimple(HImage pattern, HTuple patternName, string adaptPos, string adaptSize, string adaptAngle, string adaptGray, double threshold)`

`double HOCV.DoOcvSimple(HImage pattern, string patternName, string adaptPos, string adaptSize, string adaptAngle, string adaptGray, double threshold)`

## Description

`DoOcvSimple` evaluates the pattern in (*`pattern`*).
Before the evaluation the good-pattern has to be trained by using
the operator [`TraindOcvProj`](traind_ocv_proj.md). Both patterns should
have roughly the same (relative) extent and shape.
To specify which of the trained patterns is used as reference its
name is specified in *`patternName`*.
The next four parameters influence the automatic adaption:
*`adaptPos`* and *`adaptSize`* refer to the geometry
of the pattern. *`adaptPos`* specifies whether a shift of the
position will be adapted automatically. *`adaptSize`*
is used to adapt to changes in the size of the pattern.
*`adaptAngle`* is not implemented.
The parameter *`adaptGray`* controls the adaption to changes of
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

**`pattern`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Characters to be verified.

**`OCVHandle`** (input_control)  ocv `→` [HOCV](HOCV.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCV tool.

**`patternName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the character.

Default:
"a"

**`adaptPos`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Adaption to vertical and horizontal translation.

Default:
"true"

List of values:
"false", "true"

**`adaptSize`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Adaption to vertical and horizontal scaling of
the size.

Default:
"true"

List of values:
"false", "true"

**`adaptAngle`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Adaption to changes of the orientation
(not implemented).

Default:
"false"

List of values:
"false"

**`adaptGray`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Adaption to additive and scaling gray value changes.

Default:
"true"

List of values:
"false", "true"

**`threshold`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Minimum difference between objects.

Default:
10

Suggested values:
-1.0, 0.0, 1.0, 5.0, 10.0, 15.0, 20.0, 30.0, 40.0, 50.0, 60.0, 80.0, 100.0, 150.0

**`quality`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Evaluation of the character.

Value range:
`0.0
≤
quality
≤
1.0`

## Result

`DoOcvSimple` returns 2 (
H_MSG_TRUE)
, if
the handle and the characters are correct.
Otherwise, an exception is raised.

## Possible Predecessors

`TraindOcrClassBox`,
`TrainfOcrClassBox`,
`ReadOcv`,
`Threshold`,
`Connection`,
`SelectShape`

## Possible Successors

`CloseOcv`

## See also

`CreateOcvProj`

## Module

OCR/OCV
