# trainf_ocr_class_mlp_protected (Operator)

## Name

`trainf_ocr_class_mlp_protected` — Train an OCR classifier with data from a (protected) training file.

## Signature

`def trainf_ocr_class_mlp_protected(ocrhandle: HHandle, training_file: MaybeSequence[str], password: MaybeSequence[str], max_iterations: int, weight_tolerance: float, error_tolerance: float) -> Tuple[float, Sequence[float]]`

## Description

`trainf_ocr_class_mlp_protected` trains the OCR classifier
*`ocrhandle`* with the training data stored in the OCR
training files given by *`training_file`*. Its functionality
corresponds to the functionality of [`trainf_ocr_class_mlp`](trainf_ocr_class_mlp.md),
with the addition that `trainf_ocr_class_mlp_protected`
can process unprotected and protected training files. Protected
training files can be used only with the correct user password
*`password`*. If the number of passwords *`password`*
equals 1, then every input file *`training_file`* is checked
with that password, otherwise the number of passwords has to be
equal to the number of input files and the input file at position
n is checked with the password at position n. For unprotected
training files the passwords are ignored.

For a more detailed description of the operator's functionality see
[`trainf_ocr_class_mlp`](trainf_ocr_class_mlp.md). The concept of protecting OCR training
data in HALCON is described in [`protect_ocr_trainf`](protect_ocr_trainf.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator modifies the state of the following input parameter:

- ocrhandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ocrhandle`** (input_control, state is modified)  ocr_mlp `→` HHandle

Handle of the OCR classifier.

**`training_file`** (input_control)  filename.read(-array) `→` MaybeSequence[str]

Names of the training files.

Default:
"ocr.trf"

File extension:
.`trf`, .`otr`

**`password`** (input_control)  string(-array) `→` MaybeSequence[str]

Passwords for protected training files.

**`max_iterations`** (input_control)  integer `→` int

Maximum number of iterations of the
optimization algorithm.

Default:
200

Suggested values:
20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300

**`weight_tolerance`** (input_control)  real `→` float

Threshold for the difference of the weights of
the MLP between two iterations of the
optimization algorithm.

Default:
1.0

Suggested values:
1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001

Restriction:
`WeightTolerance >= 1.0e-8`

**`error_tolerance`** (input_control)  real `→` float

Threshold for the difference of the mean error
of the MLP on the training data between two
iterations of the optimization algorithm.

Default:
0.01

Suggested values:
1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001

Restriction:
`ErrorTolerance >= 1.0e-8`

**`error`** (output_control)  real `→` float

Mean error of the MLP on the training data.

**`error_log`** (output_control)  real-array `→` Sequence[float]

Mean error of the MLP on the training data as a
function of the number of iterations of the
optimization algorithm.

## Result

If the parameters are valid, the operator
`trainf_ocr_class_mlp_protected` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

`trainf_ocr_class_mlp_protected` may return the error 9211 (Matrix is
not positive definite) if `preprocessing` =
*"canonical_variates"* is used. This typically indicates
that not enough training samples have been stored for each class.
In this case we recommend to change `preprocessing` to
*"normalization"*. Another solution can be to add more
training samples.

## Possible Predecessors

`create_ocr_class_mlp`,
`write_ocr_trainf`,
`append_ocr_trainf`,
`write_ocr_trainf_image`,
`protect_ocr_trainf`

## Possible Successors

`do_ocr_single_class_mlp`,
`do_ocr_multi_class_mlp`,
`write_ocr_class_mlp`

## Alternatives

`read_ocr_class_mlp`

## See also

`trainf_ocr_class_mlp`,
`train_class_mlp`

## Module

OCR/OCV
