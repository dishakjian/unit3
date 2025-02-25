## Paper Solution


## Code
```.py
class WordCounter:
    def __init__(self, text):
        self.text = text

    def wordCount(self):
        words = self.text.split()
        result = {}
        for w in words:
            w = w.strip(".!?").lower()
            if w not in result:
                result[w] = 1
            else:
                result[w] += 1
        self.result = result
        return self.result

print(WordCounter("This is a sample text. It contains words that will be counted.").wordCount())
```
## Proof Code Works
![image](https://github.com/user-attachments/assets/43eafea1-aea3-4a1e-945e-c664d72ea0da)

## UML Diagram
![image](https://github.com/user-attachments/assets/a8fc62cd-6179-44f8-9f51-cf44f6c906c0)

