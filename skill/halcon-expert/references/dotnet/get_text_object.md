# GetTextObject (Operator)

## Name

`GetTextObject` — Query an iconic value of a text segmentation result.

## Signature

`static void HOperatorSet.GetTextObject(out HObject characters, HTuple textResultID, HTuple resultName)`

`HObject HTextResult.GetTextObject(HTuple resultName)`

`HObject HTextResult.GetTextObject(string resultName)`

## Description

`GetTextObject` queries the iconic result *`resultName`* of
*`textResultID`* returned by [`FindText`](find_text.md). The possible parameter
values for *`resultName`* differ, depending on the text model used
within the text segmentation process of [`FindText`](find_text.md).

In the following, first the possible parameter values for text models
with `mode` = *"auto"* are listed, and then those for
text models with `mode` = *"manual"*.

The following results can be queried:

- Result objects for text segmentation with text models with
  `mode` = *"auto"*

  For each polarity, the text lines are independently sorted from top to
  bottom and left to right. The character within the text lines are sorted from
  left to right.

  - ***"all_lines"*:** —

    Returns all characters in all segmented text
    lines.
  - ***["line", LineIndex]*:** —

    Returns all characters within the
    text line specified by *LineIndex*.
    For example, *["line", 0]* returns the first line.
  - ***["element", Index]*:** —

    Returns the character at position *Index*.
    For example, *["element", 0]* returns the first character.
- Result objects for text segmentation with text models with
  `mode` = *"manual"*

  - ***"manual_all_lines"*:** —

    Returns all characters in all segmented
    text lines.
    The text lines are sorted from top to bottom and left to right.
    The characters within the text lines are sorted from left to right.
  - ***["manual_line", Index]*:** —

    Returns all characters within the text
    line specified by *Index* (e.g., *["manual_line",0]* to
    return the first line).
    The characters within the text line are sorted from left to right.

  If *"manual_persistence"* was activated for the text model used to
  create *`textResultID`*, the following additional value can be queried:

  - ***"manual_compensated_image"*:** —

    the enhanced image used for
    segmentation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`characters`** (output_object)  object(-array) `→` [HObject](HObject.md)

Returned result.

**`textResultID`** (input_control)  text_result `→` [HTextResult](HTextResult.md), [HTuple](HTuple.md) (*IntPtr*)

Text result.

**`resultName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Name of the result to be returned.

Default:
"all_lines"

List of values:
"all_lines", "element", "line", "manual_all_lines", "manual_compensated_image", "manual_line"

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
`GetTextObject` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FindText`

## See also

`GetTextResult`

## Module

Foundation
