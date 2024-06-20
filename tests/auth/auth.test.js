const request = require('supertest');
const express = require('express');
const bodyParser = require('body-parser');
const authController = require('../../src/auth/authController');
const jwt = require('jsonwebtoken');
const { secret } = require('../../src/config/config');
const { validateSignature } = require('../../src/auth/ethUtils');

jest.mock('../../src/auth/ethUtils');

const app = express();
app.use(bodyParser.json());
app.use('/auth', authController);

describe('Auth API', () => {
    it('should return a token for a valid signature', async () => {
        validateSignature.mockResolvedValue(true);

        const response = await request(app)
            .post('/auth/login')
            .send({ address: '0x123', signature: 'valid_signature' });

        expect(response.status).toBe(200);
        expect(response.body).toHaveProperty('token');
    });

    it('should return 401 for an invalid signature', async () => {
        validateSignature.mockResolvedValue(false);

        const response = await request(app)
            .post('/auth/login')
            .send({ address: '0x123', signature: 'invalid_signature' });

        expect(response.status).toBe(401);
        expect(response.body).toHaveProperty('message', 'Invalid signature');
    });
});
