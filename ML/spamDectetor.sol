// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AIContract {
    string public inputData;
    string public outputData;

    function getInputData() public view returns (string memory) {
        return inputData;
    }

    function setInputData(string memory _inputData) public {
        inputData = _inputData;
    }

    function setOutputData(string memory _outputData) public returns(string memory){
        outputData = _outputData;
        return  outputData;
    }

    function getOutputData() public view returns (string memory) {
        return outputData;
    }

}