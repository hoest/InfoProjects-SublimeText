# InfoProjects Sublime Text package

## Installatie
Als je "[Package Control](https://sublime.wbond.net/)" hebt geïnstalleerd
in SublimeText en je wilt handigheidjes voor InfoProjects, doe dan het
volgende:

`CTRL+SHIFT+P` => `pcaddrepo` => 'Package Control: Add repository' => `<ENTER>`

Plak in het invoer-veld deze URL:

```
https://github.com/hoest/InfoProjects-SublimeText.git
```

Installeer na het uitvoeren van deze actie het pakket
"InfoProjects SublimeText" via de normale wijze.

## Inhoud van het pakket
Dit pakket bevat wat handigheidjes voor bij InfoProjects i.c.m. het werken
in Sublime Text.

### Build plugin

Met behulp van `CTRL+WINDOWS+B` krijg je toegang tot de normale `Invoke-Build.ps1`
manier die je normaliter vanuit PowerShell uitvoert. Via het invoer-veld dat
gepresenteerd wordt, kun je de build-taak invoeren.

Bijvoorbeeld, wanneer je `less,coffee` invoert, zal deze taak uitgevoerd worden:

```
powershell -NoLogo -NoProfile Invoke-Build.ps1 less,coffee
```

Wanneer je het invoer-veld leeg laat, zal de standaard build-taak `all` uitgevoerd
worden.

Vereiste voor dit alles, is dat je de GIT-repository `powershell` en `tools`
naast elkaar hebt staan, bijvoorbeeld:

```
C:\utils\powershell
C:\utils\tools
```

Daarnaast moet je de map `C:\utils\powershell\scripts\` in je PATH variabele
toevoegen, zodat scripts direct aan te roepen zijn vanuit je PowerShell. Ook moet
`git` aan te roepen zijn vanuit PowerShell.

Of je kunt onderstaande opnemen in je `$PROFILE`:

```
Set-Content Env:Path "$Env:Path;$(gc 'env:ProgramFiles(x86)')\git\bin;C:\development\intern\powershell\scripts\"
```

Met behulp van `ALT+WINDOWS+B` je hele ontwikkel-omgeving builden en deployen,
het script `Invoke-BuildDevelop.ps1 -k` wordt dan namelijk uitgevoerd.
Met dit commando is geen invoer noodzakelijk.

Overigens kun je met behulp van `CTRL+ALT+WINDOWS+B` je hele ontwikkel-omgeving
schoon optuigen, het script `Invoke-BuildDevelop.ps1` wordt dan namelijk uitgevoerd.

Wanneer je bijvoorbeeld [PoshGIT](http://dahlbyk.github.io/posh-git/) hebt geïnstalleerd,
kun je met behulp van de setting `auto_pull_tools` op `true` het argument `-p` er bij krijgen,
waardoor je `tools` eerst even geüpdatet worden.

### Syntax highlight

IPROX.log bestanden worden met kleurtjes getoond.

### XML snippets

`prop` zorgt voor onderstaande stukje code:

```xml
<prop name="${1:name}" value="${2:value}" />
```

Wanneer je bijvoorbeeld [PoshGIT](http://dahlbyk.github.io/posh-git/) hebt geïnstalleerd,
kun je met behulp van de setting `auto_pull_tools` op `true` het argument `-p` er bij krijgen,
waardoor je `tools` eerst even geüpdatet worden.

### XSLT snippets

`tcom` zorgt voor onderstaande stukje code:

```xsl
<!--
  ///////////////////////////////////////////////////////////////////////////
  ${1:omschrijving}
  ///////////////////////////////////////////////////////////////////////////
-->
```

### CoffeeScript snippets

`init` zorgt voor onderstaande stukje code:

```coffee
"use strict"
$ = @jQuery

###
${1:comment}
###
${2:code}
```
