# Optional: how good are your tests?

Passing tests only tell you the code does what your tests check. **Mutation testing** asks the opposite question: if the code were subtly wrong, would your tests notice?

A tool called **mutmut** makes many small changes ("mutants") to your code, such as changing `<` to `<=`, `+ 1` to `- 1`, or `None` to `""`, and runs your tests against each one.

- A mutant that makes a test fail is **killed**: good, your tests noticed.
- A mutant that passes every test **survived**: your tests would not catch that mistake.

## Try it

In the codespace terminal:

```
pip install mutmut
mutmut run
mutmut results
```

`mutmut run` tests every mutant of the code in `src/` (this is already set up in `pyproject.toml`). `mutmut results` lists the mutants that survived. To see exactly what one of them changed:

```
mutmut show <name-of-a-surviving-mutant>
```

## What to do with survivors

For each surviving mutant, ask: **would a user ever notice this change?**

- **Yes** → you are missing a test. Write one that fails for the mutant and passes for your real code. Log it in `ai-log.md`.
- **No** → the mutant changes nothing that matters (an "equivalent mutant"). Note it and move on.

Delete the `mutants/` folder afterwards if it gets in your way; it is ignored by git.
