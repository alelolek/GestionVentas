const express = require('express')
const router = express.Router()
const productoConttroller = require('../controllers/producto')


router.get('/todos',productoConttroller.todos)
router.get('/buscar/:id',productoConttroller.buscar)
router.post('/registrar',productoConttroller.registrar)
router.post('/modificar/:id',productoConttroller.modificar)
router.post('/eliminar/:id',productoConttroller.eliminar)


module.exports = router