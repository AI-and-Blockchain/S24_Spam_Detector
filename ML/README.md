### spamDetector

Spam Detector aims to detect if the inputting message is a spam by using NLP techniques. Specifically, it tokenizes the words in the message into tokens, and then BERT would learn from the tokens and generates the meaningful embedding. Finally, a classifier would use the embedding to check if the inputted message is a spam, so the entire process can be considered as a two classification task.

### Dataset

The dataset used for this case is SMS Spam Collection from https://archive.ics.uci.edu/dataset/228/sms+spam+collection. It contains 5572 samples, 4825 for ham and 747 for spam. 4134 samples (3619 for ham and 560 for spam) are used for training, and the rest (1206 for ham and 187 for spam) are used for testing. The training dataset (spam_set) and the testing datset (test_set) are available in https://drive.google.com/file/d/1IBOXkJ2hPnu1W1eQh94Y348xjfYl3r12/view?usp=sharing. Remember to put them in /spam so that the python could load them successfully.

### Training process flow diagram
![image](https://github.com/AI-and-Blockchain/S24_Spam_Detector/assets/55873378/106f3db4-b343-498f-aa40-0201fd0f7ef9)

### How to run
- how to train:
    python main.py
  
- how to do testing on testing set in python environment:
    python testing.py
  
- how to make ML model interact with smart contract (without front end): 
    a. revise the "contract address" in "contract_interface.py" and "abi.json" according to your deployed contract:
  
        it is to make sure the ML model could receive the message from the contract.
  
    b. send the message to the contract "spanDetector.sol" by using "setInputData" function:

        in our project, this step would be done by the front end, but this demo is without front end, so you have to send a message to the contract manually.

    c. execute the function, "process_input_msg" in "contract_interface.py".

    Then the ML model can get the message from the contract and do spam detection.
    After few seconds, the detection result would be sent back to the contract automatically.
    d. you can see the detection output in the variable "outputData" in the contract.

### Checkpoint:
A pretrained model checkpoint is in /models . In case you cannot git clone the checkpoint because of its size, you could download the checkpoint from https://drive.google.com/file/d/1bwPLWojfG432DDhHHmKeBsgtassp4Wrp/view?usp=sharing. We supply two formats: .bin and .pt
