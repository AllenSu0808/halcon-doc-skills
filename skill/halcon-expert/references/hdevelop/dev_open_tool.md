# dev_open_tool (Operator)

## Name

`dev_open_tool` — Open a HDevelop tool, a non-modal dialog, or assistant.

## Signature

`dev_open_tool( : : ToolName, Row, Column, Width, Height, GenParamName, GenParamValue : ToolId)`

## Description

`dev_open_tool` opens a HDevelop tool, a non-modal dialog, or
assistant. The parameter *`ToolName`* contains the name of the tool
to be opened.
This operator returns the *`ToolId`* of the newly created tool, which
can be used by operators like [`dev_set_tool_geometry`](dev_set_tool_geometry.md),
[`dev_show_tool`](dev_show_tool.md), [`dev_close_tool`](dev_close_tool.md) to address a specific tool.
The opened tool automatically becomes active.

The tool is closed by pressing the `Close` button of the
window frame, or by calling [`dev_close_tool`](dev_close_tool.md).

The parameters *`GenParamName`* and *`GenParamValue`* are optional.
For certain *`ToolName`* they can be used to specify which page is
displayed and more, see below.
If they are set to *[]* the tool opens with default settings.

Following the supported tools are listed, whereby they are sorted
thematically.

Concerning the **Main Windows** supported values for *`ToolName`*:

- *'graphics_window'*: Graphics Window
- *'operator_window'*: Operator Window
- *'program_window'*: Program Window
- *'variable_window'*: Variable Window

Concerning the **Assistants** supported *`ToolName`*:

- *'calibration_assistant'*: Camera Calibration Assistant

  Supported values for *`GenParamName`*:

  - *'page'*: Page to be displayed.
    Supported values for *`GenParamValue`*:

    - *'setup'*: Setup
    - *'calibration'*: Calibration
    - *'result'*: Results
    - *'code_generation'*: Code Generation

    *Example:*
    `dev_open_tool('calibration_assistant', ..., 'page', 'result', ...)`
    opens the calibration assistant and shows the tab card `Results`.
- *'image_acquisition_assistant'*: Image Acquisition Assistant

  Supported values for *`GenParamName`*:

  - *'page'*: Page to be displayed.
    Supported values for *`GenParamValue`*:

    - *'source'*: Source
    - *'connection'*: Connection
    - *'parameters'*: Parameters
    - *'code_generation'*: Code Generation

    *Example:*
    `dev_open_tool('image_acquisition', ...,'page', 'source', ...)`
    opens the image acquisition assistant and shows the tab card
    `Source`.
- *'matching_assistant'*: Matching Assistant

  Supported values for *`GenParamName`*:

  - *'page'*: Page to be displayed.
    Supported values for *`GenParamValue`*:

    - *'model_creation'*: Model Creation
    - *'model_parameter'*: Model Parameter
    - *'model_use'*: Model Use
    - *'inspect'*: Inspect
    - *'code_generation'* & Code Generation

    *Example:*
    `dev_open_tool('matching_assistant', ...,'page', 'inspect', ...)`
    opens the matching assistant and shows the tab card `Inspect`.
- *'measure1d_assistant'*: Measure Assistant

  Supported values for *`GenParamName`*:

  - *'page'*: Page to be displayed.
    Supported values for *`GenParamValue`*:

    - *'input'*: Input
    - *'edges'*: Edges
    - *'fuzzy'*: Fuzzy
    - *'result'*: Results
    - *'code_generation'*& Code Generation

    *Example:*
    `dev_open_tool('measure1d_assistant', ..., 'page', 'edges', ...)`
    opens the measure assistant and shows the tab card `Edges`.
- *'ocr_assistant'*: OCR Assistant

Concerning the **Tools** supported values for *`ToolName`*:

- *'call_stack'*: Call Stack
- *'canvas'*: Canvas Window
- *'feature_histogram'*: Feature Histogram
- *'feature_inspection'*: Feature Inspection
- *'gray_histogram'*: Gray Histogram
- *'line_profile'*: Line Profile
- *'zoom_window'*: Zoom Window
- *'ocr_training_file_browser'*: OCR Training File Browser

Concerning the **Dialogs** supported values for *`ToolName`*:

- *'browse_examples_dialog'*: Browse Examples Dialog
- *'create_procedure_dialog'*: Create Procedure Dialog
- *'edit_procedure_interface_dialog'*: Edit Procedure Interface Dialog
- *'find_replace_dialog'*: Find Replace Dialog
- *'output_console'*: Output Console
- *'quick_navigation'*: Quick Navigation

  Supported values for *`GenParamName`*:

  - *'page'*: Page to be displayed.
    Supported values for *`GenParamValue`*:

    - *'invalid_lines'*: Invalid Lines
    - *'find_results'*: Find Results
    - *'breakpoints'*: Breakpoints
    - *'bookmarks'*: Bookmarks

    *Example:*
    `dev_open_tool('quick_navigation', ..., 'page', 'breakpoints', ...)`
    opens the quick navigation window and shows the tab card
    `Breakpoints`.
