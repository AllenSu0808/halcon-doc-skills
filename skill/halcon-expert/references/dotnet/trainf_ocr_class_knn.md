# TrainfOcrClassKnn (Operator)

## Name

`TrainfOcrClassKnn` — Trains an k-NN classifier for an OCR task.

## Signature

`static void HOperatorSet.TrainfOcrClassKnn(HTuple OCRHandle, HTuple trainingFile, HTuple genParamName, HTuple genParamValue)`

`void HOCRKnn.TrainfOcrClassKnn(HTuple trainingFile, HTuple genParamName, HTuple genParamValue)`

`void HOCRKnn.TrainfOcrClassKnn(string trainingFile, HTuple genParamName, HTuple genParamValue)`

## Description

`TrainfOcrClassKnn` trains the k-NN classifier
*`OCRHandle`* with the training characters stored in the OCR
training files given by *`trainingFile`*. The training files
must have been created, e.g., using [`WriteOcrTrainf`](write_ocr_trainf.md), before
calling `TrainfOcrClassKnn`. Please, note that training characters
that have no corresponding class in the classifier *`OCRHandle`* are
discarded.

The following options may be set using *`genParamName`* and
*`genParamValue`*, respectively:

- ***"num_trees"*** —

  Sets the number of search trees. A higher number of trees improves the
  accuracy of the search, but also increases the runtime.

  Default:
   *4*.
- ***"normalization"*** —

  Activates the data normalization, if set to *"true"*.
  This will change the stored training data permanently. Therefore,
  adding data after the training is not possible.

  List of values:
   *"true"*, *"false"*.

  Default:
   *"false"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- OCRHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`OCRHandle`** (input_control, state is modified)  ocr_knn `→` [HOCRKnn](HOCRKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

**`trainingFile`** (input_control)  filename.read(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the training files.

Default:
"ocr.trf"

File extension:
.`trf`, .`otr`

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters that can be adjusted
for the k-NN classifier creation.

Default:
[]

List of values:
"normalization", "num_trees"

**`genParamValue`** (input_control)  number-array `→` [HTuple](HTuple.md) (*int* / long / string / double)

Values of the generic parameters that can be adjusted
for the k-NN classifier creation.

Default:
[]

Suggested values:
4, 5, "false", "true"

## Example (HDevelop)

```
* Train an OCR classifier
read_ocr_trainf_names ('ocr.trf', CharacterNames, CharacterCount)
create_ocr_class_knn (8, 10, 'constant', 'default', CharacterNames, [],\
                      [], OCRHandle)
trainf_ocr_class_knn (OCRHandle, 'ocr.trf', [], [])
write_ocr_class_knn (OCRHandle, 'ocr.omc')
```

## Result

If the parameters are valid, the operator
`TrainfOcrClassKnn` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`CreateOcrClassKnn`,
`WriteOcrTrainf`,
`AppendOcrTrainf`,
`WriteOcrTrainfImage`

## Possible Successors

`DoOcrSingleClassKnn`,
`DoOcrMultiClassKnn`

## Alternatives

`ReadOcrClassKnn`

## See also

`TrainClassKnn`

## Module

OCR/OCV
