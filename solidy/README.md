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

The `MessageContract` outlines the fee structure and rewards mechanism implemented in our smart contract for handling suspicious messages and voting for email whitelisting. It supports functionalities like:

- **Charging Message Fee**: The smart contract automatically deducts a fee from the user's account when they send a message flagged as suspicious for verification.
- **Charging Voting Fee**: The smart contract implements a voting fee when a user participates in voting for the whitelisting of an email address. This fee helps to discourage non-serious voting.
- **Information Logging**: During the voting process for whitelisting an email address, the smart contract logs specific information like voter’s account address and email address they voted for.
- **Rewarding Voters**: The smart contract distributes the accumulated tokens for a particular email address equally among the voters who supported its whitelisting.

![image](https://github.com/AI-and-Blockchain/S24_Spam_Detector/assets/94344406/c7f41b9b-3b11-46ec-ae86-6e925d2616bf)
