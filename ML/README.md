### spamDetector

Spam Detector aims to detect if the inputting message is a spam by using NLP techniques. Specifically, it tokenizes the words in the message into tokens, and then BERT would learn from the tokens and generates meaning embedding. Finally, a classifier would use the embedding to check if the inputted message is spam, so the entire process can be considered as a two classification task.

### Dataset

The dataset used for this case is SMS Spam Collection from https://archive.ics.uci.edu/dataset/228/sms+spam+collection. It contains 5572 samples, 4825 for ham and 747 for spam. 4134 samples (3619 for ham and 560 for spam) are used for training, and the rest (1206 for ham and 187 for spam) are used for testing.

### Training process flow diagram
