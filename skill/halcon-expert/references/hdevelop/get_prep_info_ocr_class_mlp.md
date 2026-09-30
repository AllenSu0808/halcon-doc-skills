# get_prep_info_ocr_class_mlp (Operator)

## Name

`get_prep_info_ocr_class_mlp` — Compute the information content of the preprocessed feature vectors
of an OCR classifier.

## Signature

`get_prep_info_ocr_class_mlp( : : OCRHandle, TrainingFile, Preprocessing : InformationCont, CumInformationCont)`

## Description

`get_prep_info_ocr_class_mlp` computes the information content
of the training vectors that have been transformed with the
preprocessing given by *`Preprocessing`*.
*`Preprocessing`* can be set to *'principal_components'*
or *'canonical_variates'*. The OCR classifier
*`OCRHandle`* must have been created with
[`create_ocr_class_mlp`](create_ocr_class_mlp.md). The preprocessing methods are
described with [`create_class_mlp`](create_class_mlp.md). The information content is
derived from the variations of the transformed components of the
feature vector, i.e., it is computed solely based on the training
data, independent of any error rate on the training data. The
information content is computed for all relevant components of the
transformed feature vectors (`NumInput` for
*'principal_components'* and min(`NumOutput` - 1,
`NumInput`) for *'canonical_variates'*, see
[`create_class_mlp`](create_class_mlp.md)), and is returned in
*`InformationCont`* as a number between 0 and 1. To convert
the information content into a percentage, it simply needs to be
multiplied by 100. The cumulative information content of the first
n components is returned in the n-th component of
*`CumInformationCont`*, i.e., *`CumInformationCont`*
contains the sums of the first n elements of
*`InformationCont`*. To use
`get_prep_info_ocr_class_mlp`, a sufficient number of samples
must be stored in the training files given by *`TrainingFile`*
(see [`write_ocr_trainf`](write_ocr_trainf.md)).

*`InformationCont`* and *`CumInformationCont`* can be used
to decide how many components of the transformed feature vectors
contain relevant information. An often used criterion is to require
that the transformed data must represent x% (e.g., 90%) of the
total data. This can be decided easily from the first value of
*`CumInformationCont`* that lies above x%. The number thus
obtained can be used as the value for `NumComponents` in a
new call to [`create_ocr_class_mlp`](create_ocr_class_mlp.md). The call to
`get_prep_info_ocr_class_mlp` already requires the creation of
a classifier, and hence the setting of `NumComponents` in
[`create_ocr_class_mlp`](create_ocr_class_mlp.md) to an initial value. However, if
`get_prep_info_ocr_class_mlp` is called it is typically not
known how many components are relevant, and hence how to set
`NumComponents` in this call. Therefore, the following
two-step approach should typically be used to select
`NumComponents`: In a first step, a classifier with the
maximum number for `NumComponents` is created
(`NumInput` for *'principal_components'* and
min(`NumOutput` - 1,
`NumInput`) for *'canonical_variates'*). Then, the
training samples are saved in a training file using
[`write_ocr_trainf`](write_ocr_trainf.md). Subsequently,
`get_prep_info_ocr_class_mlp` is used to determine the
information content of the components, and with this
`NumComponents`. After this, a new classifier with the
desired number of components is created, and the classifier is
trained with [`trainf_ocr_class_mlp`](trainf_ocr_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_mlp `→`  (handle)

Handle of the OCR classifier.

**`TrainingFile`** (input_control)  filename.read(-array) `→`  (string)

Names of the training files.

Default:
'ocr.trf'

File extension:
.`trf`, .`otr`

**`Preprocessing`** (input_control)  string `→`  (string)

Type of preprocessing used to transform the
feature vectors.

Default:
'principal_components'

List of values:
'canonical_variates', 'principal_components'

**`InformationCont`** (output_control)  real-array `→`  (real)

Relative information content of the transformed
feature vectors.

**`CumInformationCont`** (output_control)  real-array `→`  (real)

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
`get_prep_info_ocr_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

`get_prep_info_ocr_class_mlp` may return the error 9211
(Matrix is not positive definite) if *`Preprocessing`* =
*'canonical_variates'* is used. This typically indicates
that not enough training samples have been stored for each class.

## Possible Predecessors

`create_ocr_class_mlp`,
`write_ocr_trainf`,
`append_ocr_trainf`,
`write_ocr_trainf_image`

## Possible Successors

`clear_ocr_class_mlp`,
`create_ocr_class_mlp`

## Module

OCR/OCV
