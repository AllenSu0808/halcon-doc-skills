# dev_set_preferences (Operator)

## Name

`dev_set_preferences` — Set HDevelop preferences within a program.

## Signature

`dev_set_preferences( : : PreferenceNames, PreferenceValues : )`

## Description

`dev_set_preferences` allows to set selected preferences of
HDevelop within a program.
The following preferences are supported:

- ***'graphics_window_context_menu'*:** —

  Controls whether a right click into the graphics window opens a context
  menu or not.
  By default the context menu is enabled.
  Disabling the context menu may be sensible if the right mouse button is
  used for controlling some kind of navigation in the graphics window,
  e.g., for moving or zooming 3D objects.

  List of values:
   *'false'*, *'true'*.

  Default:
   *'true'*.
- ***'graphics_window_mouse_wheel'*:** —

  Controls whether the mouse wheel can be used to zoom the contents of
  the graphics window or not.
  By default the mouse wheel is enabled.
  Disabling the mouse wheel may be sensible if 3D objects are displayed
  and if the zooming into the objects is realized interactively with the
  help of 3D display operators.

  List of values:
   *'false'*, *'true'*.

  Default:
   *'true'*.
- ***'graphics_window_tool_tip'*:** —

  Controls whether pressing the Ctrl key over the graphics window shows
  a tool tip with the current pixel position and the gray
  values under the mouse cursor or not.
  By default the tool tip is enabled.
  Disabling the tool tip may be sensible if the state of the Ctrl key shall
  be evaluated for program based user interactions, e.g., for manipulating
  the view on 3D objects.

  List of values:
   *'false'*, *'true'*.

  Default:
   *'true'*.
- ***'suppress_handled_exceptions_dlg'*:** —

  Controls whether the error dialog should be suppressed that is by
  default opened for exceptions that are thrown during program
  execution and that are enclosed by a [`try`](try.md)-[`catch`](catch.md) block
  and can therefore be handled by an exception handler.
  This option is persistently stored into the HDevelop.ini file and can
  also be configured via the Preferences dialog / General Options /
  Experienced User.
  If an exception is thrown by a program line that is not enclosed
  by a [`try`](try.md)-[`catch`](catch.md) block, an error message dialog is
  always opened.

  List of values:
   *'false'*, *'true'*.

  Default:
   *'false'* (Any changes are persistently saved).

## Attention

This operator is not supported for code export.

## Parameters

**`PreferenceNames`** (input_control)  attribute.name-array `→`  (string)

Selection of the preferences.

Default:
'graphics_window_context_menu'

List of values:
'graphics_window_context_menu', 'graphics_window_mouse_wheel', 'graphics_window_tool_tip', 'suppress_handled_exception_dlg'

**`PreferenceValues`** (input_control)  attribute.value-array `→`  (string)

New values for the selected preferences.

Default:
'false'

List of values:
'false', 'true'

## See also

`dev_get_preferences`

## Module

Foundation
