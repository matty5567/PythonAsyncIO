<h1> Python Async </h1>

Aysc IO is a concurrent programming design that has dedicated support in Python (3.7 onwards) in the form of the <b>acyncio</b> package.

<br>

<h2>What does it mean to be asynchronous?</h2>

    - Asynchronous routines are able to "pause" while waiting on their ultimate result and let other routines run in the meantime
    - Asynchronous code, through the mechanism above, facilitates concurrent execution.

<br>

<h2>Synchronous vs Asynchronous:</h2>

Imagine one chess grandmaster playing 24 ametuers, the <b>synchronous</b> version would be the grandmaster playing each game in full one at a time, whilst the <b>asynchronous</b> version would involve the grandmaster moving from table to table playing all players at once. 

In programming, Async IO takes long waiting periods in which functions would be blocking and allows other functions to run during that downtime.

<br>

<h2>The async/ await Syntac and Native Coroutines</h2>

A <b>coroutine</b> is just a specialised version of a Python generator function, which means you can suspend its execution before reaching return and it can indirectly pass control to another coroutine for some time. 

<br>

<h2>The Rules of Async IO</h2>

The syntax <b>async def</b> introduces either a native coroutine or an asynchronous generator. <b> aysnc with </b> and <b>async for</b> are also valid.

The keyword <b>await</b> suspends execution of the surrounding coroutine and passes control back to the event loop. If python encounters an await f() inside g(), this tells python to suspend exection of g() and let something else run until f() is returned.

Whe using await f(), its required that f() is awaitable:
    - another coroutine
    - has defined an `.__await__()` dunder method

<h2>Async IO Design Patterns</h2>

---

<h3>Chaining Coroutines<h4>

A key feature of corourines is that they can be chained together, this allows you to break coroutines into smaller, manageable, recyclable coroutines.

See <b>examples/chaining_coroutines.py</b> for a code example.

<br>

<h3>Using a Queue<h4>

A number of producers, which are not associated with each other, add items to a queue, at random, unannounced times. A group of consumers pull items from the queue as they show up, greedily and without waiting for any other signal.

The Queue serves as a throughput that can communicate with the producers and consumers without them talking to each other directly.


