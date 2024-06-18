const jwt = require('jsonwebtoken');
const { secret } = require('../config/config');

const roleMiddleware = (role) => {
    return (req, res, next) => {
        const token = req.headers['authorization'].split(' ')[1];
        if (!token) {
            return res.status(401).json({ message: 'Unauthorized' });
        }

        jwt.verify(token, secret, (err, decoded) => {
            if (err) {
                return res.status(401).json({ message: 'Unauthorized' });
            }

            if (decoded.role !== role) {
                return res.status(403).json({ message: 'Forbidden' });
            }

            req.user = decoded;
            next();
        });
    };
};

module.exports = roleMiddleware;
