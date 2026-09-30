# TrainfOcrClassSvm (Operator)

## Name

`TrainfOcrClassSvm` — Train an OCR classifier.

## Signature

`static void HOperatorSet.TrainfOcrClassSvm(HTuple OCRHandle, HTuple trainingFile, HTuple epsilon, HTuple trainMode)`

`void HOCRSvm.TrainfOcrClassSvm(HTuple trainingFile, double epsilon, HTuple trainMode)`

`void HOCRSvm.TrainfOcrClassSvm(string trainingFile, double epsilon, string trainMode)`

## Description

`TrainfOcrClassSvm` trains the OCR classifier
*`OCRHandle`* with the training characters stored in the OCR
training files given by *`trainingFile`*. The training files
must have been created, e.g., using [`WriteOcrTrainf`](write_ocr_trainf.md), before
calling `TrainfOcrClassSvm`. The parameters
*`epsilon`* and *`trainMode`* have the same meaning as in
[`TrainClassSvm`](train_class_svm.md). Please, note that training characters that have
no corresponding class in the classifier *`OCRHandle`* are discarded.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- OCRHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`OCRHandle`** (input_control, state is modified)  ocr_svm `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`trainingFile`** (input_control)  filename.read(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the training files.

Default:
"ocr.trf"

File extension:
.`trf`, .`otr`

**`epsilon`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Stop parameter for training.

Default:
0.001

Suggested values:
0.00001, 0.0001, 0.001, 0.01, 0.1

**`trainMode`** (input_control)  number `→` [HTuple](HTuple.md) (*string* / int / long)

Mode of training.

Default:
"default"

List of values:
"add_sv_to_train_set", "default"

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
`TrainfOcrClassSvm` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

`TrainfOcrClassSvm` may return the error 9211 (Matrix is
not positive definite) if `preprocessing` =
*"canonical_variates"* is used. This typically indicates
that not enough training samples have been stored for each class.
In this case we recommend to change `preprocessing` to
*"normalization"*. Another solution can be to add more
training samples.

## Possible Predecessors

`CreateOcrClassSvm`,
`WriteOcrTrainf`,
`AppendOcrTrainf`,
`WriteOcrTrainfImage`

## Possible Successors

`DoOcrSingleClassSvm`,
`DoOcrMultiClassSvm`,
`WriteOcrClassSvm`

## Alternatives

`ReadOcrClassSvm`

## See also

`TrainClassSvm`

## Module

OCR/OCV
