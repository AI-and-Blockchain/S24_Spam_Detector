### spamDetector

Spam Detector aims to detect if the inputting message is a spam by using NLP techniques. Specifically, it tokenizes the words in the message into tokens, and then BERT would learn from the tokens and generates meaning embedding. Finally, a classifier would use the embedding to check if the inputted message is spam, so the entire process can be considered as a two classification task.

### Dataset

The dataset used for this case is SMS Spam Collection from https://archive.ics.uci.edu/dataset/228/sms+spam+collection. It contains 5572 samples, 4825 for ham and 747 for spam. 4134 samples (3619 for ham and 560 for spam) are used for training, and the rest (1206 for ham and 187 for spam) are used for testing.

### Training process flow diagram
![image](https://github.com/AI-and-Blockchain/S24_Spam_Detector/assets/55873378/106f3db4-b343-498f-aa40-0201fd0f7ef9)

### How to run
- how to train:
    python main.py
  
- how to do testing on testset:
    python testing.py
  
- how to make ML model interact with smart contract:
    a. revise the "contract address" in "contract_interface.py" and "abi.json" according to your deployed contract.
    b. 

   and send the message from contract to ML model. After the analysis of model, the output would be sent back to smart contract, and store in the variable "outputData". 

### Checkpoint:
A pretrained model checkpoint is in /models . In case you cannot git clone it because of its size, you could download the checkpoint from https://drive.google.com/file/d/1bwPLWojfG432DDhHHmKeBsgtassp4Wrp/view?usp=sharing. We supply two format: .bin and .pt


<font color=gray size=4>sadasdasdasdas</font> 
