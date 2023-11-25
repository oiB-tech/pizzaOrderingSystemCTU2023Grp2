const router = require('express').Router()
const db = require('../db')

/**
 * User
 * @typedef {object} User
 * @property {string} id.required - User Id
 * @property {string} username.required - User's Username
 * @property {string} password - User's Password
 * @property {string} firstName - The artist
 * @property {number} lastName - The year - double
 */


router.get('/', (req, res) => {
    let getAllQuery = db.prepare('SELECT userId as id, username, firstName, lastName FROM Users')
    res.send(getAllQuery.all())
})

router.post('/sessions', (req, res) => {

})

module.exports = router