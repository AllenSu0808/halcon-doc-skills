# GetPrepInfoOcrClassMlp (Operator)

## Name

`GetPrepInfoOcrClassMlp` — Compute the information content of the preprocessed feature vectors
of an OCR classifier.

## Signature

`static void HOperatorSet.GetPrepInfoOcrClassMlp(HTuple OCRHandle, HTuple trainingFile, HTuple preprocessing, out HTuple informationCont, out HTuple cumInformationCont)`

`HTuple HOCRMlp.GetPrepInfoOcrClassMlp(HTuple trainingFile, string preprocessing, out HTuple cumInformationCont)`

`HTuple HOCRMlp.GetPrepInfoOcrClassMlp(string trainingFile, string preprocessing, out HTuple cumInformationCont)`

## Description

`GetPrepInfoOcrClassMlp` computes the information content
of the training vectors that have been transformed with the
preprocessing given by *`preprocessing`*.
*`preprocessing`* can be set to *"principal_components"*
or *"canonical_variates"*. The OCR classifier
*`OCRHandle`* must have been created with
[`CreateOcrClassMlp`](create_ocr_class_mlp.md). The preprocessing methods are
described with [`CreateClassMlp`](create_class_mlp.md). The information content is
derived from the variations of the transformed components of the
feature vector, i.e., it is computed solely based on the training
data, independent of any error rate on the training data. The
information content is computed for all relevant components of the
transformed feature vectors (`numInput` for
*"principal_components"* and min(`numOutput` - 1,
`numInput`) for *"canonical_variates"*, see
[`CreateClassMlp`](create_class_mlp.md)), and is returned in
*`informationCont`* as a number between 0 and 1. To convert
the information content into a percentage, it simply needs to be
multiplied by 100. The cumulative information content of the first
n components is returned in the n-th component of
*`cumInformationCont`*, i.e., *`cumInformationCont`*
contains the sums of the first n elements of
*`informationCont`*. To use
`GetPrepInfoOcrClassMlp`, a sufficient number of samples
must be stored in the training files given by *`trainingFile`*
(see [`WriteOcrTrainf`](write_ocr_trainf.md)).

*`informationCont`* and *`cumInformationCont`* can be used
to decide how many components of the transformed feature vectors
contain relevant information. An often used criterion is to require
that the transformed data must represent x% (e.g., 90%) of the
total data. This can be decided easily from the first value of
*`cumInformationCont`* that lies above x%. The number thus
obtained can be used as the value for `numComponents` in a
new call to [`CreateOcrClassMlp`](create_ocr_class_mlp.md). The call to
`GetPrepInfoOcrClassMlp` already requires the creation of
a classifier, and hence the setting of `numComponents` in
[`CreateOcrClassMlp`](create_ocr_class_mlp.md) to an initial value. However, if
`GetPrepInfoOcrClassMlp` is called it is typically not
known how many components are relevant, and hence how to set
`numComponents` in this call. Therefore, the following
two-step approach should typically be used to select
`numComponents`: In a first step, a classifier with the
maximum number for `numComponents` is created
(`numInput` for *"principal_components"* and
min(`numOutput` - 1,
`numInput`) for *"canonical_variates"*). Then, the
training samples are saved in a training file using
[`WriteOcrTrainf`](write_ocr_trainf.md). Subsequently,
`GetPrepInfoOcrClassMlp` is used to determine the
information content of the components, and with this
`numComponents`. After this, a new classifier with the
desired number of components is created, and the classifier is
trained with [`TrainfOcrClassMlp`](trainf_ocr_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_mlp `→` [HOCRMlp](HOCRMlp.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`trainingFile`** (input_control)  filename.read(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the training files.

Default:
"ocr.trf"

File extension:
.`trf`, .`otr`

**`preprocessing`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of preprocessing used to transform the
feature vectors.

Default:
"principal_components"

List of values:
"canonical_variates", "principal_components"

**`informationCont`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Relative information content of the transformed
feature vectors.

**`cumInformationCont`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Cumulative information content of the transformed
feature vectors.

## Example (HDevelop)

```
* Create the initial OCR classifier.
read_ocr_trainf_names ('ocr.trf', CharacterNames, CharacterCount)
create_ocr_class_mlp (8, 10, 'constant', 'default', CharacterNames, 80, \
                      'canonical_variates', |CharacterNames|, 42, OCRHandle)
* Get the information content of the transformed feature vectors.
get_prep_info_ocr_class_mlp (OCRHandle, 'ocr.trf', 'canonical_variates', \
                             InformationCont, CumInformationCont)
* Determine the number of transformed components.
* NumComp = [...]
* Create the final OCR classifier.
create_ocr_class_mlp (8, 10, 'constant', 'default', CharacterNames, 80, \
                      'canonical_variates', NumComp, 42, OCRHandle)
* Train the final classifier.
trainf_ocr_class_mlp (OCRHandle, 'ocr.trf', 100, 1, 0.01, Error, ErrorLog)
write_ocr_class_mlp (OCRHandle, 'ocr.omc')
```

## Result

If the parameters are valid, the operator
`GetPrepInfoOcrClassMlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

`GetPrepInfoOcrClassMlp` may return the error 9211
(Matrix is not positive definite) if *`preprocessing`* =
*"canonical_variates"* is used. This typically indicates
that not enough training samples have been stored for each class.

## Possible Predecessors

`CreateOcrClassMlp`,
`WriteOcrTrainf`,
`AppendOcrTrainf`,
`WriteOcrTrainfImage`

## Possible Successors

`ClearOcrClassMlp`,
`CreateOcrClassMlp`

## Module

OCR/OCV
