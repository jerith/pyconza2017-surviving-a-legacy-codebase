<!--@exec sectitle("Act 2", "Tools and techniques")-->

$$$

### First, some tools

<div>
##### Static analysis
* flake8
* pylint
</div> <!--@exec frag()-->

<div>
##### Automated refactoring
* PyCharm
* Rope
</div> <!--@exec frag()-->

<div>
##### The human brain
</div> <!--@exec frag()-->

$$$

### Seams

<br/>

"A seam is a place where you can alter behavior in your program without editing in that place." <!--@exec frag()-->

<br/>

<div>
* imported modules
* function calls
* method calls
</div> <!--@exec frag()-->

$$$

### Exploiting seams

<br/>

Install a fake library <!--@exec frag()-->

<br/>

Monkey-patch <!--@exec frag()-->

<br/>

Subclass and override <!--@exec frag()-->

$$$NOTES

fake-plastic-pycrypto

$$$

### Breaking dependencies

Test doubles! <!--@exec frag()-->

...but how do we get them in there? <!--@exec frag()-->

<br/>

* Use seams <!--@exec frag()-->
* Encapsulate global references <!--@exec frag()-->
* Break up long functions <!--@exec frag()-->
* Add parameters <!--@exec frag()-->


$$$NOTES

Usually have to do this without tests.

$$$

#### Breaking a dependency with a seam

```pythonhl
<!-- @include code/breaking_dependencies/seams_tasks.py -->
```

We could extract `getSession()` as we did before...

...by making nontrivial changes to untested code. :-( <!--@exec frag()-->

$$$

#### Breaking a dependency with a seam

<br/>

Instead, we monkey-patch in our own `getSession()`.

<br/>

```pythonhl
<!-- @include code/breaking_dependencies/seams_test.py -->
```

<br/>

It's ugly, but we know we didn't break anything. :-) <!--@exec frag()-->

$$$

#### Encapsulating a global dependency

Instead of using `reactor` directly, put it in an attribute...

```pythonhl
<!-- @include code/breaking_dependencies/encapsulation.py -->
```

...then override that attribute in the test.

```pythonhl
<!-- @include code/breaking_dependencies/encapsulation_test.py -->
```

$$$

<!-- .slide: class="lessspaced" -->

### Changing untested code

Separate new code from old. <!--@exec frag()-->

<div>
##### Pros:
* New code can be tested in isolation
* Changes to old code are restricted
</div> <!--@exec frag()-->

<div>
##### Cons:
* Spaghetti with meatballs
* Old code doesn't improve
</div> <!--@exec frag()-->

<br/>

Use with care, clean up later. <!--@exec frag("vhc")-->

$$$

<!-- .slide: class="morespaced" -->

### The legacy code algorithm

1. Identify code that needs to change

2. Break dependencies

3. Write tests

4. Make changes

5. Refactor (where possible)

$$$

### Read this book

![Working Effectively With Legacy Code](images/working-effectively-with-legacy-code.jpg)
<!--{_width="40%"}-->
