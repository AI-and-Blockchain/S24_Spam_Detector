// SPDX-License-Identifier: MIT
pragma solidity ^0.8.6;

contract MessageContract {
    address public owner;
    uint256 public messageFee;
    mapping(address => string) public messages;
    mapping(address => uint256) public balances;

    event MessageReceived(address sender, string message);
    event RefundIssued(address recipient, uint256 amount);
    event DepositReceived(address sender, uint256 amount);
    event MessageFeeUpdated(uint256 newCharge);

    constructor() {
        owner = msg.sender;
        balances[owner] = 0;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }


    function deposit() external payable {
        require(msg.value > 0, "You must send some Ether.");
        balances[msg.sender] += msg.value;
        emit DepositReceived(msg.sender, msg.value);
    }


    function setMessageFee(uint256 _fee) external onlyOwner {
        messageFee = _fee;
        emit MessageFeeUpdated(_fee);
    }


    function sendMessage(string calldata message) external {
        require(balances[msg.sender] >= messageFee, "Insufficient balance to send message.");
        balances[msg.sender] -= messageFee; // Deduct the message charge from the user's balance.
        balances[owner] += messageFee; // Add the charge to the owner's balance.
        messages[msg.sender] = message;
        emit MessageReceived(msg.sender, message);
    }


    function refundUser(address payable recipient, uint amount) external onlyOwner {
        require(amount <= balances[owner], "Insufficient balance for refund.");
        balances[owner] -= amount; // Deduct the amount from the owner's accumulated balance
        recipient.transfer(amount);
        emit RefundIssued(recipient, amount);
    }


    function withdrawUser() external {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "No balance to withdraw.");
        balances[msg.sender] = 0;
        payable(msg.sender).transfer(amount);
    }


    function withdrawOwner() external onlyOwner {
        uint256 amount = balances[owner];
        require(amount > 0, "No charges to withdraw.");
        balances[owner] = 0;
        payable(owner).transfer(amount);
    }
}
