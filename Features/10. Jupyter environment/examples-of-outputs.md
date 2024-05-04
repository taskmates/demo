### Outputs

Let's run some code snippets and see the output.

###### Some shell commands:

```python .eval
!date
```

###### The current directory:

```python .eval
!pwd
```

###### A plot:

```python .eval
import matplotlib.pyplot as plt
from collections import Counter

# Sample text
text = "hello world"
letter_counts = Counter(text.replace(" ", ""))  # Count letters, ignore spaces

# Data for plotting
labels, values = zip(*letter_counts.items())

plt.figure()
plt.bar(labels, values)
plt.title('Letter Frequency in "hello world"')
plt.xlabel('Letters')
plt.ylabel('Frequency')
plt.show()
```
###### An error:

```python .eval
foo
```

---