- *'breakpoints_dialog'*: Quick Navigation / Breakpoints
- *'bookmarks_dialog'*: Quick Navigation / Bookmarks
- *'invalid_lines_dialog'*: Quick Navigation / Invalid Lines
- *'visualization_parameters_dialog'*: Visualization Parameters Dialog
- *'help'*: Help Browser

  Supported values for *`GenParamName`*:

  - *'page'*: Page to be displayed.
    Supported values for *`GenParamValue`*:

    - *'contents'*: Contents
    - *'operator'*: Operator
    - *'search'*: Search
    - *'index'*: Index
    - *'bookmarks'*: Bookmarks

    *Example:*
    `dev_open_tool('help', ..., 'page', 'search', ...)`
    opens the help tool and selects the tab card `Search`.
  - *'operator'*: Operator whose HTML page should be displayed.

    Supported values for *`GenParamValue`*: Operator names
    (written in snake case).

    *Example:*
    `dev_open_tool('help', ...,['page','operator'], ['search','read_image'], ...)`
    opens the help tool, selects the tab card `Search` and displays
    the description of the operator [`read_image`](read_image.md).
  - *'manual'*:
    Manual whose HTML page should be displayed.

    Supported values for *`GenParamValue`*: Manual names
    (including their path, both written in snake case).

    *Example:*
    `dev_open_tool('help', 'default', 'default', 'default', 'default', 'manual', 'hdevelop_users_guide/hdevelop_users_guide_0000', ToolId)`
    opens the manual `“HDevelop User's Guide”`.
- *'preferences'*: Preferences Dialog

  Supported values for *`GenParamName`*:

  - *'page'*: Page to be displayed.
    Supported values for *`GenParamValue`* are listed in groups of menu
    items.

    For the menu `User Interface` supported values for
    *`GenParamValue`*:

    - *'user_interface/program_window'*: Program Window
    - *'user_interface/fonts'*: Fonts
    - *'user_interface/language'*: Language
    - *'user_interface/themes'*: Themes

    For the menu `Procedures` supported values for
    *`GenParamValue`*:

    - *'procedures/directories'*: Directories
    - *'procedures/external_procedures'*: External Procedures
    - *'procedures/manage_procedure_libraries'*: Manage Procedure
      Libraries
    - *'procedures/manage_passwords'*: Manage Passwords
    - *'procedures/procedure_use'*: Procedure Use
    - *'procedures/unresolved_procedure_calls'*: Unresolved
      Procedure Calls

    For the menu `General Options` supported values for
    *`GenParamValue`*:

    - *'general_options/general_options'*: General Options
    - *'general_options/experienced_user'*: Experienced User

    For the menu `Visualization Settings`, supported values for
    *`GenParamValue`*:

    - *'visualization_settings/pen'*: Pen
    - *'visualization_settings/lut'*: LUT
    - *'visualization_settings/paint'*: Paint

    For the menu `Runtime Settings` supported values for
    *`GenParamValue`*:

    - *'runtime_settings/runtime_settings'*: Runtime Settings
    - *'runtime_settings/override_operator_behavior'*:
      Override Operator Behavior

    For the menu `Telemetry Settings` supported values for
    *`GenParamValue`*:

    - *'telemetry_settings'*: Telemetry Settings

    *Example:*
    `dev_open_tool('preferences', ..., 'page', 'user_interface/language', ...)`
    shows the page `language` from the group `User Interface`.
- *'halcon_news'*: HALCON News website - an empty *`ToolId`*
  is returned because this simply opens the news page.

The parameters *`Row`* and *`Column`* can be used to open the
tool at a specific position. Note that the offset values specified under
`Edit` ->
`Preferences` ->
`General Options` ->
`General Options` ->
`Window open offset`
are added to the row and the column index, respectively.
For more information, see the chapter
“Menu `Edit`” in the `“HDevelop User's Guide”`.
In order to apply the standard behavior, that is in general opening the tool
at the last position, *'default'* can be passed.

The parameters *`Width`* and *`Height`* can be used to open the
tool with a specific size. In order to apply the standard behavior, that
is in general opening the tool with the last size, *'default'* can
be passed. If *`Width`* and *`Height`* are less than the
minimum size of the tool the minimum size is used.

## Attention

This operator is not supported for code export.

## Parameters

**`ToolName`** (input_control)  string `→`  (string)

Name of the tool to be opened and additional
parameters.

List of values:
'bookmarks_dialog', 'breakpoints_dialog', 'browse_examples_dialog', 'calibration_assistant', 'call_stack', 'canvas', 'create_procedure_dialog', 'edit_procedure_interface_dialog', 'feature_histogram', 'feature_inspection', 'find_replace_dialog', 'graphics_window', 'gray_histogram', 'halcon_news', 'help', 'image_acquisition_assistant', 'invalid_lines_dialog', 'line_profile', 'matching_assistant', 'measure1d_assistant', 'ocr_assistant', 'ocr_training_file_browser', 'operator_window', 'output_console', 'preferences', 'program_window', 'quick_navigation', 'variable_window', 'visualization_parameters_dialog', 'zoom_window'

**`Row`** (input_control)  rectangle.origin.y `→`  (integer / string)

Row index of upper left corner.

Default:
'default'

Minimum increment:
1

Recommended increment:
1

**`Column`** (input_control)  rectangle.origin.x `→`  (integer / string)

Column index of upper left corner.

Default:
'default'

Minimum increment:
1

Recommended increment:
1

**`Width`** (input_control)  rectangle.extent.x `→`  (integer / string)

Width of the tool.

Default:
'default'

Minimum increment:
1

Recommended increment:
1

Restriction:
`Width > 0`

**`Height`** (input_control)  rectangle.extent.y `→`  (integer / string)

Height of the tool.

Default:
'default'

Minimum increment:
1

Recommended increment:
1

Restriction:
`Height > 0`

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Names of the generic parameters.

Default:
[]

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string)

Values of the generic parameters.

Default:
[]

**`ToolId`** (output_control)  dev_tool `→`  (string)

Tool identifier.

## Example (HDevelop)

```
dev_open_tool ('zoom_window',0, 0, Width, Height, [], [], ToolId)
dev_close_tool (ToolId)
```

## Result

If the values of the specified parameters are correct,
`dev_open_tool` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Successors

`dev_set_tool_geometry`,
`dev_show_tool`,
`dev_close_tool`

## Module

Foundation
