# trainf_ocr_class_knn (Operator)

## Name

`trainf_ocr_class_knn` — Trains an k-NN classifier for an OCR task.

## Signature

`def trainf_ocr_class_knn(ocrhandle: HHandle, training_file: MaybeSequence[str], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, str, float]]) -> None`

## Description

`trainf_ocr_class_knn` trains the k-NN classifier
*`ocrhandle`* with the training characters stored in the OCR
training files given by *`training_file`*. The training files
must have been created, e.g., using [`write_ocr_trainf`](write_ocr_trainf.md), before
calling `trainf_ocr_class_knn`. Please, note that training characters
that have no corresponding class in the classifier *`ocrhandle`* are
discarded.

The following options may be set using *`gen_param_name`* and
*`gen_param_value`*, respectively:

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

- ocrhandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ocrhandle`** (input_control, state is modified)  ocr_knn `→` HHandle

Handle of the k-NN classifier.

**`training_file`** (input_control)  filename.read(-array) `→` MaybeSequence[str]

Names of the training files.

Default:
"ocr.trf"

File extension:
.`trf`, .`otr`

**`gen_param_name`** (input_control)  string-array `→` Sequence[str]

Names of the generic parameters that can be adjusted
for the k-NN classifier creation.

Default:
[]

List of values:
"normalization", "num_trees"

**`gen_param_value`** (input_control)  number-array `→` Sequence[Union[int, str, float]]

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
`trainf_ocr_class_knn` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`create_ocr_class_knn`,
`write_ocr_trainf`,
`append_ocr_trainf`,
`write_ocr_trainf_image`

## Possible Successors

`do_ocr_single_class_knn`,
`do_ocr_multi_class_knn`

## Alternatives

`read_ocr_class_knn`

## See also

`train_class_knn`

## Module

OCR/OCV
