# dev_get_system (Operator)

## Name

`dev_get_system` — Query the HDevelop system within a program.

## Signature

`dev_get_system( : : SystemQueries : SystemInformations)`

## Description

The operator `dev_get_system` returns information concerning the
HDevelop system parameters.

**Read-Only Parameters**

The following system parameters can be queried:

- ***'call_stack'*:** —

  Returns the call stack, that is the procedure names and lines of the calls.
  See also “Thread View / Call Stack” in the
  [HDevelop User's Guide.](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_gui_0000.html)

  Attention:
   This option only works when executing without JIT compilation.
- ***'engine_environment'*:** —

  Returns *'HDevelop'* if it is called within HDevelop, else
  *'HDevEngine'*.
- ***'jit_enabled'*:** —

  Returns *'true'* if the JIT Compiler is enabled, *'false'* otherwise.
  Not all procedures can be JIT compiled.

## Attention

This operator is not supported for code export.

## Parameters

**`SystemQueries`** (input_control)  attribute.name-array `→`  (string)

Desired system parameters.

Default:
'engine_environment'

List of values:
'call_stack', 'engine_environment', 'jit_enabled'

**`SystemInformations`** (output_control)  attribute.value-array `→`  (string)

Current value of the system parameters.

## Module

Foundation
