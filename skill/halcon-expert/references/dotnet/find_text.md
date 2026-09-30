# FindText (Operator)

## Name

`FindText` — Find text in an image.

## Signature

`static void HOperatorSet.FindText(HObject image, HTuple textModel, out HTuple textResultID)`

`HTextResult HImage.FindText(HTextModel textModel)`

`HTextResult HTextModel.FindText(HImage image)`

`public HTextResult(HImage image, HTextModel textModel)`

`void HTextResult.FindText(HImage image, HTextModel textModel)`

## Description

`FindText` finds text specified by the *`textModel`* in the
*`image`* and returns the result in *`textResultID`*.
Specific results of *`textResultID`* can be obtained with
[`GetTextResult`](get_text_result.md) and [`GetTextObject`](get_text_object.md).

The text results in *`textResultID`* differ, depending on how
`mode` was set when creating the *`textModel`* with
[`CreateTextModelReader`](create_text_model_reader.md).

For a text model with `mode` = *"auto"* `FindText`
extracts and classifies text of arbitrary size within the *`image`*.
It is possible to restrict the search to characters with specific
attributes, see [`SetTextModelParam`](set_text_model_param.md) for details.

For a text model with `mode` = *"manual"* reasonable
parameters for the text model, including the expected character height and
width, need to be set using [`SetTextModelParam`](set_text_model_param.md).
Furthermore, the *`image`* is preprocessed such that character like
structures are enhanced. The resulting compensated image can be queried from
*`textResultID`* if *"persistence"* was set to *"true"* in
*`textModel`*.

Both the text models with `mode` = *"auto"* and
`mode` = *"manual"* apply various thresholds to the input
image and segment character candidates based on region and gray value
features. These candidates are further clustered to lines. Each line is
individually completed and tested if it fulfills the constraints of a text
line. Text models with `mode` set to *"auto"* require a text
line to consist of at least two characters, whereas text models with
`mode` set to *"manual"* require a text line to consist of at
least three characters. In a further step, punctuations and separators are
added if the correspondent parameters were set via
[`SetTextModelParam`](set_text_model_param.md). Finally, if *`textModel`* contains
*"text_line_structure"* entries, the completed line is fitted to
these structures.

`FindText` finds text which is roughly horizontally aligned
in *`image`*. [`TextLineOrientation`](text_line_orientation.md) and [`RotateImage`](rotate_image.md)
can be used to achieve this alignment.

Since memory is allocated for the text result during the call of
`FindText` and during the following operations, the text result
should be
freed explicitly by the operator [`ClearTextResult`](clear_text_result.md) as soon as it is
no longer used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image.

**`textModel`** (input_control)  text_model `→` [HTextModel](HTextModel.md), [HTuple](HTuple.md) (*IntPtr*)

Text model specifying the text to be segmented.

**`textResultID`** (output_control)  text_result `→` [HTextResult](HTextResult.md), [HTuple](HTuple.md) (*IntPtr*)

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
`FindText` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateTextModelReader`,
`SetTextModelParam`,
`TextLineOrientation`,
`TextLineSlant`

## Possible Successors

`GetTextResult`,
`GetTextObject`

## Module

OCR/OCV
