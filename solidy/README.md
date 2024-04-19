# Smart Contract Part
### This section of the S24 Spam Detector project introduces two Solidity smart contracts designed for Ethereum blockchain, offering functionalities to interact with the spam detection software.

## EmailBlacklistVoting (`blacklist.sol`)

The `EmailBlacklistVoting` contract manages an email blacklist through a democratic voting process. It allows email addresses to be added or removed from the blacklist based on community votes. Key functionalities include:

- **Setting Blacklist Status**: Only the contract owner can add an email to the blacklist or remove it.
- **Adding Email Content Hash**: Allows storing a hash of the email's content, facilitating spam identification without compromising privacy.
- **Voting to Remove from Blacklist**: Users can initiate a vote to remove an email from the blacklist. A removal requires a majority of votes and meets a minimum vote count.
- **Querying Blacklist Status**: Check if an email is blacklisted.
- **Vote Participation**: Users can cast their vote for or against the removal of an email from the blacklist.

## MessageContract (`transferToken2.sol`)

The `MessageContract` enables sending messages with Ether transactions. It incorporates a fee mechanism, ensuring that only users who have paid can send messages. It supports functionalities like:

- **Depositing Ether**: Users can deposit Ether to their balance within the contract.
- **Setting and Paying Message Fee**: The owner sets a fee for sending messages. Users must have a balance exceeding this fee to send a message.
- **Sending Messages**: After paying the fee, users can send a message.
- **Refunds**: The contract owner can issue refunds to any user.
- **Balance Withdrawal**: Users can withdraw their balance at any time. The owner can also withdraw accumulated fees.

![image](https://github.com/AI-and-Blockchain/S24_Spam_Detector/assets/94344406/2fd55b3e-0e7b-42b7-9229-07cefbd30ea8)
