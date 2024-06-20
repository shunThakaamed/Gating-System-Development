const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const { secret } = require('../config/config');

const generateToken = (address) => {
    return jwt.sign({ address }, secret, { expiresIn: '1h' });
};

module.exports = {
    generateToken,
};
