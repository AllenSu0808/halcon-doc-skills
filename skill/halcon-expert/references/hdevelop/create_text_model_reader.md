# create_text_model_reader (Operator)

## Name

`create_text_model_reader` — Create a text model.

## Signature

`create_text_model_reader( : : Mode, OCRClassifier : TextModel)`

## Description

`create_text_model_reader` creates a *`TextModel`*, which
describes the text to be segmented with [`find_text`](find_text.md).

The parameter value of *`Mode`* determines which text segmentation
approach is used. Possible values are *'auto'* and *'manual'*.

Typically, the parameter *`Mode`* should be set to *'auto'*
because this mode is more stable and requires less configuration effort.
Note that in this case, also an OCR classifier must be passed in
*`OCRClassifier`*. Only if one of the following restrictions apply,
*`Mode`* must be set to *'manual'*:

- The segmentation of text which has strong local variations of the
  polarity is required. For example, due to reflections, engraved text often
  has strong local variations.
- No suitable OCR classifier is available (see below).

If *`Mode`* = *'auto'*, [`find_text`](find_text.md) is able to extract text
of arbitrary size. It is possible to restrict the search to characters with
specific attributes, see [`set_text_model_param`](set_text_model_param.md) for details.
In particular, if the text to be segmented contains dot printed characters,
the text model parameter *'dot_print'* must be set to *'true'*.
Furthermore, an OCR classifier must be passed in *`OCRClassifier`*.
This OCR classifier must be based on a convolutional neural network (CNN) or
a multilayer perceptron (MLP). Moreover, it is strongly recommended to
use a CNN based OCR classifier with rejection class or a MLP based
classifiers that has been trained with regularization parameters (see
[`set_regularization_params_ocr_class_mlp`](set_regularization_params_ocr_class_mlp.md) and provides a rejection
class (see [`set_rejection_params_ocr_class_mlp`](set_rejection_params_ocr_class_mlp.md)).
A suitable OCR classifier can either be read with [`read_ocr_class_cnn`](read_ocr_class_cnn.md)
or [`read_ocr_class_mlp`](read_ocr_class_mlp.md), or be created with
[`create_ocr_class_mlp`](create_ocr_class_mlp.md). It is also possible to pass a string containing
the path to a pretrained OCR classifier or an OCR classifier that has
been stored with [`write_ocr_class_mlp`](write_ocr_class_mlp.md).

To enable text segmentation when *`Mode`* = *'manual'*,
reasonable parameters for the text model, including the expected
character height and width, must be set using
[`set_text_model_param`](set_text_model_param.md). In this case, the value of
*`OCRClassifier`* is ignored.

The parameters of the *`TextModel`* can be set and queried with
[`set_text_model_param`](set_text_model_param.md) and [`get_text_model_param`](get_text_model_param.md).

Since memory is allocated for the text model during the call of
`create_text_model_reader` and during the following operations, the
model should be freed explicitly by the operator [`clear_text_model`](clear_text_model.md) as
soon as it is no longer used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Mode`** (input_control)  string `→`  (string)

The Mode of the text model.

Default:
'auto'

List of values:
'auto', 'manual'

**`OCRClassifier`** (input_control)  string `→`  (string / integer)

OCR Classifier.

Default:
'Universal_Rej.occ'

Suggested values:
'Document_Rej.omc', 'Document_0-9_Rej.omc', 'Document_0-9A-Z_Rej.omc', 'Document_A-Z+_Rej.omc', 'DotPrint_Rej.omc', 'DotPrint_0-9_Rej.omc', 'DotPrint_0-9+_Rej.omc', 'DotPrint_0-9A-Z_Rej.omc', 'DotPrint_A-Z+_Rej.omc', 'HandWritten_0-9_Rej.omc', 'Industrial_Rej.omc', 'Industrial_0-9_Rej.omc', 'Industrial_0-9+_Rej.omc', 'Industrial_0-9A-Z_Rej.omc', 'Industrial_A-Z+_Rej.omc', 'OCRA_Rej.omc', 'OCRA_0-9_Rej.omc', 'OCRA_0-9A-Z_Rej.omc', 'OCRA_A-Z+_Rej.omc', 'OCRB_Rej.omc', 'OCRB_0-9_Rej.omc', 'OCRB_0-9A-Z_Rej.omc', 'OCRB_A-Z+_Rej.omc', 'OCRB_passport_Rej.omc', 'Pharma_Rej.omc', 'Pharma_0-9_Rej.omc', 'Pharma_0-9+_Rej.omc', 'Pharma_0-9A-Z_Rej.omc', 'SEMI_Rej.omc', 'Universal_Rej.occ', 'Universal_0-9_Rej.occ', 'Universal_0-9+_Rej.occ', 'Universal_0-9A-Z_Rej.occ', 'Universal_0-9A-Z+_Rej.occ', 'Universal_A-Z+_Rej.occ'

**`TextModel`** (output_control)  text_model `→`  (handle)

New text model.

## Example (HDevelop)

```
read_image (Image, 'numbers_scale')
create_text_model_reader ('auto', 'Document_Rej.omc', TextModel)
* Optionally specify text properties
set_text_model_param (TextModel, 'min_char_height', 20)
find_text (Image, TextModel, TextResultID)
* Return character regions and corresponding classification results
get_text_object (Characters, TextResultID, 'all_lines')
get_text_result (TextResultID, 'class', Class)
```

## Result

`create_text_model_reader` returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`set_text_model_param`,
`get_text_model_param`,
`find_text`

## See also

`clear_text_model`

## Module

OCR/OCV
