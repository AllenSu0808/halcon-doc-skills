# trainf_ocr_class_svm (Operator)

## Name

`trainf_ocr_class_svm` — Train an OCR classifier.

## Signature

`trainf_ocr_class_svm( : : OCRHandle, TrainingFile, Epsilon, TrainMode : )`

## Description

`trainf_ocr_class_svm` trains the OCR classifier
*`OCRHandle`* with the training characters stored in the OCR
training files given by *`TrainingFile`*. The training files
must have been created, e.g., using [`write_ocr_trainf`](write_ocr_trainf.md), before
calling `trainf_ocr_class_svm`. The parameters
*`Epsilon`* and *`TrainMode`* have the same meaning as in
[`train_class_svm`](train_class_svm.md). Please, note that training characters that have
no corresponding class in the classifier *`OCRHandle`* are discarded.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- OCRHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`OCRHandle`** (input_control, state is modified)  ocr_svm `→`  (handle)

Handle of the OCR classifier.

**`TrainingFile`** (input_control)  filename.read(-array) `→`  (string)

Names of the training files.

Default:
'ocr.trf'

File extension:
.`trf`, .`otr`

**`Epsilon`** (input_control)  real `→`  (real)

Stop parameter for training.

Default:
0.001

Suggested values:
0.00001, 0.0001, 0.001, 0.01, 0.1

**`TrainMode`** (input_control)  number `→`  (string / integer)

Mode of training.

Default:
'default'

List of values:
'add_sv_to_train_set', 'default'

## Example (HDevelop)

```
* Train an OCR classifier
read_ocr_trainf_names ('ocr.trf', CharacterNames, CharacterCount)
create_ocr_class_svm (8, 10, 'constant', 'default', CharacterNames, \
                      'rbf', 0.01, 0.01, 'one-versus-one', \
                      'normalization', 81, OCRHandle)
trainf_ocr_class_svm (OCRHandle, 'ocr.trf', 0.001, 'default')
write_ocr_class_svm (OCRHandle, 'ocr.osc')
```

## Result

If the parameters are valid the operator
`trainf_ocr_class_svm` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

`trainf_ocr_class_svm` may return the error 9211 (Matrix is
not positive definite) if `Preprocessing` =
*'canonical_variates'* is used. This typically indicates
that not enough training samples have been stored for each class.
In this case we recommend to change `Preprocessing` to
*'normalization'*. Another solution can be to add more
training samples.

## Possible Predecessors

`create_ocr_class_svm`,
`write_ocr_trainf`,
`append_ocr_trainf`,
`write_ocr_trainf_image`

## Possible Successors

`do_ocr_single_class_svm`,
`do_ocr_multi_class_svm`,
`write_ocr_class_svm`

## Alternatives

`read_ocr_class_svm`

## See also

`train_class_svm`

## Module

OCR/OCV
