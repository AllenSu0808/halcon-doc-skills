# GetSupportVectorOcrClassSvm (Operator)

## Name

`GetSupportVectorOcrClassSvm` — Return the index of a support vector from a trained OCR classifier that is
based on support vector machines.

## Signature

`static void HOperatorSet.GetSupportVectorOcrClassSvm(HTuple OCRHandle, HTuple indexSupportVector, out HTuple index)`

`double HOCRSvm.GetSupportVectorOcrClassSvm(HTuple indexSupportVector)`

## Description

The operator `GetSupportVectorOcrClassSvm` maps support
vectors of a trained SVM-based OCR classifier (given in
*`OCRHandle`*) to the original training data set. The index of
the SV is specified with *`indexSupportVector`*. The index is
counted from 0, i.e., *`indexSupportVector`* must be a number
between 0 and `numSupportVectors` - 1, where
`numSupportVectors` can be determined with
[`GetSupportVectorNumOcrClassSvm`](get_support_vector_num_ocr_class_svm.md). The index of this SV
in the training data is returned in *`index`*.
`GetSupportVectorOcrClassSvm` can, for example, be used
to visualize the support vectors. To do so, the train file that has
been used to train the SVM must be read with
[`ReadOcrTrainf`](read_ocr_trainf.md). The value returned in *`index`* must
be incremented by *1* and can then be used to select the
support vectors with [`SelectObj`](select_obj.md) from the training
characters. If more than one train file has been used in
[`TrainfOcrClassSvm`](trainf_ocr_class_svm.md) *`index`* behaves as if all train
files had been merged into one train file with
[`ConcatOcrTrainf`](concat_ocr_trainf.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_svm `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

OCR handle.

**`indexSupportVector`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Number of stored support vectors.

**`index`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Index of the support vector in the training set.

## Result

If the parameters are valid the operator
`GetSupportVectorOcrClassSvm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainfOcrClassSvm`,
`GetSupportVectorNumOcrClassSvm`

## See also

`CreateOcrClassSvm`,
`ReadOcrTrainf`,
`AppendOcrTrainf`,
`ConcatOcrTrainf`

## Module

OCR/OCV
