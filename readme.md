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
