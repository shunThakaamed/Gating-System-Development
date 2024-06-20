const express = require('express');
const bodyParser = require('body-parser');
const authController = require('./authJS/authController');

const app = express();
app.use(bodyParser.json());

app.use('/auth', authController);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
