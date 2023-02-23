from wallet import Balance

def test_getBalance():
    obj = Balance()
    obj.setBalance(20)
    assert(obj.getBalance() == 20)