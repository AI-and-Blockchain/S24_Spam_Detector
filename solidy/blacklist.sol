// SPDX-License-Identifier: MIT
pragma solidity ^0.8.6;

contract EmailBlacklistVoting {
    address public owner;
    mapping(bytes32 => bool) private blacklist;
    mapping(bytes32 => mapping(address => bool)) public hasVoted;
    mapping(bytes32 => uint256) private positiveVotes;
    mapping(bytes32 => uint256) private negativeVotes;
    mapping(bytes32 => string) private emailContentHashes; 

    uint256 public constant VOTES_REQUIRED_FOR_REMOVAL = 3;
    uint256 public constant VOTING_DURATION = 3 days;
    mapping(bytes32 => uint256) public voteEndTime;

    event EmailBlacklisted(bytes32 indexed emailHash, bool status);
    event EmailContentAdded(bytes32 indexed emailHash, string ipfsHash);
    event VoteInitiated(bytes32 indexed emailHash, uint256 endTime);
    event VoteCasted(bytes32 indexed emailHash, address voter, bool vote);
    event EmailRemovedFromBlacklist(bytes32 indexed emailHash);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    function setBlacklistStatus(string memory email, bool status) public onlyOwner {
        bytes32 emailHash = keccak256(abi.encodePacked(email));
        blacklist[emailHash] = status;
        emit EmailBlacklisted(emailHash, status);
    }

    function addEmailContentHash(string memory email, string memory ipfsHash) public onlyOwner {
        bytes32 emailHash = keccak256(abi.encodePacked(email));
        emailContentHashes[emailHash] = ipfsHash;
        emit EmailContentAdded(emailHash, ipfsHash);
    }

    function getEmailContentHash(string memory email) public view returns (string memory) {
        bytes32 emailHash = keccak256(abi.encodePacked(email));
        return emailContentHashes[emailHash];
    }

    function isBlacklisted(string memory email) public view returns (bool) {
        bytes32 emailHash = keccak256(abi.encodePacked(email));
        return blacklist[emailHash];
    }

    function initiateVote(string memory email) public {
        bytes32 emailHash = keccak256(abi.encodePacked(email));
        require(blacklist[emailHash], "Email not in blacklist");
        voteEndTime[emailHash] = block.timestamp + VOTING_DURATION;
        emit VoteInitiated(emailHash, voteEndTime[emailHash]);
    }

    function castVote(string memory email, bool voteToRemove) public {
        bytes32 emailHash = keccak256(abi.encodePacked(email));
        require(block.timestamp <= voteEndTime[emailHash], "Voting period over");
        require(!hasVoted[emailHash][msg.sender], "Already voted");
        
        uint256 totalVotes = positiveVotes[emailHash] + negativeVotes[emailHash] + 1; 

        if (voteToRemove) {
            positiveVotes[emailHash]++;
            if(positiveVotes[emailHash] >= VOTES_REQUIRED_FOR_REMOVAL && positiveVotes[emailHash] > totalVotes / 2) {
                blacklist[emailHash] = false;
                emit EmailRemovedFromBlacklist(emailHash);
            }
        } else {
            negativeVotes[emailHash]++;
        }

        hasVoted[emailHash][msg.sender] = true;
        emit VoteCasted(emailHash, msg.sender, voteToRemove);
    }

    function votesNeeded(string memory email) public view returns (uint256) {
        bytes32 emailHash = keccak256(abi.encodePacked(email));
        uint256 currentPositiveVotes = positiveVotes[emailHash];
        if(currentPositiveVotes >= VOTES_REQUIRED_FOR_REMOVAL && currentPositiveVotes > (positiveVotes[emailHash] + negativeVotes[emailHash]) / 2) {
            return 0;
        }
        return VOTES_REQUIRED_FOR_REMOVAL - currentPositiveVotes;
    }
}

