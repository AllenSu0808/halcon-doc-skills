# trainf_ocr_class_mlp (Operator)

## Name

`trainf_ocr_class_mlp` — Train an OCR classifier.

## Signature

`def trainf_ocr_class_mlp(ocrhandle: HHandle, training_file: MaybeSequence[str], max_iterations: int, weight_tolerance: float, error_tolerance: float) -> Tuple[float, Sequence[float]]`

## Description

`trainf_ocr_class_mlp` trains the OCR classifier
*`ocrhandle`* with the training characters stored in the OCR
training files given by *`training_file`*. The training files
must have been created, e.g., using [`write_ocr_trainf`](write_ocr_trainf.md), before
calling `trainf_ocr_class_mlp`.

The remaining parameters have the same meaning as in
[`train_class_mlp`](train_class_mlp.md) and are described in detail with
[`train_class_mlp`](train_class_mlp.md). A regularization of the OCR classifier and
an automatic determination of the regularization parameters (see
[`set_regularization_params_ocr_class_mlp`](set_regularization_params_ocr_class_mlp.md)) is taken into
account during the training. Furthermore, if a rejection class has
been specified using [`set_rejection_params_ocr_class_mlp`](set_rejection_params_ocr_class_mlp.md),
before the actual training the samples for the rejection class are
generated.

Please note that training characters that have no corresponding
class in the classifier *`ocrhandle`* are discarded.

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

## Example (HDevelop)

```
* Train an OCR classifier
read_ocr_trainf_names ('ocr.trf', CharacterNames, CharacterCount)
create_ocr_class_mlp (8, 10, 'constant', 'default', CharacterNames, 80, \
                      'none', 81, 42, OCRHandle)
trainf_ocr_class_mlp (OCRHandle, 'ocr.trf', 100, 1, 0.01, Error, ErrorLog)
write_ocr_class_mlp (OCRHandle, 'ocr.omc')
```

## Result

If the parameters are valid, the operator
`trainf_ocr_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

`trainf_ocr_class_mlp` may return the error 9211 (Matrix is
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
`set_regularization_params_ocr_class_mlp`

## Possible Successors

`do_ocr_single_class_mlp`,
`do_ocr_multi_class_mlp`,
`write_ocr_class_mlp`

## Alternatives

`read_ocr_class_mlp`

## See also

`train_class_mlp`

## Module

OCR/OCV
