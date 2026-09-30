# dev_get_preferences (Operator)

## Name

`dev_get_preferences` — Query HDevelop preferences within a program.

## Signature

`dev_get_preferences( : : PreferenceNames : PreferenceValues)`

## Description

`dev_get_preferences` allows to query selected preferences of
HDevelop within a program.
Until now, the following preferences are supported:

- ***'graphics_window_context_menu'*:** —

  Returns whether a right click into the graphics window opens a context
  menu or not.
  By default the context menu is enabled.
- ***'graphics_window_mouse_wheel'*:** —

  Returns whether the mouse wheel can be used to zoom the contents of
  the graphics window or not.
  By default the moue wheel is enabled.
- ***'graphics_window_tool_tip'*:** —

  Returns whether pressing the Ctrl key over the graphics window shows
  a tool tip with the current pixel position and the gray
  values under the mouse cursor or not.
  By default the tool tip is enabled.
- ***'suppress_handled_exceptions_dlg'*:** —

  Returns whether the error dialog is suppressed that is by
  default opened for exceptions that are thrown during program
  execution and that are enclosed by a [`try`](try.md)-[`catch`](catch.md) block
  and can therefore be handled by an exception handler.
  This option is persistently stored in the HDevelop.ini file and
  can be configured via the Preferences dialog / General Options /
  Experienced User.

## Attention

This operator is not supported for code export.

## Parameters

**`PreferenceNames`** (input_control)  attribute.name-array `→`  (string)

Selection of the preferences.

Default:
'graphics_window_context_menu'

List of values:
'graphics_window_context_menu', 'graphics_window_mouse_wheel', 'graphics_window_tool_tip', 'suppress_handled_exception_dlg'

**`PreferenceValues`** (output_control)  attribute.value-array `→`  (string)

Values of the selected preferences.

## See also

`dev_set_preferences`

## Module

Foundation
