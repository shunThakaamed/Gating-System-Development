const express = require('express');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const authService = require('./authService');
const { validateSignature } = require('./ethUtils');

const router = express.Router();

router.post('/login', async (req, res) => {
    const { address, signature } = req.body;
    const isValid = await validateSignature(address, signature);
    if (isValid) {
        const token = authService.generateToken(address);
        res.json({ token });
    } else {
        res.status(401).json({ message: 'Invalid signature' });
    }
});

module.exports = router;
