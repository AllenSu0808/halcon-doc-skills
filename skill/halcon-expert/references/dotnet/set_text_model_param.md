# SetTextModelParam (Operator)

## Name

`SetTextModelParam` — Set parameters of a text model.

## Signature

`static void HOperatorSet.SetTextModelParam(HTuple textModel, HTuple genParamName, HTuple genParamValue)`

`void HTextModel.SetTextModelParam(HTuple genParamName, HTuple genParamValue)`

`void HTextModel.SetTextModelParam(string genParamName, int genParamValue)`

## Description

`SetTextModelParam` sets parameters of a text model. The list of
allowed parameter values for *`genParamName`* differs, depending on
which `mode` was set when creating the text model with
[`CreateTextModelReader`](create_text_model_reader.md).
In the following, first the parameter values for text models with
`mode` = *"auto"* are listed, and then those
for text models with `mode` = *"manual"*.

The name and value of a parameter must be given in `genParamName`
and `genParamValue`. The following values are possible:

- **Parameters of text models with Mode = 'auto'**

  - **Segmentation behavior**

    - ***"min_contrast"*:** —

      The minimal contrast the characters have to
      their surrounding background.

      Value range:
       integer or float value between *1* and *255* for
      byte images and between *1* and *65.535* for uint2 images.

      Default:
       *15*
    - ***"polarity"*:** —

      *"dark_on_light"* if the text to be
      segmented is darker than its background, *"light_on_dark"* if the
      text to be segmented is lighter than its background, and *"both"* if
      both kinds of text are to be segmented.

      List of values:
       *"dark_on_light"*, *"light_on_dark"*,
      *"both"*

      Default:
       *"both"*
    - ***"eliminate_border_blobs"*:** —

      *"true"* if regions that are
      touching the border of the image domain should be discarded, otherwise
      *"false"*.

      List of values:
       *"true"*, *"false"*

      Default:
       *"false"*
    - ***"add_fragments"*:** —

      *"true"* if fragments, such as the
      dot on the 'i', should be added to the segmented characters, otherwise
      *"false"*. Be aware, that this can cause noise to be added to the
      segmented characters.

      List of values:
       *"true"*, *"false"*

      Default:
       *"true"*
    - ***"separate_touching_chars"*:** —

      Controls the
      handling of pairs or small groups of neighboring characters
      that are segmented as one single region. When selecting *"standard"*
      or *"enhanced"*, such regions are detected and separated into
      two or more single characters. While the *"enhanced"* method yields
      more accurate results, the *"standard"* method is less complex and
      thus faster. If *"separate_touching_chars"* is set to
      *"false"*, no separation of touching characters is performed.

      Remark: If *"enhanced"* is selected, the file
      *find_text_support.hotc* from the ocr subdirectory of the root
      directory of the HALCON installation is needed. It is also possible to
      place this file in the current working directory.

      List of values:
       *"false"*, *"standard"*,
      *"enhanced"*

      Default:
       *"standard"*
  - **Character size**

    - ***"min_char_height"*:** —

      The minimal height of the characters in
      pixel. If text of arbitrary height is to be segmented, *"auto"*
      may be passed. Note that *"min_char_height"* refers to characters
      only. The height of punctuation marks or separators is not restricted by
      *"min_char_height"*.

      Default:
       *"auto"*

      Restriction:
       integer or float value greater or equal to *1*.
    - ***"max_char_height"*:** —

      The maximal height of the characters in
      pixel. If text of arbitrary height is to be segmented, *"auto"*
      may be passed. Note that *"max_char_height"* refers to characters
      only. The height of punctuation marks or separators is not restricted by
      *"max_char_height"*.

      Default:
       *"auto"*

      Restriction:
       integer or float value greater or equal to *1*.
    - ***"min_char_width"*:** —

      The minimal width of the characters in
      pixel. If text of arbitrary width is to be segmented, *"auto"* may
      be passed. Note that *"min_char_width"* refers to characters only.
      The width of punctuation marks or separators is not restricted by
      *"min_char_width"*.

      Default:
       *"auto"*

      Restriction:
       integer or float value greater or equal to *1*.
    - ***"max_char_width"*:** —

      The maximal width of the characters in
      pixel. If text of arbitrary width is to be segmented, *"auto"*
      may be passed. Note that *"max_char_width"* refers to characters
      only. The width of punctuation marks or separators is not restricted by
      *"max_char_width"*.

      Default:
       *"auto"*

      Restriction:
       integer or float value greater or equal to *1*.
    - ***"min_stroke_width"*:** —

      The minimal stroke width of the
      characters in pixel. If the minimal stroke width is to be estimated
      within the text segmentation process automatically, *"auto"* may
      be passed. Note that *"min_stroke_width"* refers to characters only.
      The stroke width of punctuation marks or separators is not restricted by
      *"min_stroke_width"*.

      Default:
       *"auto"*

      Restriction:
       integer or float value greater or equal to *1*.
    - ***"max_stroke_width"*:** —

      The maximal stroke width of the
      characters in pixel. If the maximal stroke width is to be estimated
      within the text segmentation process automatically, *"auto"* may
      be passed. Note that *"max_stroke_width"* refers to characters only.
      The stroke width of punctuation marks or separators is not restricted by
      *"max_stroke_width"*.

      Default:
       *"auto"*

      Restriction:
       integer or float value greater or equal to *1*.
  - **Special characters**

    - ***"return_punctuation"*:** —

      *"true"* if small punctuation
      marks that lie close to the base line of the corresponding text line
      (e.g., dots or commas) are to be returned. *"false"* if no such
      punctuations should be returned.

      List of values:
       *"true"*, *"false"*

      Default:
       *"true"*
    - ***"return_separators"*:** —

      *"true"* if separators such as
      a minus or the equality sign should be returned as well. *"false"*
      if no separators should be returned.

      List of values:
       *"true"*, *"false"*

      Default:
       *"true"*
  - **Handling of dot prints**

    - ***"dot_print"*:** —

      *"true"* if the text to be
      segmented contains dot printed characters, otherwise *"false"*.

      List of values:
       *"true"*, *"false"*

      Default:
       *"false"*
    - ***"dot_print_tight_char_spacing"*:** —

      *"true"* if the gap
      between adjacent characters is smaller than the largest gap between two
      dots within a single character, otherwise *"false"*.
      If *"dot_print"* is set to *"false"* this parameter
      does not have any effect.
      In cases where the minimal gap size between characters is exactly known,
      *"dot_print_min_char_gap"* can be set instead. In this case the
      value of *"dot_print_tight_char_spacing"* is ignored.

      List of values:
       *"true"*, *"false"*

      Default:
       *"false"*
    - ***"dot_print_min_char_gap"*:** —

      The minimal gap size between two
      characters in pixel.
      This parameter can be used to improve the text result in cases where
      the minimal gap size between characters is smaller than the maximal gap
      size between dots within characters. If the minimal character gap size is
      not known or is bigger than the maximal dot gap size, *"auto"* may
      be passed. If *"dot_print"* is set to *"false"* this
      parameter does not have any effect. In cases where the minimal gap size
      between characters is not known but the characters are printed close to
      each other, *"dot_print_tight_char_spacing"* might be used instead.

      ![figure](../assets/8ff9724bb7bc3b7d.svg)

      Here, the minimal gap size between characters is 8 pixel.

      Default:
       *"auto"*

      Restriction:
       integer or float value greater or equal to *0*.
    - ***"dot_print_max_dot_gap"*:** —

      The maximal gap size between two
      dots within a character in pixel. If arbitrary dot printed characters are
      to be segmented, *"auto"* may be passed.
      If *"dot_print"* is set to *"false"* this parameter
      does not have any effect. In cases where the maximal dot gap size is
      larger than or equal to the minimal gap size between characters,
      *"dot_print_tight_char_spacing"* or *"dot_print_min_char_gap"*
      should be set accordingly. Setting *"dot_print_max_dot_gap"* can
      reduce the runtime of [`FindText`](find_text.md) significantly.

      ![figure](../assets/c62c509b21816c4f.svg)

      Here, the maximal gap size between dots is 3 pixel.

      Default:
       *"auto"*

      Restriction:
       integer or float value greater or equal to *1*.
  - **Line structures**

    - ***"text_line_structure"*:** —

      To simplify the search for specific
      structures (e.g., dates or serial numbers) within the segmented text, it
      is possible to define text line structures. For each text line the
      distances between the characters are calculated, and based on these
      distances, the text line is divided into text blocks. Short characters
      such as '.', '_' and '-' are ignored in this process and treated as
      spaces. Furthermore, it is possible to define user specific separators
      which are also ignored. See the description of
      *"text_line_separators"* for details. It is then tested if any of
      the user defined text line structures fit the resulting text blocks.

      For example, if the text to be found is a date with two characters
      for month, day, and year the structure would be '2 2 2'. If the year may
      consist of two or four characters, the structure would be '2 2 2-4',
      indicating that the last character block consists of two to four
      characters. It is possible to provide more than one structure to match by
      appending an index to the parameter name, e.g.,
      *"text_line_structure_0"*, *"text_line_structure_1"*.
      If *"text_line_structure"* is set to an empty string *" "*,
      the text to be found may have any structure.

      Please observe, that every text line structure which is found, is
      saved as a unique text line within the text result. Hence, when calling
      [`GetTextObject`](get_text_object.md), a 'line' then refers to a valid text line
      structure. If the whole text line containing the text line structure is
      to be returned instead, it is possible to set *"return_whole_line"*
      accordingly.

      Default:
       *" "*
    - ***"text_line_separators"*:** —

      A string containing the list of
      characters which are to be ignored in the process of finding text line
      structures, see *"text_line_structure"* for further details.
      Please note, user specific separators need to be valid characters within
      the used OCR classifier.
      For example, if *":"* and
      *"\"* are to be ignored,
      *":\\"* should be
      passed.
      Please observe, that *"\"*
      escapes any special symbol to treat it as a literal, and hence
      *"\\"* needs to be
      passed to use *"\"* as a separator.

      Suggested values:
       *"/"*, *":"*,
      *":\\"*,
      *"\\/:"*

      Default:
       *" "*
    - ***"return_whole_line"*:** —

      *"false"* if only the segmented
      text line structures are to be returned as text lines. *"true"* if
      each whole text line containing a text line structure is to be returned
      in text lines.

      List of values:
       *"true"*, *"false"*

      Default:
       *"false"*
  - **OCR classifier**

    - ***"ocr_classifier"*:** —

      The OCR classifier used within
      [`FindText`](find_text.md) for text segmentation and classification. An initial
      classifier is set when the text model is created. See
      [`CreateTextModelReader`](create_text_model_reader.md) for more information about the required
      OCR Classifier.
    - ***"num_classes"*:** —

      The number of best classes to be stored
      for each character (e.g., if *"num_classes"* is set to 2,
      [`FindText`](find_text.md) returns the classification results with the highest
      and second highest confidence).
      If *"num_classes"* exceeds the number of classes of the
      classifier stored in the text model, *"num_classes"* is decreased
      accordingly. The actual number of classes can be queried by
      [`GetTextResult`](get_text_result.md). For classifiers with rejection class,
      *"num_classes"* should be at least 2 in order to be able
      to use the second best result if a character is classified as rejection
      class.

      Default:
       *2*

      Restriction:
       integer or float value greater or equal to *1*.
