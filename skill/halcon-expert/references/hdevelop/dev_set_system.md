# dev_set_system (Operator)

## Name

`dev_set_system` — Change HDevelop system parameter within a program.

## Signature

`dev_set_system( : : SystemParameter, Value : )`

## Description

The operator `dev_set_system` sets HDevelop system parameters.

Available options for *`SystemParameter`*:

- ***'jit_enabled'*:** —

  Determines whether the JIT Compiler is enabled (*'true'*) or not
  (*'false'*).

  Note, not all procedures can be JIT compiled.

  List of values:
   *'true'*, *'false'*

  Default:
   *'false'*
- ***'all'*:** —

  Reset all system parameters to their default value.
  To do so, set *`Value`* to *'default'*.

  List of values:
   *'default'*

## Attention

This operator is not supported for code export.

## Parameters

**`SystemParameter`** (input_control)  attribute.name `→`  (string)

Name of the system parameter to be changed.

Default:
'jit_enabled'

List of values:
'all', 'jit_enabled'

**`Value`** (input_control)  attribute.value `→`  (integer / string)

New value of the system parameter.

Default:
'false'

List of values:
'default', 'false', 'true'

## Module

Foundation
