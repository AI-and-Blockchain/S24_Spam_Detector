// SPDX-License-Identifier: MIT
pragma solidity ^0.8.6;

contract transferToken {
    address public owner;
    mapping(bytes32 => uint256) private depositAmount;
    mapping(bytes32 => address[]) private voters;
    mapping(bytes32 => mapping(address => bool)) private voterExists;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    function sendMessage(string memory email) public payable {
        require(msg.value > 0, "Ether deposit required");
        bytes32 emailHash = keccak256(abi.encodePacked(email));
        depositAmount[emailHash] += msg.value;
    }

    function addVoter(address voterAddress, string memory email) public onlyOwner {
        require(voterAddress != address(0), "Invalid address.");
        bytes32 emailHash = keccak256(abi.encodePacked(email));
        require(!voterExists[emailHash][voterAddress], "Voter already added.");
        voters[emailHash].push(voterAddress);
        voterExists[emailHash][voterAddress] = true;
    }

    function shareEther(string memory email) public onlyOwner {
        bytes32 emailHash = keccak256(abi.encodePacked(email));
        address[] memory currentVoters = voters[emailHash];
        uint256 voterCount = currentVoters.length;
        require(voterCount > 0, "No voter.");

        uint256 reward = depositAmount[emailHash] / voterCount;
        
        depositAmount[emailHash] = 0;
        delete voters[emailHash];

        for (uint256 i = 0; i < voterCount; i++) {
            payable(currentVoters[i]).transfer(reward);
        }
    }
}
