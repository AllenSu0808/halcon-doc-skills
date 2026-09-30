# GetTextModelParam (Operator)

## Name

`GetTextModelParam` — Query parameters of a text model.

## Signature

`static void HOperatorSet.GetTextModelParam(HTuple textModel, HTuple genParamName, out HTuple genParamValue)`

`HTuple HTextModel.GetTextModelParam(string genParamName)`

## Description

`GetTextModelParam` queries the parameters of *`textModel`*.
With the exception of *"ocr_classifier"*, all valid parameters can
be queried. See [`SetTextModelParam`](set_text_model_param.md) for a detailed description of
the possible values for *`genParamName`* and *`genParamValue`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`textModel`** (input_control)  text_model `→` [HTextModel](HTextModel.md), [HTuple](HTuple.md) (*IntPtr*)

Text model.

**`genParamName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Parameters to be queried.

Default:
"min_contrast"

Suggested values:
"add_fragments", "dot_print", "dot_print_max_dot_gap", "dot_print_min_char_gap", "dot_print_tight_char_spacing", "eliminate_border_blobs", "max_char_height", "max_char_width", "max_stroke_width", "min_char_height", "min_char_width", "min_contrast", "min_stroke_width", "num_classes", "polarity", "return_punctuation", "return_separators", "return_whole_line", "separate_touching_chars", "text_line_separators", "text_line_structure", "text_line_structure_0", "text_line_structure_1", "text_line_structure_2", "manual_add_fragments", "manual_base_line_tolerance", "manual_char_height", "manual_char_width", "manual_eliminate_border_blobs", "manual_eliminate_horizontal_lines", "manual_fragment_size_min", "manual_is_dotprint", "manual_is_imprinted", "manual_max_line_num", "manual_persistence", "manual_polarity", "manual_return_punctuation", "manual_return_separators", "manual_stroke_width", "manual_text_line_structure", "manual_text_line_structure_0", "manual_text_line_structure_1", "manual_text_line_structure_2", "manual_uppercase_only"

**`genParamValue`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Values of Parameters.

## Result

If the input parameters are set correctly, the operator
`GetTextModelParam` returns the value 2 (
H_MSG_TRUE)
. Otherwise, an
exception will be raised.

## See also

`SetTextModelParam`

## Module

OCR/OCV
