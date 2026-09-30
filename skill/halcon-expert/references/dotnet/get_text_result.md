# GetTextResult (Operator)

## Name

`GetTextResult` — Query a control value of a text segmentation result.

## Signature

`static void HOperatorSet.GetTextResult(HTuple textResultID, HTuple resultName, out HTuple resultValue)`

`HTuple HTextResult.GetTextResult(HTuple resultName)`

`HTuple HTextResult.GetTextResult(string resultName)`

## Description

`GetTextResult` queries the control result *`resultName`* of
*`textResultID`* returned by [`FindText`](find_text.md). The possible parameter
values for *`resultName`* differ, depending on the text model used
within the text segmentation process of [`FindText`](find_text.md).

In the following, first the possible parameter values for text models
with `mode` = *"auto"* are listed, and then those for
text models with `mode` = *"manual"*.

The following results can be queried:

- **Results for text segmentation with text models with
  Mode = 'auto'**

  For each polarity, the text lines are independently sorted from top to
  bottom and left to right. The character within the text lines are sorted from
  left to right.

  - ***"num_lines"*:** —

    Number of lines found.
  - ***"num_classes"*:** —

    Number of best classes stored for each
    character. Depending on the number of classes of the used classifier this
    value might be smaller than the one set in the text model, see
    [`SetTextModelParam`](set_text_model_param.md).
  - ***"class"*:** —

    Classification results of all segmented characters
    with the OCR classifier contained in the corresponding text model. Note that
    if the classifier was trained with rejection class, `GetTextResult`
    returns the second best result for characters that are classified as
    rejection class.
  - ***["class", n]*:** —

    Similar to *"class"*, except
    that the class with the (*n*+1)-highest confidence is
    returned. For example, *["class", 0]* returns for each character the
    class with the highest confidence.
    Moreover, in contrast to *"class"*, the rejection class
    can be returned if the classifier contained in the corresponding text model
    was trained with rejection class.
  - ***["class_line", LineIndex]*:** —

    Classification results of
    the characters within the text line specified by *LineIndex* with the
    OCR classifier contained in the corresponding text model. For example,
    *["class_line", 0]* returns the character classes within the first
    text line. Note that if the classifier was trained with rejection class,
    `GetTextResult` returns the second best result for
    characters that are classified as rejection class.
  - ***["class_line", LineIndex, n]*:** —

    Similar to *["class_line", LineIndex]*, except that the classes with
    the (*n*+1)-highest confidences are returned. For example,
    *["class_line", LineIndex, 0]* returns for each character in the text
    line specified by *LineIndex* the class with the highest confidence.
    Moreover, in contrast to *["class_line", LineIndex]*, the rejection
    class can be returned if the classifier contained in the corresponding text
    model was trained with rejection class.
  - ***["class_element", Index]*:** —

    Classification result of the character at position *Index* with
    the OCR classifier contained in the corresponding text model. For example
    *["class_element", 0]* returns the *"num_classes"*
    best classes (sorted by confidence) of the first character.
  - ***"confidence"*:** —

    Returns the confidences of the classes
    for all segmented characters, see *"class"*.
  - ***["confidence", n]*:** —

    Returns the confidences of the classes with the (*n*+1)-highest
    confidence, see *["class", n]*.
  - ***["confidence_line", LineIndex]*:** —

    Returns the confidences of
    the classes of all characters within the text line specified by
    *LineIndex*, see *["class_line", LineIndex]*.
  - ***["confidence_line", LineIndex, n]*:** —

    Returns the confidences of the classes with the (*n*+1)-highest
    confidence for all characters within the text line specified by
    *LineIndex*, see *["class_line", LineIndex, n]*.
  - ***["confidence_element", Index]*:** —

    Returns the confidences corresponding to the classes of the character at
    position *Index*, see *["class_element", Index]*.
  - ***"polarity"*:** —

    Returns the polarity of all segmented characters.
  - ***["polarity_line", LineIndex]*:** —

    Returns the polarity of the
    characters in the segmented text line specified by *LineIndex*.
    For example, *["polarity_line", 0]* returns the polarity within the
    first text line.
  - ***["polarity_element", Index]*:** —

    Returns the polarity of the
    character at the position *Index*. For example
    *["polarity_char", 0]* returns the polarity of the first character.
- **Results for text segmentation with text models with
  Mode = 'manual'**

  - ***"manual_num_lines"*:** —

    Number of lines found.

  If *"manual_persistence"* was activated for the text model used to
  create *`textResultID`*, the following additional value can be queried:

  - ***"manual_thresholds"*:** —

    The thresholds used for segmentation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`textResultID`** (input_control)  text_result `→` [HTextResult](HTextResult.md), [HTuple](HTuple.md) (*IntPtr*)

Text result.

**`resultName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Name of the result to be returned.

Default:
"class"

List of values:
"class", "class_element", "class_line", "confidence", "confidence_element", "confidence_line", "manual_num_lines", "manual_thresholds", "num_classes", "num_lines", "polarity", "polarity_element", "polarity_line"

**`resultValue`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Value of ResultName.

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
`GetTextResult` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FindText`

## See also

`GetTextObject`

## Module

Foundation
