  # CMPS 6610 Problem Set 01
## Answers

**Name:** Muhammad Suhaib Rashid


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

  - 1b )    **Yes**
 
**Why:**
Using the limit comparison test:
$$
\lim_{n \to \infty} \frac{2^{n+1}}{2^n} = 
\lim_{n \to \infty} \frac{2 \cdot 2^n}{2^n} = \lim_{n \to \infty} 2 = 2
$$
 
The limit is a finite constant, so $2^{n+1} \in O(2^n)$ 

**By definition:**  $f(n) \in O(g(n))$ if there exist constants $c > 0$ and $n_0 \geq 0$ such that $f(n) \leq c\cdot g(n)$ for all $n \geq n_0$.
 
Since $2^{n+1} = 2\cdot 2^n$ 
choosing $c = 2$ and $n_0 = 0$. 
Then for all $n \geq 0$:
$$
 2\cdot 2^n \leq 2\cdot 2^n
$$
So the definition is satisfied. Hence $2^{n+1} \in O(2^n)$
  - 1c ) **No.**

 
**Why:**
$$
\lim_{n \to \infty} \frac{2^{2^n}}{2^n} = \lim_{n \to \infty} 2^{2^n - n}
$$
 
Since $2^n$ grows exponentially and $n$ grows only linearly, $2^n - n \to \infty$ as $n \to \infty$. 
Therefore:
 
$$
\lim_{n \to \infty} 2^{2^n - n} = \infty
$$
 
so, $2^{2^n} \notin O(2^n)$.
 
  - 1d ) **No.**
 
**Why:**
$$
\lim_{n \to \infty} \frac{n^{1.01}}{\log^2 n}
$$
 
Substitute $n = 2^a$ 
By taking log on both sides 
$$\log n = a$$$$\log^2 n = a^2$$and 
$$n^{1.01} = 2^{1.01a}$$
So limit becomes:
$$\lim_{a \to \infty} \frac{2^{1.01a}}{a^2}
$$
 
This is an exponential over a polynomial, which is a standard divergent limit.
 
$$
\lim_{a \to \infty} \frac{2^{1.01a}}{a^2} = \infty
$$
 
which means $n^{1.01} \notin O(\log^2 n)$.
 

  - 1e )  **No.**
 
**Why:**
$$
\lim_{n \to \infty} \frac{\sqrt{n}}{\log^3 n}
$$
 
Substitute $n = 2^a$ 
Square Root on both sides:
 $$\sqrt n = 2^{a/2}$$Taking log on both sides:$$\log n = a$$$$\log^3 n = a^3$$
So the limit becomes: 
$$
\lim_{m \to \infty} \frac{2^{m/2}}{m^3}
$$
 
This is an exponential over a polynomial ($\frac{\infty}{\infty}$ form)
so:
 
$$
\lim_{m \to \infty} \frac{2^{m/2}}{m^3} = \infty
$$
 
i.e. $\sqrt{n} \notin O(\log^3 n)$.

  - 1f ) **Yes.**
 
**Why:**
$$
\lim_{n \to \infty} \frac{\sqrt{n}}{\log^3 n} = \infty \quad 
$$
 
As shown in question **1e** the limit is $\infty$, so$$\sqrt{n} \in \Omega(\log^3 n)$$ 
 

  - 1g

2. **SPARC to Python**

  - 2b ) `foo(a, b)` computes the GCD of `a` and `b`. It repeatedly replaces the larger number with the remainder of dividing it by the smaller one, until one of the numbers hits 0 — at that point the other number is the GCD.

  - 2c ) **Work** = total operations; **span** = longest chain of dependent operations.
 Each call to `foo` does O(1) work and makes exactly **one** recursive call (no branching), so the whole computation is a single sequential chain: $\text{Work}(n) = \text{Span}(n)$.
 The number of recursive calls is bounded by $O(\log(\min(a,b)))$ (Lamé's theorem). So, letting $n = \max(a,b)$:
 $$\text{Work}(n) = \text{Span}(n) = O(\log n)$$
 Since Work = Span, parallelism (Work/Span) is $O(1)$ — the recursion is inherently sequential.

3. **Parallelism and recursion**

  - 3b ) A single loop scans all $n$ elements once, doing O(1) work per iteration (comparison, increment/reset, comparison against max). Since it's one sequential loop with no parallelism, every iteration lies on the same dependency chain:
 $$\text{Work}(n) = O(n), \qquad \text{Span}(n) = O(n)$$

  - 3d ) Each call splits the array in half, recurses on both halves, then does O(1) work combining the two `Result`s. Since neither recursive call runs in parallel here (they execute one after the other), both Work and Span follow the same recurrence:
 
$$W(n) = 2W(n/2) + O(1) \;\Rightarrow\; O(n)$$
$$S(n) = 2S(n/2) + O(1) \;\Rightarrow\; O(n)$$
 So $\text{Work}(n) = O(n)$ and $\text{Span}(n) = O(n)$ — being recursive alone doesn't help unless the calls actually run concurrently.
  - 3e ) Total work doesn't change — the same number of operations happen regardless of scheduling:
 
$$W(n) = 2W(n/2) + O(1) \;\Rightarrow\; O(n)$$

But now the two recursive calls run concurrently, so the span only accounts for the slower of the two branches, not both added together:
 
$$S(n) = \max\big(S(n/2), S(n/2)\big) + O(1) = S(n/2) + O(1) \;\Rightarrow\; O(\log n)$$
 
So $\text{Work}(n) = O(n)$, $\text{Span}(n) = O(\log n)$ — this is where parallelism pays off, since the parallelism (Work/Span) becomes $O(n/\log n)$, versus $O(1)$ in 3b and 3d.

4. **GCD**
