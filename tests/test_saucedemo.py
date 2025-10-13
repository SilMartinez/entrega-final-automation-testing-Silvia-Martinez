import pytest




@pytest.fixture
def driver():
    #configuracion para consultar a selenium web driver

def test_login():
    #logueo de usuarios con username y password
    #click al boton de login
    #redirigir a la pagina de inventario
    #verificar el titulo de pagina, inventory

def test_catalogo():
    #logueo de usuarios con username y password
    #click al boton de login
    #verificar el titulo pero del html
    #comprobar si existen productos visibles en la pagina (len())
    #verificar elementos imp de la pagina


def test_carrito():
    #logueo de usuarios con username y password
    #click al boton de login
    #llevarme a la pagina del carrito de compra
    #incremento del carrito a agregar un producto
    #comprobar que el carrito aparezca el producto correctamente