# TrainfOcrClassMlpProtected (Operator)

## Name

`TrainfOcrClassMlpProtected` — Train an OCR classifier with data from a (protected) training file.

## Signature

`static void HOperatorSet.TrainfOcrClassMlpProtected(HTuple OCRHandle, HTuple trainingFile, HTuple password, HTuple maxIterations, HTuple weightTolerance, HTuple errorTolerance, out HTuple error, out HTuple errorLog)`

`double HOCRMlp.TrainfOcrClassMlpProtected(HTuple trainingFile, HTuple password, int maxIterations, double weightTolerance, double errorTolerance, out HTuple errorLog)`

`double HOCRMlp.TrainfOcrClassMlpProtected(string trainingFile, string password, int maxIterations, double weightTolerance, double errorTolerance, out HTuple errorLog)`

## Description

`TrainfOcrClassMlpProtected` trains the OCR classifier
*`OCRHandle`* with the training data stored in the OCR
training files given by *`trainingFile`*. Its functionality
corresponds to the functionality of [`TrainfOcrClassMlp`](trainf_ocr_class_mlp.md),
with the addition that `TrainfOcrClassMlpProtected`
can process unprotected and protected training files. Protected
training files can be used only with the correct user password
*`password`*. If the number of passwords *`password`*
equals 1, then every input file *`trainingFile`* is checked
with that password, otherwise the number of passwords has to be
equal to the number of input files and the input file at position
n is checked with the password at position n. For unprotected
training files the passwords are ignored.

For a more detailed description of the operator's functionality see
[`TrainfOcrClassMlp`](trainf_ocr_class_mlp.md). The concept of protecting OCR training
data in HALCON is described in [`ProtectOcrTrainf`](protect_ocr_trainf.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator modifies the state of the following input parameter:

- OCRHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`OCRHandle`** (input_control, state is modified)  ocr_mlp `→` [HOCRMlp](HOCRMlp.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`trainingFile`** (input_control)  filename.read(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the training files.

Default:
"ocr.trf"

File extension:
.`trf`, .`otr`

**`password`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Passwords for protected training files.

**`maxIterations`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of iterations of the
optimization algorithm.

Default:
200

Suggested values:
20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300

**`weightTolerance`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Threshold for the difference of the weights of
the MLP between two iterations of the
optimization algorithm.

Default:
1.0

Suggested values:
1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001

Restriction:
`WeightTolerance >= 1.0e-8`

**`errorTolerance`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Threshold for the difference of the mean error
of the MLP on the training data between two
iterations of the optimization algorithm.

Default:
0.01

Suggested values:
1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001

Restriction:
`ErrorTolerance >= 1.0e-8`

**`error`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Mean error of the MLP on the training data.

**`errorLog`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Mean error of the MLP on the training data as a
function of the number of iterations of the
optimization algorithm.

## Result

If the parameters are valid, the operator
`TrainfOcrClassMlpProtected` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

`TrainfOcrClassMlpProtected` may return the error 9211 (Matrix is
not positive definite) if `preprocessing` =
*"canonical_variates"* is used. This typically indicates
that not enough training samples have been stored for each class.
In this case we recommend to change `preprocessing` to
*"normalization"*. Another solution can be to add more
training samples.

## Possible Predecessors

`CreateOcrClassMlp`,
`WriteOcrTrainf`,
`AppendOcrTrainf`,
`WriteOcrTrainfImage`,
`ProtectOcrTrainf`

## Possible Successors

`DoOcrSingleClassMlp`,
`DoOcrMultiClassMlp`,
`WriteOcrClassMlp`

## Alternatives

`ReadOcrClassMlp`

## See also

`TrainfOcrClassMlp`,
`TrainClassMlp`

## Module

OCR/OCV
