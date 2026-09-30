# find_text (Operator)

## Name

`find_text` — Find text in an image.

## Signature

`find_text(Image : : TextModel : TextResultID)`

## Description

`find_text` finds text specified by the *`TextModel`* in the
*`Image`* and returns the result in *`TextResultID`*.
Specific results of *`TextResultID`* can be obtained with
[`get_text_result`](get_text_result.md) and [`get_text_object`](get_text_object.md).

The text results in *`TextResultID`* differ, depending on how
`Mode` was set when creating the *`TextModel`* with
[`create_text_model_reader`](create_text_model_reader.md).

For a text model with `Mode` = *'auto'* `find_text`
extracts and classifies text of arbitrary size within the *`Image`*.
It is possible to restrict the search to characters with specific
attributes, see [`set_text_model_param`](set_text_model_param.md) for details.

For a text model with `Mode` = *'manual'* reasonable
parameters for the text model, including the expected character height and
width, need to be set using [`set_text_model_param`](set_text_model_param.md).
Furthermore, the *`Image`* is preprocessed such that character like
structures are enhanced. The resulting compensated image can be queried from
*`TextResultID`* if *'persistence'* was set to *'true'* in
*`TextModel`*.

Both the text models with `Mode` = *'auto'* and
`Mode` = *'manual'* apply various thresholds to the input
image and segment character candidates based on region and gray value
features. These candidates are further clustered to lines. Each line is
individually completed and tested if it fulfills the constraints of a text
line. Text models with `Mode` set to *'auto'* require a text
line to consist of at least two characters, whereas text models with
`Mode` set to *'manual'* require a text line to consist of at
least three characters. In a further step, punctuations and separators are
added if the correspondent parameters were set via
[`set_text_model_param`](set_text_model_param.md). Finally, if *`TextModel`* contains
*'text_line_structure'* entries, the completed line is fitted to
these structures.

`find_text` finds text which is roughly horizontally aligned
in *`Image`*. [`text_line_orientation`](text_line_orientation.md) and [`rotate_image`](rotate_image.md)
can be used to achieve this alignment.

Since memory is allocated for the text result during the call of
`find_text` and during the following operations, the text result
should be
freed explicitly by the operator [`clear_text_result`](clear_text_result.md) as soon as it is
no longer used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image.

**`TextModel`** (input_control)  text_model `→`  (handle)

Text model specifying the text to be segmented.

**`TextResultID`** (output_control)  text_result `→`  (handle)

Result of the segmentation.

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

If the parameters are valid, the operator
`find_text` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_text_model_reader`,
`set_text_model_param`,
`text_line_orientation`,
`text_line_slant`

## Possible Successors

`get_text_result`,
`get_text_object`

## Module

OCR/OCV
