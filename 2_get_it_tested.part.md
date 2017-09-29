<!--@exec sectitle("Act 1", "Get it tested")-->

$$$

### Write some tests

<br/>

<div>
<div>
All done, let's go home.

![Unicorn kitten victory](images/pink-cat-with-unicorn-horn.png)
<!--{_width="20%"}-->
</div> <!--@exec ifrag("strike")-->
</div> <!--@exec frag()-->

<br/>
<br/>

### If only it were that easy. <!--@exec frag()-->

$$$

<!-- .slide: class="morespaced" -->

### Why is it not that easy?

<div>

It just wasn't written to be testable.

* Spaghetti

* Giant functions

* Global mutable state

* Tightly coupled dependencies

</div> <!--@exec frag()-->

$$$

### It gets worse over time

<br/>

Changing legacy code is scary.

<br/>

It doesn't get refactored. <!--@exec frag()-->

<br/>

Things get hacked in. <!--@exec frag()-->

$$$

### All is not lost!

<br/>

We can make legacy code testable.

<br/>

Very carefully. <!--@exec frag()-->

<br/>

With limited, controlled changes. <!--@exec frag()-->

$$$

#### Small example: `create_vm`

I want to modify this celery task...
```python
<!-- @include code/example_create_vm/before.py -->
```

<br/>

<div>
...but it creates a remote XenServer API session.
```python
<!-- @include code/example_create_vm/getSession.py -->
```

</div> <!--@exec frag()-->

$$$

#### Small example: `create_vm`

Factor out everything that uses the session...
```pythonhl
<!-- @include code/example_create_vm/after.py -->
```

<div>
...build a test double for the session object...
```python
<!-- @include code/example_create_vm/FakeXenServer.py -->
```

</div> <!--@exec frag()-->

...and then write some tests. <!--@exec frag()-->

$$$

<!-- .slide: class="morespaced" -->

#### Things to note

We made one small change to the legacy code. <!--@exec frag()-->

We did not change the behaviour of the legacy code. <!--@exec frag()-->

<span>We did not change the signature of `create_vm`.</span> <!--@exec frag()-->

We built a test double that will be useful elsewhere. <!--@exec frag()-->

We can now start making safe, tested changes. <!--@exec frag("vhc")-->

$$$

<!-- .slide: class="lessspaced" -->

### Testing legacy code

##### Focus on the task at hand <!--@exec frag()-->

* Only test the relevant code <!--@exec frag()-->

* Hacks are okay <!--@exec frag()-->

##### Write investigative tests <!--@exec frag()-->

* "What does it do if I give it this input?" <!--@exec frag()-->

* Copy "expected" values from actual output <!--@exec frag()-->
