# TrainfOcrClassSvmProtected (Operator)

## Name

`TrainfOcrClassSvmProtected` — Train an OCR classifier with data from a (protected) training file.

## Signature

`static void HOperatorSet.TrainfOcrClassSvmProtected(HTuple OCRHandle, HTuple trainingFile, HTuple password, HTuple epsilon, HTuple trainMode)`

`void HOCRSvm.TrainfOcrClassSvmProtected(HTuple trainingFile, HTuple password, double epsilon, HTuple trainMode)`

`void HOCRSvm.TrainfOcrClassSvmProtected(string trainingFile, string password, double epsilon, string trainMode)`

## Description

`TrainfOcrClassSvmProtected` trains the OCR classifier
*`OCRHandle`* with the training data stored in the OCR
training files given by *`trainingFile`*. Its functionality
corresponds to the functionality of [`TrainfOcrClassSvm`](trainf_ocr_class_svm.md),
with the addition that `TrainfOcrClassSvmProtected`
can process unprotected and protected training files. Protected
training files can be used only with the correct user password
*`password`*. If the number of passwords *`password`*
equals 1, then every input file *`trainingFile`* is checked
with that password, otherwise the number of passwords has to be
equal to the number of input files and the input file at position
n is checked with the password at position n. For unprotected
training files the passwords are ignored.

For a more detailed description of the operator's functionality see
[`TrainfOcrClassSvm`](trainf_ocr_class_svm.md). The concept of protecting OCR training
data in HALCON is described in [`ProtectOcrTrainf`](protect_ocr_trainf.md).

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

**`password`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Passwords for protected training files.

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

## Result

If the parameters are valid the operator
`TrainfOcrClassSvmProtected` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

`TrainfOcrClassSvmProtected` may return the error 9211 (Matrix is
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
`WriteOcrTrainfImage`,
`ProtectOcrTrainf`

## Possible Successors

`DoOcrSingleClassSvm`,
`DoOcrMultiClassSvm`,
`WriteOcrClassSvm`

## Alternatives

`ReadOcrClassSvm`

## See also

`TrainfOcrClassSvm`,
`TrainClassSvm`

## Module

OCR/OCV