- **Parameters of text models with Mode = 'manual'**

  - ***"manual_char_height"*:** —

    Height of the characters in pixel.
    Refers to an uppercase character.

    Default:
     *30*
  - ***"manual_char_width"*:** —

    Width of the characters in pixel.
    Refers to an uppercase character.

    Default:
     *20*
  - ***"manual_stroke_width"*:** —

    Stroke width of the characters in
    pixel.

    Default:
     *4.0*
  - ***"manual_base_line_tolerance"*:** —

    Maximum base line deviation of
    the characters (in percent of *"manual_char_height"*).

    Default:
     *0.15*
  - ***"manual_polarity"*:** —

    *"dark_on_light"* if the text to be
    segmented is darker than its background, otherwise *"light_on_dark"*.

    Default:
     *"dark_on_light"*
  - ***"manual_uppercase_only"*:** —

    *"true"* if the text to be
    segmented contains uppercase characters or numbers only, otherwise
    *"false"*.

    Default:
     *"false"*
  - ***"manual_is_dotprint"*:** —

    *"true"* if the text to be
    segmented is a dotprint, otherwise *"false"*.

    Default:
     *"false"*
  - ***"manual_is_imprinted"*:** —

    *"true"* if the text to be
    segmented suffers of local changes of polarity due to reflections,
    otherwise *"false"*.
    Default:
     *"false"*
  - ***"manual_eliminate_horizontal_lines"*:** —

    *"true"* if there
    are longer horizontal structures close to the text to be segmented,
    otherwise *"false"*.
    Default:
     *"false"*
  - ***"manual_eliminate_border_blobs"*:** —

    *"true"* if regions
    that are touching the border of the image domain should be discarded,
    otherwise *"false"*.

    Default:
     *"false"*
  - ***"manual_max_line_num"*:** —

    Maximum number of lines to be found.
    Zero or negative values indicate no limitation. Setting
    *"manual_max_line_num"* to a low value may strongly improve the
    runtime of [`FindText`](find_text.md).

    Default:
     no limitation
  - ***"manual_return_punctuation"*:** —

    *"true"* if punctuation
    marks (e.g., dots or comma) should be added to the segmented characters.

    Default:
     *"true"*
  - ***"manual_return_separators"*:** —

    *"true"* if separators such
    as a minus or the equality sign should be added to the segmented characters.

    Default:
     *"true"*
  - ***"manual_add_fragments"*:** —

    *"true"* if fragments, such as
    the dot on the 'i', should be added to the segmented characters. Be aware,
    that this can cause noise to be added to the segmented characters.

    Default:
     *"true"*
  - ***"manual_fragment_size_min"*:** —

    minimum area of fragment regions
    that are added if *"manual_add_fragments"* is set to *"true"*.

    Default:
     *1*
  - ***"manual_text_line_structure"*:** —

    specifies the structure of the
    text to be found to reduce the search space and to avoid false positives.
    The structure is a string that contains the number of characters for every
    character block and spaces between these character blocks. For example, if
    the text to be found is a date with two characters for month, day, and year
    the structure would be '2 2 2'. If the year may also consist of four
    characters the structure would be '2 2 2-4', indicating that the last
    character block consists of two to four characters.
    It is possible to provide more than one structure to match by appending an
    index to the parameter name, e.g., *"manual_text_line_structure_0"*,
    *"manual_text_line_structure_1"*.
    If *"manual_text_line_structure"* is set to an empty string ' ', the
    text to be found may have any structure.

    Default:
     *" "*
  - ***"manual_persistence"*:** —

    *"true"* if selected intermediate
    results should be kept with the output result of [`FindText`](find_text.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- textModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`textModel`** (input_control, state is modified)  text_model `→` [HTextModel](HTextModel.md), [HTuple](HTuple.md) (*IntPtr*)

Text model.

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the parameters to be set.

Default:
"min_contrast"

Suggested values:
"add_fragments", "dot_print", "dot_print_max_dot_gap", "dot_print_min_char_gap", "dot_print_tight_char_spacing", "eliminate_border_blobs", "max_char_height", "max_char_width", "max_stroke_width", "min_char_height", "min_char_width", "min_contrast", "min_stroke_width", "num_classes", "ocr_classifier", "polarity", "return_punctuation", "return_separators", "return_whole_line", "separate_touching_chars", "text_line_separators", "text_line_structure", "text_line_structure_0", "text_line_structure_1", "text_line_structure_2", "manual_add_fragments", "manual_base_line_tolerance", "manual_char_height", "manual_char_width", "manual_eliminate_border_blobs", "manual_eliminate_horizontal_lines", "manual_fragment_size_min", "manual_is_dotprint", "manual_is_imprinted", "manual_max_line_num", "manual_persistence", "manual_polarity", "manual_return_punctuation", "manual_return_separators", "manual_stroke_width", "manual_text_line_structure", "manual_text_line_structure_0", "manual_text_line_structure_1", "manual_text_line_structure_2", "manual_uppercase_only"

**`genParamValue`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Values of the parameters to be set.

Default:
10

Suggested values:
"true", "false", "dark_on_light", "light_on_dark", "both", "auto", "standard", "enhanced"

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

If the input parameters are set correctly, the operator
`SetTextModelParam` returns the value 2 (
H_MSG_TRUE)
. Otherwise, an
exception will be raised.

## Possible Predecessors

`CreateTextModelReader`

## Possible Successors

`FindText`

## See also

`GetTextModelParam`

## Module

OCR/OCV
