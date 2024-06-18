const Web3 = require('web3');
const web3 = new Web3(Web3.givenProvider || 'http://localhost:8545');

const validateSignature = async (address, signature) => {
    const message = `Authentication request: ${address}`;
    const signer = web3.eth.accounts.recover(message, signature);
    return signer.toLowerCase() === address.toLowerCase();
};

module.exports = {
    validateSignature,
};
