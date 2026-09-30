# ControlIoInterface (Operator)

## Name

`ControlIoInterface` — Perform an action on the I/O interface.

## Signature

`static void HOperatorSet.ControlIoInterface(HTuple IOInterfaceName, HTuple action, HTuple argument, out HTuple result)`

`static HTuple HIODevice.ControlIoInterface(string IOInterfaceName, string action, HTuple argument)`

`static HTuple HIODevice.ControlIoInterface(string IOInterfaceName, string action, string argument)`

## Description

`ControlIoInterface` performs an action on the I/O
interface. The supported parameters are interface-specific and
listed in the corresponding documentation of the used I/O interface
that can be found in the directory `doc/html/reference/io`.

The special value *"keep_open"* for *`action`* is used to
control when the interface should be unloaded. If *`argument`* is set
to *"true"*, the interface will remain loaded until the HALCON
process is terminated. If it is set to *"false"*, the interface will
be unloaded as soon as all its device instances are closed. This is the
default behavior.

## Attention

On Windows Systems, error dialog boxes from the operating system can occur
when dependency modules of the interface are not found, e.g., the according
SDK was not installed. The occurrence of the error boxes can be controlled by
setting Windows' Error Mode. Please refer to the description of SetErrorMode
within the Windows MSDN documentation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`IOInterfaceName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

HALCON I/O interface name.

Default:
[]

Suggested values:
"ADLINK-DAQPilot", "ADLINK-EOS", "Advantech", "Contec", "Hilscher-cifX", "Interface", "Linux-GPIO", "NIDAQmx", "OPC_Classic", "OPC_UA"

**`action`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the action to perform.

**`argument`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

List of arguments for the action.

Default:
[]

**`result`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long / double)

List of results returned by the action.

## Result

If the parameters are valid, the operator `ControlIoInterface`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised. In this
case an extended error information may be set and can be queried with
the operator [`GetExtendedErrorInfo`](get_extended_error_info.md).

## See also

`QueryIoInterface`

## Module

Foundation
